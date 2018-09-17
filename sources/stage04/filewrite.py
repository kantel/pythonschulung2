import os
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

fout = open("file1.txt", "a")
content = fout.write("Alles neu mächt der Mai!\n")

fout.close()