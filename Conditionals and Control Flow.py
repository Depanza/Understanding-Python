if True:
    print("Hi roboto")
#Thsi will display nothing
if False:
    print("Nothing here to see")

num = [1, 2, 3, 4, 5, 6, 7]
num_sq = []
is_a_factor_of_3 = []
is_even = []
is_odd = []

#Squares each number in the num list and appends it tothe num_sq container list
for x in num:
    y = x**2
    num_sq.append(y)

print(num_sq)

for x in num:
    if x % 2 ==0:
        is_even.append(x)
    else:
        is_odd.append(x)

print(is_even,is_odd)

for x in num:
    if x % 3 ==0:
        is_a_factor_of_3.append(x)
    elif x % 2 == 0:
        is_even.append(x)
    else:
        is_odd.append(x)

print("Is a factor of 3 : ",is_a_factor_of_3,"Is even: ", is_even,"Is odd: ",is_odd)

'''
While Loop
'''

num = 5
i = 0

while i< num:
    i += 1
    print(i) 

x = 10
y = 20
i = 0

while i < x:
    y = y*2
    if y > 2000:
        break      #break out of the while loop
    print(y, i)
    i += 0.000000000001

number = 100
i = 0
#Prints out odd numbers between 0 and 100
while i < number:
    i += 1
    if i % 2 == 0:
        continue        #skips even numbers
    print(i)