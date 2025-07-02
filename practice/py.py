
# Exercise 3: Hard - Advanced Password Security Checker
# Objective: Practice complex conditional logic with multiple validation criteria and nested conditions.
# Problem:
# Create an advanced password security checker that evaluates a password based on multiple criteria and provides detailed feedback. The program should check for various security requirements and give a security score.
# Password Criteria:

# Length Requirements:

# Minimum 8 characters (required)
# 12+ characters (strong bonus)
# 16+ characters (excellent bonus)


# Character Variety:

# At least one lowercase letter (required)
# At least one uppercase letter (required)
# At least one digit (required)
# At least one special character: !@#$%^&*()_+-=[]{}|;:,.<>? (strong bonus)


# Security Patterns:

# No common patterns like "123", "abc", "password" (case-insensitive)
# No repeated characters more than 2 times in a row
# No keyboard patterns like "qwerty", "asdf"


# Advanced Checks:

# Not a common weak password from a predefined list
# No personal information patterns (if username provided)



# Scoring System:

# Start with 0 points
# Length 8-11: +2 points
# Length 12-15: +3 points
# Length 16+: +4 points
# Each required criteria met: +2 points
# Special characters: +2 points
# No common patterns: +2 points
# No repeated characters: +1 point
# No keyboard patterns: +1 point
# Not in weak password list: +2 points

# Security Levels:

# 0-5 points: Very Weak
# 6-8 points: Weak
# 9-12 points: Moderate
# 13-15 points: Strong
# 16+ points: Very Strong

# Requirements:

# Use complex nested conditional statements
# Create helper functions for pattern checking
# Provide detailed feedback for each failed criteria
# Suggest improvements for weak passwords
# Handle edge cases and invalid input
# Use loops within conditionals where appropriate

# Example Output:
# Advanced Password Security Checker
# ==================================
# Enter your password: MyP@ssw0rd123!
# Enter your username (optional): john_doe

# Analyzing password security...

# ✓ Length requirement met (13 characters)
# ✓ Contains lowercase letters
# ✓ Contains uppercase letters  
# ✓ Contains digits
# ✓ Contains special characters
# ✓ No common weak patterns detected
# ✓ No excessive repeated characters
# ✓ No keyboard patterns detected
# ✓ Not in common weak password list
# ✓ No obvious personal information detected

# SECURITY SCORE: 16/18
# SECURITY LEVEL: Very Strong

# Your password meets all security requirements!

# Suggestions for even better security:
# - Consider using a longer passphrase (20+ characters)
# - Avoid dictionary words when possible
# Bonus Features:

# Add a password strength meter (visual representation)
# Include a password generator suggestion feature
# Check against a list of commonly breached passwords
# Add support for checking multiple passwords in sequence


# Character Variety:


SPECIAL_CHARS = set("!@#$%^&*()_+-=[]{}|;:,.<>?")
KEYWARD_PATTERNS = ["qwerty", "asdf"]
COMMON_PATTERNS = ["123", "abc", "password"]

def evaluate_password(password):
    score = 0
    feedback = []
    
    length = len(password)
    if length >= 16:
        feedback.append("Excellent length (16+ characters)")
        score += 3
    elif length >= 12:
        feedback.append("Strong length (12-15 characters)")
        score += 2
    elif length >= 8:
        feedback.append("Moderate length (8-11 characters)")
        score += 1
    else:
        feedback.append("Too short! Very Weak password.")
    
    # Character checks
    if any(char.islower() for char in password):
        score += 1
        feedback.append("Contains lowercase letter")
    else:
        feedback.append("No lowercase letter")

    if any(char.isupper() for char in password):
        score += 1
        feedback.append("Contains uppercase letter")
    else:
        feedback.append("No uppercase letter")

    if any(char.isdigit() for char in password):
        score += 1
        feedback.append("Contains digit")
    else:
        feedback.append("No digit")

    if any(char in SPECIAL_CHARS for char in password):
        score += 1
        feedback.append("Contains special character")
    else:
        feedback.append("No special character (optional, but adds strength)")


# Security Patterns:

# No common patterns like "123", "abc", "password" (case-insensitive)
# No repeated characters more than 2 times in a row
# No keyboard patterns like "qwerty", "asdf"


    if any(pattern in password.lower() for pattern in COMMON_PATTERNS):
        score -= 2
        feedback.append("Contains common pattern (e.g., 123, abc, password)")

    if any(pattern in password.lower() for pattern in KEYWARD_PATTERNS):
        score -= 2
        feedback.append("Contains keyboard pattern (e.g., qwerty, asdf)")

    is_repeated = any(password[i] == password[i+1] == password[i+2] for i in range(len(password) - 2))
    if is_repeated:
        score -= 1
        feedback.append("Contains repeated characters (e.g., aaa)")

    print("\nFeedback:")

    print(f"\nTotal Score: {score}")


print("Password Checker\n")
password = "sfdXQdsg@DS2kF22"
evaluate_password(password)


# password = "asadfEQ@!"

# print()
