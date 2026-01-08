import re
import string

file_path = "sample_input.txt"

# Read original text
with open(file_path, "r", encoding="utf-8") as f:
    original_text = f.read()

# 1. Remove HTML tags
clean_text = re.sub(r"<.*?>", "", original_text)

# 2. Remove punctuation
clean_text = clean_text.translate(str.maketrans("", "", string.punctuation))

# 3. Remove extra spaces and new lines
clean_text = re.sub(r"\s+", " ", clean_text).strip()

# Append cleaned text to the same file
with open(file_path, "a", encoding="utf-8") as f:
    f.write("\n\nclean:\n")
    f.write(clean_text)
