import numpy
numpy.set_printoptions(sign=' ')
a=numpy.array(list(map(float,input().split())))
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))
'''
import numpy as np
arr = np.array(input().split(), float)
print(str(np.floor(arr)).replace('.', '. ').replace('[', '[ ').replace('. ]', '.]'),
      str(np.ceil(arr)).replace('.', '. ').replace('[', '[ ').replace('. ]', '.]'),
      str(np.rint(arr)).replace('.', '. ').replace('[', '[ ').replace('. ]', '.]'), sep = "\n")
      
import numpy
def smarter_print(array):
    for num in array:
        if num >= 10:
            smart_print(array)
            return
    smart_print(array, 1, 2, 2)
    return
def smart_print(array, front = 2, middle = 3, final = 2):
    string = '['
    for i in range(len(array)):
        if i == 0:
            string = string + front * ' ' + str(int(array[i])) + '.'
        elif i == len(array) - 1:
            string = string + final * ' ' + str(int(array[i])) + '.'
        else:
            string = string + middle * ' ' + str(int(array[i])) + '.'
    string = string + ']'
    print(string)
    return
float_list = list(map(float, input().split()))
float_array = numpy.array(float_list)
smarter_print(numpy.floor(float_array))
smarter_print(numpy.ceil(float_array))
smarter_print(numpy.rint(float_array))`
'''
