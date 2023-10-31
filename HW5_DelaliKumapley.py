## Delali Kumapley
## CS100 H11
## HW 5 
## October 12, 2023

'''
1. Create a list named months of the months of the year. Write a for loop that iterates over the elements of months and prints out each one that begins with letter 'J', one month per line.
'''

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for month in months:
  if(month[0] == 'J'):
    print(month)

'''
2. Write a for loop that iterates over all of the integers in the range 0 through 99, inclusive, and prints
out all of those numbers that are divisible by both 2 and 5.
'''

for i in range(0,100):
  if(i % 2 == 0):
    if(i % 5 == 0):
      print(i)

'''
3. Consider the strings created by these assignment statements:

Write a for loop that prints out all the vowels in horton in the order they appear in
horton.
'''

horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"


for l in horton:
  for vow in vowels:
    if vow == l:
      print(l)
   

      