import os
    def lineremover2():
    if not os.path.isfile("business1.txt"):
        print("{} does not exist ".format("business1.txt"))
        return
    with open("business1.txt") as filehandle:
        lines = filehandle.readlines()

    with open("business1.txt", 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)
