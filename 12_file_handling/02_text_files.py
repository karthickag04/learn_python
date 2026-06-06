# 02_text_files.py
# Reading and Writing Text Files in Python
#
# This tutorial demonstrates how to read, write, and append text to files.

def write_text_file(filename):
    print(f"--- Writing to '{filename}' ---")
    
    # Mode 'w' overwrites the file if it already exists.
    with open(filename, "w") as file:
        # 1. Using write() to write a single string
        file.write("Python is an amazing programming language.\n")
        file.write("It is widely used for data science, web development, and automation.\n")
        
        # 2. Using writelines() to write a list of strings
        more_lines = [
            "File handling is a key part of programming.\n",
            "This is line 4.\n",
            "This is line 5.\n"
        ]
        file.writelines(more_lines)
    
    print(f"File '{filename}' created and written successfully.")


def read_text_file_all(filename):
    print(f"\n--- Reading Entire '{filename}' at Once ---")
    
    # Mode 'r' is the default mode for open().
    with open(filename, "r") as file:
        # read() reads the whole file as a single string.
        content = file.read()
        print(content)


def read_text_file_line_by_line(filename):
    print(f"--- Reading '{filename}' Line-by-Line (Memory Efficient) ---")
    
    # Reading line-by-line is memory efficient because it doesn't load
    # the entire file into memory at once.
    with open(filename, "r") as file:
        # We can iterate directly over the file object!
        line_number = 1
        for line in file:
            # strip() removes leading/trailing whitespaces (like the newline \n)
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1


def read_text_file_as_list(filename):
    print(f"\n--- Reading '{filename}' into a List ---")
    
    with open(filename, "r") as file:
        # readlines() returns a list containing each line of the file as an item
        lines = file.readlines()
        
    print(f"List of lines: {lines}")
    print(f"Total lines: {len(lines)}")
    print(f"First line: {lines[0].strip()}")


def append_to_text_file(filename):
    print(f"\n--- Appending to '{filename}' ---")
    
    # Mode 'a' stands for 'append'. It adds new content to the end of the file
    # without deleting the existing content.
    with open(filename, "a") as file:
        file.write("This line was added using append ('a') mode!\n")
    
    print(f"Appended new content to '{filename}'.")


if __name__ == "__main__":
    target_file = "learning_notes.txt"
    
    # 1. Write initial content
    write_text_file(target_file)
    
    # 2. Read entire file
    read_text_file_all(target_file)
    
    # 3. Read line by line
    read_text_file_line_by_line(target_file)
    
    # 4. Read as a list
    read_text_file_as_list(target_file)
    
    # 5. Append new data
    append_to_text_file(target_file)
    
    # 6. Read again to show the appended line
    print("\n--- Reading file after append ---")
    read_text_file_all(target_file)
