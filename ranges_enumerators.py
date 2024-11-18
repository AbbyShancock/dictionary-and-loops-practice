#RANGES PRACTICE 1

my_list = list(range(2500, 2589))
print(my_list)


# #RANGES PRACTICE 2

my_list2 = list(range(3, 301, 3))
print(my_list2)


# #RANGES PRACTICE 3

sum_squares = sum([x**2 for x in range(1, 16)])
print(sum_squares)


#ENUMERATOR PRACTICE 1
list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]

for index, name in enumerate(list_names):
    print(f'{name} is found at index {index}')



# #ENUMERATOR PRACTICE 2
indices_list = list(enumerate("Python"))
print(indices_list)



#ENUMERATOR PRACTICE 3
list_names2 = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"] 
for index, name in enumerate(list_names2):
    if name.startswith("M"):
        print(index)

