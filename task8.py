def write_and_append_file():
    # Step 1: Take user input and write to output.txt
    user_input = input("Enter text to write to the file: ")
    with open("output.txt", "w") as file:
        file.write(user_input + '\n')

    # Step 2: Append additional data to the file
    more_data = input("Enter additional text to append to the file: ")
    with open("output.txt", "a") as file:
        file.write(more_data + '\n')

    # Step 3: Read and display final content of the file
    print("\nFinal content of output.txt:")
    with open("output.txt", "r") as file:
        print(file.read())

# Run the function
write_and_append_file()
