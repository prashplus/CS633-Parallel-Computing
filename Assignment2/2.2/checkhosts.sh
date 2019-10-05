#! /bin/bash
rm hosts
touch hosts
#echo "csews1" >> hosts
count=0
for i in csews{1..116}
do
	value=$(grep -w $i allhosts)
	if test -z "$value"
	then
		echo $i
	else
		echo $value
		if ping -c1 -w1 $i &>/dev/null
		then
			echo $i
			echo $i >> hosts
			count=`expr $count + 1`
		fi
	fi
	if [ $count -eq 30 ]
	then
		break
	fi
done