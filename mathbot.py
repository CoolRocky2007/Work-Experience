import openai
import os
from dotenv import load_dotenv
import json

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def todolist():
    tasks = []
    
    while True:
        print("1. Add Task")
        print("2. Remove Tasks")
        print("3. Show Tasks")
        print("4. Quit")
        choice = int(input("Enter your choice >: "))

        if choice == 1:
            task = input("Enter a task >: ")
            tasks.append(task)
        elif choice == 2:
            task = input("Enter a task to remove >: ")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Task not found")
        elif choice == 3:
            print("Tasks: ")
            for task in tasks:
                print(f"- {task}")
        elif choice == "4":
            break
        else:
            print("invalid choice")
    return tasks

def math(op, num1, num2):
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "/":
        result = num1 / num2
    elif op == "*":
        result = num1*num2
    again = ("Do you want to perform another calculation with these numbers [y/n]: ")
    if again.lower() == "y":
        op = input("Please enter an operation: ")
        return math(op, result, num2)
    else:
        return result


message_history = [{"role": "user", "content": f"You are an AI assistant. You will help the user with maths problems. You will use the maths function passed to you to accomplish this. You will also call the todolist function if the user wants to create a todo list."},
                   {"role": "assistant", "content": f"OK"}]
name = str(input("Please enter your name >: "))

def chat(inp, role = "user"):
    message_history.append({"role": role, "content": inp})

    completion = openai.chat.completions.create(
    model = "gpt-4.1-nano",
    messages = message_history,
    )

    reply_content = completion.choices[0].message.content
    print(f"OK {name}, {reply_content}")
    message_history.append({"role": "assistant", "content": reply_content})
    return reply_content

tasks = todolist()
chat(f"I have completed setting up my to-do list: {tasks}")

op = input("Enter the operation you want to do (+, -, *, /) >: ")
num1 = float(input("Enter the first number >: "))
num2 = float(input("Enter the second number >: "))
result = math(op, num1, num2)
chat(f"I did a maths operation: {op} with numbers {num1} and {num2}, result was {result}")

for i in range(2):
    user_input = input(">: ")
    print("User's input was", user_input)
    print()
    chat(user_input)

with open("math.txt", "w") as memory:
    json.dump({
        "name": name,
        "tasks": tasks,
        "message_history": message_history
    }, memory, indent=2)
    