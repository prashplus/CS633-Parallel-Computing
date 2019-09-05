#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

#define BUFFER 262144

int main(int argc, char** argv) 
{
    int arr[BUFFER] = {0};
    int myrank, size;
    double start_time;

    MPI_Init(NULL, NULL);
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    // We are assuming at least 2 processes for this task
    if (world_size < 2) {
        fprintf(stderr, "World size must be greater than 1 for %s\n", argv[0]);
        MPI_Abort(MPI_COMM_WORLD, 1);
    }

    start_time = MPI_Wtime();

    if (world_rank < size-1) {
        MPI_Send(
        /* data         = */ arr, 
        /* count        = */ BUFFER, 
        /* datatype     = */ MPI_INT, 
        /* destination  = */ size-1, 
        /* tag          = */ 99, 
        /* communicator = */ MPI_COMM_WORLD);
    } else {
        int count, recvarr[size][BUFFER];
        MPI_Irecv(
        /* data         = */ recvarr[i],
        /* count        = */ BUFFER, 
        /* datatype     = */ MPI_INT, 
        /* source       = */ MPI_ANY_SOURCE, 
        /* tag          = */ MPI_ANY_TAG, 
        /* communicator = */ MPI_COMM_WORLD, 
        /* status       = */ MPI_STATUS_IGNORE);
        printf("Process 1 received number %d from process 0\n", number);
    }
    MPI_Finalize();
}