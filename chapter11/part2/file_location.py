import os

file_path = os.path.abspath("./prompt/system_prompt.txt")
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
