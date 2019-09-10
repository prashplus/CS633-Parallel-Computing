//Assignment 1.1
//MPI Send/Recieve
#include<mpi.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char** argv)
    {
        MPI_Init(NULL, NULL);

        int world_rank,world_size,i,j,size;
        size = atoi(argv[1]); 
        MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
        MPI_Comm_size(MPI_COMM_WORLD, &world_size);
        MPI_Status status1;
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
        
        
        for(j=0;j<100;j++){
        if(world_rank == 0)
            {
                for(i=0; i< (world_size -1);i++)
                    {
                    MPI_Recv(
                        a,
                        size,
                        MPI_DOUBLE,
                        i+1,
                        7,
                        MPI_COMM_WORLD,
                        &status1);
                    }
            }
        else
            {
                    MPI_Send(
                        a,
                        size,
                        MPI_DOUBLE,
                        0,
                        7,
                        MPI_COMM_WORLD);
            }
        }
        if(world_rank == 0)
            {
            time= MPI_Wtime() - stime;
            printf("Bandwidth is %lf \n",(size*0.0008*(world_size - 1))/time);
            fprintf(fptr,"%lf\n",(size*0.0008*(world_size - 1))/time);
            fclose(fptr);
            }










        ////Part 2
        double stime2= MPI_Wtime(),speed2,time2;

        //Dummy data
        double buffer[size], buffer2[size];


        MPI_Request request[world_size-1];
        MPI_Status status[world_size -1];


        //File Access Define
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
        
        
        for(j=0;j<100;j++){
        if(world_rank == 0)
            {
                for(i=0; i< (world_size -1);i++)
                    {
                    MPI_Irecv(buffer, size, MPI_DOUBLE, i+1, 12, MPI_COMM_WORLD, &request[i]);
                    }
                    MPI_Waitall(world_size-1,request, status);
                    

            }
        else
            {
                    MPI_Isend(buffer2, size, MPI_DOUBLE, 0, 12, MPI_COMM_WORLD, &request[world_rank-1]);
                    MPI_Wait(&request[world_rank-1], &status[world_rank-1]);
            }
        }
        if(world_rank == 0)
            {
            time2= MPI_Wtime() - stime2;
            printf("Bandwidth is %lf with time %lf \n",(size*0.0008*(world_size - 1))/time2,time2);
            fprintf(fptr,"%lf\n",(size*0.0008*(world_size - 1))/time2);
            fclose(fptr);
            }
        MPI_Finalize();
    }