import re

def check_password_strength(password):
    print(f"\nChecking: {password}")

    # Check if password starts or ends with whitespace
    if re.search(r'^\s|\s$', password):
        print("✗ Should not start or end with whitespace")
    
    # Minimum length 8 characters
    if not re.search(r'.{8,}', password):
        print("✗ Too short (minimum 8 characters)")

    # At least one uppercase letter
    if not re.search(r'[A-Z]', password):
        print("✗ Missing uppercase letter")

    # At least one lowercase letter
    if not re.search(r'[a-z]', password):
        print("✗ Missing lowercase letter")

    # At least one digit
    if not re.search(r'[0-9]', password):
        print("✗ Missing number")

    # At least one special character from the set
    if not re.search(r'[!@#$%^&*()\-+=|\\{}[\]:;"\'<>,.?/~]', password):
        print("✗ Missing special character")

    # Too many repeated characters (like aaa or 111)
    if re.search(r'(.)\1{2,}', password):
        print("Note: Repeating characters too much")

    print("Check complete.\n")

# Test passwords
password = input("Enter your password:")
check_password_strength(password)      
check_password_strength("fab111")
check_password_strength("Dahlia@123")     # Strong
check_password_strength("   cat@123   ")  # Starts/ends with whitespace
check_password_strength("Caaat@123")      # Repeating character
