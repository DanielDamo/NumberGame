#number game, players take turns adding numbers
#between 1 and 10 and the person who reaches the target
#wins. AI always goes first ;)

def AI(sum : int, target) -> int:
    perfectNums = []
    temp = target
    while temp > 10 and temp > sum:
        perfectNums.append(temp - 11)
        temp -= 11
    perfectNums.append(target)
    idealNum = 0
    difference = 1000000
    for num in perfectNums:
        if num - sum > 0 and num - sum < difference:
            difference = num - sum
            idealNum = num
    add = idealNum - sum

    print("AI added " + str(add) + ". New sum is: " + str(sum + add))
    return (add)

target = int(input("What do you want the target to be?: "))
turnCount = 1
total = 0
while total < target:
    if turnCount % 2 == 0:
        num = int(input("SUM: " + str(total) + "\nEnter a number between 1 and 10 to: "))
        while num not in range(1,11):
            num = int(input("Not a valid input, please enter a number between 1 and 10: "))
        total += num
    else:
        total += AI(total, target)
    turnCount += 1

if turnCount % 2 == 0:
    print("You lose!")
else:
    print("You win!")

input()