# solve by using concept of OOPs 
class user:
    def __init__(self,name):
        self.name = name

class message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

class chatroom:
    def __init__(self):
        self.users = []
        self.messages = [] 

    def join_user(self, user):
        self.users.append(user)
        print(f"{user.name} has joined the chatroom.")

    def leave_user(self, user):
        self.users.remove(user)
        print(f"{user.name} has left the chatroom.")

    def send_message(self, msg):
        self.messages.append(msg)
        print(msg.sender.name + ":", msg.text)

    def show_chat_history(self):
        print("\nChat History:\n")
        for msg in self.messages:
             print(msg.sender.name + ":", msg.text)   


u1 = user("Taha")
u2 = user("Ali")

room = chatroom()

room.join_user(u1)
room.join_user(u2)

m1 = message(u1, "Hello Everyone")
m2 = message(u2, "Hi Taha")

room.send_message(m1)
room.send_message(m2)

room.show_chat_history()
room.leave_user(u2)             
