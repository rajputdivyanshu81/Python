d = {} #this is the way to create empty dictionary

marks ={
    "Harry" : 100,
    "Shubham" : 56,
    "Rohan" : 23
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry":99,"Bhumika":100})
# print(marks)


# print(marks.get("Harry"))
# print(marks["Harry"])

# what is the difference between the use of these things and these return different values when names of those changes to something other name

print(marks.get("Harry2"))#prints none
print(marks["Harry2"])#returns an error