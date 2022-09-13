import enum
import numpy as np
from multiprocessing.sharedctypes import Value
from optparse import Values
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from turtle import right, title, width
from unittest import result
from sys import exit
from matplotlib.pyplot import close, subplot
import pandas as pd
import matplotlib.pyplot as plt
from pyparsing import anyOpenTag
import seaborn as sns
from pandas import read_excel

root = Tk()
root.title('Heatmap generator!')
root.geometry("400x600")

bool_cnn_fuerzas = False
bool_clinic_fuerzas = False
bool_cnn_frecuencia = False
bool_clinic_frecuencia = False
bool_emol_fuerzas = False
bool_emol_frecuencia = False
bool_chile_fuerzas = False
bool_chile_frecuencia = False

def cargar_archivos():
    path = filedialog.askopenfilenames()
    for item in path:
        if(item.__contains__('Fuerzas')):
            if(item.__contains__('CNN')):
                cnn_fuerzas = read_excel(item)
                lista_valores_cnn = list(cnn_fuerzas.columns.values)
                global bool_cnn_fuerzas
                bool_cnn_fuerzas = True
                for item in lista_valores_cnn:
                    my_listbox.insert(END, item)
            if(item.__contains__('Clinic')):
                clinic_fuerzas = read_excel(item)
                lista_valores_clinic = list(clinic_fuerzas.columns.values)
                global bool_clinic_fuerzas
                bool_clinic_fuerzas = True
                for item in lista_valores_clinic:
                    my_listbox.insert(END, item)
            if(item.__contains__('Emol')):
                emol_fuerzas = read_excel(item)
                lista_valores_emol = list(emol_fuerzas.columns.values)
                global bool_emol_fuerzas
                bool_emol_fuerzas = True
                for item in lista_valores_emol:
                    my_listbox.insert(END, item)
            if(item.__contains__('Chile')):
                chile_fuerzas = read_excel(item)
                lista_valores_chile = list(chile_fuerzas.columns.values)
                global bool_chile_fuerzas
                bool_chile_fuerzas = True
                for item in lista_valores_chile:
                    my_listbox.insert(END, item)
        if(item.__contains__('Frecuencia')):
            if(item.__contains__('CNN')):
                cnn_frecuencia = read_excel(item)
                lista_valores_cnn_frecuencia = list(cnn_frecuencia.columns.values)
                global bool_cnn_frecuencia
                bool_cnn_frecuencia = True
                for item in lista_valores_cnn_frecuencia:
                    my_listbox.insert(END, item)
            if(item.__contains__('Clinic')):
                clinic_frecuencia = read_excel(item)
                lista_valores_clinic_frecuencia = list(clinic_frecuencia.columns.values)
                global bool_clinic_frecuencia
                bool_clinic_frecuencia = True
                for item in lista_valores_clinic_frecuencia:
                    my_listbox.insert(END, item)
            if(item.__contains__('Emol')):
                emol_frecuencia = read_excel(item)
                lista_valores_emol = list(emol_frecuencia.columns.values)
                global bool_emol_frecuencia
                bool_emol_frecuencia = True
                for item in lista_valores_emol:
                    my_listbox.insert(END, item)
            if(item.__contains__('Chile')):
                chile_frecuencia = read_excel(item)
                lista_valores_chile = list(chile_frecuencia.columns.values)
                global bool_chile_frecuencia
                bool_chile_frecuencia = True
                for item in lista_valores_chile:
                    my_listbox.insert(END, item)
    done()

def done():
    messagebox.showinfo("Exito", "Archivo subido correctamente")

def wrong_date():
    messagebox.showinfo("Error", "Fecha ingresa no existe dentro de la data")

def generar_heatmap():
    parametros = []
    parametros_palabras = []
    result = ''
    for item in my_listbox.curselection():
        result = str(my_listbox.get(item))
        parametros_palabras.append(result)
    for item in my_listbox.curselection():
        parametros.append(item)
    primera_fecha = l_name.get()
    ultima_fecha = address.get()
    crear_grafico(parametros, primera_fecha, ultima_fecha, parametros_palabras)
    
