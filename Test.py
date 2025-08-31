file_name = "test.txt"
content_to_write = "Hello this is a simple test file to count words."


with open(file_name, "w") as f:
    f.write(content_to_write)


with open(file_name, "r") as f:
    text = f.read()
    words = text.split()
    word_count = len(words)

print(word_count)