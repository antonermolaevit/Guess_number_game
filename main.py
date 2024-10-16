import random


gameIsOn = True
while gameIsOn:

    hiddenNum = random.randint(1, 100)

    attemptCount = 1

    print()
    print("(¯`·._.·"*3, "--- ★ ---", "·._.·´¯)"*3)
    print("#"*19, " ИГРА УГАДАЙ ЧИСЛО ", "#"*19)
    print("(¯`·._.·"*3, "\\(★ ω ★)/", "·._.·´¯)"*3)

    userNum = int(input("\nУгадай число от 1 до 100: "))
    while userNum != hiddenNum:
        if userNum < hiddenNum:
            print(f"(￢_￢;) — {userNum} мало...")
            print(f"Это была {attemptCount}-я попытка. Попробуй еще раз:")
            userNum = int(input())
            attemptCount += 1
        elif userNum > hiddenNum:
            print(f"(」⊙_⊙)」 — {userNum} много!")
            print(f"Это была {attemptCount}-я попытка. Попробуй еще раз:")
            userNum = int(input())
            attemptCount += 1

    print(f"\n{"\\(★ o ★)/ — ПОБЕДА!".center(56, " ")} ")
    print(f"Ты угадал число {userNum}".center(56, " "))
    print(f"У тебя получилось с {attemptCount}-й попытки.".center(56, " "))
    print("(¯`·._.·"*3, f" {userNum} | {attemptCount} ", "·._.·´¯)"*3)

    print()
    print("Хочешь сыграть ещё раз?".center(56, " "))
    print("Если да, введи любой символ и нажми Enter.".center(56, " "))
    print("Если хочешь завершить игру, просто нажми Enter.".center(56, " "))

    gameIsOn = input()
