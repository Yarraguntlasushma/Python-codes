import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    print("Please specify the length and number of passwords to generate.")

    try:
        length = int(input("Enter the length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))

        if length <= 0 or num_passwords <= 0:
            raise ValueError("Length and number of passwords must be positive integers.")

        print("\nGenerated Passwords:")
        for _ in range(num_passwords):
            password = generate_password(length)
            print(password)

    except ValueError as e:
        print("Error:", e)
        print("Please enter valid positive integers for length and number of passwords.")

if __name__ == "__main__":
    main()
