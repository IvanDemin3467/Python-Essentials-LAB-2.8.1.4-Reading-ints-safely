# Python-Essentials-LAB-2.8.1.4-Reading-ints-safely

**Estimated time**

15-25 minutes

**Level of difficulty**

Medium

**Objectives**

•	improving the student's skills in defining functions;

•	using exceptions in order to provide a safe input environment.

**Scenario**

Your task is to write a function able to input integer values and to check if they are within a specified range.

The function should:

•	accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;

•	if the user enters a string that is not an integer value, the function should emit the message Error: wrong input, and ask the user to input the value again;

•	if the user enters a number which falls outside the specified range, the function should emit the message Error: the value is not within permitted range (min..max) and ask the user to input the value again;

•	if the input value is valid, return it as a result.

**Test data**

Test your code carefully.

This is how the function should react to the user's input:
```
Enter a number from -10 to 10: 100
Error: the value is not within permitted range (-10..10)
Enter a number from -10 to 10: asd
Error: wrong input
Enter number from -10 to 10: 1
The number is: 1
```

**Complete code includes only one function:**

```
read_int(prompt, min, max):
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
```
