
#Question 4(i)
# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.

#solution
favourite_foods =["rice" , "irish" , "bananas", "spaghetti" ]
print(f"My fourite food is : {favourite_foods}")

# adding two favourite dishes
favourite_foods.append("chicken")
favourite_foods.append("pilawo")
 # removing one favourite dish
favourite_foods.remove("bananas")

for dishes in favourite_foods:
    print(f"My updated list is : {favourite_foods}")

 






#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.

#solution
numbers = [2 , 5 , 8 , 10 , 3 , 6 ]
print(numbers[0])
print(numbers[-1])

numbers.reverse()
print(f" The reverse order of the list is :{numbers}" )

total = sum(numbers)
print(f"The sum of the numbers {numbers} is : {total}")