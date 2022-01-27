import os.path
import random
mypath = os.path.expanduser("~\\pythontesti")
if not os.path.exists(mypath):
    os.makedirs(mypath)


def lotto():
  indexes = [(i+1) for i in range(40)]
  numbers = []

  for x in range(7):
    index = random.randrange(0,len(indexes)-1)
    numbers.append(indexes[index])
    indexes.pop(index)
  
  #numbers.sort()
  string = ','.join(str(number) for number in numbers)
  return string

filename = "lotto.txt"
mypath += "\\"
file = open(mypath + filename, "w")
msg = "Lottoarvonnan numerot ovat: " + str(lotto())
file.write(msg)
file.close()
print(msg)

lotto()