def crear_grafico(parametros, primera_fecha, ultima_fecha, parametros_palabras):
    if(bool_cnn_fuerzas == True):
        fechas_cnn = pd.read_excel('Fuerzas_CNN-Nacional (2013-2022).xlsx')
        index_primera_fecha = fechas_cnn.index[fechas_cnn['Fechas'] == primera_fecha].tolist()
        if(len(index_primera_fecha) == 0):
            return wrong_date()
        first_num = int(index_primera_fecha[0])
        index_ultima_fecha = fechas_cnn.index[fechas_cnn['Fechas'] == ultima_fecha].tolist()
        if(len(index_ultima_fecha) == 0):
            return wrong_date()
        last_num = int(index_ultima_fecha[0])
        height = last_num - first_num
        cnn_fuerzas = pd.read_excel('Fuerzas_CNN-Nacional (2013-2022).xlsx', usecols=parametros, skiprows=range(first_num), nrows=height+1)
        cnn_fuerzas.columns = parametros_palabras
        corr = cnn_fuerzas.corr()
        save = sns.heatmap(corr, annot=True, cmap="YlGnBu", cbar=False)
        plt.show()
    if(bool_clinic_fuerzas == True):
        fechas_clinic = pd.read_excel('Fuerzas_TheClinic (sin compuestas).xlsx')
        index_primera_fecha = fechas_clinic.index[fechas_clinic['Fechas']== primera_fecha].tolist()
        if(len(index_primera_fecha) == 0):
            return wrong_date()
        first_num = int(index_primera_fecha[0])
        index_ultima_fecha = fechas_clinic.index[fechas_clinic['Fechas']== ultima_fecha].tolist()
        if(len(index_ultima_fecha) == 0):
            return wrong_date()
        last_num = int(index_ultima_fecha[0])
        height = last_num - first_num
        clinic_fuerzas = pd.read_excel('Fuerzas_TheClinic (sin compuestas).xlsx', usecols=parametros, skiprows=range(first_num), nrows=height+1)
        clinic_fuerzas.columns = parametros_palabras
        corr = clinic_fuerzas.corr()
        save = sns.heatmap(corr, annot=True, cmap="YlGnBu", cbar=False)
        plt.show()
    if(bool_emol_fuerzas == True):
        fechas_emol = pd.read_excel('Fuerzas_Emol-Nacional.xlsx')
        index_primera_fecha = fechas_emol.index[fechas_emol['Fechas']== primera_fecha].tolist()
        if(len(index_primera_fecha) == 0):
            return wrong_date()
        first_num = int(index_primera_fecha[0])
        index_ultima_fecha = fechas_emol.index[fechas_emol['Fechas']== ultima_fecha].tolist()
        if(len(index_ultima_fecha) == 0):
            return wrong_date()
        last_num = int(index_ultima_fecha[0])
        height = last_num - first_num
        emol_fuerzas = pd.read_excel('Fuerzas_Emol-Nacional (2013-2022).xlsx', usecols=parametros, skiprows=range(first_num), nrows=height+1)
        emol_fuerzas.columns = parametros_palabras
        corr = emol_fuerzas.corr()
        save = sns.heatmap(corr, annot=True, cmap="YlGnBu", cbar=False)
        plt.show()
    if(bool_chile_fuerzas == True):
        fechas_chile = pd.read_excel('Fuerzas_SoyChile (ok).xlsx')
        index_primera_fecha = fechas_chile.index[fechas_chile['Fechas']== primera_fecha].tolist()
        if(len(index_primera_fecha) == 0):
            return wrong_date()
        first_num = int(index_primera_fecha[0])
        index_ultima_fecha = fechas_chile.index[fechas_chile['Fechas']== ultima_fecha].tolist()
        if(len(index_ultima_fecha) == 0):
            return wrong_date()
        last_num = int(index_ultima_fecha[0])
        height = last_num - first_num
        chile_fuerzas = pd.read_excel('Fuerzas_SoyChile (ok).xlsx', usecols=parametros, skiprows=range(first_num), nrows=height+1)
        chile_fuerzas.columns = parametros_palabras
        corr = chile_fuerzas.corr()
        save = sns.heatmap(corr, annot=True, cmap="YlGnBu", cbar=False)
        plt.show()    

