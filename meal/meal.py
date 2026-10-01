

def main():
    time = input("what time is it? ")
    convert(time) = decimal_time

    if  7.00 <= decimal_time <= 8.00:
            print("breakfast time")
    elif 12.00 <= decimal_time <= 13.00:
            print("lunch time")
    elif 18.00 <= decimal_time <= 19.00:
            print("dinner time")

def convert(time):
    hrs, mins = time.split(":")
    hrs = int(hrs)
    mins = int(mins)
    decimal_time = hrs + mins/60
    return decimal_time


if __name__ == "__main__":
    main()
