# =========================================================
# FILE OPERATIONS IN PYTHON (COMPLETE NOTES)
# =========================================================

# 1️⃣ OPENING A FILE
# Syntax:
# open(file_name, mode)
#
# Common Modes:
# 'r'  -> Read (default)
# 'w'  -> Write (Overwrites file if it exists)
# 'a'  -> Append (Adds data at the end of the file)
# 'x'  -> Create (Throws error if file already exists)
# 'b'  -> Binary mode (rb, wb, ab)
# 't'  -> Text mode (default)
# '+'  -> Read + Write


# =========================================================
# READING FROM FILES
# =========================================================
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters

# Reading all lines into a list
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(lines)


# =========================================================
# WRITING TO FILES
# =========================================================
# Overwriting a file
with open('example.txt', 'w') as file:
    file.write("Hello World\n")
    file.write("This will overwrite the file!")

# Appending to a file
with open('example.txt', 'a') as file:
    file.write("\nThis line is appended at the end.")

# Writing multiple lines
lines = ['First line\n', 'Second line\n', 'Third line\n']
with open('example.txt', 'w') as file:
    file.writelines(lines)


# =========================================================
# FILE POINTER METHODS
# =========================================================
with open('example.txt', 'r') as file:
    print(file.tell())  # Current position (start = 0)
    file.read(5)        # Reads 5 characters
    print(file.tell())  # New position after reading
    file.seek(0)        # Go back to start
    print(file.read(5))


# =========================================================
# BINARY FILE OPERATIONS
# =========================================================

# Writing binary data
with open('binaryfile.bin', 'wb') as file:
    file.write(b"This is binary data\n")
    file.write(b"Binary data can store images, videos, etc.")

# Reading binary data
with open('binaryfile.bin', 'rb') as file:
    data = file.read()
    print("Binary Data Read:", data)

# Copying a binary file (example: copying an image)
with open('image.jpg', 'rb') as src_file:
    with open('image_copy.jpg', 'wb') as dest_file:
        dest_file.write(src_file.read())

# Appending binary data
with open('binaryfile.bin', 'ab') as file:
    file.write(b"\nNew data appended in binary format!")


# =========================================================
# EXCEPTION HANDLING IN FILE OPERATIONS
# =========================================================
try:
    with open('data.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist. Please check the path.")
except PermissionError:
    print("Permission denied!")
finally:
    print("File handling operation completed.")


# =========================================================
# CHECKING IF FILE EXISTS & DELETING FILES
# =========================================================
import os
if os.path.exists('example.txt'):
    print("File exists!")
else:
    print("File not found!")

# Deleting a file
if os.path.exists('sample.txt'):
    os.remove('sample.txt')
    print("File deleted!")
else:
    print("File does not exist!")


# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

# 1. Count the number of words in a file
with open('example.txt', 'r') as file:
    text = file.read()
    word_count = len(text.split())
    print(f"Total Words: {word_count}")

# 2. Copy content from one text file to another
with open('example.txt', 'r') as src, open('copy.txt', 'w') as dst:
    dst.write(src.read())

# 3. Write and read student marks
students = ["Nived: 90\n", "Krish: 85\n", "Anu: 78\n"]
with open('marks.txt', 'w') as file:
    file.writelines(students)

with open('marks.txt', 'r') as file:
    print(file.read())

# 4. Copying a binary file (like PDF)
with open('document.pdf', 'rb') as src, open('document_copy.pdf', 'wb') as dst:
    dst.write(src.read())

# 5. Reading a file in chunks (useful for big files)
with open('largefile.bin', 'rb') as file:
    chunk_size = 1024
    while chunk := file.read(chunk_size):
        print(f"Read {len(chunk)} bytes")
