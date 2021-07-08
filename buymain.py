import  dt
import ListSplit
import smtplib
from random import randint
import re
import detail
import time
import info
global stock
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
code=random_with_N_digits(4)
stock=[]
subject = " verfication code "
msg = "verification code is",code
subject1 = "Stock details "
msg1="stock details",stock    
global email
def send_email(subject, msg):
    try:
        email=str(input("enter email : "))
        print(" "*50+"checking your email")
        time.sleep(1)
        check_email(email)
        print(" "*50+"your entered email is : "+email)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(info.EMAIL_ADDRESS,info.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(info.EMAIL_ADDRESS,email, message)
        server.quit()
        print(" "*50+"Success: Email sent!")
    except:
        print("Email failed to send.")
def send_email1(subject1, msg1):
    try:
        email=str(input("enter email : "))
        print(" "*50+"checking your email")
        time.sleep(1)
        check_email(email)
        print(" "*50+"your entered email is : "+email)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(info.EMAIL_ADDRESS,info.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject1, msg1)
        server.sendmail(info.EMAIL_ADDRESS,email, message)
        server.quit()
        print(" "*50+"Success: Email sent!")
    except:
        print("Email failed to send.")
class Validator(object):

    def __init__(self, email):
        self.email = email

    def check_for_symbol(self):
        if re.search("[@.]", self.email) is None:
            return False
        else:
            return True

    def check_length(self):
        if len(self.email) >= 12:
            return True
        else:
            return False
def email_to_verify():
    return input('Enter your email address: ')
def check_email(email):
    validator = Validator(email)
    symbol = validator.check_for_symbol()
    if symbol is False:
        print ("Your email address is not valid. Failed symbols..")

    length = validator.check_length()
    if length is False:
        print ("Your email is not valid. Failed length")
        
    if length and symbol is True:
        print ("Email is a valid email address.")
        verfied_email=email
def enter_email():    
    send_email(subject, msg)
def buyBook():
    success=False
    while(True):
        firstName=input(" "*50+"Enter the first name of the buyer: ")
        if firstName.isalpha():
            break
        print(" "*50+"please input alphabet from A-Z")
    while(True):
        lastName=input(" "*50+"Enter the last name of the buyer: ")
        if lastName.isalpha():
            break
        print(" "*50+"please input alphabet from A-Z")
            
    t="buy-"+firstName+".txt"
    with open(t,"w+") as f:
        f.write("               online book store  \n")
        f.write("                   buyed By: "+ firstName+" "+lastName+"\n")
        f.write("    Date: " + dt.getDate()+"    Time:"+ dt.getTime()+"\n\n")
        f.write("S.N. \t\t Bookname \t      Authorname \n" )
    
    while success==False:
        print(" "*50+"Please select a option below:")
        for i in range(len(ListSplit.cost)):
            print(" "*50+"Enter", i, "to buy book", ListSplit.bookname[i]," and price is",ListSplit.cost[i])
    
        try:   
            a=int(input())
            
            if(int(ListSplit.quantity[a])>0):
                print(" "*50+"Book is available")
                with open(t,"a") as f:
                    f.write("1. \t\t"+ ListSplit.bookname[a]+"\t\t  "+ListSplit.authorname[a]+"\n")
                print(" "*50+"proceed to verification and detail gateway ")    
                print(" "*50+"enter your details")
                # detail.detail()
                send_email(subject, msg)
                time.sleep(4)
                userinput=int(input(" "*50+"Enter the verfication code send to you via Email"))
                print (" "*50+"(verifying)")
                if (userinput==code):
                    print(" "*50+"verification done")
                    ListSplit.quantity[a]=int(ListSplit.quantity[a])-1
                    with open("Stock.txt","w+") as f:
                        for i in range(6):
                            f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+ListSplit.cost[i]+","+ListSplit.language[i]+","+ListSplit.rating[i]+","+ListSplit.date[i]+","+ListSplit.edition[i]+"\n")
                    print(" "*50+"transaction succesful")
                    exit() 
                elif(userinput!=code):
                    print(" "*50+"invalid code")
                    exit()
            else:
                print(" "*50+"visit after 10 days")    
        except ValueError:
            print("")
            print(" "*50+"Please choose as suggested.")
def credentials():
    stock=[]
    with open('stock.txt') as infile:
        for line in infile:
            stock.append(line)
    msg1="stock details",stock  
    send_email1(subject1,msg1)