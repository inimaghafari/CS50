from validator_collection import validators

try:
    email = input("Email: ")
    result = validators.email(email)

    if result:
        print("Valid")
        
except Exception:
    print("Invalid")
