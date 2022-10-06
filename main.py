def transcribe(seq):
    trans_seq = ""
    for char in seq:
        trans_seq += RNA_dict[char]
    return trans_seq


def complement(seq):
    compl_seq = ""
    for char in seq:
        compl_seq += DNA_dict[char]
    return compl_seq


def reverse(seq):
    return seq[::-1]


def reverse_complement(seq):
    rev_compl_seq = ""
    for char in seq:
        rev_compl_seq += DNA_dict[char]
    return rev_compl_seq[::-1]


commands = ["transcribe", "complement", "reverse", "reverse complement"]

RNA_dict = {"T": "U",
            "A": "A",
            "G": "G",
            "C": "C",
            "t": "u",
            "a": "a",
            "g": "g",
            "c": "c"}

DNA_dict = {"T": "A",
            "A": "T",
            "G": "C",
            "C": "G",
            "t": "a",
            "a": "t",
            "g": "c",
            "c": "g"}

while True:
    user_command = input("Please, enter command: ")

    if user_command == "exit":
        print("Have a nice day =^.^=")
        exit()

    elif user_command not in commands:
        print("Invalid command. Please, try again!")

    else:
        user_sequence = input("Please, enter your sequence: ")
        
        if user_command == "transcribe":
            try:
                print(transcribe(user_sequence))
            except KeyError:
                print("Invalid alphabet! Please, try again.")

        elif user_command == "reverse":
            try:
                print(reverse(user_sequence))
            except KeyError:
                print("Invalid alphabet! Please, try again.")

        elif user_command == "complement":
            try:
                print(complement(user_sequence))
            except KeyError:
                print("Invalid alphabet! Please, try again.")

        elif user_command == "reverse complement":
            try:
                print(reverse_complement(user_sequence))
            except KeyError:
                print("Invalid alphabet! Please, try again.")
