# Assignment 1: AI-Generated Python Problems
# Name: [Your Name Here]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
I'm learning Python basics in a high school programming class. I have some experience with GDScript and Java. Can you create 5-7 practice problems that cover:
* Variables and basic data types
* Conditionals (if/elif/else)
* Loops (for and while)
* Functions
* Basic list operations

Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs.

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
# Python Practice Problems

## Problem 1: Temperature Converter (Variables & Conditionals)
**Concepts:** Variables, input/output, conditionals, basic math

Write a program that converts temperatures between Celsius and Fahrenheit. The program should:
1. Ask the user for a temperature value
2. Ask whether they want to convert from 'C' to 'F' or 'F' to 'C'
3. Perform the conversion and display the result
4. Handle invalid conversion types with an error message

**Formulas:**
- Celsius to Fahrenheit: F = (C × 9/5) + 32
- Fahrenheit to Celsius: C = (F - 32) × 5/9

**Example Input/Output:**
```
Enter temperature: 25
Convert from (C)elsius or (F)ahrenheit? C
25.0°C = 77.0°F

Enter temperature: 80
Convert from (C)elsius or (F)ahrenheit? F
80.0°F = 26.67°C

Enter temperature: 100
Convert from (C)elsius or (F)ahrenheit? X
Invalid conversion type!
```
"""





def convert_temp():
    var1 = float(input())
    var2 = var1
    print("Convert from (C)elsius or (F)ahrenheit? ")
    convert = input()
    if convert == "C" or convert == "Celsius" or convert == "c" or convert == "celsius":
        var2 *= 9.0/5.0
        var2 += 32
        print(str(var1)+"°C = "+str(var2)+"°F")
        #F = (C × 9/5) + 32
    elif convert == "F" or convert == "Fahrenheit" or convert == "f" or convert == "fahrenheit":
        var2 -= 32
        var2 *= 5.0/9.0
        print(str(var1)+"°F = "+str(var2)+"°C")
        #C = (F - 32) × 5/9
    else:
        print("Invalid conversion type!")

"""
---

## Problem 2: Grade Calculator (More Conditionals)
**Concepts:** Multiple conditionals, elif statements, input validation

Create a program that calculates letter grades based on numerical scores:
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: Below 60

The program should also validate that the score is between 0 and 100.

**Example Input/Output:**
```
Enter your score: 85
Your grade is: B

Enter your score: 92
Your grade is: A

Enter your score: 105
Error: Score must be between 0 and 100

Enter your score: 45
Your grade is: F
```
"""
def grade_calculator():
    print("Enter your score: ")
    grade = float(input())
    if grade >= 90:

"""
---

## Problem 3: Number Guessing Game (While Loops & Conditionals)
**Concepts:** While loops, random numbers, conditionals, counters

Create a number guessing game where:
1. The computer picks a random number between 1 and 100
2. The player has up to 7 attempts to guess it
3. After each guess, tell the player if their guess is too high, too low, or correct
4. Keep track of the number of attempts
5. End the game when they guess correctly or run out of attempts

**Example Input/Output:**
```
I'm thinking of a number between 1 and 100!
You have 7 attempts.

Attempt 1 - Enter your guess: 50
Too low! Try again.

Attempt 2 - Enter your guess: 75
Too high! Try again.

Attempt 3 - Enter your guess: 63
Congratulations! You guessed it in 3 attempts!

--- OR ---

Attempt 7 - Enter your guess: 45
Too low! Game over. The number was 67.
```

**Hint:** Use `import random` and `random.randint(1, 100)` to generate a random number.

---

## Problem 4: List Statistics Function (Functions & Lists)
**Concepts:** Functions, list operations, for loops, math operations

Write a function called `calculate_stats(numbers)` that takes a list of numbers and returns a dictionary containing:
- The sum of all numbers
- The average (mean)
- The minimum value
- The maximum value
- The count of numbers

Then write a main program that asks the user to input numbers (one per line) until they enter 'done', and then displays the statistics.

**Example Input/Output:**
```
Enter numbers (type 'done' to finish):
10
25
5
30
15
done

Statistics:
Sum: 85
Average: 17.0
Minimum: 5
Maximum: 30
Count: 5
```

---

## Problem 5: Word Frequency Counter (Nested Loops & Advanced Lists)
**Concepts:** For loops, string operations, lists, dictionaries, conditionals

Write a program that:
1. Asks the user to enter a sentence
2. Counts how many times each word appears (case-insensitive)
3. Displays the words and their frequencies, sorted by frequency (highest first)
4. Ignores common punctuation (periods, commas, exclamation marks, question marks)

**Example Input/Output:**
```
Enter a sentence: The quick brown fox jumps over the lazy dog. The fox is quick!

Word frequencies:
the: 3
quick: 2
fox: 2
brown: 1
jumps: 1
over: 1
lazy: 1
dog: 1
is: 1
```

---

## Problem 6: Password Validator Function (Complex Conditionals & String Operations)
**Concepts:** Functions, string methods, complex conditionals, loops

Create a function `validate_password(password)` that checks if a password meets these criteria:
- At least 8 characters long
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit
- Contains at least one special character (!@#$%^&*)

The function should return a tuple: (is_valid, list_of_issues)

Write a main program that keeps asking for passwords until a valid one is entered.

**Example Input/Output:**
```
Enter a password: hello
Password issues:
- Must be at least 8 characters long
- Must contain at least one uppercase letter
- Must contain at least one digit
- Must contain at least one special character

Enter a password: HelloWorld
Password issues:
- Must contain at least one digit
- Must contain at least one special character

Enter a password: HelloWorld123!
Password is valid!
```

---

## Problem 7: Shopping Cart Manager (All Concepts Combined)
**Concepts:** Functions, lists, dictionaries, loops, conditionals, string formatting

Create a shopping cart program with these features:
1. A menu system with options to add items, remove items, view cart, and checkout
2. Items have names and prices
3. The cart should track quantities of each item
4. Calculate subtotal, tax (8.5%), and total
5. Allow removing items or changing quantities

**Functions to implement:**
- `add_item(cart, name, price, quantity)`
- `remove_item(cart, name, quantity)`
- `display_cart(cart)`
- `calculate_total(cart, tax_rate)`

**Example Input/Output:**
```
=== SHOPPING CART ===
1. Add item
2. Remove item
3. View cart
4. Checkout
5. Exit

Choose an option: 1
Item name: Apple
Price: 1.50
Quantity: 3
Added 3 Apple(s) at $1.50 each to cart.

Choose an option: 3
=== YOUR CART ===
Apple x3 @ $1.50 each = $4.50

Subtotal: $4.50
Tax (8.5%): $0.38
Total: $4.88

Choose an option: 4
Thank you for your purchase!
Final total: $4.88
```

---

## Tips for Success:
1. Start with Problem 1 and work your way up
2. Test your programs with different inputs, including edge cases
3. Use meaningful variable names
4. Add comments to explain complex logic
5. Don't be afraid to break complex problems into smaller functions
6. Remember that Python is case-sensitive and uses indentation for code blocks
"""











# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
#convert_temp()

print("\nTesting Problem 2:")
# Add your tests here

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


