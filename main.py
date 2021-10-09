import math
import sys, os

from pandas import *
import pandas as pd
from numpy import *
import numpy as np
import random
import re
from sys import *

# ubicacion = input(str("Hola para leer tu archivo indicame la direccion y el archivo como tal y su extension: "))

df = pd.DataFrame(pd.read_excel("./reviews_sentiment.xlsx", sheet_name=0))


'''def KNN():
    iter = int(input("Numero de iteraciones: "))
    listSumColum = []
    ListAttributeString = []
    ListAttributeNumeric = []
    TableFrecuencyString = []
    TableFrecuencyNumeric = []
    CountTest = 0  # CONTADOR DE FILAS DE PRUEBA
    CountTrainer = 0  # CONTADOR DE FILAS DE ENTRENAMIENTO
    ListTrainer = []  # FILAS QUE SERAN DE ENTRENAMIENTO
    NumIteraciones = 0  # CANTIDAD DE VECES QUE SE VA ITERAR LA FUNCION ZERO-R
    MaxRows = df.shape[0]  # CANTIDAD MAXIMA DE FILAS DEL DATA FRAME
    CountTrainer = MaxRows * 0.7  # CANTIDAD DE FILAS DE ENTRENAMIENTO 70%
    CountTest = MaxRows - int(CountTrainer)  # CANTIDAD DE FILAS DE PRUEBAS
    print("La cantidad de Filas del Dataframe es: ", df.shape[0])
    print("Cantidad de filas para Entrenamiento:  ", int(CountTrainer))
    print("Cantidad de filas para Pruebas:  ", int(CountTest))

    # CANTIDAD DE VECES QUE SE VA ITERAR EL ZERO-R
    for a in range(iter):

        print("\n \n \n _____________________Iteración numero ", str(a + 1), "_____________________")
        # SE CREA LA LISTA DE ENTRENAMIENTO CON NUMEROS RANDOM
        ListTrainer = random.sample(range(int(MaxRows)), int(CountTrainer))
        ListTest = range(int(MaxRows))
        ListTest = list(ListTest)

        # SE CREA UNA LISTA CON TODOS LOS VALORES Y SE ELIMINAN LOS DE LISTA DE ENTRENAMIENTO
        for x in ListTrainer:
            ListTest.remove(x)

        # CREAMOS DATAFRAME EN BASE EL INDICE DE LISTA DE ENTRENAMIENTO
        DataFrameTrainer = df.loc[ListTrainer]
        # CREAMOS DATAFRAME EN BASE EL INDICE DE LA LISTA DE PRUEBAS
        DataFrameTest = df.loc[ListTest]
        print("\n---Datos de Entrenamiento---")
        print(DataFrameTrainer)
        print("\n---Datos de Prueba---")
        print(DataFrameTest)
        # OBTENEMOS LOS NOMBRES DE LAS COLUMNAS
        columns_names = list(DataFrameTrainer.columns.values)
        # OBTENEMOS LA COLUMNA CLASE
        ClassName = columns_names.pop()
        # EN ESTE APARTADO IMPRIMIMOS LA CLASE QUE MAS SE REPITE LA CANTIDAD DE VECES QUE SE ENCUENTRA TANTO EN EL DATAFRAME DE PRUEBA Y ENTRENAMIENTO
        DataFrameTrainerNumeric =  DataFrameTrainer.select_dtypes(include=['int64', 'float64'])
        DataFrameTrainerString = DataFrameTrainer.select_dtypes(include=['object', 'bool'])

        columns_numeric = list(DataFrameTrainerNumeric.columns.values)
        columns_string = list(DataFrameTrainerString.columns.values)

        # AGREGANDO ETIQUETAS DE LOS ATRIBUTOS
        for a in columns_string:
            ListAttributeString.append(DataFrameTrainerString[a].unique().tolist())

        # SE CONSTRUYE LAS TABLAS DE FRECUENCIA


        sys.exit()

    #os.system("PAUSE")
    #print("\n" * 100)'''

