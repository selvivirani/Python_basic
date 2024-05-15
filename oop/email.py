def main():
    
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password:")

   
    if not (username and email and password):
        print("Error: Please fill in all fields.")
    else:
        
        print("\nEntered Information:")
        print("Username:", username)
        print("Email:", email)
        print("Password:", "*" * len(password)) 

if __name__ == "__main__":
    main()