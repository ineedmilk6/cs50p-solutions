def main():
    text = input("enter ur text: ")
    print(convert(text))

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text
main()

