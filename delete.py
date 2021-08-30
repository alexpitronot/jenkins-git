import os
if os.path.exists("data.txt"):
  file=open("data.txt","r")

  for i in file:
   print(i)
  file.close()

  os.remove("data.txt")
  