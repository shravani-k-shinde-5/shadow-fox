
Australia = ["Sydney","Melbourne","Brisbane""Perth"]

UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]

India = ["Mumbai","Bangalore","Chennai","Delhi"]


city1=input("ENTER 1st city :")
city2=input("ENTER 2nd city :")
if((city1 in UAE )and( city2 in UAE)):
  print("BOTH CITIES ARE IN UAE")
elif((city1 in India) and (city2 in India)):
  print("BOTH CITIES ARE IN INDIA")
elif((city1 in Australia) and (city2 in Australia)):
  print("BOTH CITIES ARE IN INDIA")
else:
  print("BOTH CITIES ARE NOT IN SAME COUNTRY")