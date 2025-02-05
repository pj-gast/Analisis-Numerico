import math as mt


#Considera la definicion sinh como:
#sinh(x) = e^x - e^-x / 2
#Calcule el valor del sinh(x) para x = 2pi

#1: Evaluando directamente

x = mt.pi*2
sinh = mt.sinh(x)

#2: Usando la función exponencial

sinh2 = (mt.exp(x) - mt.exp(-x))/2

#3: Usando la definición:
    
sinh3 = (mt.e**x - mt.e**-x)/2

print(sinh)
print(sinh2)
print(sinh3)
    
#from cmath (complejos) import sin,sinh
