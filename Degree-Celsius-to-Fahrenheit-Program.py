# Program 1 :-
# Convert Degree to Fahrenheit Simple Method
Celsius = float(input("Enter the Temperature Value (Degree Celsius): "))
fahrenheit = (Celsius * 1.8) + 32  # calculate fahrenheit
print('%0.1f Degree Celsius is equal to %0.1f degree Fahrenheit' % (Celsius, fahrenheit))
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Program 2 :-
Temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(Temp[:-1])
i_convention = Temp[-1]

if i_convention.upper() == "C":
    Result = int(round((9 * degree) / 5 + 32))
    o_Convention = "Fahrenheit"
elif i_convention.upper() == "F":
    Result = int(round((degree - 32) * 5 / 9))
    o_Convention = "Celsius"
else:
    print("Input proper convention.")
    quit()
print("The temperature in", o_Convention, "is", Result, "degrees.")
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
