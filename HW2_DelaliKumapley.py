# Delali Kumapley
# CS 100 Section H11
# HW 02, September 21, 2023

# =============================================================
#1. This question practices the use of a list method. Assign to the variable grades a list of 10 letter grades from among 'A', 'B', 'C', 'D', and 'F'. For example: 

grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']

# Write a Python expression that creates a list named frequency, in which the elements are the number of times each of the letters A, B, C, D and F appear in grades. For example, for the above value of grades, the following would be correct output: frequency = [4, 2, 2, 0, 2] Your expression must give the correct values for any list of grades, not just the one in your list. 
# Hint: use the list method count.

frequency = [0,0,0,0,0]
for i in grades:
  if i == 'A':
    frequency[0] = grades.count('A')
  elif i == 'B':
    frequency[1] = grades.count('B')
  elif i == 'C':
    frequency[2] = grades.count('C')
  elif i == 'D':
    frequency[3] = grades.count('D')
  elif i == 'F':
    frequency[4] = grades.count('F')

print(frequency)


# =============================================================


#2. This question practices list membership, list indexes and list slices.

# a. Write a Python statement that creates a list named dog_breeds that contains the elements 'collie', 'sheepdog', 'Chow', and 'Chihuahua' in the order given.

dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']
print(dog_breeds)
# b. Write a Python statement that uses list slicing to create a list herding_dogs that is made up of the first two elements of dog_breeds.

herding_dogs = dog_breeds[:2]
print(herding_dogs)
## print(dog_breeds)

# c. Write a Python statement that uses list indexing to create a list tiny_dogs that is made up of the last element of dog_breeds.
tiny_dogs = [dog_breeds[3]]
print(tiny_dogs)

# d. Write a Python statement that tests whether 'Persian' is in the list dog_breeds and prints either True or False depending on the answer.

print('Persian' in dog_breeds)

#if 'Persian' in dog_breeds:
 # print("True")
#elif 'Persian' not in dog_breeds:
  #print("False")

# =============================================================