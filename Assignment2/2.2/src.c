//Assignment 1.1
//MPI Send/Recieve
#include<mpi.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int size,scount=0,rcount=0;

void my_bcast(double* data, int count, MPI_Datatype datatype, int root, MPI_Comm communicator)
{
    int world_rank;
    MPI_Comm_rank(communicator, &world_rank);
    int world_size;
    MPI_Comm_size(communicator, &world_size);
    MPI_Request request[2];
    MPI_Status status[2];
    int recvRank,sendRank,i,j;
    int elements_per_proc = size/world_size;
    double *recvdata = (double*) malloc(elements_per_proc * sizeof(double)), *recvdata2 = (double*) malloc(size * sizeof(double));
    double buffer[elements_per_proc],buffer2[elements_per_proc];

    MPI_Barrier(MPI_COMM_WORLD);

    MPI_Scatter(data, elements_per_proc, MPI_DOUBLE, recvdata, elements_per_proc, MPI_DOUBLE, 0, MPI_COMM_WORLD);

    MPI_Barrier(MPI_COMM_WORLD);

    // printf("\nScatter Start \n");
    // for(i = 0;i<elements_per_proc;i++)
    //     {
    //         printf("%lf \n",recvdata[i]);
    //     }
    // printf("Scatter Stop \n");

    //MPI_Barrier(MPI_COMM_WORLD);
    
    //MPI_Allgather(recvdata, elements_per_proc, MPI_DOUBLE, &recvdata2, size, MPI_FLOAT,MPI_COMM_WORLD);

    for(i = 0;i<elements_per_proc;i++)
                {
                    recvdata2[rcount]=recvdata[i];
                    rcount++;
                }
    //rcount = elements_per_proc;
    for(i = 0 ; i<world_size-1 ; i++)
        {
                for(j = 0;j<elements_per_proc;j++)
                {
                    buffer[j]=recvdata2[scount];
                    scount++;
                }
            
            recvRank=(world_rank+world_size - 1)%world_size;
            sendRank=(world_rank + 1)%world_size;
            MPI_Isend(buffer, elements_per_proc, MPI_DOUBLE, sendRank, 999, MPI_COMM_WORLD, &request[0]);
            MPI_Irecv(buffer2, elements_per_proc, MPI_DOUBLE, recvRank, 999, MPI_COMM_WORLD, &request[1]);
            MPI_Waitall(2,request,status);

            for(j = 0; j<elements_per_proc ; j++)
                {
                    recvdata2[rcount]=buffer2[j];
                    rcount++;
                }
        }

    MPI_Barrier(MPI_COMM_WORLD);

    // printf("\nAllgather Start \n");
    // for(i = 0;i<size;i++)
    //     {
    //         printf("%lf \n",recvdata2[i]);
    //     }
    // printf("Allgather Stop\n");    
}

int main(int argc, char** argv)
    {
        MPI_Init(NULL, NULL);

        int world_rank,world_size;

        double mpi_bcast_time,new_bcast_time,ftime1,ftime2;
        size = atoi(argv[1]);
        int inputFile = atoi(argv[2]); //input file number
        
        //File Opening depending on the argument(file no)
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
        if(fptr == NULL)
        {
            printf("Error!");   
            exit(1);             
        }

        MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
        MPI_Comm_size(MPI_COMM_WORLD, &world_size);
        MPI_Status status1;

        //Dummy data
        double *data= (double*) malloc(size* sizeof(double));


        //Initializer
        // for (int i = 0; i< size; i++)
        //     data[i]=i;


        if(world_size < 2)
        {
            fprintf(stderr, "World Size must be greate than 1 for %s\n", argv[0]);
            MPI_Abort(MPI_COMM_WORLD, 1);
        }
        
        
        // Time my_bcast
        // Synchronize before starting timing
        MPI_Barrier(MPI_COMM_WORLD);
        new_bcast_time -= MPI_Wtime();
        my_bcast(data, size, MPI_DOUBLE, 0, MPI_COMM_WORLD);
        // Synchronize again before obtaining final time
        MPI_Barrier(MPI_COMM_WORLD);
        new_bcast_time += MPI_Wtime();

        // Time MPI_Bcast
        MPI_Barrier(MPI_COMM_WORLD);
        mpi_bcast_time -= MPI_Wtime();
        MPI_Bcast(data, size, MPI_DOUBLE, 0, MPI_COMM_WORLD);
        MPI_Barrier(MPI_COMM_WORLD);
        mpi_bcast_time += MPI_Wtime();
        
        MPI_Reduce(&mpi_bcast_time, &ftime1, 1, MPI_DOUBLE, MPI_MAX, 0, MPI_COMM_WORLD);
        MPI_Reduce(&new_bcast_time, &ftime2, 1, MPI_DOUBLE, MPI_MAX, 0, MPI_COMM_WORLD);


        if(world_rank == 0)
            {
            double b1 = (size*0.000008*(world_size - 1))/ftime1;
            double b2 = (size*0.000008*(world_size - 1))/ftime2;
            printf("MPI Bcast time: %lf \nNEW MPI Time: %lf\n",ftime1,ftime2);
            printf("Bandwidth MPI Bcast: %lf, NEW MPI Bcast : %lf \n",b1,b2);
            fprintf(fptr,"%lf\n",b1);
            fprintf(fptr,"%lf\n",b2);
            fclose(fptr);
            }
        MPI_Finalize();
    }