cant_minutos = int(input("Digite la cantidad de minutos que dura la llamada")) # input
                   
if cant_minutos <= 3:
  print("el valor de la llamda son 300 pesos") 
         
else:
 valor_llamada = 300+50*(cant_minutos-3)


print("el valor de la llamada es:" +str(valor_llamada))
