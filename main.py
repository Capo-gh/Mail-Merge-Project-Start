PLACE_HOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("Input/Letters/starting_letter.txt") as starting_letter_file:
    letter_contents = starting_letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace("[name]", stripped_name)
        print(new_letter)

        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as output_file:
            output_letter_file = output_file.write(new_letter)

