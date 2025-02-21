print("Help General Grievous to increase his light sabers collection!")
print("Which planet is most likely to have a jedi on it?")
print("A. Hoth")
print("B. Coruscant")
print("C. Endor")
respota: str = input("Enter the letter of the correct answer: ")
if respota == "B" or respota == "b":
    print("Correct!")
    print("But now you must find the easiest target to steal a light saber from.")
    print("Which of these are you sending General Grievous to?")
    print("A. A jedi master")
    print("B. A jedi knight")
    print("C. A padawan")
    respota2: str = input("Enter the letter of the correct answer: ")
    if respota2 == "C" or respota2 == "c":
        print("Correct!")
        print("General Grievous has successfully increased his light saber collection!")
    elif respota2 == "B" or respota2 == "b":
        print("Incorrect!")
        print("General Grievous was defeated but manage to escape, he is also not very happy with you!")
    else:
        print("Incorrect!")
        print(
            "General Grievous was defeated and captured, a great lost for the separatists!")
elif respota == "A" or respota == "a":
    print("Incorrect!")
    print("There are no jedi on Hoth, General Grievous is very angry with your failure!")
else:
    print("Incorrect!")
    print("There are no jedi on Endor, General Grievous is very angry with your failure!")
