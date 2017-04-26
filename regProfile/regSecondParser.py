import os
import sys
import random
import re
import subprocess

input = sys.argv[1]
output = sys.argv[2]
start = int(sys.argv[3])
end = int(sys.argv[4])

inputFile = open(input+"_split", 'r')

inputCountFile = open(input+"_count", 'r')

outputFile = open(output+"_"+str(start)+"_"+str(end)+".txt", 'w')



count=int(inputCountFile.readline().split()[0])


random_samples=random.sample(xrange(0,count), end-start)


lines = inputFile.readlines()
for i in range(0,end-start):
    outputFile.write(lines[random_samples[i]].split()[0]+"\t"+lines[random_samples[i]].split()[2]+"\n")
    