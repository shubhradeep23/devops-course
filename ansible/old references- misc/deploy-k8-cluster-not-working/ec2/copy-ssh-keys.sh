#!/bin/bash

for server in `cat server_ips`; do
    sshpass -p "root" ssh-copy-id -i ~/.ssh/id_rsa.pub root@$server
done

