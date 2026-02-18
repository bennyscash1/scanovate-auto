from datetime import date
import random
import os

def generate_random_numbers(count=5):
    return ''.join(str(random.randint(0, 9)) 
                   for _ in range(count))


def generate_email(valid_email=True):
    random_part = generate_random_numbers()

    if valid_email:
        return f"bennys+{random_part}@gmail.com"

    invalid_emails = [
        f"bennys{random_part}gmail.com", 
        f"bennys+{random_part}@",             
        f"@gmail.com",                         
        f"bennys+{random_part}@gmail",         
        f"bennys+{random_part}@.com",          
        f"bennys+{random_part}!@gmail.com", 
        f"bennys +{random_part}@gmail.com",    
    ]

    return random.choice(invalid_emails)
    

def generate_full_name():
    first_names = ["John", "Jane", "Alice", "Bob", "Charlie"]
    last_names = ["Doe", "Smith", "Johnson", "Brown", "Davis"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    return f"{first_name} {last_name}"


def generate_numbers_string(length):
    return ''.join(str(random.randint(0, 9)) for _ in range(length))


def generate_user_id():
    id_digits = [0] * 9

    # Generate the remaining digits randomly starting from the second position
    for i in range(1, 8):
        id_digits[i] = random.randint(0, 9)

    total_sum = 0
    for i in range(8):
        digit = id_digits[i]
        if i % 2 == 0:
            total_sum += digit
        else:
            doubled = digit * 2
            total_sum += (doubled % 10) + (doubled // 10)

    # Calculate checksum digit
    check_digit = (10 - (total_sum % 10)) % 10
    id_digits[8] = check_digit

    return "".join(map(str, id_digits))