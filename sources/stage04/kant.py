import os
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

fd = open("kant.txt")
content = fd.read()
print(content)