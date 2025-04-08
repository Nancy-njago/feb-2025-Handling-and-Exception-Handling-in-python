# file_read_write.py

# Read from original file and write modified content to a new file
with open("C:/Users/nanak/Desktop/FEBCOHORT/PYTHON/WEEK4/bio.txt", "r") as infile:

    Nancy_Bio = infile.read()

# Modify content (e.g., make it uppercase)
modified_Nancy_Bio = Nancy_Bio.upper()

# Write modified content to a new file
with open("C:/Users/nanak/Desktop/FEBCOHORT/PYTHON/WEEK4/output.txt", "w") as outfile:
    outfile.write(modified_Nancy_Bio)

print("Modified_Nancy_Bio written to output.txt 🎉")

# error_handling_lab.py

filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile content:\n")
        print(content)
except FileNotFoundError:
    print("🚫 Error: File not found. Please check the filename and try again.")
except PermissionError:
    print("🚫 Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"🚫 An unexpected error occurred: {e}")

