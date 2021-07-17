import turtle
from math import sqrt, pow
t = turtle.Turtle()
x = int(input('Digite o tamanho do lado do triângulo: '))
hipotenusa = sqrt(pow(x,2)+pow(x,2))
t.forward(x)
t.left(135)
t.forward(hipotenusa)
t.left(135)
t.forward(x)
