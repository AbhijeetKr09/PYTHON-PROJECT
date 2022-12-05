
from statistics import mode


for n in range(1, 5):
    name = input("name: ")
    with open("line-bot/patronage.txt", mode='a') as pat_list:
        pat_list.write(f"{n}: {name} \n")
    
with open("line-bot/patronage.txt", mode='r') as pat_list:
    content = pat_list.read()
    print(content)