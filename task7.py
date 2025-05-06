def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("File content:\n")
            for line in file:
                print(line, end='')  # 'end' avoids adding extra newlines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Run the function with the desired file
read_file('sample.txt')
