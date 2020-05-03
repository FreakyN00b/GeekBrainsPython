text = open("test.txt", "w")
some_text = input("Tell me something: \n")
while some_text:
    text.writelines(some_text + "\n")
    some_text = input("Tell me something: \n")
    if not some_text:
        break
text.close()

with open("test.txt") as text:
    content = text.read()
    print(f"File content: \n{content}")
    text.seek(0)
    content = text.readlines()
    print(f"Total stings count: {len(content)}")
    text.seek(0)
    content = text.read()
    content = content.split()
    print(f"Total words count: {len(content)}")
    text.seek(0)
    string_1 = text.readline().split()
    string_2 = text.readline().split()
    string_3 = text.readline().split()
    print(len(string_1), len(string_2), len(string_3))
