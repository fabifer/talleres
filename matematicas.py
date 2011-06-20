#!/usr/bin/python
#-*- coding: utf-8 -*-
#matematicas.py: ejemplo de estructuras de datos

def validarEntero(s):
  ingresoCorrecto = False
  while(not ingresoCorrecto):
    try:
      valor = int(raw_input(s))
      ingresoCorrecto = True
    except ValueError:
      print("Debes ingresar un numero entero")
  return valor  


def sumarYRestar(n1, d1, n2, d2):
  print("")
  print("PRIMER PASO: Hallar el denominador comun")
  print "Escribiremos el denominador comun como el producto entre", d1, "y",d2
  print("")
  msj1 = "Escriba el producto entre " + str(d1) + " y " + str(d2) + ": "
  prod = validarEntero(msj1)
  while(prod <> d1 * d2):
    print("El resultado ingresado no es correcto. Intentalo nuevamente")
    print("")
    prod = validarEntero(msj1)
  print("Muy bien. A partir de ahora trabajaremos con este resultado como denominador de las fracciones")
  
  print("")
  print "SEGUNDO PASO: Escribe las fracciones equivalentes de las fracciones originales con denominador ", prod
  print("")
  print str(n1) + "/" + str(d1) + " = --/" + str(prod)
  print("")
  msj2 = "Ingresa el numerador que corresponde a la fraccion de la derecha: "
  num1 = validarEntero(msj2)
  while(num1 <> prod * n1 / d1):
    print "El resultado ingresado no es correcto. La fraccion " + str(num1) + "/" + str(prod) + " no es equivalente a la fraccion " + str(n1) + "/" + str(d1)
    print("")
    print str(n1) + "/" + str(d1) + " = --/" + str(prod)
    print("")
    num1 = validarEntero(msj2)
  print("Muy bien. Hagamos el mismo procedimiento para la segunda fraccion")
  print("")
  print str(n2) + "/" + str(d2) + " = --/" + str(prod)
  print("")
  num2 = validarEntero(msj2)
  while(num2 <> prod * n2 / d2):
    print "El resultado ingresado no es correcto. La fraccion " + str(num2) + "/" + str(prod) + " no es equivalente a la fraccion " + str(n2) + "/" + str(d2)
    print("")
    print str(n2) + "/" + str(d2) + " = --/" + str(prod)
    print("")
    num1 = validarEntero(msj2)
  print("Muy bien. Ahora tenemos dos fracciones con el mismo denominador")
  print("")
  
  
def sumar(n1, d1, n2, d2):
  
  aux2 = str(n1) + "/" + str(d1) + " + " + str(n2) + "/" + str(d2)
  asteriscos = "               "
  for x in range(0, len(aux2) / 2 + 1):
    asteriscos = asteriscos + " *"
  if((len(aux2) % 2 == 0)):
    asteriscos = asteriscos + "  *"
  else:
    asteriscos = asteriscos + " * *"
  
  print("")
  print asteriscos
  print "    EJERCICIO   * " + aux2 + " *"
  print asteriscos
  print("")
  
  sumarYRestar(n1, d1, n2, d2)
  print("TERCER PASO: Suma las fracciones de igual denominador")
  print("Lo unico que debes hacer es sumar los numeradores")
  prod = d1 * d2
  num1 = prod * n1 / d1
  num2 = prod * n2 / d2
  mensaje = "Escribe el resultado de sumar " + str(num1) + " y " + str(num2) + ": "
  numResultado = validarEntero(mensaje)
  while(numResultado <> num1 + num2):
    print("El resultado ingresado no es correcto. Intentalo nuevamente")
    numResultado = validarEntero(mensaje)
  print("")
  print "Muy bien. Por lo tanto " + aux2 + " = " + str(numResultado) + "/" + str(prod)
  simplificar(n1, d1, n2, d2, numResultado, prod)


def restar(n1, d1, n2, d2):
  
  aux2 = str(n1) + "/" + str(d1) + " - " + str(n2) + "/" + str(d2)
  asteriscos = "               "
  for x in range(0, len(aux2) / 2 + 1):
    asteriscos = asteriscos + " *"
  if((len(aux2) % 2 == 0)):
    asteriscos = asteriscos + "  *"
  else:
    asteriscos = asteriscos + " * *"
  
  print("")
  print asteriscos
  print "    EJERCICIO   * " + aux2 + " *"
  print asteriscos
  print("")
  
  sumarYRestar(n1, d1, n2, d2)
  print("TERCER PASO: Resta las fracciones de igual denominador")
  print("Lo unico que debes hacer es restar los numeradores")
  prod = d1 * d2
  num1 = prod * n1 / d1
  num2 = prod * n2 / d2
  mensaje = "Escribe el resultado de restar " + str(num1) + " menos " + str(num2) + ": "
  numResultado = validarEntero(mensaje)
  while(numResultado <> num1 - num2):
    print("El resultado ingresado no es correcto. Intentalo nuevamente")
    numResultado = validarEntero(mensaje)
  print("")
  print "Muy bien. Por lo tanto " + aux2 + " = " + str(numResultado) + "/" + str(prod)
  simplificar(n1, d1, n2, d2, numResultado, prod)
  

