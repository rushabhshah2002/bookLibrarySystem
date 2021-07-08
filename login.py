import csv
from getpass import getpass
import owner
def main():
    with open("users.txt","r") as file:
        file_reader = csv.reader(file)
        user_find(file_reader)
        file.close()
 
def user_find(file):
    user = input(" "*50+"Enter your username: ")
    for row in file:
        if row[0] == user:
            print(" "*50+"username found", user)
            user_found = [row[0],row[1]]
            pass_check(user_found)
            break
        else:
            print()
 
def pass_check(user_found):
    user = getpass(" "*50+"enter your password: ")
    if user_found[1] == user:
        print(" "*50+"welcome  to  admin options")
        owner.owner()
        
    else:
        print(" "*50+"password not match")
        user_find(file_reader)
 

