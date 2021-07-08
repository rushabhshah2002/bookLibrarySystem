import os
def lineremover():
    if not os.path.isfile("Stock.txt"):
        print("{} does not exist ".format("Stock.txt"))
        return
    with open("Stock.txt") as filehandle:
        lines = filehandle.readlines()
    with open("Stock.txt", 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)













