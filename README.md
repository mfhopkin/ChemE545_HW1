# ChemE545_HW1
For depositing files for HW1 Q3

## extract_parameter function

This was done using if statements to go through the keys of the dictionary. Each arguement was a
different layer in the nested dictionary. The if statements go through them, and save them as variable
to access the next layer in the nested dictionary. If any of the input args don't exist
"invalid_input" or "out of range" is returned.

## calculate_solution_weights function

This is accomplished through a series of for loops and if_statements

First, the function takes the strings in the list solutions_needed and splits them into substrings chemical & concentration. The “M” is removed from the concentration substring & it is turned into a float to make calculations in the function easier later.
A for loop is used to iterate through the list of chemical substrings to see if they are in the molecular_weights dictionary. If it isn’t, “unknown” is appended to a list. Another for loop is then used to take the index of the chemical substring, give the value of that key from the molecular_weights dictionary, and uses the same index value from the concentration substring list to calculate the weight needed. If “unknown” is given (because the chemical was not a key in the dictionary), the for loop skips over it and continues. At the end, it appends the solutions_needed string in the list with the weight needed of that chemical to make the concentration of solution needed. Otherwise, the index in the solutions_needed list is replaced with “unknown”.

## Git commands
After the repository was made, the shh link was used to create a copy to my local computer.
I used cd to go into the repository.
I used cp to copy the python functions containing functions to the repository.
I used git add to add it, commit with 'm' with a messager to commit the file, and finally
push to push the file to the repository online.
