# new_list = [expression for item in iterable if condition]

values = [1, 2, 3, 4, 5, 6, 9.5]

square_values = [x**2 for x in values]
print (square_values)


even_values = [x for x in values if isinstance(x, int) and x % 2 == 0]
print(even_values)





temperature_fahrenheit = [32, 212, 275]

degrees_celsius = [(f- 32) * (5/9) for f in temperature_fahrenheit]
print(degrees_celsius)
