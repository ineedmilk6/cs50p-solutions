word = input("Input:")

output = ""
for c in word:
    if c.lower() not in ["a", "e", "i", "o", "u"]:
        output += c
print ("output:", output)
