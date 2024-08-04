class Employee:
    language = "python"
    salary =1200000
# yha hmko self dena hi padta hai
    def __init__(self):#dunder method hai ye and ye automatically call ho jat ahai
       
       print("i am creating an object")

    def getInfo(self):
      print(f"the language is {self.language} and the salary is {self.salary}")


# ye static mark krne ke bad self hi jaruurat nhi hoti hai

    @staticmethod
    def greet():
       print("good morning")

harry = Employee()
harry.name = ("Divyanshu Rajput")
harry.language = "javascript" #at a instance deya jata hai and ye help karega
print(harry.name,harry.salary)