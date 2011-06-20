#!/usr/bin/python
#-*- coding: utf-8 -*-
#ing.py: ejemplo de estructuras de datos


print ("")
print ("Bienvenido a la actividad 1 de Inglés. Para comenzar, realizaremos un crucigrama sobre colores.")
print ("")
print ("Debes encontrar los 7 nombres de colores en Inglés correspondientes a cada línea, según las pistas.")
print ("")

contador = 0
acerto1 = False
acerto2 = False
acerto3 = False
acerto4 = False
acerto5 = False
acerto6 = False
acerto7 = False
termino = False

while (not termino):
  
  if (acerto1):
    print ("1.          R E D")
  else:
    print ("1.          R _ _")
    
  if (acerto2):
    print ("2.      B L A C K")
  else:
    print ("2.      _ _ A _ _")
    
  if (acerto3):
    print ("3.      W H I T E")
  else:
    print ("3.      _ _ I _ _")
    
  if (acerto4):
    print ("4.  G R E E N")
  else:
    print ("4.  _ _ _ _ N")
    
  if (acerto5):
     print ("5.          B L U E")
  else:
     print ("5.          B _ _ _")
    
  if (acerto6):
    print ("6.  Y E L L O W")
  else:
    print ("6.  _ _ _ _ O _")
    
  if (acerto7):
    print ("7.    B R O W N")
  else:
    print ("7.    _ _ _ W _")
    
  
  print("")
  
  print("Pistas: Cada palabra corresponde al color de:")
  print("")
  print("1. Tomatoes")
  print("2. Panda bear")
  print("3. Paper")
  print("4. Grass")
  print("5. Sky")
  print("6. Sun")
  print("7. Chocolate")
  print("")
  
  try:
    num_palabra = int(raw_input("Qué palabra adivinaste? (ingresá su numero): "))
  
    if ((num_palabra >= 1) and (num_palabra <= 7)):
      
      if (num_palabra == 1):
	
	if acerto1:
	  print ""
	  print "Ya adivinaste esta palabra."
	else:
	  palabra = raw_input("Cuál es la palabra?: ")
	  print ""
	  if ((palabra == "red") or (palabra == "RED") or (palabra == "Red")):
	    
	    print ("Muy bien!, has acertado")
	    contador += 1
	    acerto1 = True
	  else:
	    print ("La palabra que ingresaste es incorrecta, intenta nuevamente")
	  
      if (num_palabra == 2):
	if acerto2:
	  print "" 
	  print "Ya adivinaste esta palabra."
	else:
	  palabra = raw_input("Cuál es la palabra?: ") 
	  print ""
	  if ((palabra == "black") or (palabra == "BLACK") or (palabra == "Black")):
	    print ("Muy bien!, has acertado")
	    contador += 1
	    acerto2 = True
	  else:
	    print ("La palabra que ingresaste es incorrecta, intenta nuevamente")
	  
      if (num_palabra == 3):
	if acerto3:
	  print ""  
	  print "Ya adivinaste esta palabra."
	else:
	  palabra = raw_input("Cuál es la palabra?: ") 
	  print ""
	  if ((palabra == "white") or (palabra == "WHITE") or (palabra == "White")):
	    print ("Muy bien!, has acertado")
	    contador += 1
	    acerto3 = True
	  else:
	    print ("La palabra que ingresaste es incorrecta, intenta nuevamente")
	  
      if (num_palabra == 4):
	if acerto4:
	  print ""  
	  print "Ya adivinaste esta palabra."
	else:
	  palabra = raw_input("Cuál es la palabra?: ") 
	  print ""
	  if ((palabra == "green") or (palabra == "GREEN") or (palabra == "Green")):
	    print ("Muy bien!, has acertado")
	    contador += 1
	    acerto4 = True
	  else:
	    print ("La palabra que ingresaste es incorrecta, intenta nuevamente")
	  
      if (num_palabra == 5):
	if acerto5:
	  print ""  
	  print "Ya adivinaste esta palabra."
	else:
	  palabra = raw_input("Cuál es la palabra?: ") 
	  print ""
	  if ((palabra == "blue") or (palabra == "BLUE") or (palabra == "Blue")):
	    print ("Muy bien!, has acertado")
	    contador += 1
	    acerto5 = True
	  else:
	    print ("La palabra que ingresaste es incorrecta, intenta nuevamente")
	  
      if (num_palabra == 6):
	if acerto6:
	  print ""  
	  print "Ya adivinaste esta palabra."
	else:
	  palabra = raw_input("Cuál es la palabra?: ") 
	  print ""
	  if ((palabra == "yellow") or (palabra == "YELLOW") or (palabra == "Yellow")):
	    print ("Muy bien!, has acertado")
	    contador += 1
	    acerto6 = True
	  else:
	    print ("La palabra que ingresaste es incorrecta, intenta nuevamente")
	  
      if (num_palabra == 7):
	if acerto7:
	  print "" 
	  print "Ya adivinaste esta palabra."
	else:
	  palabra = raw_input("Cuál es la palabra?: ")
	  print ""
	  if ((palabra == "brown") or (palabra == "BROWN") or (palabra == "Brown")):
	    print ("Muy bien!, has acertado")
	    contador += 1
	    acerto7 = True
	  else:
	    print ("La palabra que ingresaste es incorrecta, intenta nuevamente")
	  
      if (contador == 7):
	termino = True
	
    else:
      print ("El número ingresado no es correcto. Ingresalo nuevamente.")	
	
  except ValueError:
    print "Debes ingresar un número entero. Intentalo nuevamente."
    
  print ("")  
  
  
print ("1.          R E D")

print ("2.      B L A C K")

print ("3.      W H I T E")

print ("4.  G R E E N")

print ("5.          B L U E")

print ("6.  Y E L L O W")

print ("7.    B R O W N")

print ("")

print ("¡Felicitaciones!, has adivinado todas las palabras correctamente.")
      
print ("")
      
    
    
    
    
    
    
  
  
  
  
  
  