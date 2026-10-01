def main():
    amount = bill_to_float(input("how much was the bill? : "))
    percent = percent_to_float(input("what percentage of ur bill would you like to tip? : "))
    tip = amount * percent
    total = tip + amount
    print(f"your tip will be ${tip:.2f}")
    print(f"your final amount will be, ${total:.2f}")

def bill_to_float(d):
    d = d.replace("$", " ")
    return float(d)

def percent_to_float(p):
    p = p.replace("%", " ")
    p = float(p)/100
    return(p)

main()
