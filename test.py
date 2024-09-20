one_d_array = [10, 20, 30, 40, 50]
for index,element in enumerate(one_d_array) :
    print(f"index:{index},element:{element}");
# add new element
one_d_array.append(60)
#add an element at a given position
one_d_array.insert(1,12)
#add multiple element after
one_d_array.extend([1,2,3])
#remove specific element
one_d_array.remove(60)
#remove last element 
one_d_array.pop()
#remove an element at a given position
del one_d_array[5]
#remove all element in an array
one_d_array.clear()

print(one_d_array)

    