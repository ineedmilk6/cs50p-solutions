

def main():
    x = get_int()

    print(x)

def get_int():
    while True:
        try:
            s = input("Fraction: ")
            x, y = s.split("/")
            x = int(x)
            y = int(y)

            if y == 0 or x < 0 or y <=0:
                continue
            percent = round(x/y *100)

            if percent <= 1:
                 return"E"

            elif percent >= 99:
                return"F"

            else:
                return f"{percent}%"

        except ValueError:
            pass

main()

