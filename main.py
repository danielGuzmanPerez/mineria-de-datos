# import math
import sys, os

# from pandas import *
import pandas as pd
from numpy import *
import numpy as np
import random

# import re
# from sys import *

# ubicacion = input(str("Hola para leer tu archivo indicame la direccion y el archivo como tal y su extension: "))
# global Column_Target
Column_Target = 0
# global TargetType
TargetType = 0

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


def DistribucionNormal(media, desv, x):
    total = 1 / (sqrt(2 * math.pi) * desv) * math.e ** -(((x - media) ** 2) / (2 * desv ** 2))
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
    return DataFrameTrainer, DataFrameTest


def SepararStringConNumerico(DataFrameTrainer):  # Divide los datos del dataframe segun el tipo de dato que sean
    columns_numeric_Name = list((DataFrameTrainer.select_dtypes(include=['int64', 'float64'])).columns.values)
    columns_string_Name = list((DataFrameTrainer.select_dtypes(include=['object', 'bool'])).columns.values)
    return columns_numeric_Name, columns_string_Name


def DefinirTipoDeDato(HeaderString, HeaderNumeric):
    TipesString = df[HeaderString].dtypes
    TipesNumeric = df[HeaderNumeric].dtypes

    return TipesString, TipesNumeric


def CalcularDistanciaEuclidiana(DataFrameTest, DataFrameTrainer, HeaderNamesNumeric, Column_Target, TargetType):
    suma = 0
    ListaSuma = []
    ListaEuclidiana = []

    # SE ELIMINA LA COLUMNA TARGET PARA NO COMPARARLA
    if TargetType == "regresion":
        DataFrameTest.drop([Column_Target], axis=1)
        DataFrameTrainer.drop([Column_Target], axis=1)
        HeaderNamesNumeric.remove(Column_Target)

    for test in range(len(DataFrameTest)):  # Itera cada una de las FILAS del dataframe test
        ListaSuma = []
        for trainer in range(len(DataFrameTrainer)):  # Itera cada una de las FILAS del dataframe test
            # SE UTILIZA LA FUNCION LINALG.NORM PARA OBTENER LA DISTANCIA EUCLIDIANA
            suma = linalg.norm(
                DataFrameTrainer[HeaderNamesNumeric].iloc[trainer].values - DataFrameTest[HeaderNamesNumeric].iloc[
                    test].values)
            ListaSuma.append(suma)  # SE AGREGA LA SUMA TOTAL A LA LISTA
            suma = 0
        ListaEuclidiana.append(ListaSuma)
    return ListaEuclidiana


def SumarDIstancias(ListaHamming, ListaEuclidiana):
    suma = []
    # NO IMPORTA QUE LISTA SE ITERE, AMBAS CONTIENEN LA MISMA CANTIDAD
    for lista in range(len(ListaHamming)):
        for posicion in range(len(ListaHamming[lista])):
            ListaHamming[lista][posicion] = ListaHamming[lista][posicion] + ListaEuclidiana[lista][posicion]

    return ListaHamming


def CalcularDistanciaHamming(DataFrameTest, DataFrameTrainer, HeaderNamesString, Column_Target, TargetType):
    suma = 0
    ListaSuma = []
    ListaHamming = []
    if TargetType == "clasificacion":  # SE ELIMINA LA COLUMNA TARGET PARA NO COMPARARLA
        DataFrameTest.drop([Column_Target], axis=1)
        DataFrameTrainer.drop([Column_Target], axis=1)
        HeaderNamesString.remove(Column_Target)

    for test in range(len(DataFrameTest)):  # Itera cada una de las FILAS del dataframe test
        ListaSuma = []
        for trainer in range(len(DataFrameTrainer)):  # Itera cada una de las FILAS del dataframe test
            for x in range(
                    len(DataFrameTrainer[HeaderNamesString].iloc[trainer].values)):  # ITERA CADA COLUMNA DE CADA FILA
                if DataFrameTrainer[HeaderNamesString].iloc[trainer, x] != DataFrameTest[HeaderNamesString].iloc[
                    test, x]:  # SI LOS DATOS SON DISTINTOS SE SUMA 1
                    suma += 1

            ListaSuma.append(suma)  # SE AGREGA LA SUMA TOTAL A LA LISTA
            suma = 0
        ListaHamming.append(ListaSuma)
    return ListaHamming


def minmax_norm(df_input):
    return (df_input - df_input.min()) / (df_input.max() - df_input.min())


