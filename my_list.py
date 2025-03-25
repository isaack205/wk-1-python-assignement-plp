my_list = []  # Initialize an empty list
print(my_list)  # Print the empty list

my_list.append(10), my_list.append(20), my_list.append(30), my_list.append(40)  # Append values 10, 20, 30, and 40 to the list
print(my_list)  # Print the list after appending values

my_list.insert(1, 15)  # Insert the value 15 at the second position in the list
print(my_list)  # Print the list after inserting 15

my_list.extend([50, 60, 70])  # Extend the list with another list [50, 60, 70]
print(my_list)  # Print the list after extending

my_list.remove(70)  # Remove the value 70 from the list
print(my_list)  # Print the list after removing 70

my_list.sort()  # Sort the list in ascending order
print(my_list)  # Print the sorted list

print(my_list[3])  # Print the fourth element in the list
