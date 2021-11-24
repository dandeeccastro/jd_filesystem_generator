#!/bin/python3
import os 
import getopt
import yaml
import math
import sys

JD_ID = 00.00

def usage():
    print(
"""
JD Filesystem Generator v0.1.0
by Z0ng4 0f th3 str33ts

Generates filesystems based on the Johnny Decimal filesystem 
format by using a properly formatted YAML file. Proper file 
formatting is defined in YAML FORMATTING

USAGE: main.py [OPTIONS]

OPTIONS:
    -h:                 Displays this help message 
    -f, --file <file>:  Will generate filesystem based on <file> instead of ./jd.yml 
    -p, --path <path>:  Will generate filesystem with <path> as root instead of ./

YAML FORMATTING:
    
    The YAML file format is defined in the example below. Final folders 
    are set with dashes, whereas middle and start folders are not. The 
    script wont run beyond three layers deep

    Start Folder 1:
        Middle Folder 1:
            - End Folder 1
            - End Folder 2
            - End Folder 3
            - End Folder 4
        Middle Folder 2:
    Start Folder 2:
        ...

"""
)

def createFilesystem(layer, jd_data):
    if layer > 3:
        print("Você passou dos limites amigão")
        return 
    elif type(jd_data) is dict:
        for kv_pair in jd_data.items():
            updateJD_ID(layer)
            os.mkdir(f"{getJD_IDPrefix(layer)} {kv_pair[0]}")
            os.chdir(f"./{getJD_IDPrefix(layer)} {kv_pair[0]}")
            createFilesystem(layer + 1, kv_pair[1])
        os.chdir("..")
    else:
        for i in jd_data:
            updateJD_ID(layer)
            os.mkdir(f"{getJD_IDPrefix(layer)} {i}")
        os.chdir("..")

def getJD_IDPrefix(layer):
    global JD_ID
    result = math.floor(JD_ID)

    if (layer == 1):
        result -= result % 10 
        return f"{result} - {result + 9}"
    elif (layer == 2):
        return f"{result}"
    elif (layer == 3):
        return "{0:.2f}".format(round(JD_ID,2))
        

def updateJD_ID(layer):
    global JD_ID
    if (layer == 1):
        JD_ID += 10

        jd_id_int = math.floor(JD_ID)
        jd_id_int -= jd_id_int % 10 
        JD_ID = float(jd_id_int)

    elif (layer == 2):
        JD_ID += 1

        JD_ID = float(math.floor(JD_ID))

    elif (layer == 3):
        JD_ID += .01

    return

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:p:",["file=","path="])
    except getopt.GetoptError as err:
        print(err)

    jd_file = "./jd.yml"
    jd_path = "./"

    for opt, arg in opts: 
        if opt in ('-h','--help'):
            usage()
            sys.exit()
        elif opt in ('-f','--file'):
            jd_file = arg 
        elif opt in ('-p','--path'):
            path = arg
        else:
            print("Argument {} not recognized",arg)
            usage()
            sys.exit(2)

    jd_file = open(jd_file,"r")
    jd_dict = yaml.safe_load(jd_file)
    os.chdir(jd_path)

    createFilesystem(1,jd_dict)

    jd_file.close()