def DistribucionNormal(media,desv,x):
        total = 1/(sqrt(2*math.pi)*desv)*math.e**-(((x-media)**2)/(2*desv**2))
        return total
def DividirDataFrame(df):
    MaxRows = df.shape[0]  # CANTIDAD MAXIMA DE FILAS DEL DATA FRAME
    CountTrainer = MaxRows * 0.7  # CANTIDAD DE FILAS DE ENTRENAMIENTO 70%
    CountTest = MaxRows - int(CountTrainer)  # CANTIDAD DE FILAS DE PRUEBAS
    print("La cantidad de Filas del Dataframe es: ", df.shape[0])
    print("Cantidad de filas para Entrenamiento:  ", int(CountTrainer))
    print("Cantidad de filas para Pruebas:  ", int(CountTest))
    # SE CREA LA LISTA DE ENTRENAMIENTO CON NUMEROS RANDOM
    ListTrainer = random.sample(range(int(MaxRows)), int(CountTrainer))
    ListTest = range(int(MaxRows))
    ListTest = list(ListTest)

    # SE CREA UNA LISTA CON TODOS LOS VALORES Y SE ELIMINAN LOS DE LISTA DE ENTRENAMIENTO
    for x in ListTrainer:
        ListTest.remove(x)

    # CREAMOS DATAFRAME EN BASE EL INDICE DE LISTA DE ENTRENAMIENTO
    DataFrameTrainer = df.loc[ListTrainer]
    # CREAMOS DATAFRAME EN BASE EL INDICE DE LA LISTA DE PRUEBAS
    DataFrameTest = df.loc[ListTest]
    print("\n---Datos de Entrenamiento---")
    print(DataFrameTrainer.head(5).to_string())
    print("\n---Datos de Prueba---")
    print(DataFrameTest)
    return DataFrameTrainer, DataFrameTest

def SepararStringConNumerico(DataFrameTrainer, DataFrameTest): # Divide los datos del dataframe segun el tipo de dato que sean
    columns_numeric_Name = list((DataFrameTrainer.select_dtypes(include=['int64', 'float64'])).columns.values)
    columns_string_Name = list((DataFrameTrainer.select_dtypes(include=['object', 'bool'])).columns.values)
    return columns_numeric_Name, columns_string_Name

def DefinirTipoDeDato(HeaderString,HeaderNumeric):
    TipesString =df[HeaderString].dtypes
    TipesNumeric = df[HeaderNumeric].dtypes

    return TipesString,TipesNumeric

def CalcularDistanciaEuclidiana():
    pass
def CalcularDistanciaManhattan():
    pass
def CalcularDistanciaHamming():
    pass
def Normalizar():
    pass
def KNN():
    DataFrames = DividirDataFrame(df)               #SE RECIBEN LOS DATAFRAME DE DIVIDIRDATAFRAME() Y SE DIVIDEN
    DataFrameTrainer = DataFrames[0]
    DataFrameTest = DataFrames[1]
    HeaderNames = SepararStringConNumerico(DataFrameTrainer, DataFrameTest)
    HeaderNamesNumeric = HeaderNames[0]             #CONTIENE EL NOMBRE DE LAS COLUMNAS QUE SON NUMERICAS
    HeaderNamesString = HeaderNames[1]              #CONTIENE EL NOMBRE DE LAS COLUMNAS QUE SON CATEGORICAS
    Types =  DefinirTipoDeDato(HeaderNamesString,HeaderNamesNumeric)
    TipesString = Types[0]                          #SE OBTIENE EL TIPO DE DATO DE CADA COLUMNA
    TipesNumeric = Types[1]







while True:
    print("1) KNN")
    print("0) Salir")
    op = input()

    if op == "1":
        KNN()
    elif op == "0":
        break
