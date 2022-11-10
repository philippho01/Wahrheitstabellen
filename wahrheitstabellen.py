import os

file_name = "tabellen.txt"

if os.path.exists(file_name):
    print("File " + file_name + "already exists.")
else:
    file= open(file_name, "xt")