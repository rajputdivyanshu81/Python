#using the walrus opertor

if(n := len([1,2,3,4,5])) > 3:print(f"list is too long ({n}elements,expected <= 3)") 
#output list is too long (5 elements,expected <= 3)