
def FileWrite(fileName, contains):
    print("def FileWrite")
    file = open(fileName, "a")
    file.write(contains)
    file.write("\n")
    file.close()


def FileRead(fileName):
    print("def FileRead")
    file = open(fileName,"r")
    print(file.read())
    file.close()
