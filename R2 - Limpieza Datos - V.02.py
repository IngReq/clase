import datetime as dt
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd 
import numpy as np
from datetime import datetime, timedelta

formato = "%d/%m/%Y"
contador = 0            
fechadesde = dt.datetime(2007, 1, 1)
fechahasta = dt.datetime(2018, 2, 19)
try:               
    while fechadesde <= fechahasta:
        if dt.weekday(fechadesde) == 5 or dt.weekday(fechadesde) == 6:
            contador +=1
            fechaactual = fechadesde.strftime(formato)
            print(contador, fechaactual, 'es domingo')
        fechadesde = fechadesde + timedelta(days=1)
print(contador)

bolsaLeer=''
nombreBolsa=''
while(op==True):
    try:
        bolsa = int(input("Datos: 1-Google Finance || 2-YahooFinance "))
        nombreBolsa=input("Nombre de la bolsa ")
        if(bolsa==1):
            bolsaLeer='dataGoogle'
            op=False
        elif(bolsa==2):
            bolsaLeer='dataYahoo'
            op=False
        else:
            op=True
    except:
        print("Solo digitos")
print(bolsaLeer)
fechadesde = dt.datetime(2007, 1, 1)
fechahasta = dt.datetime(2018, 2, 19)
diferenciaFechas = fechahasta - fechadesde
print("Diferencia:", diferenciaFechas)

lista_fechas = [fechadesde + dt.timedelta(days=d) for d in range((fechahasta - fechadesde).days + 1)] 
diasCompletos=pd.DataFrame(np.array(lista_fechas), columns=['Date'])
print(diasCompletos)

dr = pd.date_range(start=fechadesde, end=fechahasta)
dft = pd.DataFrame()

df1=pd.read_csv(bolsaLeer+'/'+nombreBolsa+'.csv', parse_dates=True, index_col=0)
cont=0
contDiasFestivos=0
diasFestivosLista=[]
listFinesSemana=[]
contD=0
totRegistros=0
for r in df1.index:
    try:
        a = r.year
        m = r.month
        d = r.day
        fecha = dt.date(a, m, d)
        dia=fecha.strftime('%A').upper()
        for i in range(contadorFestivos):
            if(r==datesHoliday.iloc[i,0]):
                contDiasFestivos+=1
                diasFestivosLista.append(r)
        if(dia=='SATURDAY' or dia=='SUNDAY'):
            cont=cont+1
            listFinesSemana.append(contD)
            selectorFin=fecha
        contD=contD+1
    except:
        print("No hay fecha")
        continue
    totRegistros=totRegistros+1

suma=contFines+contDiasFestivosT
diasH2=diferenciaFechas.days-suma
print("¿Cuántos días DEBE HAbER ?")
print(diasH2)

festivos=pd.DataFrame(np.array(diasFestivosLista), columns=['columnaFestivos'])

finesD=pd.DataFrame(np.array(listFinesSemana), columns=['columnaFines'])

df=pd.read_csv(bolsaLeer+'/'+nombreBolsa+'.csv', parse_dates=True, index_col=None)




for i in finesD.index:
    selectorIndice=finesD['columnaFines'].loc[i]
    #Borrar Fines de semana encontrados
    df.drop(selectorIndice, inplace=True)

for i in datesHoliday.index:
    df = df.append({'Date': datesHoliday['Date'].loc[i]}, ignore_index=True)

datesHoliday = datesHoliday.set_index('Date')
for i in diasCompletos.index:
    if i in datesHoliday.index:
        diasCompletos.drop(i, inplace=True)

for i in diasCompletos.index:
    if i in finesD.index:
        diasCompletos.drop(i, inplace=True)

print(diasCompletos)

#Borrar fechas duplicadas
df.drop_duplicates(subset=['Date'], inplace=True)
#df=df.sort_values(["Date"])
df=df.reset_index(drop=True)

