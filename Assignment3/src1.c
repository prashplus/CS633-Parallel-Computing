#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <float.h>
#include "mpi.h"

//For most of the calculations since prepoint struct is not suitable for direct use ;)
typedef struct clusterpoint
{
        double x;
        double y;
        double z;
        int cluster;
} cPoint;

//For reading data from input files
typedef struct prepoint
{
        double id;
        double a;
        double b;
        double c;
} prePoint;

//For calculating distance b/w 2 points
double distance(cPoint p1, cPoint p2);

// Finding the nearest b/w one and all
int near(cPoint p,cPoint *c,int n,double *dt);

//Kmeans Initializatoin (random)
void kmplus(cPoint * allPoints, int len, cPoint * c, int K );

//main kmeans algo
void kmeans(cPoint *allPoints, int len,cPoint * c,int K, int *clusterSize);


int main(int argc, char *argv[])
{
    //###########INIT############
    int np, myrank, i, j, c, count;

    //MPI Stuff ;)
    MPI_Init( &argc, &argv );
	MPI_Comm_size(MPI_COMM_WORLD, &np);
	MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
    MPI_Status status;

    //file names appending material
    char *lName[] = {"0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"};
    //Output file name array
    char *fileEnd[] = {"0.txt","1.txt","2.txt.txt","3.txt","4.txt","5.txt","6.txt","7.txt","8.txt","9.txt","10.txt","11.txt","12.txt","13.txt","14.txt","15.txt","16.txt","17.txt"};
	char outBuffer[35], a[5], filename1[30]; 
    //Cluster centers
    int K = 20; 

    //Array to store cluster centres
    cPoint * centr = (cPoint *)malloc(K*sizeof(cPoint));
    int  * clusterSize = (int *)malloc(K*sizeof(int));

    //Time recording variables
    double totalTime = MPI_Wtime();
    double sumPreTime = 0;
    double sumClusTime = 0;
    double avgPreProTime = 0;
    double avgClusTime = 0;
    double maxtTime = 0;
    char tInfo[200]="";

    //File (receive data) stuff
    const int root = 0;
    int *recvcounts = NULL;
    int *recvcount = NULL;
    int totalLength = 0;
    int *displs = NULL;
    char *tString = NULL;
    
    //File dividation
    int nfiles = atoi(argv[1]);
    int extraFiles = nfiles%np;
    int perProcess = nfiles/np;
    int arr[np+1];
    arr[0] = 0;

    for(i =1; i <= np ; i++)
    {
        if(extraFiles > 0)arr[i] = arr[i-1]+perProcess + 1;
        else arr[i] = arr[i-1]+ perProcess;
        extraFiles--; 
    }

    strcpy(outBuffer,argv[3]);
    strcat(outBuffer,fileEnd[np]);

    sprintf(a,"%d",np);
    char str[100000]="";

    if(myrank == 0)
    {
        sprintf(str,"%s","Number of processes: "); strcat(str,a);
    }

    for(j = arr[myrank] ; j<arr[myrank+1]; j++)
    {
        MPI_Datatype pointtype; 
        MPI_Type_contiguous(4,MPI_DOUBLE,&pointtype);
        MPI_Type_commit(&pointtype);
        
        MPI_File fh;
        MPI_Offset filesize;
        
        strcpy(filename1,argv[2]); 
        
        //Timing the preprocessing of each time step
        double preTime = MPI_Wtime();
        
        MPI_File_open(MPI_COMM_SELF,strcat(filename1,lName[j]) ,MPI_MODE_RDONLY,MPI_INFO_NULL,&fh);
        MPI_File_get_size(fh,&filesize);
        
        filesize = filesize/sizeof(double);
        prePoint *allpoints = (prePoint *)malloc(filesize*sizeof(double));
        
        MPI_File_read(fh, allpoints, filesize,pointtype , &status);
        
        //number of points actually read
        
        MPI_Get_count( &status, pointtype, &count );
        MPI_File_close(&fh);
        
        preTime = MPI_Wtime()-preTime;
        sumPreTime+=preTime;

        //Point buffer
        cPoint *allcpoints = (cPoint *)malloc(count*sizeof(cPoint));
        for(i = 0; i < count ; i++)
        {
            allcpoints[i].x = allpoints[i].a;
            allcpoints[i].y = allpoints[i].b;
            allcpoints[i].z = allpoints[i].c;
            allcpoints[i].cluster = -1;
        }
        
        //###########Clustering################
        
        //Clustering Timmer
        double clustering_time = MPI_Wtime();
        
        //Initializing the cluster-centres using kmean++ algorithm
        kmplus(allcpoints,count,centr,K);

        //Kmeans call
        kmeans(allcpoints,count,centr,K,clusterSize);
        
        clustering_time = MPI_Wtime()-clustering_time;
        sumClusTime+=clustering_time;
        
        //Printing cluster-size and their centres
        char temp[3]; 
        sprintf(temp,"T%d",j+1);
        strcat(str,"\n");
        strcat(str,temp);
        strcat(str,": ");

        char k[2];
        sprintf(k,"%d",K);
        strcat(str,k);
        
        for(c = 0 ; c < K ; c++)
        {
            //concat all the outputs
            char carr[20]="";
            strcat(str,", ");
            sprintf(carr,"<%d",clusterSize[c]);
            strcat(str,carr);
            sprintf(carr,"%lf",centr[c].x);
            strcat(str,", ");
            strcat(str,carr);
            sprintf(carr,"%lf",centr[c].y);
            strcat(str,", ");
            strcat(str,carr);
            sprintf(carr,"%lf>",centr[c].z);
            strcat(str,", ");
            strcat(str,carr);
        }
    }

    totalTime = MPI_Wtime() - totalTime;
    //########## Time calculation and all ###############
    //Reducing out the time that we need
    
    MPI_Reduce(&sumPreTime,&avgPreProTime,1,MPI_DOUBLE,MPI_SUM,0,MPI_COMM_WORLD);
    MPI_Reduce(&sumClusTime,&avgClusTime,1,MPI_DOUBLE,MPI_SUM,0,MPI_COMM_WORLD);
    MPI_Reduce(&totalTime,&maxtTime,1,MPI_DOUBLE,MPI_MAX,0,MPI_COMM_WORLD);

    
    int mylen = strlen(str);
    
    if (myrank == root)
        recvcounts = malloc( np * sizeof(int)) ;

    //Gathering lenths since file is not evenly distributed
    MPI_Gather(&mylen, 1, MPI_INT, recvcounts, 1, MPI_INT,root, MPI_COMM_WORLD);

    if (myrank == root) {
        displs = malloc( np * sizeof(int) );

        displs[0] = 0;
        totalLength += recvcounts[0]+1;

        for (i=1; i<np; i++) {
           totalLength += recvcounts[i]+1;   /* plus one for space or \0 after words */
           displs[i] = displs[i-1] + recvcounts[i-1] + 1;
        }

        /* allocate string, pre-fill with spaces and null terminator */
        tString = malloc(totalLength * sizeof(char));            
        for (i=0; i<totalLength-1; i++)
            tString[i] = ' ';
        tString[totalLength-1] = '\0';
    }

    //Since we have calculated the receive buffer, counts, and displacements. So now we can gather the strings
    MPI_Gatherv(str, mylen, MPI_CHAR,tString, recvcounts, displs, MPI_CHAR,root, MPI_COMM_WORLD);

    //Adding timings to the total string
    if(myrank == root)
    {
        avgPreProTime /= np;
        avgClusTime /= np;
        char t1[50] = "";
        sprintf(t1,"Average time to preprocess: %lf",avgPreProTime);
        strcat(tInfo,"\n");
        strcat(tInfo,t1);
        sprintf(t1,"Average time to process: %lf\n",avgClusTime);
        strcat(tInfo,"\n");
        strcat(tInfo,t1);
        sprintf(t1,"Total time: %lf\n",maxtTime);
        strcat(tInfo,t1);
        printf("%lf %lf %lf\n",avgPreProTime,avgClusTime,maxtTime);
    }

    //Final File Write
    if(myrank == root)
    {
        FILE * fp = fopen(outBuffer,"w");
        fprintf(fp,"%s",tString);
        fprintf(fp,"%s",tInfo);
        fclose(fp);
    } 

    MPI_Finalize();
    return 0;
}

