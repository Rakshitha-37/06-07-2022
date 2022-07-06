#operators


num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

#Arithmetic operators

print('Sum is {0}'.format(int(num1)+int(num2)))
print('Diff is {0}'.format(int(num1)-int(num2)))
print('Product is {0}'.format(int(num1)*int(num2)))
print('Quotient is {0}'.format(int(num1)/int(num2)))
print('Remainder is {0}'.format(int(num1)%int(num2)))
print('{0} power of {1} is {2}'.format(int(num1),int(num2), int(num1)**int(num2)))

#Logical operators

print('{0} and {1} is {2}'.format(int(num1),int(num2), int(num1) and int(num2)))
print('{0} or {1} is {2}'.format(int(num1),int(num2), int(num1) or int(num2)))
print('not of {0} is {1}'.format(int(num1), not int(num1)))




