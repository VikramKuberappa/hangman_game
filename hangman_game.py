# Hangman game
import random
import os
import sys
states = ["andrapradesh", "bihar", "chattisgarh", "karnataka", "kerala",
          "tamilnadu", "gujarat", "maharastra", "westbengal", "assam", ]
temp = random.choice(states)
temp1 = list(temp)
# print(temp)
length = len(temp1)
ans = list("_"*length)
print(ans)
chance = 0
count = 0
store = []
letter = '-'
while chance < 9:
    if count == length:
        chance = chance+1
        print("chances over:{}".format(chance))
        count = 0
    else:
        count = 0
        letter = str(input("Guess a letter: "))
        if letter in store:
            print("Already entered value!!")
        else:
            store.append(letter)
            for x in range(0, length):
                if temp[x] == letter:
                    ans[x] = letter
                    os.system('cls')
                    print(ans)
                    if temp1 == ans:
                        print("Correct answer, its {}!!!".format(temp))
                        sys.exit()
                    else:
                        pass
                else:
                    count = count+1
else:
    print("Wrong answer,its {}!!!".format(temp))
