import ListSplit
import writing
import sorting
import reading
import time
import graphmaking
import graphmaking1

def owner():
    print(" "*50+"enter 1 to enter data")
    print(" "*50+"enter 2 to sort data")
    print(" "*50+"enter 3 to read data")
    print(" "*50+"enter 4 to plot the graph")
    a=int(input(" "*50+"enter your choice"))
    time.sleep(2)
    if(a==1):
        writing.write()
    elif(a==2):
        print(" "*50+"enter 1 to srot with respect to day")    
        print(" "*50+"enter 2 to srot with respect to year")
        b=int(input(" "*50+"enter your choice"))
        if(b==1):
            sorting.sortieday()
        elif(b==2):
            sorting.sortieyear()
    elif(a==3):
        reading.reunion()
    elif(a==4):
        print(" "*50+"To plot bar graph")
        print(" "*50+"To plot line graph ")
        b=int(input(" "*50+"enter your choice"))
        if(b==1):
            graphmaking1.graph1()
        elif(b==2):
            graphmaking.graph()

