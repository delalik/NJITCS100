
## Delali Kumapley
## CS 100 H11
## Homework 09
##  November 9, 2023

'''
Problem 1
Write a function
file_copy that takes two string parameters (in_file and out_file) and copies the content of in_file into
out_file. Assume that in_file exists before file_copy is called. For example, the following would be
correct input and output:
#>>> file_copy('created_equal.txt', 'copy.txt')
#>>> copy_f = open('copy.txt')
#>>> copy_f.read()
'We hold these truths to be self-evident,\nthat all men are created equal\n'
'''

def file_copy(in_file, out_file):
    inFile = open(in_file, 'r')
    outFile = open(out_file, 'w')
    content = inFile.read()
    outFile.write(str(content))
    inFile.close()
    outFile.close()
    return outFile

#print(file_copy('created_equal.txt', 'copy.txt'))


