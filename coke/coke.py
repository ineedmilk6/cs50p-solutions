

due = 50
while due>0:
    print("amount due:", due)

    givenamt = int(input("insert coin: "))
    if givenamt in [25, 10, 5]:
       due -= givenamt

print("change owed:", abs(due))

