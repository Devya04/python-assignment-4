# python-assignment-4
# 📘 Python File Handling Tasks

This repository contains two beginner-friendly Python programs demonstrating how to handle files using basic operations such as reading, writing, appending, and error handling.

---

## ✅ Task 1: Read a File with Error Handling

### 📝 Problem Statement:
Write a Python program that:
1. Opens and reads a text file named `sample.txt`.
2. Prints its content line by line.
3. Handles errors gracefully if the file does not exist.

### 🧠 Key Concepts:
- File reading using `with open()`
- Exception handling using `try-except`
- Looping through file lines

### 💻 Sample Code:
```python
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("File content:\n")
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Run the function
read_file('sample.txt')

def write_and_append_file():
    # Step 1: Write user input to output.txt
    user_input = input("Enter text to write to the file: ")
    with open("output.txt", "w") as file:
        file.write(user_input + '\n')

    # Step 2: Append additional user input
    more_data = input("Enter additional text to append to the file: ")
    with open("output.txt", "a") as file:
        file.write(more_data + '\n')

    # Step 3: Read and display the final file content
    print("\nFinal content of output.txt:")
    with open("output.txt", "r") as file:
        print(file.read())

# Run the function
write_and_append_file()
