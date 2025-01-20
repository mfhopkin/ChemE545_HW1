def calculate_solution_weights(molecular_weights,solutions_needed):

#defines a function that takes molecular_weights and solutions_needed as the arg inputs

    current_inventory = list(molecular_weights.keys())
#this creates a list of the keys from the molecular_weights dicitonary
#it is used later to see if the chemicals in solutions_needed are in the molecular_weights dictionary
    chemicals_listed = []
    chemicals_needed = []
    solutions_to_make = []
    concentrations_needed = []
#these all define empty lists to append later
    
    for i in solutions_needed:
        chemical = i.split('-')[0]
        chemicals_listed.append(chemical)
        concentration = i.split('-')[1].replace('M','')
        concentrations_needed.append(float(concentration))
#this for loop iterates through each item in the solutions_needed list
#it saves the first value of the string as a chemical variable using .split
#which uses the hyphen to split the string into substring and we want to first part of the hyphen to store as the chemical [0]
#then appends it to the chemicals_listed list
#the second part of the string is stored as a substring in the concentration variable [1], again using the hyphen
#also uses ".replace" to take the M in the substring and replaces it with with an empty string so it is easier to use this value later
#adds the concentrations and appends them to the list concentrations_needed and also stores it as a float
#so the weight calculation later is easier to use

    for element in chemicals_listed:
        if element in current_inventory:
            chemicals_needed.append(element)
        else:
            chemicals_needed.append('unknown')
#this if statement takes the chemical name list defined earlier, which is made from the molecular_weights dictionary
#if the element in list is in chemicals_listed list made from above (made using a substring from the solutions_needed string list)
#then it is appended to a new list chemicals_needed
#otherwise appends "unknown"
#if "return: is used in the else statement instead, if a chemical is not in the molecular_weights dictionary,
#the funcion just stops
#so instead a null value is appended to the list so the function continues

    for i in range(len(chemicals_needed)):
        chemical = chemicals_needed[i]
#for loop that takes an index in the range of the length of the list_chemicals needed
#saves the index in that list as the variable chemical

        if chemical == "unknown":
            solutions_needed[i] = 'unknown'
            continue 
#from above: when a chemical wasn't in the molecular_weights dictionary key list, 'unknown' was appended to the chemicals_needed
#because there is no molecular_weight associated with it, will create problems if a calculation is tried to be made
#so the for loop skips over it using "continue"
#otherwise, it would get stuck
        
        molecular_weight = molecular_weights.get(chemical)
#using the chemical variable string to find it's associated value from it's key in the molecular_weights dictionary
#saves it to the variable molecular_weight
        concentration = concentrations_needed[i]
#uses the index from chemicals_needed in the for loop to find the associated index in the concentrations_needed list
#saves it to the concentration variable
    
        weight = molecular_weight * concentration
#calculates the weight of the chemical needed based on its molecular weight from the dictionary & concentration from solutions_needed

        solutions_needed[i] = f"{chemicals_listed[i]}-{weight}g"
#using the index from the for loop, appends the same index in the solutions_needed list
#to append the string with the calculated weight and adds g for grams
    return solutions_needed

#returns the appended solutions_needed list
