import datetime

def calculate(dob):
    ""
    date = datetime.datetime.strptime(dob, "%Y-%m-%d")
    age = datetime.datetime.now() - date
    print("Your age is", age)

def main():
    ""
    dob = input("Enter your date of Birth (eg 1990-01-01) : ")
    calculate(dob)

if __name__ == "__main__":
    main()