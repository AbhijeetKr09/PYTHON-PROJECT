

with open("./Mail Merge Project Start/Input/Names/invited_names.txt", mode='r') as f:
    names = f.readlines()
with open("./Mail Merge Project Start/Input/Letters/starting_letter.txt", mode='r') as f:
    letter = f.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace("[name]", f"{stripped_name}")
        with open(f"./Mail Merge Project Start/Output/ReadyToSend/letter_{stripped_name}.txt", mode='w') as f:
            f.write(new_letter)

