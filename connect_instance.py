#!/usr/bin/env python3

import subprocess

# Parse the aws instances public IPv4 address via AWS-CLI
getIP = subprocess.run(["aws ec2 describe-instances --instance-ids i-0befac3ec3a120396 --query 'Reservations[].Instances[].PublicDnsName' | rg aws"], shell=True, stdout=subprocess.PIPE, text=True)
parseIP = getIP.stdout[5:-2]
#print(parseIP)

# Connect to instance
subprocess.run([f"ssh -i 'net0.pem' ubuntu@{parseIP}"], shell=True, text=True)


#bash get_instance_pubDNS.sh | rg -e (["'])(?:(?=(\\?))\2.)*?\1

