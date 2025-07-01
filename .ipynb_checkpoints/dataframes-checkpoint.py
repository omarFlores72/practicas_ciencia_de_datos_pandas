import pandas as pd
import numpy as np
#from tabulate import tabulate

#creando un array
data = np.array([[2,4], [6,8], [10,12]])

#creando un dataframe
df = pd.DataFrame(data, index=['row1', 'row2', 'row3'],
            columns=['col1', 'col2'])
#print(data, df)

#leyendo csv
df_examen = pd.read_csv('/home/omar/pandas/csv/StudentsPerformance.csv')
#print(df_examen.describe())

#pd.set_option('display.max_rows', 500)
#print(df_examen)

"""seleccionar columna de un dataframe"""
df_examen
