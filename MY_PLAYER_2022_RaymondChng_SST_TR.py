flag = True
# list_name_totals[]
list_name_totals = []
count = 1
total = 0
while flag:
    name = input("Please enter the Player's name: ")
    # length_string = name.len()
    length_string = len(name)
    name = name.upper()
    print("You are player " + str(count))
    # for x in range(length_string - 1):
    for x in range(length_string):
        char = name[x]
        # value = num(char)
        value = ord(char)
        # total = value + value
        total += value
    # list_name_totals.append(value)
    list_name_totals.append(total)
    print("Your total is " + str(total))
    more = input("Would you like to enter another player's name? Enter Yes or No. ")
    if more == "No":
        flag = False
    else:
        count +=1
        # reset total
        total = 0
# highest = ceil(list_name_totals)
highest = max(list_name_totals)
# for x in range(list_name_totals):
for x in range(len(list_name_totals)):
    if list_name_totals[x] == highest:
        # position = x
        position = x+1
print("The highest value is " + str(highest) + " and that is player " + str(position))

