#programs for illustrating for loop
'''
pattern:
0
01
012
0123
01234
'''

num = input('Enter number: ')

for i in range(int(num)):
    for j in range(i+1):
        print(j, end = "")
    print()

        
str = "Hello world"

for i in str:
    print(i)
