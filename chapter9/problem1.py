
with open("poem.txt", "r") as f:
    content = f.read()
    if "twinkle" in content:
        print("The word 'twinkle' is present in the content.")
    else:
        print("The word 'twinkle' is not present in the content.")

f.close()
