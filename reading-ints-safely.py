#This is the Python Essentials 2 LAB 2.8.1.4 Reading ints safely

def read_int(prompt, min, max):
    # This function accepts three arguments:
    # a prompt, a low acceptable limit, and a high acceptable limit.
    #
    # If the user enters a string that is not an integer value,
    # the function emits the message "Error: wrong input",
    # and ask the user to input the value again.
    #
    # If the user enters a number which falls outside the specified range,
    # the function emits the message "Error: the value is not within permitted range (min..max)
    # and asks the user to input the value again.
    #
    # If the input value is valid, function returns it as a result.
    while True:
        v = input(prompt)
        try:
            v = int(v)
            assert v >= min and v <= max
        except AssertionError:
            print("Error: the value is not within permitted range (-10..10)")
        except ValueError:
            print("Error: wrong input")
        else:
            return v


# Main
if __name__ == "__main__":
    v = read_int("Enter a number from -10 to 10: ", -10, 10)
    print("The number is:", v)

