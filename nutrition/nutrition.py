
fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    # ... rest from the poster
}

item = input("Item: ").strip().lower()

if item in fruits:
    print("Calories:", fruits[item])
