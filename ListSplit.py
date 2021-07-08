def listSplit():
    global bookname
    global authorname
    global quantity
    global cost
    global language
    global rating
    global date
    global edition
    bookname=[]
    authorname=[]
    quantity=[]
    cost=[]
    language=[]
    rating=[]
    date=[]
    edition=[]
    with open("stock.txt","r") as f:
        
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    bookname.append(a)
                elif(ind==1):
                    authorname.append(a)
                elif(ind==2):
                    quantity.append(a)
                elif(ind==3):
                    cost.append(a)
                elif(ind==4):
                    language.append(a)
                elif(ind==5):
                    rating.append(a)
                elif(ind==6):  
                    date.append(a)
                elif(ind==7):
                    edition.append(a)


                ind+=1