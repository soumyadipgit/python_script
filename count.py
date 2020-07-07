words=lines=chars=0
result=[]
with open("solitary.txt")as file:
   for line in file:
     line=line.strip("\n")
     word=line.split()
     lines+=1
     words+=len(word)
     chars+=len(line)
print("no of lines:{}no.of words:{}no.of chars:{}".format(lines,words,chars))
