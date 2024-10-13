from formatText import formated_msg

def send(name, email):
    msg= formated_msg(name= name, email=email)

    return msg

send_msg = send("Samuel", "sam@gmail.com")

print(send_msg)