def Normalizar(DataFrameTrainer, DataFramePrueba, HeaderNamesString, HeaderNamesNumeric, HeaderNames):
    opcion2 = 0
    opcion = int(input("\nQue tipo de Columna eligiras para target? \n 0)Numerico \n 1)Categorico\n Tu Opcion:"))
    if opcion == 1:
        count = 0
        for column_names in HeaderNamesString:
            print("Opcion ", count, column_names)
            count += 1
        opcion2 = int(input("\nCual es la Columna que Elijes como target: "))
    elif opcion == 0:
        count = 0
        for column_names in HeaderNamesNumeric:
            print("Opcion ", count, column_names)
            count += 1
        opcion2 = int(input("\nCual es la Columna que Elijes como target: "))
    Column_Target = HeaderNames[opcion][opcion2]  # Se selecciona la columna Target
    if opcion == 0:
        TargetType = "regresion"
    elif opcion == 1:
        TargetType = "clasificacion"
        print("\nObjetivo del problema: ", TargetType)
    print("\n Columna Target: ", Column_Target)

    # SE CREA UNA COPIA DE AMBOS DATAFRAMES PARA NORMALIZARLOS
    DataframeNumerico = DataFrameTrainer.copy()
    DataframeNumericoPrueba = DataFramePrueba.copy()

    # SE ELIMINAN LAS COLUMNAS QUE NO SE DESEAN NORMALIZAR
    DataframeNumerico.drop(HeaderNamesString, axis='columns', inplace=True)
    DataframeNumericoPrueba.drop(HeaderNamesString, axis='columns', inplace=True)

    # SE NORMALIZAN LOS DATAFRAMES
    b = minmax_norm(DataframeNumerico)
    c = minmax_norm(DataframeNumericoPrueba)

    # SE REMPLAZA LA COLUMNA TARGET YA QUE NO DEBE ESTAR NORMALIZADA
    if opcion == 0:  #
        b[Column_Target] = DataFrameTrainer[Column_Target]
        c[Column_Target] = DataFramePrueba[Column_Target]

    return b, c, Column_Target, TargetType

    #SE OBTIENEN LOS K VALORES MAS CERCANOS  Y SU PRPOMEDIO O LA CLASE QUE MÁS SE REPITE
    #SE OBTIENE EL ERROR CUADRATICO O PORCENTAJE DE ACIERTOS
def Resultado( K, DataFrameTest, DataFrameTrainer,ListaSuma,TargetType,Column_Target):
    ContadorCategorico = 0
    ListaPromedio = []

    for a in range(int(len(DataFrameTest.index.values))):
        DataFrameTrainer.insert(int(len(DataFrameTrainer.columns.values)), "Distancia Con Valor de Prueba " + str(a),
                                ListaSuma[a])
        #SE IMPRIME EL DATAFRAME CON LAS COLUMNAS DE DISTANCIAS
        print("\n_____________________________________________________________ Datos de prueba " + str(a) + ":\n ",
              DataFrameTest.iloc[a])
        # SE OBTIENEN LAS FILAS CON LAS K DISTANCIAS MÁS PEQUEÑAS
        Temp = DataFrameTrainer.nsmallest(K, "Distancia Con Valor de Prueba " + str(a))

        # EN CASO QUE EL TARGET SEA CATEGORICO
        if TargetType == "clasificacion":
            # SE OBTIENE LA EL VALOR DE LA COLUMNA QUE MAS VECES SE REPITE
            Valor1 = Temp[Column_Target].value_counts().idxmax()
            # SE OBTIENE EL VALOR ORIGINAL
            Valor2 = DataFrameTest[Column_Target].iloc[a]
            print("\nValor predecido: ", Valor1)
            print("\nValor real: ", Valor2)
            if Valor1 == Valor2:
                print("\nPrediccion correcta")
                ContadorCategorico += 1
            else:
                print("\nPrediccion incorrecta")

        # EN CASO QUE EL TARGET SEA NUMERICO
        elif TargetType == "regresion":
            # SE OBTIENE EL PROMEDIO DE LA COLUMNA TARGET DE LOS K VALORES
            promedio = Temp[Column_Target].mean()
            ListaPromedio.append(promedio)
            print("\n El Promedio es: ", promedio)
            print("Valor real: ", DataFrameTest[Column_Target].iloc[a])

    #SE MUESTRAN LOS RESULTADOS
    if TargetType == "clasificacion":
        print("\nPorcentaje de aciertos: ", (ContadorCategorico / len(DataFrameTest.index)) * 100)
    elif TargetType == "regresion":
       print("\nError Cuadratico medio para este conjunto de datos: ",(np.square(DataFrameTest[Column_Target].values- ListaPromedio)).mean())

    print("\n ---------------------------------------------------Distancias---------------------------------------- ")
    print(DataFrameTrainer.to_string())



