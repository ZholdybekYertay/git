#1
day = 1

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Other day")

#2
grade = "A"

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case _:
        print("Unknown grade")


#3
command = "start"

match command:
    case "start":
        print("Program started")
    case "stop":
        print("Program stopped")
    case _:
        print("Unknown command")


#4
number = 5

match number:
    case 1 | 2 | 3:
        print("Small number")
    case 4 | 5:
        print("Medium number")
    case _:
        print("Large number")

#5
x = 10
y = 5
operation = "+"

match operation:
    case "+":
        print(x + y)
    case "-":
        print(x - y)
    case "*":
        print(x * y)
    case "/":
        print(x / y)
    case _:
        print("Invalid operation")
