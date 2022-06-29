#!/usr/bin/env python3
import subprocess

subprocess.run(["aws ec2 start-instances --instance-ids i-0befac3ec3a120396"], shell=True)
