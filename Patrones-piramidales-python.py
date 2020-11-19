#Python 3.7.3 
##Figura Right side start Pyramid Patterns 
n=int(input("Ingresa el tamaño:"))

for i in range(0,n):
     for j in range(0,i+1):
         print('*', end = '')
     print("\r")
     
for i in range(n,0,-1):
      for j in range(0,i-1):
           print('*',  end = '')
      print("\r")

