ques = input("Write question below: (Hint: click photo, copy text and paste here.)\n").lower().replace(',', '')
type1 = ["what", "is", "the", "area", "of"]
ques_list = ques.split(" ")
print(ques_list)
if any(x in type1 for x in ques_list):
    shape = input("write the name of shape\n")
else:
    print("nothing found relative in question")