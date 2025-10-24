
Australia = ["Sydney","Melbourne","Brisbane""Perth"]

UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]

India = ["Mumbai","Bangalore","Chennai","Delhi"]

city=input("enter the name of the city :")
if (city in Australia):
  print(f"the {city} is in AUSTRALIA")
elif(city in UAE):
  print(f"the {city} is in UAE")
elif(city in India):
  print(f"the {city} is in INDIA")
else:
  print(f"the {city} NOT FOUND")