def generar_barras():
    parametros = []
    parametros_palabras = []
    result = ''
    for item in my_listbox.curselection():
        result = str(my_listbox.get(item))
        parametros_palabras.append(result)
    for item in my_listbox.curselection():
        parametros.append(item)
    primera_fecha = l_name.get()
    ultima_fecha = address.get()
    crear_barras(parametros, primera_fecha, ultima_fecha, parametros_palabras)

def crear_barras(parametros, primera_fecha, ultima_fecha, parametros_palabras):
    if(bool_cnn_frecuencia == True):
        fechas_cnn = pd.read_excel('Frecuencias_CNN-Nacional (2013-2022).xlsx')
        index_primera_fecha = fechas_cnn.index[fechas_cnn['Fechas'] == primera_fecha].tolist()
        if(len(index_primera_fecha) == 0):
            return wrong_date()
        first_num = int(index_primera_fecha[0])
        index_ultima_fecha = fechas_cnn.index[fechas_cnn['Fechas'] == ultima_fecha].tolist()
        if(len(index_ultima_fecha) == 0):
            return wrong_date()
        last_num = int(index_ultima_fecha[0])
        height = last_num - first_num
        cnn_frecuencia = pd.read_excel('Frecuencias_CNN-Nacional (2013-2022).xlsx', usecols=parametros, skiprows=range(first_num), nrows=height+1)
        cnn_frecuencia_fechas = pd.read_excel('Frecuencias_CNN-Nacional (2013-2022).xlsx', usecols=[0], skiprows=range(first_num), nrows=height+1)
        flag = False
        cols = len(parametros)
        i = 0
        j = 0
        while (flag == False):
            if(j < cols):
                temp = cnn_frecuencia.iloc[i,j]    
                array_temp = temp.split("-")
                result = sum(map(int, array_temp))
                cnn_frecuencia.iat[i,j] = result
                j = j + 1
            if(j+1 > cols):
                j = 0
                i = i + 1
            if(i == height+1):
                break;
        fechas_cnn_frecuencia = cnn_frecuencia_fechas.to_numpy()
        cnn_frecuencia.columns = parametros_palabras
        cnn_frecuencia.insert(0, "Fechas", fechas_cnn_frecuencia)
        cnn_frecuencia.plot(x = cnn_frecuencia.columns[0], kind="line")
        plt.title("Frecuencia")
        plt.xlabel("Fechas")
        plt.ylabel("Cantidad")
        plt.show()
    if(bool_emol_frecuencia == True):
        fechas_emol = pd.read_excel('Frecuencias_Emol-Nacional.xlsx')
        index_primera_fecha = fechas_emol.index[fechas_emol['Fechas'] == primera_fecha].tolist()
        if(len(index_primera_fecha) == 0):
            return wrong_date()
        first_num = int(index_primera_fecha[0])
        index_ultima_fecha = fechas_emol.index[fechas_emol['Fechas'] == ultima_fecha].tolist()
        if(len(index_ultima_fecha) == 0):
            return wrong_date()
        last_num = int(index_ultima_fecha[0])
        height = last_num - first_num
        emol_frecuencia = pd.read_excel('Frecuencias_Emol-Nacional.xlsx', usecols=parametros, skiprows=range(first_num), nrows=height+1)
        emol_frecuencia_fechas = pd.read_excel('Frecuencias_Emol-Nacional.xlsx', usecols=[0], skiprows=range(first_num), nrows=height+1)
        flag = False
        cols = len(parametros)
        i = 0
        j = 0
        while (flag == False):
            if(j < cols):
                temp = emol_frecuencia.iloc[i,j]    
                array_temp = temp.split("-")
                result = sum(map(int, array_temp))
                emol_frecuencia.iat[i,j] = result
                j = j + 1
            if(j+1 > cols):
                j = 0
                i = i + 1
            if(i == height+1):
                break;
        fechas_emol_frecuencia = emol_frecuencia_fechas.to_numpy()
        emol_frecuencia.columns = parametros_palabras
        emol_frecuencia.insert(0, "Fechas", fechas_emol_frecuencia)
        emol_frecuencia.plot(x = emol_frecuencia.columns[0], kind="line")
        plt.title("Frecuencia")
        plt.xlabel("Fechas")
        plt.ylabel("Cantidad")
        plt.show()
    if(bool_chile_frecuencia == True):
        fechas_chile = pd.read_excel('Frecuencias_SoyChile.xlsx')
        index_primera_fecha = fechas_chile.index[fechas_chile['Fechas'] == primera_fecha].tolist()
        if(len(index_primera_fecha) == 0):
            return wrong_date()
        first_num = int(index_primera_fecha[0])
        index_ultima_fecha = fechas_chile.index[fechas_chile['Fechas'] == ultima_fecha].tolist()
        if(len(index_ultima_fecha) == 0):
            return wrong_date()
        last_num = int(index_ultima_fecha[0])
        height = last_num - first_num
        chile_frecuencia = pd.read_excel('Frecuencias_SoyChile.xlsx', usecols=parametros, skiprows=range(first_num), nrows=height+1)
        chile_frecuencia_fechas = pd.read_excel('Frecuencias_SoyChile.xlsx', usecols=[0], skiprows=range(first_num), nrows=height+1)
        flag = False
        cols = len(parametros)
        i = 0
        j = 0
        while (flag == False):
            if(j < cols):
                temp = chile_frecuencia.iloc[i,j]    
                array_temp = temp.split("-")
                result = sum(map(int, array_temp))
                chile_frecuencia.iat[i,j] = result
                j = j + 1
            if(j+1 > cols):
                j = 0
                i = i + 1
            if(i == height+1):
                break;
        fechas_chile_frecuencia = chile_frecuencia_fechas.to_numpy()
        chile_frecuencia.columns = parametros_palabras
        chile_frecuencia.insert(0, "Fechas", fechas_chile_frecuencia)
        chile_frecuencia.plot(x = chile_frecuencia.columns[0], kind="line")
        plt.title("Frecuencia")
        plt.xlabel("Fechas")
        plt.ylabel("Cantidad")
        plt.show()
    if(bool_clinic_frecuencia == True):
        fechas_clinic = pd.read_excel('Frecuencias_TheClinic (sin compuestas).xlsx')
        index_primera_fecha = fechas_clinic.index[fechas_clinic['Fechas'] == primera_fecha].tolist()
        if(len(index_primera_fecha) == 0):
            return wrong_date()
        first_num = int(index_primera_fecha[0])
        index_ultima_fecha = fechas_clinic.index[fechas_cnn['Fechas'] == ultima_fecha].tolist()
        if(len(index_ultima_fecha) == 0):
            return wrong_date()
        last_num = int(index_ultima_fecha[0])
        height = last_num - first_num
        clinic_frecuencia = pd.read_excel('Frecuencias_TheClinic (sin compuestas).xlsx', usecols=parametros, skiprows=range(first_num), nrows=height+1)
        clinic_frecuencia_fechas = pd.read_excel('Frecuencias_TheClinic (sin compuestas).xlsx', usecols=[0], skiprows=range(first_num), nrows=height+1)
        flag = False
        cols = len(parametros)
        i = 0
        j = 0
        while (flag == False):
            if(j < cols):
                temp = clinic_frecuencia.iloc[i,j]    
                array_temp = temp.split("-")
                result = sum(map(int, array_temp))
                clinic_frecuencia.iat[i,j] = result
                j = j + 1
            if(j+1 > cols):
                j = 0
                i = i + 1
            if(i == height+1):
                break;
        fechas_clinic_frecuencia = clinic_frecuencia_fechas.to_numpy()
        clinic_frecuencia.columns = parametros_palabras
        clinic_frecuencia.insert(0, "Fechas", fechas_clinic_frecuencia)
        clinic_frecuencia.plot(x = clinic_frecuencia.columns[0], kind="line")
        plt.title("Frecuencia")
        plt.xlabel("Fechas")
        plt.ylabel("Cantidad")
        plt.show()

