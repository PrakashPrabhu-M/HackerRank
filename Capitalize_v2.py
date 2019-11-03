'''
Python 3

print(input().title()) will not work because the question is asking to capitalise firse letter of each word keeping in mind that "if it is a letter". Title and Capitalise are different in function as:

'abcd'.title()

results in 'Abcd' but

'12abcd'.title()

results in '12Abcd'. This is not what we want.

We just want to capitalise first letter of each word, not the first occuring letter of a word.
Instead, use this: 
'''
s = input()
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)
