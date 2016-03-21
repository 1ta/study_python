import math

Gaso_gallon = float(input("Enter the gallon of gasoline: "))
Gaso_litre = Gaso_gallon*3.7854118
Num_petroleum = Gaso_gallon/19.5
Wegh_CO2 = Gaso_gallon*20
Energy = Gaso_gallon*115000
Vol_ethyl = Energy/75700
Price_Gaso = Gaso_gallon*3

print("the gasoline in litre is:",Gaso_litre,"litre")
print("the number of petroleum needed is:",Num_petroleum,"tank")
print("the weight of carbon oxide produced is:",Wegh_CO2,"pounds")
print("the energy of gasoline equals to",Vol_ethyl,"litre ethyl")
print("the price of the gasoline is",Price_Gaso,"dollars")
