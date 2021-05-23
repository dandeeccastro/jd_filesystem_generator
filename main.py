import os 
import argparse
import yaml
import math

JD_ID = 00.00

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
    parser = argparse.ArgumentParser(description="Gerador de Sistema de Arquivos Johnny Decimal")

    parser.add_argument("--file", 
            type=str, 
            default="jd.yaml", 
            help="O arquivo a ser usado para gerar o sistema de arquivos. Padrão: jd.yaml")
    parser.add_argument("--path", 
            type=str, 
            default="./", 
            help="A pasta aonde o sistema de arquivos será gerado. Padrão: diretório atual")

    args = parser.parse_args()

    os.chdir(args.path)
    jd_file = open(args.file,"r")
    jd_dict = yaml.safe_load(jd_file)

    createFilesystem(1,jd_dict)

    jd_file.close()
