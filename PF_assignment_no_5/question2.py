with open("log.txt", "a") as f:
    f.write("This is a log entry.\n")

with open("log.txt", "r") as f:
    data = f.read()
    print("Log File Contents:\n")
    print(data)

