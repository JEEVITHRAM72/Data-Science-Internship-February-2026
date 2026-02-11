# Logic Building Task 1

# Task 1: Login check
username = "admin"
password = "1234"

user_input = "admin"
pass_input = "1234"

if user_input == username and pass_input == password:
    print("Login Successful")
else:
    print("Invalid Credentials")


# Task 2: Pass/Fail analyzer
marks = [45, 78, 90, 33, 60]
passed = 0
failed = 0

for m in marks:
    if m >= 50:
        passed += 1
    else:
        failed += 1

print("Total Passed:", passed)
print("Total Failed:", failed)


# Task 3: Simple data cleaner
names = [" Alice ", "bob", " CHARLIE "]
cleaned = []

for n in names:
    n = n.strip()
    n = n.lower()
    cleaned.append(n)

print("Cleaned Names:", cleaned)


# Task 4: Message length analyzer
messages = ["Hi", "Welcome to the platform", "OK"]

for msg in messages:
    length = len(msg)
    print("Message:", msg, "| Length:", length)

    if length > 10:
        print("Long message detected")


# Task 5: Error message count
logs = ["INFO", "ERROR", "WARNING", "ERROR"]
error_count = 0

for entry in logs:
    if entry == "ERROR":
        error_count += 1

print("Total ERROR entries:", error_count)
