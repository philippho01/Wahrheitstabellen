fileWriter = open("tabellen.txt", "wt")

#NAND

fileWriter.write("      NAND      \n")
fileWriter.write("================\n")
fileWriter.write("|A:  |B:   |C:  \n")
fileWriter.write("+----+-----+----\n")

fileWriter.close()

fileWriter = open("tabellen.txt", "at")

a = False
b = False
x = not(a and b)

fileWriter.write(str(a) + "|"+ str(b)+"|"+ str(x)+"\n")

a = False
b = True
x = not(a and b)

fileWriter.write(str(a) + "|"+ str(b)+"|"+ str(x)+"\n")

a = True
b = False
x = not(a and b)

fileWriter.write(str(a) + "|"+ str(b)+"|"+ str(x)+"\n")

a = True
b = True
x = not(a and b)
fileWriter.write(str(a) + "|"+ str(b)+"|"+ str(x)+"\n")

#AND

fileWriter.write("\n")
fileWriter.write("======AND=======\n")
fileWriter.write("|A:  |B:   |C:  \n")
fileWriter.write("+----+-----+----\n")

a = False
b = False
x = a and b

fileWriter.write(str(a) + "|"+ str(b)+"|"+str(x)+"\n")

a = False
b = True
x = a and b

fileWriter.write(str(a) + "|"+ str(b)+"|"+str(x)+"\n")

a = True
b = False
x = a and b


fileWriter.write(str(a) + "|"+ str(b)+"|"+str(x)+"\n")

a = True
b = True
x = a and b

fileWriter.write(str(a) + "|"+ str(b)+"|"+str(x)+"\n")

#OR

fileWriter.write("\n")
fileWriter.write("       OR       \n")
fileWriter.write("================\n")
fileWriter.write("|A:  |B:   |C:  \n")
fileWriter.write("+----+-----+----\n")

a = False
b = False
x = a or b

fileWriter.write(str(a) + "|"+ str(b)+"|"+str(x)+"\n")

a = False
b = True
x = a or b

fileWriter.write(str(a) + "|"+ str(b)+"|"+str(x)+"\n")

a = True
b = False
x = a or b

fileWriter.write(str(a) + "|"+ str(b)+"|"+str(x)+"\n")

a = True
b = True
x = a or b

fileWriter.write(str(a) + "|"+ str(b)+"|"+str(x)+"\n")

#NOT

fileWriter.write("\n")
fileWriter.write("    NOT   \n")
fileWriter.write("==========\n")
fileWriter.write("|A:  |X:  \n")
fileWriter.write("+----+----\n")

a = False
x = not a

fileWriter.write(str(a) + "|"+ str(x)+"\n")

a = True
x = not a

fileWriter.write(str(a) + "|"+ str(x)+"\n")

#NOR

fileWriter.write("\n")
fileWriter.write("       NOR      \n")
fileWriter.write("================\n")
fileWriter.write("|A:  |B:   |C:  \n")
fileWriter.write("+----+-----+----\n")

a = False
b = False
x = not(a or b)

fileWriter.write(str(a) + "|"+ str(b)+"|"+str(x)+"\n")

a = False
b = True
x = not(a or b)

fileWriter.write(str(a) + "|"+ str(b)+"|"+str(x)+"\n")

a = True
b = False
x = not(a or b)

fileWriter.write(str(a) + "|"+ str(b)+"|"+str(x)+"\n")

a = True
b = True
x = not(a or b)

fileWriter.write(str(a) + "|"+ str(b)+"|"+str(x)+"\n")



