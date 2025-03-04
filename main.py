import random

# T9 mapping for letters to numbers
T9_MAP = {
    'a': 2, 'b': 2, 'c': 2,
    'd': 3, 'e': 3, 'f': 3,
    'g': 4, 'h': 4, 'i': 4,
    'j': 5, 'k': 5, 'l': 5,
    'm': 6, 'n': 6, 'o': 6,
    'p': 7, 'q': 7, 'r': 7, 's': 7,
    't': 8, 'u': 8, 'v': 8,
    'w': 9, 'x': 9, 'y': 9, 'z': 9
}

def generate_employee_id(initials):
    # Ensure initials are lowercase for the T9 mapping
    initials = initials.lower()

    # Get the first, middle, and last letters from the initials
    first_letter = initials[0] if len(initials) > 0 else ''
    middle_letter = initials[len(initials) // 2] if len(initials) > 1 else ''
    last_letter = initials[-1] if len(initials) > 2 else ''

    # Convert initials to T9 format
    first_number = T9_MAP.get(first_letter, 0)
    middle_number = T9_MAP.get(middle_letter, 0)
    last_number = T9_MAP.get(last_letter, 0)

    # Generate a random 4-digit number
    random_number = random.randint(1000, 9999)

    # Combine the letters' T9 values and the random number
    employee_id = f"{first_number}{middle_number}{last_number}{random_number}"
    
    return employee_id

# Prompt user for initials
initials = input("Enter your initials: ")

# Generate employee ID
employee_id = generate_employee_id(initials)

# Display the result
print(f"Your Employee ID is: {employee_id}")
