//Assignment 2.1
//MPI Send/Recieve in Pair
#include<mpi.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char** argv)
    {
        MPI_Init(NULL, NULL);

        int world_rank,world_size,size, inputFile, sender, receiver, i ,j;
        //Input Data size
        size = atoi(argv[1]);

        //Things needed to be written in input file for ploting
        inputFile = atoi(argv[2]); //input file number

        MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
        MPI_Comm_size(MPI_COMM_WORLD, &world_size);
        MPI_Request request1,request2;
        MPI_Status status1,status2;
        double *a = (double *)malloc(size*sizeof(double));
        double *b = (double *)malloc(size*sizeof(double));

        //timer
        double speed,stime,etime,ftime, t[30][30];
        for(i=0;i<world_size;i++)
        {
            for(j=0;j<world_size;j++)
            {
                t[i][j]=0;
            }
    
        }

        //File pointer init for different files depending on the data size
        FILE *fptr;
        if (inputFile == 1)
            {
                fptr = fopen("data1.txt","a");
            }
        else if(inputFile == 2)
            {
                fptr = fopen("data2.txt","a");
            }
        else
            {
                fptr = fopen("data3.txt","a");
            }
        
        //return if Files not present
        if(fptr == NULL)
        {
            printf("Error!");   
            exit(1);             
        }

        //1 to 1 mapping of all 30 nodes and all the send recieves
        for(i = 0;i < world_size ;i++)
            {
                for (j = i;j < world_size;j++)
                    {
                        //Diaganols
                        if(world_rank == i && i == j)
                            {
                                stime = MPI_Wtime();
                                MPI_Isend(a, size, MPI_DOUBLE, i, 7, MPI_COMM_WORLD, &request1);
                                MPI_Irecv(b, size, MPI_DOUBLE, i, 7, MPI_COMM_WORLD, &request2);
                                
                                MPI_Wait(&request2, &status2);
                                MPI_Wait(&request1, &status1);
                                etime = MPI_Wtime() - stime;
                                t[i][i]=etime;
                                
                            }
                        else if(world_rank == i)
                                {
                                    stime = MPI_Wtime();
                                    MPI_Send(a, size, MPI_DOUBLE, j, 7, MPI_COMM_WORLD);
                                    etime = MPI_Wtime()-stime;
                                    t[i][j]=etime;

                                    stime = MPI_Wtime();
                                    MPI_Recv(b, size, MPI_DOUBLE, j, 7, MPI_COMM_WORLD, &status1);
                                    etime = MPI_Wtime()-stime;
                                    t[j][i]=etime;
                                }
                        else if(world_rank == j)
                                {
                                    stime = MPI_Wtime();
                                    MPI_Recv(b, size, MPI_DOUBLE, i, 7, MPI_COMM_WORLD, &status2);
                                    etime = MPI_Wtime()-stime;
                                    t[i][j]=etime;

                                    stime = MPI_Wtime();
                                    MPI_Send(a, size, MPI_DOUBLE, i, 7, MPI_COMM_WORLD);
                                    etime = MPI_Wtime()-stime;
                                    t[j][i]=etime;
                                }
                    }
            }
        //Reduce to the max time by MPI_Reduce
        double mtime[world_size][world_size];
        for(i =0 ;i<world_size; i++)
        {
            MPI_Reduce(t[i] , mtime[i], world_size, MPI_DOUBLE , MPI_MAX, 0, MPI_COMM_WORLD);
        }
        //Calculate and store the Bandwidth in a file
        if(world_rank == 0)
            {
                for(i = 0;i < world_size ;i++)
                    {
                    for (j = 0;j < world_size;j++)
                        {
                        speed = (size*0.000008)/mtime[i][j];
                        printf("Bandwidth %lf \n",speed);
                        fprintf(fptr,"%d %d %lf\n",i,j,speed);  
                        }
                    }
            fclose(fptr);
            }
        
        MPI_Finalize();
        return 0;
    }