#Convertir grados Fahrenheit a Celsius
F=float(input("Ingrese los grados Fahrenheit: "))
if F%1==0:  #Si no tiene decimales se convierte en entero.
   F=int(F)
C=5/9*(F-32) #Funcion para convertir de F a C
if C%1!=0:  #Si tiene decimales se redondea a dos decimales.
  C=round(C,2)  
  if C%1==0:  #Si no tiene decimales se convierte en entero.
     C=int(C)
else:      
  C=int(C)


print(f'{F} grado(s) Fahrenheit equivalen a {C} grado(s) Celsius ')


#Convertir grados Celsius a Fahrenheit
C=float(input("Ingrese los grados Celsius: "))
if C%1==0:  
   C=int(C)
F=9/5*C + 32 #Funcion para convertir de F a C
if F%1!=0:
   F=round(F,2)
   if F%1==0:  
     F=int(F)
else:      
  F=int(F)   


print(f'{C} grado(s) Celsius equivalen a {F} grado(s) Fahrenheit ')
