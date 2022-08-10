from random import randint
loop = 0
output = []
amount = int(input("How many random numbers do you want to generate?"))
small = int(input("What is the smallest number you want?"))
big = int(input("What is the biggest number you want?"))
if small > big:
  print("Your smallest number is bigger than your biggest number!")
  exit()
while loop < amount:
  x = randint(small, big)
  print(x)
  output.append(x)
  loop = loop + 1
text = "Printed %d numbers between %d and %d." % (amount, small, big)
print(text)
file = input("Would you like a text file of the results? y or n?")
if file == "y":
  with open('outputfile.txt', 'w') as filehandle:
    for output in output:
       filehandle.write('%s\n' % output)
  print("File has been created.")
elif file == "n":
  print("File has not been created")
else:
  print("Error, wrong input detected")
