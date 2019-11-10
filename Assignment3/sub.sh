#!/bin/bash
#PBS -N assign3
#PBS -q small
#PBS -l nodes=2:ppn=8
#PBS -l walltime=07:00:00
#merge output and error into a single job_name.number_of_job_in_queue.
#PBS -j oe
#export fabric infiniband related variables
export I_MPI_FABRICS=shm:tmi
export I_MPI_DEVICE=rdma:OpenIB-cma
#change directory to where the job has been submitted from
cd $PBS_O_WORKDIR
mpiicc -o main.out src.c
#source paths
source /opt/software/intel17_update4/initpaths intel64
#run the job on required number of cores
sort $PBS_NODEFILE > hosts
mpiicc -o main.out src.c
python hpcrun.py
