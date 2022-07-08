#!/bin/bash

aws ec2 describe-instances --query Reservations[*].Instances[*].[PrivateIpAddress] > server-ips
sed -i 's/\[//g' server-ips
sed -i 's/\]//g' server-ips
sed -i 's/\"//g' server-ips
sed -i 's/\,//g' server-ips
cat server-ips | sed '/^$/d' > server_ips
rm server-ips
