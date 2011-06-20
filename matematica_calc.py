#!/usr/bin/python
#-*- coding: utf-8 -*-
#ing.py: ejemplo de estructuras de datos


print ""
print "Bienvenido a la actividad de Matematica. Aqui podras resolver ejercicios de operaciones entre 2 fracciones. Si quieres realizar una cuenta que tenga mas de 2 fracciones, debes resolverlas de a dos."

otraOp = 1

while (otraOp <> 2):

    print ""
    print "Que operacion entre fracciones quieres hacer? (elige la opcion):"
    print ""
    print "1- Suma"
    print ""
    print "2- Resta"
    print ""
    print "3- Multiplicacion"
    print ""
    print "4- Division"
    print ""
    operacion = int(raw_input("Operacion: "))
    print ""
    
    numerador1 = int(raw_input("Ingresa el numerador de la primer fraccion: "))
    print ""
    denominador1 = int(raw_input("Ingresa el denominador de la primer fraccion: "))
    print ""
    numerador2 = int(raw_input("Ingresa el numerador de la segunda fraccion: "))
    print ""
    denominador2 = int(raw_input("Ingresa el denominador de la segunda fraccion: ")) 
    print ""
    
    if (operacion == 1):
         result1 = numerador1*denominador2
         result2 = numerador2*denominador1
         result1 = result1 + result2
         result2 = denominador1*denominador2
         
         a = abs(result1)
         b = abs(result2)
        
         while b <> 0:
        	temp = b
        	b = a % b
        	a = temp
    
         result1 = result1/a
         result2 = result2/a
         
         print "La fraccion resultado es: "  + str(result1) + " / " + str(result2)
         print ""
         print "Numerador: " + str(result1) + " Denominador: " + str(result2)
                  
    elif (operacion == 2):
         result1 = numerador1*denominador2
         result2 = numerador2*denominador1
         result1 = result1 - result2
         result2 = denominador1*denominador2
         
         a = abs(result1)
         b = abs(result2)
        
         while b <> 0:
        	temp = b
        	b = a % b
        	a = temp
    
         result1 = result1/a
         result2 = result2/a
         
         print "La fraccion resultado es: "  + str(result1) + " / " + str(result2)
         print ""
         print "Numerador: " + str(result1) + " Denominador: " + str(result2)
         
    elif (operacion == 3): 
         result1 = numerador1*numerador2
         result2 = denominador1*denominador2
         print "La fraccion resultado es: "  + str(result1) + " / " + str(result2)
         print ""
         print "Numerador: " + str(result1) + " Denominador: " + str(result2)
         
    elif (operacion == 4): 
         result1 = numerador1*denominador2
         result2 = numerador2*denominador1
         print "La fraccion resultado es: "  + str(result1) + " / " + str(result2)
         print ""
         print "Numerador: " + str(result1) + " Denominador: " + str(result2)
         
         
    print ""
    print "¿Quieres realizar una nueva operación? (elige la opción):"
    print ""
    print "1- Si"
    print ""
    print "2- No"
    print ""
    otraOp = int(raw_input("Opción: "))
