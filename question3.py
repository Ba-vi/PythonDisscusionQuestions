
#Question 3
# Using loop of your choice, WITI  has tasked you to automate a simple grading system. 
# As a python student, write a program using functions and conditions to display the grades that 
# the students will be receiving. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89% Grade is   B
# 70% - 79% Grade is   C                                                        
# 60% - 69%  Grade is  D                  
# 50% - 59%  Grade is  E  
# < 50%                Fail 

# solution

    # Function to determine the grade based on score
def calculate_grade(score):
    score = int(input("Enter the student's score : "))
    if score == 90 and score <=100:
        print("A") 
    elif score == 80 and score <=89:
        print("B")
    elif score == 70 and score <=79:
        print("C")
    elif score == 60 and score <= 69:
        print("D")
    elif score == 50 and score <= 59:
        print("E")    
    else:
        print("F")

# List to store student scores
scores = []

# Input loop for student scores
while True:
    try:
        score_input = input("Enter a student's score: ")
        
        if score_input == 'done':
            break  # Exit the loop if the user types 'done'
        
        score = float(score_input)  # Convert input to float
        
        # Check if the score is within a valid range
        if 0 <= score <= 100:
            scores.append(score)
        else:
            print("Please enter a score between 0 and 100.")
    
    except ValueError:
        print("Invalid input. Please enter a numeric score.")

# Output grades for each score
print("\nStudent Grades:")
for score in scores:
    grade = calculate_grade(score)
    print(f"Score: {score} - Grade: {grade}")
calculate_grade()    
