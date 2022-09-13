#import pandas as pd
#import seaborn as sb
#from pylab import savefig

#file_location = 'Fuerzas_TheClinic (sin compuestas).xlsx'
#df = pd.read_excel('Fuerzas_CNN-Nacional (2013-2022).xlsx', sheet_name = 'Hoja1')
#col_list = ["Fechas", "AFP", "40 Horas", "abuso", "abusos", "acuerdos", "acusación", "autoridad", "calentamiento global", "cambio climatico", "conflicto", "consenco", "Constitución", "constitucional", "constituyente", "consumidor", "consumidores", "consumo", "corrupción", "crecimiento", "crisis", "cuarenta horas", "derecha", "desarrollo", "descontento", "destitución", "disenso", "drogas", "educación", "elecciones", "élite", "empresario", "empresarios", "empresas", "encuestas", "estallido social", "feminismo", "género", "gratuidad", "identidad", "igualdad",  "impuestos", "izquierda", "instituciones", "isapre", "jornada laboral", "laboral", "libertad", "lucro", "malestar", "marcha", "millonarios", "modelo", "narcotráfico", "obras públicas", "orden", "partidos politicos", "pensiones", "pobres", "pobreza", "poder", "progreso", "protesta", "redes sociales", "reforma", "reforma tributaria", "reformas", "ricos", "riqueza", "salud", "Sernac", "soberanía", "social", "sociales", "terrorismo", "trabajo", "tratados", "violencia"]

#data = pd.read_excel(file_location)
#CorMatrix = data.corr()
#CorMatrix.head()

#sb.set(font_scale = 0.15)
#save = sb.heatmap(CorMatrix, annot=True, cmap="YlGnBu", cbar=False)
#figure = save.get_figure()
#figure.savefig('heatmap.png', dpi = 3000)


#382437-d1558342-615d-4715-8b04-f26df29838a3
#def clear():
#   print("Clear")

   

   

#button1= ttk.Button(win, text= "Search", command=search).place(x=90, y=30)

#button2= ttk.Button(win, text= "Clear", command= clear).place(x=90,y=60)

from csv import excel
import pandas as pd
import seaborn as sb
import datetime
from datetime import timedelta
import openpyxl

def salir():
   flag = False

def parametros():
   flag_parametros = True
   print("0)Salir\n 2)AFP\n 3)40 Horas\n 4)abuso\n 5)abusos\n 6)acuerdos\n 7)acusación\n 8)autoridad\n 9)calentamiento global\n 10)cambio climatico\n 11)conflicto\n 12)consenco\n 13)Constitución\n 14)constitucional\n 15)constituyente\n 16)consumidor\n 17)consumidores\n 18)consumo\n 19)corrupción\n 20)crecimiento\n 21)crisis\n 22)cuarenta horas\n 23)derecha\n 24)desarrollo\n 25)descontento\n 26)destitución\n 27)disenso\n 28)drogas\n 29)educación\n 30)elecciones\n 31)élite\n 32)empresario\n 33)empresarios\n 34)empresas\n 35)encuestas\n 36)estallido social\n 37)feminismo\n 38)género\n 39)gratuidad\n 40)identidad\n 41)igualdad\n 42)impuestos\n 43)izquierda\n 44)instituciones\n 45)isapre\n 46)jornada laboral\n 47)laboral\n 48)libertad\n 49)lucro\n 50)malestar\n 51)marcha\n 52)millonarios\n 53)modelo\n 54)narcotráfico\n 55)obras públicas\n 56)orden\n 57)partidos politicos\n 58)pensiones\n 59)pobres\n 60)pobreza\n 61)poder\n 62)progreso\n 63)protesta\n 64)redes sociales\n 65)reforma\n 66)reforma tributaria\n 67)reformas\n 68)ricos\n 69)riqueza\n 70)salud\n 71)Sernac\n 72)soberanía\n 73)social\n 74)sociales\n 75)terrorismo\n 76)trabajo\n 77)tratados\n 78)violencia\n")
   while(flag_parametros == True):
      parametro = input("Eliga los parametros a añadir para realizar el grafico: ")
      if (parametro != '0'):
         lista_parametros.append(parametro)
      if (parametro == '0'):
         flag_parametros = False
         print(lista_parametros)
         return lista_parametros


def grafico():
   print("Indique el periodo de fechas a ingresar, siendo la fecha minima 08/11/2011 y la fecha maxima a elegir el 18/03/2022")
   fecha_inicial = input("Ingrese la fecha minima:\n")
   fecha_maxima = input("Ingrese la fecha maxima:\n")
   if(cnnFuerzas.isin([fecha_inicial]).any().any() == False):
      print("Vuelva a ingresas las fechas")
   if(cnnFuerzas.isin([fecha_inicial]).any().any() == True):
      data = pd.DataFrame(cnnFuerzas, columns=lista_parametros)
      #CorMatrix = cnnFuerzas.corr()
      #CorMatrix.head()
      #sb.set(font_scale = 0.15)
      #save = sb.heatmap(CorMatrix, annot=True, cmap="YlGnBu", cbar=False)
      #figure = save.get_figure()
      #figure.savefig('heatmap.jpeg', dpi = 4000)
      fechaPrimaria = datetime.datetime.strptime(fecha_inicial, '%Y/%m/%d')
      fechaSecundaria = datetime.datetime.strptime(fecha_maxima, '%Y/%m/%d')
      first_fecha_cnn = datetime.datetime.strptime(primera_fecha_cnn, '%Y/%m/%d')
      resultado_mayor = (fechaSecundaria - first_fecha_cnn) / timedelta(days=1)
      resultado_mayor = int(resultado_mayor)
      resultado_menor = (fechaPrimaria - first_fecha_cnn) / timedelta(days=1)
      resultado_menor = int(resultado_menor)
      print(data)
      resultado = (fechaSecundaria - fechaPrimaria) / timedelta(days=1)
      data.iloc[fechaPrimaria:fechaSecundaria]
      print(data)
      data = pd.DataFrame(cnnFuerzas, columns=lista_parametros)
   #CorMatrix = test.corr()
   #CorMatrix.head()
   #sb.set(font_scale = 0.15)
   #save = sb.heatmap(CorMatrix, annot=True, cmap="YlGnBu", cbar=False)
   #figure = save.get_figure()
   #figure.savefig('heatmap_test.jpeg', dpi = 4000)
   #sheet = test.get_sheet_by_name('Hoja1')
   #print(sheet.cell(row = 1, column = 2).value)   

flag = True
lista_parametros = []
lista = []
primera_fecha_cnn = '2011/11/08'
fechas = [0]
#cnnFrecuencia = pd.read_excel('Frecuencias_CNN-Nacional (2013-2022).xlsx')
#theClinicFrecuencia = pd.read_excel('Frecuencias_TheClinic (sin compuestas).xlsx')
cnnFuerzas = pd.read_excel('Fuerzas_CNN-Nacional (2013-2022).xlsx')
#test = openpyxl.load_workbook('test.xlsx')
#test = pd.read_excel('test.xlsx')
#theClinicFuerzas = pd.read_excel('Fuerzas_TheClinic (sin compuestas).xlsx')
while (flag == True):
   print("Presione el numero para realizar la accion:\n 1)Seleccionar parametros\n 2)Generar grafico\n 3)Salir")
   opcion = input("Que desea hacer?\n")
   if (opcion == '1'):
      parametros()
   if(opcion == '2'):
      grafico()
   if (opcion == '3'):
      salir()
      break