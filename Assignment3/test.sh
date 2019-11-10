#!/bin/bash
awk '!/pattern/' cse/data1/time1.txt > temp && mv temp cse/data1/time1.txt
awk '!/pattern/' cse/data2/time2.txt > temp && mv temp cse/data2/time2.txt