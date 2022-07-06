#operators

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

#bitwise operator

print('{0} & {1} is {2}'.format(int(num1),int(num2), int(num1) & int(num2)))
print('{0} | {1} is {2}'.format(int(num1),int(num2), int(num1) | int(num2)))
print('{0} ^ {1} is {2}'.format(int(num1),int(num2), int(num1) ^ int(num2)))
print('{0} << 1 is {1}'.format(int(num1), int(num1) << 1))
print('{0} >> 1 is {1}'.format(int(num1), int(num1) >> 1))
print('~{0} is {1}'.format(int(num1), ~(int(num1))))
