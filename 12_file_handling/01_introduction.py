# 01_introduction.py
# File Handling Introduction in Python
#
# This tutorial introduces the basic concepts of opening, writing, reading,
# and closing files in Python.

def manual_file_handling():
    print("--- Method 1: Manual File Handling ---")
    
    # 1. Opening a file
    # We use the open() function. 
    # The first argument is the filename, and the second is the 'mode'.
    # 'w' mode stands for 'write'. It creates a new file or overwrites an existing one.
    file = open("intro_manual.txt", "w")
    
    try:
        # 2. Writing to the file
        file.write("Hello, World!\n")
        file.write("This file was handled manually using open() and close().\n")
        print("Successfully wrote data to 'intro_manual.txt'.")
    finally:
        # 3. Closing the file
        # It is CRITICAL to close the file to free up system resources.
        # We put this in a try-finally block to make sure it runs even if an error occurs.
        file.close()
        print("File 'intro_manual.txt' closed successfully.")


def modern_file_handling():
    print("\n--- Method 2: Modern File Handling (Recommended) ---")
    
    # Python provides a 'with' statement, also known as a Context Manager.
    # It automatically handles closing the file for you, even if an error occurs!
    with open("intro_modern.txt", "w") as file:
        file.write("Hello, Python!\n")
        file.write("This file was handled using the 'with' statement.\n")
        print("Successfully wrote data to 'intro_modern.txt'.")
    
    print("Note: The file is now automatically closed.")


def read_intro_files():
    print("\n--- Reading the files we just created ---")
    
    # 'r' mode stands for 'read'. It opens the file for reading.
    print("Reading 'intro_manual.txt':")
    with open("intro_manual.txt", "r") as file:
        content = file.read()
        print(content)
        
    print("Reading 'intro_modern.txt':")
    with open("intro_modern.txt", "r") as file:
        content = file.read()
        print(content)


if __name__ == "__main__":
    print("Starting Introduction to File Handling...\n")
    manual_file_handling()
    modern_file_handling()
    read_intro_files()
