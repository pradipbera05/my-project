import demoji
demoji.download_codes()
text = "I love coding! 💻🔥 Python is great 🐍✨"
text2={1: "Rock 🪨", 2: "Paper 📄", 3: "Scissors ✂️"}
emojis_found=demoji.findall(text)

print("Emojis found:", emojis_found)

dict_values_string="".join(text2.values())

emojis_found2=demoji.findall(dict_values_string)
clean_text = demoji.replace(text, repl="[:\1:]") 
# Or replace with an empty string to remove them
simple_text = demoji.replace(text, "")

print("Text with labels:", clean_text)
print("Text without emojis:", simple_text)

print("Emojis found in dictionary:", emojis_found2)