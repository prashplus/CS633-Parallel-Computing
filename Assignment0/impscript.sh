#!/bin/bash
for i in  `seq 1 116`;
do
    ssh csews$i uptime;
    #cat .ssh/id_rsa.pub | ssh fahad@172.27.19.$i 'cat >> .ssh/authorized_keys'
done
