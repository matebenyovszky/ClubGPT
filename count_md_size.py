import os
import glob

# List all .md files in the directory
files = glob.glob('*.md')
print()

# Print each file and its character count
for file in files:
    if os.path.isfile(file) and file != "README.md":
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                size = len(content)
                if size > 8000:
                    print(f"WARNING: {file}: {size} characters")
                else:
                    print(f"{file}: {size} characters")
        except UnicodeDecodeError:
            print(f"Cannot read file {file} due to UnicodeDecodeError")