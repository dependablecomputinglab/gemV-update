import os
import sys
import random
import re


#parse phase
parseFile = open(sys.argv[1], 'r')
missLog = open(sys.argv[2], 'w')
fullLog = open(sys.argv[3], 'w')
while True:
    parseLine = parseFile.readline()
    if not parseLine:break
    parseLine_split = parseLine.split(":")
    if parseLine_split[2] == " CacheHit":
        fullLog.write("CH " + parseLine_split[6]+"\n")
    elif parseLine_split[2] == " CacheMiss":
        missLog.write("CM " + parseLine_split[6]+"\n")
        fullLog.write("CM " + parseLine_split[6]+"\n")
    elif "\tCorrect\t" in parseLine_split[2]:
        fullLog.write("BC " + parseLine_split[2].split("\t")[5])
    elif "\tIncorrect\t" in parseLine_split[2]:
        missLog.write("BM " + parseLine_split[2].split("\t")[5])
        fullLog.write("BM " + parseLine_split[2].split("\t")[5])
    elif "injectEarlySN" in parseLine_split[2]:
        missLog.write("IS " + parseLine_split[2].split(' ')[3])
        fullLog.write("IS " + parseLine_split[2].split(' ')[3])
parseFile.close()
missLog.close()
fullLog.close()
