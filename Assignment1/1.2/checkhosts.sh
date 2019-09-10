#! /bin/bash
rm hosts
touch hosts
echo "csews31" >> hosts
for i in csews{20..30}
do
	if ping -c1 -w1 $i &>/dev/null
	then 
		echo $i >> hosts
	fi
done