def KNN():
    ListaPromedio = []
    ContadorCategorico = 0
    ListaHamming = []
    ListaEuclidiana = []
    ListaSuma = []
    DataFrames = DividirDataFrame(df)  # SE RECIBEN LOS DATAFRAME DE DIVIDIRDATAFRAME() Y SE DIVIDEN
    DataFrameTrainer = pd.DataFrame(DataFrames[0])
    DataFrameTest = pd.DataFrame(DataFrames[1])
    HeaderNames = SepararStringConNumerico(DataFrameTrainer)
    HeaderNamesNumeric = HeaderNames[0]  # CONTIENE EL NOMBRE DE LAS COLUMNAS QUE SON NUMERICAS
    HeaderNamesString = HeaderNames[1]  # CONTIENE EL NOMBRE DE LAS COLUMNAS QUE SON CATEGORICAS
    Types = DefinirTipoDeDato(HeaderNamesString, HeaderNamesNumeric)
    TipesString = Types[0]  # SE OBTIENE EL TIPO DE DATO DE CADA COLUMNA
    TipesNumeric = Types[1]

    # IMPRIMIMOS LOS DATAFRAME
    print("\n------------------------------------Datos de Entrenamiento------------------------------------")
    print(DataFrameTrainer.head(5).to_string())
    print("\n", DataFrameTrainer.describe())
    print("\n------------------------------------Datos de Prueba------------------------------------")
    print(DataFrameTest.head(5).to_string())
    if len(HeaderNamesNumeric) > 0:  # SE NORMALIZAN LOS DATAFRAMES SOLO SI CONTIENE VALORES NUMERICOS
        DataFrameTemp = Normalizar(DataFrameTrainer, DataFrameTest, HeaderNamesString, HeaderNamesNumeric, HeaderNames)
        DataFrameTrainerNorm = DataFrameTemp[0]
        DataFrameTestNorm = DataFrameTemp[1]
        Column_Target = DataFrameTemp[2]
        TargetType = DataFrameTemp[3]
        print("\n------------------------------------DATOS NORMALIZADOS--------------------------------------")
        DataFrameTrainer[list(DataFrameTrainerNorm.columns.values)] = DataFrameTrainerNorm[
            list(DataFrameTrainerNorm.columns.values)]
        DataFrameTest[list(DataFrameTestNorm.columns.values)] = DataFrameTestNorm[
            list(DataFrameTestNorm.columns.values)]
        print(DataFrameTrainer.head(5).to_string())

    K = int(input("\nIngrese el valor de K "))
    # SE OBTIENEN LAS DISTANCIAS
    # EN CASO DE QUE EL DATAFRAME CONTENGA VALORES CATEGORICOS
    if (len(HeaderNamesString) > 0):
        ListaHamming = CalcularDistanciaHamming(DataFrameTest, DataFrameTrainer, HeaderNamesString, Column_Target,
                                                TargetType)

    # EN CASO DE QUE EL DATAFRAME CONTENGA VALORES NUMERICOS
    if len(HeaderNamesNumeric) > 0:
        ListaEuclidiana = CalcularDistanciaEuclidiana(DataFrameTest, DataFrameTrainer, HeaderNamesNumeric,
                                                      Column_Target, TargetType)

        # SE SUMAN LAS DISTANCIAS EN CASO DE EXISTIR VALORES MIXTOS
    if len(HeaderNamesString) > 0 and len(HeaderNamesNumeric) > 0:
        ListaSuma = SumarDIstancias(ListaHamming, ListaEuclidiana)

        # EN CASO QUE TODAS LAS COLUMNAS SEAN CATEGORICAS
    elif len(HeaderNamesString) > 0:
        ListaSuma = ListaHamming

        # EN CASO QUE TODAS LAS COLUMNAS SEAN NUMERICAS
    elif len(HeaderNamesNumeric) > 0:
        ListaSuma = ListaEuclidiana

    Resultado(K,DataFrameTest, DataFrameTrainer, ListaSuma,TargetType,Column_Target)
    sys.exit()


while True:
    print("1) KNN")
    print("0) Salir")
    op = input()

    if op == "1":
        KNN()
    elif op == "0":
        break
