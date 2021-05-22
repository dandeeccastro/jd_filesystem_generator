import os 
import argparse
import yaml
import math

JD_ID = 00.00
# Recebe um pedaço da árvore JD
# Se for a lista de folhas, itera por elas e termina
# Se for nó, cria ele, entra e se chama de novo
def create_directory(layer, jd_data):
    if type(jd_data) is dict:
        for kv_pair in jd_data.items():
            update_jd_id(layer)
            os.mkdir(f"{get_jd_id_prefix(layer)} {kv_pair[0]}")
            os.chdir(f"./{get_jd_id_prefix(layer)} {kv_pair[0]}")
            create_directory(layer + 1, kv_pair[1])
        os.chdir("..")
    else:
        for i in jd_data:
            update_jd_id(layer)
            os.mkdir(f"{get_jd_id_prefix(layer)} {i}")
        os.chdir("..")

def get_jd_id_prefix(layer):
    global JD_ID
    result = math.floor(JD_ID)

    if (layer == 1):
        result -= result % 10 
        return f"{result} - {result + 9}"
    elif (layer == 2):
        return f"{result}"
    elif (layer == 3):
        return "{0:.2f}".format(round(JD_ID,2))
        

def update_jd_id(layer):
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
    jd_file = open("jd.yaml","r")
    jd_dict = yaml.safe_load(jd_file)

    print(jd_dict)
    create_directory(1,jd_dict)

    jd_file.close()
