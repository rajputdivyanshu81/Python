marks1 = int(input("enter marks 1:"))
marks2 = int(input("enter marks 2:"))
marks3 = int(input("enter marks 3:"))
marks4 = int(input("enter marks 4:"))

# check for the total percentage
total_percentage = (100)*(marks1 + marks2 + marks3 + marks4)/400

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33):
    print("you are pass",total_percentage)
else:
    print("you failed ,try again next year",total_percentage)

