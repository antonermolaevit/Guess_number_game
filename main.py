import random


def inputIsCorrect(userInput) -> bool:
    if userInput.isdigit() == False:
        print(f"{userInput} — это не число цифрами")
        return False
    if int(userInput) > 100:
        print(f"Число {userInput} больше 100")
        return False
    if int(userInput) < 1:
        print(f"Число {userInput} меньше 1")
        return False
    else:
        return True

def getCorrectInput() -> int:
    userInput = input()
    while inputIsCorrect(userInput) == False:
        userInput = input("Введи число от 1 до 100: ")

    return int(userInput)

def diaplayInitialDecoration():
    print()
    print("(¯`·._.·"*3, "--- ★ ---", "·._.·´¯)"*3)
    print("#"*19, " ИГРА УГАДАЙ ЧИСЛО ", "#"*19)
    print("(¯`·._.·"*3, "\\(★ ω ★)/", "·._.·´¯)"*3)

def displayAnswerDecoration(answerNum, attempt):
        if answerNum < hiddenNum:
            print(f"(￢_￢;) — {answerNum} мало...")
            print(f"Это была {attempt}-я попытка. Попробуй еще раз:")           
        elif answerNum > hiddenNum:
            print(f"(」⊙_⊙)」 — {answerNum} много!")
            print(f"Это была {attempt}-я попытка. Попробуй еще раз:")

def displayFinalDecoration(number, attempt):
    print(f"\n{"\\(★ o ★)/ — ПОБЕДА!".center(56, " ")} ")
    print(f"Ты угадал число {number}".center(56, " "))
    print(f"У тебя получилось с {attempt}-й попытки.".center(56, " "))
    print("(¯`·._.·"*3, f" {number} | {attempt} ", "·._.·´¯)"*3)

    print()
    print("Хочешь сыграть ещё раз?".center(56, " "))
    print("Если да, введи любой символ и нажми Enter.".center(56, " "))
    print("Если хочешь завершить игру, просто нажми Enter.".center(56, " "))


gameIsOn = True
while gameIsOn:

    hiddenNum = random.randint(1, 100)

    diaplayInitialDecoration()
    print("\nУгадай число от 1 до 100: ")
    
    userNum = getCorrectInput()
    attemptCount = 1
    while userNum != hiddenNum:
        displayAnswerDecoration(userNum, attemptCount)
        attemptCount += 1
        userNum = getCorrectInput()

    displayFinalDecoration(userNum, attemptCount)

    gameIsOn = input()
