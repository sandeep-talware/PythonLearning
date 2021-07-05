import threading


class threadOperation(threading.Thread):

    def __init__(self, threadId, name, number1, number2):
        threading.Thread.__init__(self)
        self.threadID = threadId
        self.setName(name)
        self.number1 = number1
        self.number2 = number2

    def run(self) -> None:
        print("starting .. ThreadID : " + str(self.threadID))
        print("starting .. Thread_Name : " + self.getName())
        for i in range(200):
            print("This is Thread for addition : " + self.getName())
        print("Addition of Thread " + self.getName() + " is : " + str(self.number1 + self.number2))
        print("stopping .. ThreadID : " + str(self.threadID))
        print("stopping .. Thread_Name : " + self.getName())
