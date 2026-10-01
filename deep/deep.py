qsn = input("what is the answer to the Great Question of Life, the Universe and Everything? ")
qsn = qsn.strip().lower()
match qsn:
    case "42" | "forty-two" | "forty two"  :
        print("Yes")
    case _:
        print("No")