def generar_barras_especificas():
    parametros = []
    parametros_palabras = []
    result = ''
    for item in my_listbox.curselection():
        result = str(my_listbox.get(item))
        parametros_palabras.append(result)
    for item in my_listbox.curselection():
        parametros.append(item)
    primera_fecha = l_name.get()
    ultima_fecha = address.get()
    crear_barras_especificas(parametros, primera_fecha, ultima_fecha, parametros_palabras)

def crear_barras_especificas(parametros, primera_fecha, ultima_fecha, parametros_palabras):
    titular = []
    bajada = []
    cuerpo = []
    if(bool_cnn_frecuencia == True):
        fechas_cnn = pd.read_excel('Frecuencias_CNN-Nacional (2013-2022).xlsx')
        index_primera_fecha = fechas_cnn.index[fechas_cnn['Fechas'] == primera_fecha].tolist()
        if(len(index_primera_fecha) == 0):
            return wrong_date()
        first_num = int(index_primera_fecha[0])
        index_ultima_fecha = fechas_cnn.index[fechas_cnn['Fechas'] == ultima_fecha].tolist()
        if(len(index_ultima_fecha) == 0):
            return wrong_date()
        last_num = int(index_ultima_fecha[0])
        height = last_num - first_num
        cnn_frecuencia = pd.read_excel('Frecuencias_CNN-Nacional (2013-2022).xlsx', usecols=parametros, skiprows=range(first_num), nrows=height+1)
        cnn_frecuencia_fechas = pd.read_excel('Frecuencias_CNN-Nacional (2013-2022).xlsx', usecols=[0], skiprows=range(first_num), nrows=height+1)
        flag = False
        cols = len(parametros)
        i = 0
        j = 0
        while (flag == False):
            if(j < cols):
                temp = cnn_frecuencia.iloc[i,j]    
                array_temp = temp.split("-")
                titular.append(array_temp[0])
                bajada.append(array_temp[1])
                cuerpo.append(array_temp[2])
                cnn_frecuencia.iat[i,j] = result
                j = j + 1
            if(j+1 > cols):
                j = 0
                i = i + 1
            if(i == height+1):
                break;
        x = 0;
        y = 0;
        z = 0;
        matriz_titular = np.empty((height+1, cols), int)
        matriz_bajada = np.empty((height+1, cols), int)
        matriz_cuerpo = np.empty((height+1, cols), int)
        for x in range(height+1):
            for y in range (cols):
                matriz_titular[x][y] = titular[z];
                z = z+1;
        x = 0;
        y = 0;
        z = 0;
        for x in range(height+1):
            for y in range (cols):
                matriz_bajada[x][y] = bajada[z];
                z = z+1
        x = 0
        y = 0
        z = 0
        for x in range(height+1):
            for y in range (cols):
                matriz_cuerpo[x][y] = cuerpo[z]
                z = z+1
        df_titular = pd.DataFrame(matriz_titular)
        df_bajada = pd.DataFrame(matriz_bajada)
        df_cuerpo = pd.DataFrame(matriz_cuerpo)
        df_titular.columns = parametros_palabras
        df_bajada.columns = parametros_palabras
        df_cuerpo.columns = parametros_palabras
        fechas_cnn_frecuencia = cnn_frecuencia_fechas.to_numpy()
        df_titular.insert(0, "Fechas", fechas_cnn_frecuencia)
        df_bajada.insert(0, "Fechas", fechas_cnn_frecuencia)
        df_cuerpo.insert(0, "Fechas", fechas_cnn_frecuencia)
        # ax = df_titular.plot(x = df_titular.columns[0], kind="line")
        # df_bajada.plot(x = df_bajada.columns[0], kind="line", ax = ax)
        # df_cuerpo.plot(x = df_cuerpo.columns[0], kind="line", ax = ax)
        df_titular.plot(x = df_titular.columns[0], kind="line", title ="# de Titulares")
        df_bajada.plot(x = df_bajada.columns[0], kind="line", title ="# de Bajadas")
        df_cuerpo.plot(x = df_cuerpo.columns[0], kind="line", title ="# de Cuerpo")
        plt.show()
    if(bool_emol_frecuencia == True):
        fechas_emol = pd.read_excel('Frecuencias_Emol-Nacional.xlsx')
        index_primera_fecha = fechas_emol.index[fechas_emol['Fechas'] == primera_fecha].tolist()
        if(len(index_primera_fecha) == 0):
            return wrong_date()
        first_num = int(index_primera_fecha[0])
        index_ultima_fecha = fechas_emol.index[fechas_emol['Fechas'] == ultima_fecha].tolist()
        if(len(index_ultima_fecha) == 0):
            return wrong_date()
        last_num = int(index_ultima_fecha[0])
        height = last_num - first_num
        emol_frecuencia = pd.read_excel('Frecuencias_Emol-Nacional.xlsx', usecols=parametros, skiprows=range(first_num), nrows=height+1)
        emol_frecuencia_fechas = pd.read_excel('Frecuencias_Emol-Nacional.xlsx', usecols=[0], skiprows=range(first_num), nrows=height+1)
        flag = False
        cols = len(parametros)
        i = 0
        j = 0
        while (flag == False):
            if(j < cols):
                temp = emol_frecuencia.iloc[i,j]    
                array_temp = temp.split("-")
                titular.append(array_temp[0])
                bajada.append(array_temp[1])
                cuerpo.append(array_temp[2])
                emol_frecuencia.iat[i,j] = result
                j = j + 1
            if(j+1 > cols):
                j = 0
                i = i + 1
            if(i == height+1):
                break;
        x = 0;
        y = 0;
        z = 0;
        matriz_titular = np.empty((height+1, cols), int)
        matriz_bajada = np.empty((height+1, cols), int)
        matriz_cuerpo = np.empty((height+1, cols), int)
        for x in range(height+1):
            for y in range (cols):
                matriz_titular[x][y] = titular[z];
                z = z+1;
        x = 0;
        y = 0;
        z = 0;
        for x in range(height+1):
            for y in range (cols):
                matriz_bajada[x][y] = bajada[z];
                z = z+1
        x = 0
        y = 0
        z = 0
        for x in range(height+1):
            for y in range (cols):
                matriz_cuerpo[x][y] = cuerpo[z]
                z = z+1
        df_titular = pd.DataFrame(matriz_titular)
        df_bajada = pd.DataFrame(matriz_bajada)
        df_cuerpo = pd.DataFrame(matriz_cuerpo)
        df_titular.columns = parametros_palabras
        df_bajada.columns = parametros_palabras
        df_cuerpo.columns = parametros_palabras
        fechas_emol_frecuencia = emol_frecuencia_fechas.to_numpy()
        df_titular.insert(0, "Fechas", fechas_emol_frecuencia)
        df_bajada.insert(0, "Fechas", fechas_emol_frecuencia)
        df_cuerpo.insert(0, "Fechas", fechas_emol_frecuencia)
        # ax = df_titular.plot(x = df_titular.columns[0], kind="line")
        # df_bajada.plot(x = df_bajada.columns[0], kind="line", ax = ax)
        # df_cuerpo.plot(x = df_cuerpo.columns[0], kind="line", ax = ax)
        df_titular.plot(x = df_titular.columns[0], kind="line", title ="# de Titulares")
        df_bajada.plot(x = df_bajada.columns[0], kind="line", title ="# de Bajadas")
        df_cuerpo.plot(x = df_cuerpo.columns[0], kind="line", title ="# de Cuerpo")
        plt.show()
    if(bool_chile_frecuencia == True):
        fechas_chile = pd.read_excel('Frecuencias_SoyChile.xlsx')
        index_primera_fecha = fechas_chile.index[fechas_chile['Fechas'] == primera_fecha].tolist()
        if(len(index_primera_fecha) == 0):
            return wrong_date()
        first_num = int(index_primera_fecha[0])
        index_ultima_fecha = fechas_chile.index[fechas_chile['Fechas'] == ultima_fecha].tolist()
        if(len(index_ultima_fecha) == 0):
            return wrong_date()
        last_num = int(index_ultima_fecha[0])
        height = last_num - first_num
        chile_frecuencia = pd.read_excel('Frecuencias_SoyChile.xlsx', usecols=parametros, skiprows=range(first_num), nrows=height+1)
        chile_frecuencia_fechas = pd.read_excel('Frecuencias_SoyChile.xlsx', usecols=[0], skiprows=range(first_num), nrows=height+1)
        flag = False
        cols = len(parametros)
        i = 0
        j = 0
        while (flag == False):
            if(j < cols):
                temp = chile_frecuencia.iloc[i,j]    
                array_temp = temp.split("-")
                titular.append(array_temp[0])
                bajada.append(array_temp[1])
                cuerpo.append(array_temp[2])
                chile_frecuencia.iat[i,j] = result
                j = j + 1
            if(j+1 > cols):
                j = 0
                i = i + 1
            if(i == height+1):
                break;
        x = 0;
        y = 0;
        z = 0;
        matriz_titular = np.empty((height+1, cols), int)
        matriz_bajada = np.empty((height+1, cols), int)
        matriz_cuerpo = np.empty((height+1, cols), int)
        for x in range(height+1):
            for y in range (cols):
                matriz_titular[x][y] = titular[z];
                z = z+1;
        x = 0;
        y = 0;
        z = 0;
        for x in range(height+1):
            for y in range (cols):
                matriz_bajada[x][y] = bajada[z];
                z = z+1
        x = 0
        y = 0
        z = 0
        for x in range(height+1):
            for y in range (cols):
                matriz_cuerpo[x][y] = cuerpo[z]
                z = z+1
        df_titular = pd.DataFrame(matriz_titular)
        df_bajada = pd.DataFrame(matriz_bajada)
        df_cuerpo = pd.DataFrame(matriz_cuerpo)
        df_titular.columns = parametros_palabras
        df_bajada.columns = parametros_palabras
        df_cuerpo.columns = parametros_palabras
        fechas_chile_frecuencia = chile_frecuencia_fechas.to_numpy()
        df_titular.insert(0, "Fechas", fechas_chile_frecuencia)
        df_bajada.insert(0, "Fechas", fechas_chile_frecuencia)
        df_cuerpo.insert(0, "Fechas", fechas_chile_frecuencia)
        # ax = df_titular.plot(x = df_titular.columns[0], kind="line")
        # df_bajada.plot(x = df_bajada.columns[0], kind="line", ax = ax)
        # df_cuerpo.plot(x = df_cuerpo.columns[0], kind="line", ax = ax)
        df_titular.plot(x = df_titular.columns[0], kind="line", title ="# de Titulares")
        df_bajada.plot(x = df_bajada.columns[0], kind="line", title ="# de Bajadas")
        df_cuerpo.plot(x = df_cuerpo.columns[0], kind="line", title ="# de Cuerpo")
        plt.show()
    if(bool_clinic_frecuencia == True):
        fechas_clinic = pd.read_excel('Frecuencias_TheClinic (sin compuestas).xlsx')
        index_primera_fecha = fechas_clinic.index[fechas_clinic['Fechas'] == primera_fecha].tolist()
        if(len(index_primera_fecha) == 0):
            return wrong_date()
        first_num = int(index_primera_fecha[0])
        index_ultima_fecha = fechas_clinic.index[fechas_clinic['Fechas'] == ultima_fecha].tolist()
        if(len(index_ultima_fecha) == 0):
            return wrong_date()
        last_num = int(index_ultima_fecha[0])
        height = last_num - first_num
        clinic_frecuencia = pd.read_excel('Frecuencias_TheClinic (sin compuestas).xlsx', usecols=parametros, skiprows=range(first_num), nrows=height+1)
        clinic_frecuencia_fechas = pd.read_excel('Frecuencias_TheClinic (sin compuestas).xlsx', usecols=[0], skiprows=range(first_num), nrows=height+1)
        flag = False
        cols = len(parametros)
        i = 0
        j = 0
        while (flag == False):
            if(j < cols):
                temp = clinic_frecuencia.iloc[i,j]    
                array_temp = temp.split("-")
                titular.append(array_temp[0])
                bajada.append(array_temp[1])
                cuerpo.append(array_temp[2])
                clinic_frecuencia.iat[i,j] = result
                j = j + 1
            if(j+1 > cols):
                j = 0
                i = i + 1
            if(i == height+1):
                break;
        x = 0;
        y = 0;
        z = 0;
        matriz_titular = np.empty((height+1, cols), int)
        matriz_bajada = np.empty((height+1, cols), int)
        matriz_cuerpo = np.empty((height+1, cols), int)
        for x in range(height+1):
            for y in range (cols):
                matriz_titular[x][y] = titular[z];
                z = z+1;
        x = 0;
        y = 0;
        z = 0;
        for x in range(height+1):
            for y in range (cols):
                matriz_bajada[x][y] = bajada[z];
                z = z+1
        x = 0
        y = 0
        z = 0
        for x in range(height+1):
            for y in range (cols):
                matriz_cuerpo[x][y] = cuerpo[z]
                z = z+1
        df_titular = pd.DataFrame(matriz_titular)
        df_bajada = pd.DataFrame(matriz_bajada)
        df_cuerpo = pd.DataFrame(matriz_cuerpo)
        df_titular.columns = parametros_palabras
        df_bajada.columns = parametros_palabras
        df_cuerpo.columns = parametros_palabras
        fechas_clinic_frecuencia = clinic_frecuencia_fechas.to_numpy()
        df_titular.insert(0, "Fechas", fechas_clinic_frecuencia)
        df_bajada.insert(0, "Fechas", fechas_clinic_frecuencia)
        df_cuerpo.insert(0, "Fechas", fechas_clinic_frecuencia)
        # ax = df_titular.plot(x = df_titular.columns[0], kind="line")
        # df_bajada.plot(x = df_bajada.columns[0], kind="line", ax = ax)
        # df_cuerpo.plot(x = df_cuerpo.columns[0], kind="line", ax = ax)
        df_titular.plot(x = df_titular.columns[0], kind="line", title ="# de Titulares")
        df_bajada.plot(x = df_bajada.columns[0], kind="line", title ="# de Bajadas")
        df_cuerpo.plot(x = df_cuerpo.columns[0], kind="line", title ="# de Cuerpo")
        plt.show()

# Create Text Boxes
l_name = Entry(root, width=50)
l_name.pack()
l_name.insert(0, "Ingrese fecha inicial con formato YY/MM/DD")
address = Entry(root, width=50)
address.pack()
address.insert(0, "Ingrese fecha final con formato YY/MM/DD")

my_frame = Frame(root)
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)


my_listbox = Listbox(my_frame, width=50, yscrollcommand=my_scrollbar.set, selectmode=MULTIPLE)
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side = RIGHT, fill=Y)
my_frame.pack()
my_listbox.pack(pady = 15)

# Create Submit Button
subida = Button(root, text="Cargar archivos", command=cargar_archivos)
subida.pack(pady=10, padx=10, ipadx=100)

graficos = Button(root, text="Grafico heatmap", command=generar_heatmap)
graficos.pack(pady=10, padx=10, ipadx=100)

barras = Button(root, text="Grafico de linea de tendencia general", command=generar_barras)
barras.pack(pady=10, padx=10, ipadx=50)

exportar = Button(root, text="Grafico de titular-bajada-cuerpo", command=generar_barras_especificas)
exportar.pack(pady=10, padx=10, ipadx=60)


root.mainloop()