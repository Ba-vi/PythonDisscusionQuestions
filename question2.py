# Question 2(i)

# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and sen their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese"


#solution
def calculate_bmi():
    weight = float(input("Enter the weight in kilograms:"))
    height = float(input("Enter the height in meters:"))
    BMI = weight/height
    if BMI < 18.5:
        print(f"under weight")
    elif 18.5<= BMI <=24.9:
        print(f"Normal weight")
    elif 25<= BMI <=29.9:
        print(f"overweight")
    else:
        print(f"Obese")
calculate_bmi()                   
 





# Question 2(ii)
# Use a function to calculate the volume of a cylinder V = π r2 h. Choose a function name in line with what you want to 
# achieve. Radius r and height h should be in parameters. Make sure you use the real pie value (import math)

# solution
def volume_of_a_cylinder():
    radius = float(input("Enter the radius of a cylinder :"))
    height = float(input("Enter the height of a cylinder :"))
    import math
    pie = math.pi
    volume = pie*radius**2*height
    print(f"The volume of a cylinder with radius {radius} and height {height} is {volume}")
volume_of_a_cylinder()    
