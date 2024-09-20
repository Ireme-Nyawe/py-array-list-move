import array
two_d_array = [
    [1, 2, 3],  # First row
    [4, 5, 6],  # Second row
    ["akimana", "lasr"]   # Third row
]
# Modifying an element
two_d_array[2][1] = 10
#add new element
two_d_array.append([2,"aa"])
two_d_array.insert(1,[12,13,16])

my_array = array.array('i', [1, 2, 3, 4])
my_array.insert(2,1)
print(my_array)
print(two_d_array)
print(type(my_array))
