
import smtplib
# class Validator(object):


#     def __init__(self, email):
#         self.email = email

#     def check_for_symbol(self):
#         if re.search("[@.]", self.email) is None:
#             return False
#         else:
#             return True

#     def check_length(self):
#         if len(self.email) >= 12:
#             return True
#         else:
#             return False
# def email_to_verify():
#     return input('Enter your email address: ')


# def check_email(email):
#     validator = Validator(email)
#     symbol = validator.check_for_symbol()
#     if symbol is False:
#         print ("Your email address is not valid. Failed symbols..")

#     length = validator.check_length()
#     if length is False:
#         print ("Your email is not valid. Failed length")
        
#     if length and symbol is True:
#         print ("Email is a valid email address.")
#         verfied_email=email

stock=[]
with open('stock.txt') as infile:
   for line in infile:
    stock.append(line)

def send_email(subject, msg):
    try:
        email=str(input("enter email : "))
        print(" "*50+"checking your email")
        time.sleep(1)
        check_email(email)
        print(" "*50+"your entered email is : "+email)
        server = smtplib.SMTP('smtp.gmail.com:587')
        print("a")
        server.ehlo()
        server.starttls()
        server.login("onlinebookstore2020@gmail.com","rushabh@123")
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail("onlinebookstore2020@gmail.com",email, message)
        server.quit()
        print(" "*50+"Success: Email sent!")
    except:
        print("Email failed to send.")
subject = "Stock details "
msg="stock details",stock

send_email(subject, msg)
