from turtle import *
import random

n = int(input("Combient du Cercle tu Veux: "))
angle = 360 / n

speed(0)

for j in range(n):
    color((random.random(),random.random(),random.random()))
    circle(100)
    left(angle)

done()
