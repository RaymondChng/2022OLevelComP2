# num_students = 10
# for x in range (num_students):
#    colour = input("What is the student's favourite colour? ")

colour = None
colours = []
count = 0

print("To quit the program, type 'q'")
while colour != 'q':
    colour = input("What is the student's favourite colour? ")
    if colour != 'q':
        colours.append(colour.lower())

# print(colours)

search = input("Which colour would you like to look up?").lower()

for c in colours:
    if search == c:
        count += 1

print("There are", count, "students who chose", search, "as their favourite colour.")
        
