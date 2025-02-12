# Welcome Message: Display a welcome message to the user.
# 2. Display Questions: Show a series of multiple-choice questions (at least 5).
# 3. User Input: Allow the user to select an answer for each question.
# 4. Calculate Score: Keep track of the user's correct answers and calculate the final score.
# 5. Display Results: Show the user's total score and a message based on their performance.
# 6. Data Validation: Ensure valid input by checking that the user selects an answer within the
# given choices.
# 7. Thank You Message: Thank the user for taking the quiz.
 
def welcome():
    print("Welcome Message")
score = 0
 
 
welcome()
q1 = input("What is the capital city of France? ").capitalize()
 
if q1 == "Paris":
    score = score + 1
    print(f"Correct Answer: Score is {score}")
 
   
else:
    print("Incorrect Answer")
    score = score + 0

print("Question 2: I hope you're ready!")
q2 = input("In a game of Rock-Paper-Scissors, What beats Paper? ").capitalize()
 
if q2 == "Scissors":
    score = score + 1
    print(f"Correct Answer: Score is {score}")
 
   
else:
    print("Incorrect Answer")
    score = score + 0

print("Question 3: Halfway there, Keep it up")
q3 = input("Pokemon is a franchise created by what game company? ").capitalize()
 
if q3 == "Nintendo":
    score = score + 1
    print(f"Correct Answer: Score is {score}")
 
   
else:
    print("Incorrect Answer")
    score = score + 0

print("Question 4: Believe in the me that believes in you!")
q4 = input("What Christian Holiday is celebrated on the 25th December? ").capitalize()
 
if q4 == "Christmas":
    score = score + 1
    print(f"Correct Answer: Score is {score}")
 
   
else:
    print("Incorrect Answer")
    score = score + 0

print("I lied. This is the halfway point!")
q5 = input("When did WWII start? ").capitalize()
 
if q5 == "1939":
    score = score + 1
    print(f"Correct Answer: Score is {score}")
 
   
else:
    print("Incorrect Answer")
    score = score + 0

print("On to the second half of questions!")
q6 = input("Spiderman is a superhero who is a part of what Universe? ").capitalize()
 
if q6 == "Marvel":
    score = score + 1
    print(f"Correct Answer: Score is {score}")
 
   
else:
    print("Incorrect Answer")
    score = score + 0

print("I hope your school knowledge is still fresh!")
q7 = input("In the book Frankenstein, Does the Monster have a name? ").capitalize()
 
if q7 == "No":
    score = score + 1
    print(f"Correct Answer: Score is {score}")
 
   
else:
    print("Incorrect Answer")
    score = score + 0

print("Have you ever been to Japan? I want to go eventually.")
q8 = input("What is the currency of Japan? ").capitalize()
 
if q8 == "Japanese yen":
    score = score + 1
    print(f"Correct Answer: Score is {score}")
 
   
else:
    print("Incorrect Answer")
    score = score + 0

print("2 more to go and I'm already running out of things to type up!")
q9 = input("Autumn,Summer,Spring. What season am I missing? ").capitalize()
 
if q9 == "Winter":
    score = score + 1
    print(f"Correct Answer: Score is {score}")
 
   
else:
    print("Incorrect Answer")
    score = score + 0

print("This is end! Here's my final question!")
q10 = input("What coding language was used to create this quiz? ").capitalize()
 
if q10 == "Python":
    score = score + 1
    print(f"Correct Answer: Score is {score}")
 
   
else:
    print("Incorrect Answer")
    score = score + 0

print("Congratulations on completing the quiz, You got " + str(score) + " questions correct!")

print("Congratulations on completing the quiz, You got " + str((score/10) * 100) + " %.")