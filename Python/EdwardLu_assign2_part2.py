# Edward Lu, Febuary 2th, CSCI-UA.0002-003 7640, EdwardLu_assign2_part2.py
temperature = input("Enter a temperature in degrees Fahrenheit:") # let users to enter a temperature in degrees Fahrenheit
c = (float(temperature) - 32) * (5/9) # convert "temperature" from string to float and then minus 32. Then divide the difference by 5/9. Get temperature in degrees Celsius
k = c + 273.15 # get temperature in degrees Kelvin by computing the sum of "c" and 273.15. Get temperature in degrees Kelvin
r = float(temperature) + 459.67 # convert "temperature" from string to float and plus 459.67. Get temperature in degrees Rankine
de = (100 - c) * (3/2) # compute the difference of 100 minus "c" and multiply the difference with 3/2. Get temperature in degrees Delisle
n = c * (33/100) # compute the product of "c" and 33/100. Get temperature in degrees Newton
print() # print a line break
print(format(float(temperature), ",.2f"), "degrees Fahrenheit...") # convert temperature from string to float and keep 2 numbers behind decimal point. Print "degrees Fahrenheit"
print() # print a line break
print("... in degrees Celsius", format(c, ">14,.2f"), "C") # format c by keep 2 numbers behind decimal point. And print the unit of Celsius.
print("... in degrees Kelvin",format(k, ">15,.2f"), "K") # format k by keep 2 numbers behind decimal point. And print the unit of Kelvin.
print("... in degrees Rankine",format(r, ">14,.2f"), "R") # format r by keep 2 numbers behind decimal point. And print the unit of Rankine.
print("... in degrees Delisle",format(de, ">14,.2f"), "De") # format de by keep 2 numbers behind decimal point. And print the unit of Delisle.
print("... in degrees Newton",format(n, ">15,.2f"), "N") # format n by keep 2 numbers behind decimal point. And print the unit of Newton.

# the following line would cause a syntax error because I forgot to delimit
# the string specifier in the format funtion
# print("...in degrees Celsius", format(c, >14.2f), "C")

# the following line would cause a logic error because the value I'm formatting is in
# Kelvin. So it does not match with the logic which is "in degrees Celsius".
# print("...in degrees Celsius", format(k, ">14.2f"), "C")

# the following line would case a runtime error if I accidentally type "0" on the
# denominator
# c = (float(temperature) - 32) * (5/0)

# the following line would cause a syntax error because I forgot to close the
# parentheses of format function
# print("...in degrees Celsius", format(c, ">14.2f", "C")

# the following line would cause a logic error because the value I'm formatting is in
# Delisle. So it does not mathch with the logic which is "in degrees Newton".
# print("...in degrees Newton",format(de, ">15.2f"), "N")
