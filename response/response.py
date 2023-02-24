from validator_collection import validators

def main():
    email_address = input("What's your email address? ")
    try:
        emailisvalid = validators.email(email_address)
        print("Valid")
    except:
        print("Invalid")