double distance(cPoint p1, cPoint p2)
{
    double x,y,z;
    x = p1.x - p2.x;
    y = p1.y - p2.y;
    z = p1.z - p2.z;
    return (x*x + y*y + z*z);
}

int near(cPoint p,cPoint *c,int n,double *dt)
{
    *dt = DBL_MAX; 
    int index, i =0 ;
    for(i = 0 ;i<n;i++)
    {
        double x = distance(p, c[i]);
        if(x < *dt)
        {
            *dt = x;
            index = i;
        }
    }
    return index;
}

void kmplus(cPoint * allPoints, int len, cPoint * c, int K )
{
    //Initializing first centroid
    c[0] = allPoints[rand()%len];
    int n = 0,i,j;
    double temp;
    
    for(j = 1; j < K ; j++)
    {
        cPoint nextCenter;
        n++;
        double dt = 0;
        
        for(i = 0; i < len ; i++)
        {
            temp = 0;
            near(allPoints[i], c, n, &temp);
            if(temp > dt) {
                dt = temp;
                nextCenter = allPoints[i];
            }
        }
    c[j] = nextCenter;
    }
}


//Kmeans algo main
void kmeans(cPoint *allPoints, int len,cPoint * c,int K, int *clusterSize)
{
    int flag = 1,rounds,i,j;
    double dt;
    for(rounds = 0; rounds < 500 ; rounds++)
    {
        if(!flag) 
            break;
        flag = 0;

        //Initializing centres for all points
        for (i = 0; i < len; i++)
        {
            int newcluster = near(allPoints[i],c,K,&dt);
            if (allPoints[i].cluster != newcluster )
                flag = 1;
            allPoints[i].cluster = newcluster; 
        }
        //for each cluster
        for(i = 0; i < K; i++)
        {
            double x=0,y=0,z=0;
            int count=0;
            for(j = 0; j < len ; j++ )
            {
                if(i == allPoints[j].cluster)
                {   
                    x+=allPoints[j].x;
                    y+=allPoints[j].y;
                    z+=allPoints[j].z;
                    count++;
                }
            }
            if(count <= 10)
            {
                c[i] = allPoints[rand()%len];
            }
            else if (count != 0)
            {
                c[i].x = x/count;
                c[i].y = y/count;
                c[i].z = z/count;
                clusterSize[i] = count;
            }   
        }
    }   
}