def simplificar(n1, d1, n2, d2, num, den):
  print("")
  print("CUARTO PASO: Simplifica la fraccion obtenida como resultado")
  a = num
  b = den
  n = num
  m = den
  while(a % b <> 0):
    a, b = b, a % b
  if(b == 1):
    print("En este caso la fraccion es irreducible. No es necesario simplificar")
  else:
    print("Para ello debes calcular el maximo común divisor entre el numerador y el denominador")
    msj = "Ingresa el maximo común divisor entre " + str(num) + " y " + str(den) + ": "
    mcd = validarEntero(msj)
    while(mcd <> b):
      print("El resultado ingresado no es correcto. Intentalo nuevamente")
      mcd = validarEntero(msj)
    print("")
    print("Correcto. Ahora divide el numerador y el denominador entre el maximo comun divisor hallado")
    msj1 = "Ingrese el resultado de dividir " + str(num) + " entre " + str(mcd) + ": "
    msj2 = "Ingrese el resultado de dividir " + str(num) + " entre " + str(mcd) + ": "
    n = validarEntero(msj1)
    while(n <> num / mcd):
      print("El resultado ingresado no es correcto. Intentalo nuevamente")
      n = validarEntero(msj1)
    m = validarEntero(msj2)
    while(m <> den / mcd):
      print("El resultado ingresado no es correcto. Intentalo nuevamente")
      m = validarEntero(msj2)
  print("")
  print("Muy bien. Has finalizado el ejercicio")
  print("") 
  aux2 = "* " + str(n1) + "/" + str(d1) + " + " + str(n2) + "/" + str(d2) + " = " + str(n) + "/" + str(m) + " *"
  asteriscos = "*"
  for x in range(0, len(aux2) / 2 - 2):
    asteriscos = asteriscos + " *"
  if(len(aux2) % 2 == 0):
    asteriscos = asteriscos + "  *"
  else:
    asteriscos = asteriscos + " * *"
  print("")
  print "      " + asteriscos
  print "      " + aux2 
  print "      " + asteriscos


print ("")
print ("Bienvenido a la actividad de Matematicas. A continuacion veras una ayuda para sumar o restar fracciones.")

print ("")

num1 = 0
den1 = 0
num2 = 0
den2 = 0

while(num1 == 0):
  try:
    num1 = int(raw_input("Escribe el numerador de la primera fraccion (debe ser un entero distinto de cero): "))
  except ValueError:
    print("Debe ingresar un numero entero distinto de cero")
while(den1 == 0):
  try:
    den1 = int(raw_input("Escribe el denominador de la primera fraccion (debe ser un entero distinto de cero): "))
  except ValueError:
    print("Debe ingresar un numero entero distinto de cero")
while(num2 == 0):
  try:
    num2 = int(raw_input("Escribe el numerador de la segunda fraccion (debe ser un entero distinto de cero): "))
  except ValueError:
    print("Debe ingresar un numero entero distinto de cero")
while(den2 == 0):
  try:
    den2 = int(raw_input("Escribe el denominador de la segunda fraccion (debe ser un entero distinto de cero): "))
  except ValueError:
    print("Debe ingresar un numero entero distinto de cero")
    
print("")
  
opcion = raw_input("Si deseas sumar estas fracciones, ingresa la letra S. Si deseas restar estas fracciones, ingresa la letra R. Presiona 'Enter' para continuar: ")
while((opcion <> "R") and (opcion <> "S") and (opcion <> "s") and (opcion <> "r")):
  print("Debes ingresar 'R' para restar o 'S' para sumar")
  print("")
  opcion = raw_input("Si deseas sumar estas fracciones, ingresa la letra S. Si deseas restar estas fracciones, ingresa la letra R. Presiona 'Enter' para continuar: ")
  
if((opcion == "R") or (opcion == "r")):
  restar(num1, den1, num2, den2)
if((opcion == "S") or (opcion == "s")):
  sumar(num1, den1, num2, den2)
