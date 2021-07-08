import ListSplit
import bookauthorsearch
import bookpricesearch
import booklanguagesearch
import bookratingsearch
import time
def search():
    print(" "*50+"[cost] [authoname] [bookname] [language]")
    time.sleep(2)
    print (" "*50+"From above chose any option from which you want to chose book ")
    print(" "*50+"If you want to chose book according to language write 4 ")
    print(" "*50+"If you want to find rating of any book write 5 ")
    print(" "*50+"If you want to chose according cost write 3")
    print(" "*50+"If you want to chose according to author name write 1 ")
    print(" "*50+"If you want to according to  bookname write 0 ")
    searchInput = int(input("Enter the number here :"))
    if searchInput==1:
        bookauthorsearch.author()
    elif searchInput==3:
        bookpricesearch.price()
    elif searchInput==4:
        booklanguagesearch.languager()
    elif searchInput==5:
        bookratingsearch.rating()
    else:
        print(" "*50+"you have entered wrong input")

        