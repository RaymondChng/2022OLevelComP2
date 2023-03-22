def square_side(sq_perimeter):
    side_length = sq_perimeter / 4
    return side_length

def square_area(sq_perimeter):
    side_length = square_side(sq_perimeter)
    return side_length * side_length

def circle_diam(circumference):
    diameter = circumference / 3.14
    return diameter

def circle_area(circumference):
    radius = 0.5 * circle_diam(circumference)
    area = 3.14 * radius * radius
    return area

def output_message(shape, area):
    print("The area of the", shape, "is", area, ".")
    
# main
def main():
    print("Choose a shape to find the area of.")
    print("[1] Square")
    print("[2] Circle")
    print("[0] Quit")
    choice = input("Enter choice: ")

    allowed = ['0', '1', '2']
    valid_input = False
    while valid_input == False:
        if choice in allowed:
            valid_input = True
        else:
            print("Invalid choice")
            choice = input('Please try again: ')

    if choice == '1':
        sq_perimeter = float(input("Enter perimeter of square: "))
        area = square_area(sq_perimeter)
        output_message('square', area)
    elif choice == '2':
        circumference = float(input("Enter circumference of circle: "))
        area = circle_area(circumference)
        output_message('circle', area)
    else:
        print("Bye.")

#run program
main()
