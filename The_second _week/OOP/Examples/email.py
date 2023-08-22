# A practice for create a email system that have a attributes like sender, reciver, subject, and send method.
from __future__ import annotations
import time

class Email():
    """Email services manager(just send and see inboxes)"""
    messages:list[str] = []
    reciver:list[str] = []
    users:list[str] = ["mahdi", "ali","narges", "mother"]
    def __init__(self,email) -> None:
        self.email = email


    def auth(self) -> None:
        """Authenticate"""
        check = input("Enter you name : \n")
        check += self.email
        if check in Email.users:
            print (f"Hi {check}")
            print(40 * "-")
            return True
        else:
            print("you don't have any account") 

    def send_email(self)-> None:
        """Send email to the account"""
        text  = input("Please enter your message\n")
        Email.messages.append(text)
        size = len(text)
        if  size < 20:
            reciver_input  = input(f"who recieve your email?\n{Email.users}\n")
            if reciver_input in Email.users:
                Email.reciver.append(reciver_input)
                print ("your email send to ", Email.reciver)
        else : 
            print("your message is too long")
        print(40 * "-")


    def show_messages(self)-> None:
        """Show all messages"""
        print (f"your inbox :\n send email to {Email.reciver} and message is {Email.messages}" )
        print(40 * "-")


    def goodbye(self) ->None :
        """bye bye"""
        print("goodbye")            


def main():
    user = Email("")
    print(40 * "-")
    if user.auth() :
        while True :
            input_menu = int(input("what do you want ?\n1-send email,\n2-show messages.\n3-Exit\n"))
            
            if input_menu == 1 :
                user.send_email()
                time.sleep(3)
            elif input_menu == 2 :
                user.show_messages()
                time.sleep(3)
            elif input_menu == 3 :
                user.goodbye()
                break
            else :
                print("Please enter current number")    

if __name__ == "__main__":
    main()