my_List = [1,3,5,7,11,13,15,17,25]

for my_var in my_List:
    print(my_var)

"""You can't loop through a integer/number. You get TypeError: 'int' object is not iterable"""
#for i in 10:
#    print(i)
'''but string are iterable'''
for x in "100":
    print(x)

for i in range(0, 20):
    print(i)

user_1 = {"user_name": "josh", "id":"1", "email":"ru@gmail.com"}
user_2 = {"user_name": "veli", "id":"5", "email":"boy@yahoo.com"}
user_3 = {"user_name":"pers", "id":"7", "email":"istant@facebook.com"}

my_users = [user_1, user_2, user_3]

#Prints usernames in my_users db
for user in my_users:
    print(user['user_name'])

#Prints coressponding emails of users
for user in my_users:
    print(user['email'])


#Prints users id
for user in my_users:
    if 'id' in user:
        print(user['id'])

chosen_user = {}
find_user_with_this_id = 7

for user in my_users:
    if 'id' in user:
        if user['id'] == str(find_user_with_this_id):
            chosen_user = user

print(chosen_user)
print("\n")

for x in range(0,10):
    for user in my_users:
        if user['id'] == str(x):
            print(user)


