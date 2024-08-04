def rem(l,word):
    for item in l:
        l.remove(word)
        return l
    
l = {"harry","rahul","ravi"}

print(rem(l,"rahul"))


