import pymysql
from sqlalchemy import create_engine
import pandas as pd
conn = create_engine('mysql+pymysql://root:@localhost:3306/sakila').connect()
codigosql = "select *  from film"
data = pd.read_sql(codigosql, conn)
lista = pd.DataFrame(data)
print(lista)
print('Registros: ', len(lista.index))
print('Columnas: ', len(lista.count()))
print('Estadisticas: ', lista.describe())
print('Media 2: ', lista['replacement_cost'].mean())
print('Moda: ', lista['replacement_cost'].mode())