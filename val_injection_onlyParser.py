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
    if parseLine_split[2] == " CacheMiss":
        missLog.write("CM " + parseLine_split[6]+"\n")
    elif parseLine_split[2] == " ICMiss":
        missLog.write("IM " + parseLine_split[6]+"\n")
    elif parseLine_split[2] == " IQSquashedInstIssued":
        missLog.write("SI " + parseLine_split[6]+"\n")
    elif parseLine_split[2] == " iewLSQFullEvents":
        missLog.write("LF " + parseLine_split[6]+"\n")
    elif "\tIncorrect\t" in parseLine_split[2]:
        missLog.write("BM " + parseLine_split[2].split("\t")[5])
    elif "injectEarlySN" in parseLine_split[2]:
        missLog.write("IS " + parseLine_split[2].split(' ')[3])
parseFile.close()
missLog.close()
fullLog.close()
