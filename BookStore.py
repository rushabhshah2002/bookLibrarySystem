import dt
import buymain
import search
import login
import detail
import cleanData
import cleandata2
import os
def start():
    flag=True
    while(flag):
        print("=-"*83)
        print("=-"*83)        
        print(" "*50+"Welcome to the online book store"+" "*50)
        print("=-"*83)
        print("=-"*83) 
        print(" "*50+"-Enter 1. To Display")
        print()
        print(" "*50+"-Enter 2. to search")
        print()
        print(" "*50+"-Enter 3. To Buy a book")
        print()
        print(" "*50+"-Enter 4. To register your crendtials for further details of stock")      
        print()
        print(" "*50+"-Enter 5. To exit")
        print()
        try:
            a=int(input(" "*50+"-Select a choice from 1-6: "))
            print()
            if(a==1):
                with open('stock.txt') as infile:
                    for line in infile:
                        print(line)
            elif(a==2):
                search.search()
            elif(a==3):
                ListSplit.listSplit()
                buymain.buyBook()

            elif(a==4):
                buymain.credentials()
            elif(a==5):
                print(" "*50+"Thank you for using online book store")
                cleanData.lineremover()
                cleandata2.lineremover2()
                break
            elif(a==0000 or a==1111):
                login.main()
                flag=False
                cleanData.lineremover()
                cleandata2.lineremover2()
            else:
                print(" "*50+"Please enter a valid choice from 1-5")
        except ValueError:
            print(" "*50+"Please input as suggested.")
start()