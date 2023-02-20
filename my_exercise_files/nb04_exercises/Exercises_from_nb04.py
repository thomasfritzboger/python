import numpy as np

numbers = np.arange(10,30).reshape(4,5)

#print yellow 10
yellow = numbers[0,0]
print('yellow: ' + str(yellow))

#print red 11,12,13
red = numbers[0,1:-1]
print('red: ' + str(red))

#print green 12,17,22
green = numbers[0:3,2]
print('green: ' + str(green))

#print purple 14,24
purple = numbers[::2,-1]

result_as_2D = numbers[0:-1:2, -1::2] # if you want 2D array

print('purple: ' + str(purple))
print('purple i 2D array: ' + str(result_as_2D))
print(result_as_2D.flatten().tolist()) #print the 2D array as one line

#print blue 11,16,21,26,13,18,23,28
blue = numbers[:,1:-1:2]

result = np.array([numbers[:,1],numbers[:,3]])
print('blue: ' + str(blue.flatten()))
print(result)
