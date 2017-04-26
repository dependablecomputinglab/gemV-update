import os
import sys
import random
import re

arch = sys.argv[1]
bench = sys.argv[2]
injectArch = sys.argv[3]
valFileName = sys.argv[4]
start = int(sys.argv[5])

    #HwiSoo: stringsearch sha bitcount qsort susan jpeg done
if(bench == 'hello'):
	runtime = 1203432
elif(bench == 'matmul'):
	runtime = 102119000 #valid for DC LAB server
elif(bench == 'stringsearch'):
	runtime = 96401000 #valid for DC LAB server
elif(bench == 'susan'):
	runtime = 1184289000 #valid for DC LAB server
elif(bench == 'gsm'):
	runtime = 15973624000 #valid for DC LAB server
elif(bench == 'jpeg'):
	runtime = 10380764000 #valid for DC LAB server
elif(bench == 'bitcount'):
	runtime = 1284616500 #valid for DC LAB server
elif(bench == 'qsort'):
	runtime = 12622084000 #valid for DC LAB server
elif(bench == 'dijkstra'):
	runtime = 27277285000 #valid for DC LAB server
elif(bench == 'basicmath'):
	runtime = 251651656000 #valid for DC LAB server
elif(bench == 'crc'):
	runtime = 1091403357500 #valid for DC LAB server
elif(bench == 'fft'):
	runtime = 28748840000
elif(bench == 'typeset'):
	runtime = 83872940000
elif(bench == 'patricia'):
	runtime = 99999999999999
elif(bench == 'sha'):
	runtime = 2782611000
elif(bench == 'ispell'):
	runtime = 99999999999999

os.system("mkdir " + str(bench))
#f = open(str(bench) + "/val_" + str(injectArch)+"_"+str(start)+"_"+str(end)+".txt", 'w') 

#os.system("rm -rf " + str(bench) + "/val_" + str(injectArch)+"_"+str(start)+"_"+str(end)+".txt")
#os.system("rm -rf " + str(bench) + "/sec_" + str(injectArch)+"_"+str(start)+"_"+str(end)+".txt")

valFile = open(valFileName, 'r')
i=start-1

while True:
    i=i+1
    valLine = valFile.readline()
    if not valLine:break
    valLine_split=valLine.split('\t')
    if (injectArch == "Reg"):
        injectTime = valLine_split[0]
        injectLoc = valLine_split[1]
        valFailure = valLine_split[2]
        valRuntime = valLine_split[3]
    elif (injectArch == "LSQ"):
        injectTime = valLine_split[0]
        injectLoc = valLine_split[1]
        valFailure = valLine_split[2]
        valRuntime = valLine_split[3]
    if valRuntime == "200"  or valRuntime == "200.0" or valRuntime == "failure" or valFailure == "NF":
        continue

    if (injectArch == "Reg" or injectArch == "RegHard"):
        if(bench == 'susan') or (bench == 'jpeg'):
            os.system("./symptom_inject_output.sh " + str(arch) + " " + str(bench) + " " + str(injectTime) + " " + str(injectLoc) + " " + str(i) + " " + str(injectArch) + " " + str(2*runtime) + " " + str(i).zfill(5)  + " > " + str(bench) + "/FI_" + str(injectArch) + "_" + str(i))
        else:
            os.system("./symptom_inject.sh " + str(arch) + " " + str(bench) + " " + str(injectTime) + " " + str(injectLoc) + " " + str(i) + " " + str(injectArch) + " " + str(2*runtime) + " > " + str(bench) + "/FI_" + str(injectArch) + "_" + str(i))
    if (injectArch == "FU"):
        if(bench == 'susan') or (bench == 'jpeg'):
            os.system("./symptom_inject_output.sh " + str(arch) + " " + str(bench) + " " + str(injectTime) + " " + str(injectLoc) + " " + str(i) + " " + str(injectArch) + " " + str(2*runtime) + " " + str(i).zfill(5)  + " > " + str(bench) + "/FI_" + str(injectArch) + "_" + str(i))
        else:
            os.system("./symptom_inject.sh " + str(arch) + " " + str(bench) + " " + str(injectTime) + " " + str(injectLoc) + " " + str(i) + " " + str(injectArch) + " " + str(2*runtime) + " > " + str(bench) + "/FI_" + str(injectArch) + "_" + str(i))
    if (injectArch == "LSQ"):
        if(bench == 'susan') or (bench == 'jpeg'):
                os.system("./symptom_inject_output.sh " + str(arch) + " " + str(bench) + " " + str(injectTime) + " " + str(injectLoc) + " " + str(i) + " " + str(injectArch) + " " + str(2*runtime) + " " + str(i).zfill(5)  + " > " + str(bench) + "/FI_" + str(injectArch) + "_" + str(i))
        else:
                os.system("./symptom_inject.sh " + str(arch) + " " + str(bench) + " " + str(injectTime) + " " + str(injectLoc) + " " + str(i) + " " + str(injectArch) + " " + str(2*runtime) + " > " + str(bench) + "/FI_" + str(injectArch) + "_" + str(i))
    #parse phase
    parseFile = open(bench + "/" + injectArch + "/FI_" + str(i), 'r')
    missLog = open(bench +"/" + injectArch + "/missLog_" + str(i), 'w')
    fullLog = open(bench +"/" + injectArch + "/fullLog_" + str(i), 'w')
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

    os.system("rm " + bench + "/" + injectArch + "/FI_" + str(i))   