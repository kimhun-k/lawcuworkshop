## Question 1
print("QUESTION 1")
print("\n")
surname = input("Enter your last name: ")
if len(surname) > 15:
    print("Unfortunately, your surname is not SAT-compatible.")
else:
    print("Your surname is SAT-compatible.")
print("\n")

## Question 2
print("QUESTION 2")
print("\n")
print("Welcome to leap year checking!") 
year = int(input("Please enter the year (In Thai Buddism): "))
christyear = year - 543
if christyear % 4 == 0 or christyear % 400 == 0:
    print(str(year) + " is a leap year!")
else:
    print(str(year) + " is unfortunately NOT a leap year.")
print("\n")

## Question 3
print("QUESTION 3")
print("\n")
while True:
    mainanswer = input("Do you want to go to the university? (Type Y for Yes, and N for No.): ")
    if mainanswer == "Y":
        break # continue to the next question
    elif mainanswer == "N":
        break # continue to the next question
    else:
        print("Sorry, we can't properly detect your answer.")

secondquest = input("If yes, do you have a specific university in mind?: ")
thirdquest = input("Interesting, which field of study are you interested in?: ")
if mainanswer == "Y":
    print("You should apply to LLBel Chula.")
elif mainanswer == "N":
    print("Too bad! :(")
print("\n")

## QUESTION 4
print("QUESTION 4")
print("\n")
firstword = input("Enter the first word: ")
secondword = input("Enter the second word: ")
if firstword.isupper() and secondword.isupper():
    print("Oops!")
else:
    print(firstword + " " + secondword)
print("\n")

## QUESTION 5
print("QUESTION 5")
print("\n")
print("Let's reflect your expenses of this week!")
Maxmoney = 0
moneys = []
for i in range(7):
    money = float(input("How much did you spend?: " ))
    moneys.append(float(money))
    total = sum(moneys)
    if money > Maxmoney:
        Maxmoney = money
average = float(total) / int(7)
print(f"Your average amount of money used per day is {average}")
print(f"The maximum amount of money used per day is {Maxmoney}")
print("\n")

## QUESTION 6
print("QUESTION 6")
print("\n")
print("What do you think of LLBel? :)")
while True:
    word1 = input("What do you think?: ")
    word2 = input("What else?: ")
    if word1 == "LLBel" and word2 == "rocks":
        break # exit the loop girl
    else:
        continue
print("Yes! LLBel definitely rocks.")

print("\n")

print("DONE!")