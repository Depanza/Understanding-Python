txt = ["a", "b","c"]
print(*txt)


def say_hi(name):
    print(f"Hi {name}. Good morning")

say_hi("Samuel")

txt_message = '''Hello {name}!
Thank you for signing up for this {hackaton}. You gonna love it.'''

def formated_msg(my_name="Samuel", my_hackaton="Open Source"):
    my_msg = txt_message.format(name=my_name, hackaton=my_hackaton)
    return my_msg

print(formated_msg())