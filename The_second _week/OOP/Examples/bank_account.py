# An example for OOP(class, methods and attributes)
from __future__ import annotations # for some changes is updated version of python (or use typing)
from pprint import pprint
from typing import List
import time


class BankAccount():
    """
    Bank account Management.
    """
    all_account_numbers:List[int] = list()
    last_account_number = 999
    def __init__(self, name:str) -> None:
        BankAccount.last_account_number += 1
        an = BankAccount.last_account_number
        self.account_number = an
        BankAccount.all_account_numbers.append(an)
        self.name = name
        self.balance = 0
    
    def display(self) -> None:
        """Display the information"""
        print(f"Hi {self.name}, your account number is : {self.account_number} \n and your balance is : {self.balance}")
        pprint(40 * "-")

    def deposit(self) ->None:
        """Decrease the balance and money"""
        amount = int(input("how much you want to deposit ??:"))
        if amount :
            self.balance += amount 
            print(f"your balance now is : {self.balance}")
        else :
            print("Nice to meet you")
        print(40 * "-")

    def withdraw(self) -> None:
        """Increase your balance and money"""
        amount = int(input("how much you want to withdraw ??:"))
        if amount > self.balance : 
            print("your balance is insufficient")
        else :
            self.balance -= amount
            print(f"your balance now is : {self.balance}")
        print(40 * "-")
    def goodbye(self) ->None :
        """bye bye"""
        print("goodbye")

def main():
    user = BankAccount("Mahdi Abbasi")
    print(40 * "-")
    pprint(f'Welcome to the bank account:')
    user.display()
    

    while True :
        input_menu = int(input("what do you want ?\n1-deposit,\n2-withdraw.\n3-Exit\n"))
        
        if input_menu == 1 :
            user.deposit()
            time.sleep(3)
        elif input_menu == 2 :
            user.withdraw()
            time.sleep(3)
        elif input_menu == 3 :
            user.goodbye()
            break
        else :
            pprint("Please enter current number")    

if __name__ == "__main__":
    main()