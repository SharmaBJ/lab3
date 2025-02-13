#!/usr/bin/env python3
'''Lab 3 Inv 2 function free_space'''
# Author ID: bsharma60@myseneca.ca

import subprocess

def free_space():
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, shell=True)
    output, _ = p.communicate()
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())

