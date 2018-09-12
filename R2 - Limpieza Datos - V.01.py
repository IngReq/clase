import datetime as dt
#Obtener que dia es la fecha
x=dt.datetime(2007,1,1)
a = x.year
m = x.month
d = x.day
fecha = dt.date(a, m, d)
print (fecha.strftime('%A').upper())

#Leer del archivo de texto csv
df1=pd.read_csv('data/A.csv', parse_dates=True, index_col=0)
print(df1.columns)
cont=0
for r in df1.index:
    print (r)
    a = r.year
    m = r.month
    d = r.day
    fecha = dt.date(a, m, d)
    dia=fecha.strftime('%A').upper()
    print (dia)
    if(dia=='SATURDAY' or dia=='SUNDAY'):
        con=cont+1
        print("Fin de semana")

print("contador: "+str(cont))