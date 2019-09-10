#!/bin/bash
mpiexec -np 2 ./main.out 16
mpiexec -np 2 ./main.out 128
mpiexec -np 2 ./main.out 8192
mpiexec -np 2 ./main.out 131072
mpiexec -np 2 ./main.out 524288