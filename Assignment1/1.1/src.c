//Assignment 1.1
//MPI Send/Recieve
#include<mpi.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char** argv)
    {
        MPI_Init(NULL, NULL);

        int world_rank,world_size,i,size;
        size = atoi(argv[1]); 
        MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
        MPI_Comm_size(MPI_COMM_WORLD, &world_size);

        //timer
        double stime= MPI_Wtime(),speed,time;

        //Dummy data
        double a[size];

        //File Access Define
        FILE *fptr;
        fptr = fopen("data.txt","a");
        if(fptr == NULL)
        {
            printf("Error!");   
            exit(1);             
        }
        
        if(world_size < 2)
        {
            fprintf(stderr, "World Size must be greate than 1 for %s\n", argv[0]);
            MPI_Abort(MPI_COMM_WORLD, 1);
        }
        
        if(world_rank == 0)
            {
                for(i=0;i<100;i++)
                    {
                    MPI_Send(
                        a,
                        size,
                        MPI_DOUBLE,
                        1,
                        i,
                        MPI_COMM_WORLD);
                    }
            }
        else if(world_rank == 1)
            {
                for(i=0;i<100;i++)
                    {
                    MPI_Recv(
                        a,
                        size,
                        MPI_DOUBLE,
                        0,
                        i,
                        MPI_COMM_WORLD,
                        MPI_STATUS_IGNORE);
                    }
                //time=MPI_Wtime() - stime;
            }
        if(world_rank == 1)
            {
            time= MPI_Wtime() - stime;
            //speed = (size*0.0008)/time;
            printf("Bandwidth %lf \n",(size*0.0008)/time);
            fprintf(fptr,"%lf\n",(size*0.0008)/time);
            fclose(fptr);
            }
        MPI_Finalize();
    }
