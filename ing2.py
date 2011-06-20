#!/usr/bin/python
#-*- coding: utf-8 -*-
#ing.py: ejemplo de estructuras de datos




print ("")
print ("Bienvenido a la actividad de Inglés. Para comenzar, realizaremos una sopa de letras sobre temas que hayas visto.")

print ("")
print ("Debes encontrar 2 nombres de colores en Inglés, 2 nombres de días de la semana en Inglés, 2 números del 10 al 20 en Inglés y 2 estaciones.")
print ("Recuerda que las palabras pueden estar en cualquier sentido,: vertical u horizontal, hacia atrás o hacia adelante, hacia arriba o hacia abajo.")

print ("")

acertoSpring=False
acertoWinter=False
acertoEleven=False
acertoFifteen=False
acertoOrange=False
acertoPurple=False
acertoTuesday=False
acertoSunday=False
termine = False

print ("* * * * * * * * * * * * * * * * * * * * * *")
print ("* W E A X F F Q G K A H P S N E C H T V M *")
print ("* Q Q S U N D A Y T X X N Y T R V D W S V *")
print ("* O U P E H O W I X R G I J U V J Z U W L *")
print ("* P O R A N G E L A Q J N E E T F I F M S *")
print ("* R R I A E B L I R Q B T V S R K D U P T *")
print ("* S H N J T S P W B B N E M D C N U C D I *")
print ("* D O G X F L R Y T L E R G A Z M K O N H *")
print ("* K Y P Y Z A U Z F D G A C Y K G L Y L U *")
print ("* Z C F H P Y P E L E V E N Y M F I N J O *")
print ("* * * * * * * * * * * * * * * * * * * * * *")

while (not termine):
  print("")
  
  palabra = raw_input("Escribe una palabra que encuentres en mayúsculas: ")
  if (palabra == "SPRING"):
    acertoSpring = True
    print("Muy bien! Has acertado")
  elif (palabra == "WINTER"):
    acertoWinter = True
    print("Muy bien! Has acertado")
  elif (palabra == "ELEVEN"):
    acertoEleven = True
    print("Muy bien! Has acertado")
  elif (palabra == "FIFTEEN"):
    acertoFifteen = True
    print("Muy bien! Has acertado")
  elif (palabra == "ORANGE"):
    acertoOrange = True
    print("Muy bien! Has acertado")
  elif (palabra == "PURPLE"):
    acertoPurple = True
    print("Muy bien! Has acertado")
  elif (palabra == "TUESDAY"):
    acertoTuesday = True
    print("Muy bien! Has acertado")
  elif (palabra == "SUNDAY"):
    acertoSunday = True
    print("Muy bien! Has acertado")
  else:
    print("La palabra que ingresaste no está, inténtalo nuevamente")
    
  termine = acertoSpring and acertoWinter and acertoEleven and acertoFifteen and acertoOrange and acertoPurple and acertoTuesday and acertoSunday
  
print("")
print("Felicitaciones! Has ganado")
    
  
  