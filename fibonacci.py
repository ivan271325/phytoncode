n=int(input("Introduce un valor para 'n': "))

primero=0
segundo=1
sum=0
count=1
print("Secuencia de Fibonacci: ")

while(count<=n):    
  print(sum)
  count+=1
  primero=segundo
  second=sum
  sum=primero+segundo	

