#!/bin/python3
import os 
import getopt
import yaml
import math
import sys

JD_ID = 00.00
META = False

def parseArgs():
    try: 
        opts, args = getopt.getopt(sys.argv[1:], "hf:p:m", 
                ["help", "file=", "path="])
    except:
        print("Puts mano q merda hein")
        sys.exit(2)

    source_file = "../res/jd.yaml"
    dest_path = "./"

    for opt, arg in opts: 
        if opt in ("-h","--help"): 
            print("Puts mano pede ajuda") 
            sys.exit(2)
        elif opt in ("-f", "--file"):
            source_file = arg
        elif opt in ("-p", "--path"):
            dest_path = arg
        elif opt in ("-m", "--meta"):
            META = True
        else:
            assert False, "unknown option" 

    return source_file, dest_path

def generateLayerPrefix(jd_id, level):
    if level == 1: 
        result = "{} - {}".format(math.floor(jd_id),math.floor(jd_id + 9))
    elif level == 2: 
        result = "{}".format(round(jd_id))
    else:
        result = "{:.2f}".format(jd_id)
    return result

def generateFileSystem(jd_data, dest_path): 
    global JD_ID

    os.chdir(dest_path)

    for upper in jd_data: 

        JD_ID += 10 
        current_upper_macro = JD_ID
        upper_name = "{} {}".format(generateLayerPrefix(JD_ID,1), upper)
        print(upper_name) 

        os.mkdir(upper_name)
        os.chdir(upper_name)

        for middle in jd_data[upper]:

            JD_ID += 1
            current_middle_macro = JD_ID
            middle_name = "{} {}".format(generateLayerPrefix(JD_ID,2), middle)
            print(middle_name) 

            os.mkdir(middle_name)
            os.chdir(middle_name) 

            for end in jd_data[upper][middle]:
                JD_ID += .01
                end_name = "{} {}".format(generateLayerPrefix(JD_ID,3), end)
                print(end_name) 

                os.mkdir(end_name)

            os.chdir("..")
            JD_ID = current_middle_macro

        os.chdir("..")
        JD_ID = current_upper_macro 

if __name__ == '__main__':

    source_file, dest_path = parseArgs()
    source_stream = open(source_file,'r') 
    jd_data = yaml.load(source_stream,Loader=yaml.Loader) 

    generateFileSystem(jd_data, dest_path)

    print(source_file, dest_path) 
    print("OKi") 
