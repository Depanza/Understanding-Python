txt_message = '''Hello {my_name}!
Is this gmail: {my_email} connected to your github account. Let me know.'''

def formated_msg(name, email):
    my_msg = txt_message.format(my_name=name, my_email =email)
    return my_msg


message = formated_msg("Samuel", "@.com")
print(message)