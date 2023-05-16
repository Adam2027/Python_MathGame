print("Math Game")
 
score = 0

# Question 1
print("1. What is 4 + 700?")
answer1 = input("Enter your answer: ")

if answer1 == "704":
    score += 1
    print("Correct!")
else:
    score -= 1
    print("Wrong!")

# Question 2
print("2. What is the square root of 64?")
answer2 = input("Enter your answer: ")

if answer2 == "8":
    score += 1
    print("Correct!")
else:
    score -= 1
    print("Wrong!")

# Question 3
print("3. What is 15 divided by 3?")
answer3 = input("Enter your answer: ")

if answer3 == "5":
    score += 1
    print("Correct!")
else:
    score -= 1
    print("Wrong!")

# Question 4
print("4. What is 12 multiplied by 5?")
answer4 = input("Enter your answer: ")

if answer4 == "60":
    score += 1
    print("Correct!")
else:
    score -= 1
    print("Wrong!")

# Question 5
print("5. What is the result of 7 to the power of 2?")
answer5 = input("Enter your answer: ")

if answer5 == "49":
    score += 1
    print("Correct!")
else:
    score -= 1
    print("Wrong!")

# Question 6
print("6. What is the value of pi (approximately)?")
answer6 = input("Enter your answer: ")

if answer6 == "3.14159":
    score += 1
    print("Correct!")
else:
    score -= 1
    print("Wrong!")

print(f"Your score: {score}")
