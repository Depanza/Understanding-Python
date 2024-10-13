'''
String formating
'''
name  = "Sameul"
py_packagge = "Reflex"
template = '''Hi everyone,
I am {name} and welcome to the first tutorial on building website using {py_package}.
{py_package} allows you to build your website without having a knowledge in JavaScripts'''

print(template)

print(template.format(name="Samuel", py_package="Reflex"))

pi =  3.142534345
print("The value for pi is {}".format(pi))
print("The value for pi is {:f}".format(pi))
print("The value for pi is {:.2f}".format(pi)) #to 2 decimal places
print("The value for pi is {:.3f}".format(pi)) #to 3 decimal places

'''
F strings
'''
name = "Aster"
age = 19
fav_color = "blue"

print(f"Hi!, \n My name is {name}. I am {age} years old and {fav_color} is my favourite color.")
