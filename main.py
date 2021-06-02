import turtle
color = input("Ingrese color de lapiz blue, green, red: ")
turtle.color(color)
turtle.shape("turtle")
angulo = int(input("Ingrese un angulo para su dibujo: "))
longitud = "0"
cont = 0
while longitud != 0 :
    longitud = int(input("Ingrese la longitud de la linea, si ingresa cero se detiene: "))
    turtle.forward(longitud)
    turtle.right(angulo)
    cont = cont+1
    
print("Ingrese longitud de figura interna: ")
while longitud != 0:
    longitud0 = int(input("Ingrese la longitud de la linea, si ingresa cero se detiene: "))
    turtle.forward(longitud/2)      
    turtle.left(angulo)
print("\nGracias por dibujar con nosotros.")