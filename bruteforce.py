import hashlib
import itertools
import string
import time

'''
Checking password if it follows the established rules:
    1. The password should be at least 8 characters long.
    2. The password should contain at least one uppercase letter.
    3. The password should contain at least one lowercase letter.
    4. The password should contain at least one digit.
    5. The password should contain at least one special character.
'''

def validate_password(password):
    if len(password) < 4:
        return False, 'Password must contain at least 8 characters.'

    if not any(char.isupper() for char in password):
        return False, 'Password must contain at least one uppercase letter.'

    if not any(char.islower() for char in password):
        return False, 'Password must contain at least one lowercase letter.'

    if not any(char.isdigit() for char in password):
        return False, 'Password must contain at least one digit.'

    # if all(char not in string.punctuation for char in password):
    #     return False, 'Password must contain at least one special character.'

    return True, 'Password meets all requirements.'

# Hashing password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Brute force simulator
def brute_force(hashed_password, maximum_length=3):
    # Generate all possible combinations of characters
    possible_characters = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    
    start_time = time.time()  # Start timing the brute-force process
    
    for password_length in range(1, maximum_length + 1):
        for password_guess in itertools.product(possible_characters, repeat=password_length):
            password_guess = ''.join(password_guess)
            attempts += 1
            
            if hash_password(password_guess) == hashed_password:
                end_time = time.time()  # End timing
                time_taken = end_time - start_time  # Calculate time taken
                print(f"Password found: {password_guess}")
                print(f"Attempts: {attempts}")
                print(f"Time taken: {time_taken:.2f} seconds")
                return password_guess
    
    end_time = time.time()  # End timing if password is not found
    time_taken = end_time - start_time
    print(f"Password not found within {attempts} attempts.")
    print(f"Time taken: {time_taken:.2f} seconds")
    return None

# Main function
def main():
    # Entering the password to validate and crack
    target_password = input("Enter the password to be cracked: ")
    
    # Validating password
    valid, message = validate_password(target_password)
    if not valid:
        print(f"Password validation failed: {message}")
        return  # Exit the program if the password doesn't meet the requirements
    
    print("Password validation passed.")
        
    # Hash the password 
    hashed_password = hash_password(target_password)
    print(f"Hashed password: {hashed_password}")
    
    # Start brute force attack simulation
    brute_force(hashed_password, maximum_length=len(target_password))

# Execute the main function
if __name__ == "__main__":
    main()
