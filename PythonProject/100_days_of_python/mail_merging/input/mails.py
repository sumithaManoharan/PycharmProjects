import re

with open ("names.txt", "r") as file:
    names = file.readlines()
with open ("../letters/letters.txt", "r") as file:
    letters = file.readlines()

for name in names:
    current_letter = letters.copy()
    name = name.strip()
    current_letter[0]=current_letter[0].replace("name",name)
    with open(f"../output/{name}_invitation.txt", "w") as file:
        file.writelines(current_letter)