# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 18:14:49 2019

@author: El Macho
"""

import pandas as pd

#Pandas 'ta chido
#Paso 1. Pandas trabaja sobre DataFrame
#DataFrame() es la función de pandas que permite crear DataFrames
#Las llaves me permiten crear HashMaps (Dictionaries) en Python
#Los corchetes me permiten crear Listas
miTabla = pd.DataFrame({"Header1":["Row1","Row2","Row3"],
                        "Header2":["Row1","Row2","Row3"], 
                        "Header3":["Row1","Row2","Row3"]})
print(miTabla)

#miTabla con índices
miTabla = pd.DataFrame({"Header1":["Row1","Row2","Row3"],
                        "Header2":["Row1","Row2","Row3"], 
                        "Header3":["Row1","Row2","Row3"]},
                        index=["Lecturas2017","Lecturas2018","Lecturas2019"]
                        )
print(miTabla)

#La otra estructura de datos de pandas son las series
miSerie1 = pd.Series(["Row1","Row2","Row3"])
print(miSerie1)

#Series con nombres (índices)
miSerie1 = pd.Series(["Row1","Row2","Row3"], index=["Lec1","Lec2","Lec3"])
print(miSerie1)

miArchivo = pd.read_csv("datasets/miPrueba.csv", index_col=0)
print(miArchivo)

miSegundoArchivo = pd.read_csv("datasets/prueba.csv")
print(miSegundoArchivo)

miTabla.to_csv("datasets/julia.csv")














