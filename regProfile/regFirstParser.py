import os
import sys
import random
import re

input = sys.argv[1]
output = sys.argv[2]

inputFile = open(input, 'r')
splitFile = open(output+"_split", 'w')

linecount=0

while True:
    inputLine = inputFile.readline()
    if not inputLine: break
    line_split = inputLine.split()
    idx = int(line_split[6])
    tickFrom = int(line_split[10])
    tickTo = int(line_split[12])
    #split
    tickIndex = tickFrom
    if idx>=128: continue
    while tickIndex+500 <= tickTo:
        splitFile.write(str(idx)+"\t"+str(tickIndex)+"\t"+str(tickIndex+500)+"\t"+"\n")
        tickIndex=tickIndex+500
        linecount=linecount+1
inputFile.close()
splitFile.close()

countFile = open(output+"_count",'w')
countFile.write(str(linecount))
