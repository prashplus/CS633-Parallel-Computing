//Assignment 2.1
//MPI Send/Recieve in Pair
#include<mpi.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char** argv)
    {
        MPI_Init(NULL, NULL);

        int world_rank,world_size,i,size, inputFile, sender, receiver;
        //Input Data size
        size = atoi(argv[1]);

        //Things needed to be written in input file for ploting
        inputFile = atoi(argv[2]); //input file number
        sender = atoi(argv[3]); //sender number
        receiver = atoi(argv[4]); //receiver number

        MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
        MPI_Comm_size(MPI_COMM_WORLD, &world_size);

        //timer
        double stime= MPI_Wtime(),speed,time,ftime;

        //Dummy data
        double a[size];

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
        
        
        if(fptr == NULL)
        {
            printf("Error!");   
            exit(1);             
        }
        //terminate the program if number of processes is not equal to 2
        if(world_size != 2)
        {
            fprintf(stderr, "World Size must be equal to 2 for %s\n", argv[0]);
            MPI_Abort(MPI_COMM_WORLD, 1);
            exit(1);
        }
        
        if(world_rank == 0)
            {
                    //Main Send function
                    MPI_Send(
                        a,
                        size,
                        MPI_DOUBLE,
                        1,
                        7,
                        MPI_COMM_WORLD);
            }
        else if(world_rank == 1)
            {
                    //Main Receive Function
                    MPI_Recv(
                        a,
                        size,
                        MPI_DOUBLE,
                        0,
                        7,
                        MPI_COMM_WORLD,
                        MPI_STATUS_IGNORE);
                //time=MPI_Wtime() - stime;
            }

        time= MPI_Wtime() - stime;

        MPI_Reduce(&time, &ftime, 1, MPI_DOUBLE, MPI_MAX, 0, MPI_COMM_WORLD);

        //Calculate and store the Bandwidth in a file
        if(world_rank == 0)
            {
            //speed = (size*0.0008)/time;
            printf("Bandwidth %lf \n",(size*0.000008)/ftime);
            fprintf(fptr,"%d %d %lf\n",sender,receiver,(size*0.000008)/ftime);
            fclose(fptr);
            }
        MPI_Finalize();
        return 0;
    }