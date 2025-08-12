#step 1: Create an empty list
my_list = []

#step 2: Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#step 3: inserting value 15 at the second position in the list(index 1)
my_list.insert (1, 15)

#step 4: Extending the list with another list of [50, 60, 70]
my_list.extend (50)
my_list.extend (60)
my_list.extend (70)

#step 5: Remove the last element - in this case 70
my_list.remove()

#step 6: Sort the list in ascending order
my_list.sort()

#step 7: Find and print the index of 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)


#Optional: print the final list to verify
print("Final list: ", my_list)
