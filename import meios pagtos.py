import pandas as pd
from datetime import datetime
from matplotlib.pyplot import pause
import pyautogui
import pyperclip
import time
import os
import time


# search_dir = "C:\\Users\\j.cesar.VASP\\Downloads"
# os.chdir(search_dir)
# files = filter(os.path.isfile, os.listdir(search_dir))
# files = [os.path.join(search_dir, f) for f in files] # add path to each file
# files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
# print(files)

# old_file = os.path.join(search_dir, files[0])
# time.sleep(5)

# new_file = os.path.join(search_dir, "003.csv")
# os.rename(old_file, new_file)


#tratar arquivo saida de frota

import numpy as np
import xlwt
import openpyxl

pathfile = 'C:\\Users\\j.cesar.VASP\\Downloads\\003.csv'
df = pd.read_csv(open( pathfile, 'r'), skiprows = 1, sep=';', encoding='UTF-8', usecols=[2, 5, 6, 7])

df.columns = ["FORMA DE PAGAMENTO","DATA","VALOR TOTAL","AGENCIA"]
# break

df["VALOR TOTAL"] = [float(str(i).replace(".","").replace(",", ".")) for i in df["VALOR TOTAL"]]
df['VALOR TOTAL'] = df['VALOR TOTAL'].astype(float) 
df_pix_por_agencia = df[df['FORMA DE PAGAMENTO'] == "PIX"].groupby(['AGENCIA','DATA'])['VALOR TOTAL'].sum()

# print(df_pix_por_agencia)
print('\n')
print('\033[33;36mTOTAL PIX POR AGENCIA: R$ \n{}\033[0;0m\n'.format(df_pix_por_agencia))


# resultado = round(df_pix_por_agencia,)
# total = resultado.sum()

# print(resultado)
# print(total)

data_atual = datetime.now().strftime("%d-%m-%Y")

data_atual = input("digite a data do arquivo: ")

df_pix_por_agencia.to_excel("C:\\Users\\j.cesar.VASP\\Downloads\\PIX AGENCIA"+data_atual +".xlsx")


# try:
#     os.remove("C:\\Users\\j.cesar.VASP\\Downloads\\003.csv")
#     print("Arquivo deletado com sucesso!")
# except FileNotFoundError:
#     print("O arquivo não foi encontrado.")
# except Exception as e:
#     print(f"Ocorreu um erro ao deletar o arquivo: {str(e)}")

# import globus.py
