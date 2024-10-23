
# Question 1(i)
# Temperature Classifier: Using a function, write a Python script that takes a temperature as input and classifies it into the 
# following categories: 
# Below 0°C: Freezing
# 0 to 10°C: Cold 
# 11 to 20°C; Moderate 
# 21 to 30°C: Warm 
# Above 30°C: Hot 

def temp_classifier():
    temp = int(input("Enter the temperature in celcious degrees:"))
    if temp <= 0:
        print(f"Freezing")
    elif temp >= 0 and temp <= 10:
        print(f"cold")
    elif temp >= 11 and temp <= 20:
        print(f"moderate")
    elif temp >= 21 and temp <= 30:
        print(f"warm")
    else:
        print(f"hot")
temp_classifier()







# Question 1(ii)
# The volume of a sphere with radius r is (4/3)*pie*r**2. What is the volume of the sphere with radius 8. 
# Use a function and make sure the radius is entered from the keyboard and provide the answer in 1 decimal place

#solution
def volume_of_a_sphere():
       r = float(input("Enter the radius of a sphere:"))
       import math
       pie = math.pi
       volume = 4/3*pie*r**2
       print(f"The volume of a sphere with radius {r} is : {volume:.1f}")
volume_of_a_sphere()
