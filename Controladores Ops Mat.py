"""Deberá leer dos números 
brindados por el usuario, luego preguntar qué tipo de operación desea realizar/visualizar 
(multiplicación, división, residuo de la división o potenciación). Tomar en cuenta:
•	En caso de elegir división, esta no se podrá realizar segundo valor es igual a cero (volver a solicitar dicho número)
•	En caso de elegir potenciación, preguntar cual de los siguientes escenarios desea elegir:

Caso	                                    Operación
Cada número potenciado al cuadrado	        〖x1〗^(2 ) y 〖x2〗^(2 )
Cada número potenciado al cubo	            〖x1〗^(3 ) y 〖x2〗^(3 )
Primer numero con potencia del segundo	    〖x1〗^(x2 )
Segundo numero con potencia del primero	    〖x2〗^(x1 )


Al finalizar la operación, preguntar al usuario si desea realizar una nueva operación """


num1 = 0
num2 = 0


ops = 0 #Operaciones definida por el usuario
ops2 = 0 #Nombre de la operacion
totalOps = 0 #Total del resultado de la operacion

res = 0 #Respuesta del usuario

ca = 0 # Numero del caso, para potenciacion

#Asignacion de controladores 

controlador = True

#Asignacion de contadores

countMulti = 0
countDiv = 0
countRes = 0
countPot = 0

#Asignacion de iterador

i = 0

print ("Operaciones matematicas")


while controlador:
    #Lectura y validacion de datos
    print("----------------------------------------------------------------------------------")

    print("Empieza la ronda numero {}".format(i+1))

    print("\nMultiplicacion: 1 \nDivision: 2  \nResiduo de la division: 3 \nPotenciacion: 4")

    ops = int(input("\n¿Que tipo de operacion desea realizar?: "))
    while ops <= 0 or ops > 4:
        print("\nHa ingresado un valor fuera del rango para el tipo de operacion, intente otra vez")
        ops = int(input("¿Que tipo de operacion desea realizar?: "))
    print("Valor de operación nuevo aceptado ") 

    num1 = float(input("\nIngrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    if ops == 1:
        ops2 = "Multiplicacion"
        countMulti += 1
    elif ops == 2:
        ops2 = "Division"
        countDiv += 1
    elif ops == 3:
        ops2 = "Residuo de la division"
        countRes += 1
    else:
        ops2 = "Potenciacion"
        countPot += 1
    print("\nEl tipo de operacion es {} ".format(ops2))

    #Calculo de datos

    if ops == 1:
        totalOps = num1 * num2
        print("\nEl resultado es {}".format(totalOps))
    elif ops == 2:
        while num2 == 0:
            print("\nPara la operacion {} debe ingresar otra vez el segundo numero disntito a CERO".format(ops2))
            num2 = float(input("Ingrese nuevo valor del segundo numero: "))
        print("Valor nuevo aceptado")
        totalOps = num1 / num2
        print("\nEl resultado es {}".format(totalOps))
    elif ops == 3:
        totalOps = num1 % num2
        print("\nEl resultado es {}".format(totalOps))
    elif ops == 4:
        print("\nElegir uno de los siguiente casos de potenciacion")
        print("\nCada número potenciado al cuadrado: 1 \nCada número potenciado al cubo: 2 \nPrimer numero con potencia del segundo: 3 \n Segundo numero con potencia del primero: 4")
        ca =    int(input("\nIngresa el numero segun el caso deseado: "))
        while ca < 1 or ca >= 5:
            print("\nHa ingresado un valor fuera del rango , intente otra vez")
            ca = int(input("\nIngresa el numero segun el caso deseado: "))
        print("\nValor del caso nuevo aceptado ") 
        if ca == 1:
            print("El valor uno es: ",num1**2)
            print("El valor dos es: ",num2**2)
        elif ca == 2:
            print("El valor uno es: ",num1**3)
            print("El valor dos es: ",num2**3)
        elif ca == 3:
            print("El valor uno es: ",num1**num2)
        else:
            print("El valor dos es: ",num2**num1)
    
    res = input("\n Opcion Si: s \n Opcion No: n \n¿Desea realizar otra operacion?: ")
    
    while res != "s" and res != "n":
        print("Respuesta invalida, intente de nuevo")
        res = input("\n Opcion Si: s \n Opcion No: n \n¿Desea realizar otra operacion?: ")

    if res == "s":
        print("\nDe vuelta al menu")
    elif res == "n":
        controlador = False
        print("Fin del programa")

    i += 1

print("-------------------------------------------------------------------------")

print("\nEl total de multiplicaciones fue: {}".format(countMulti))
print("\nEl total de divisiones fue: {}".format(countDiv))
print("\nEl total de residuos de la division fue: {}".format(countRes))
print("\nEl total de potenciaciones fue: {}".format(countPot))