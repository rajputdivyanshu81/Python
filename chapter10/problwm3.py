from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train No: {self.trainNo} from {fro} to {to}")
        
    def getStatus(self):
        print(f"Train No: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

s = Train(12399)
s.book("Rampur","Delhi")