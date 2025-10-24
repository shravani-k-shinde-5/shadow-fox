def formatfun(a,b):
  return format(a,b)

result=formatfun(145,'o')
print("the result is :",result)


#2
def pond(r,sq):
  Area=3.14*r**2
  sqs=sq*Area
  return(f"the AREA OF THE POND IS {Area} .sqm AND THE WATER IN POND IS {int(sqs)} litres")


print(pond(84,1.4))


#3
D=490
T=7
print(f"YOU TRAVELLED {D} IN {T} MINUTES WITH SPEED OF {D/(T*60)} m/s")