letter = '''Dear <|Name|>
you are selected!
<|Date|> '''

# you can do chaining after the use of the replace funcrtion

print(letter.replace("<|Name|>","Divyanshu").replace("<|Date|","25 sept 2027"))