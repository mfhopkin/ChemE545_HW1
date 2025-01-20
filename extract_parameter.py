unit_operations_data = {
    "distillation_column": {"temperature": [150, 160, 170], "pressure": [2, 2.5, 3], "flow_rate": [100, 110, 120]},
    "reactor": {"temperature": [250, 260, 270], "pressure": [5, 5.5, 6], "residence_time": [10, 12, 14]},
    "heat_exchanger": {"temperature_in": [80, 90, 100], "temperature_out": [50, 60, 70], "flow_rate": [200, 210, 220]}
}
#dictionary within a dictionary 

#from class: don't need dict as arg
def extract_parameter(unit_name,parameter_name,index):
    
#a function that takes in unit_name, parameter_name, and index as args
    
    if unit_name in unit_operations_data.keys(): 
        key_1 = unit_operations_data[unit_name]
        
#to continue with other if statements, need to make sure unit_name inputted is in the initial unit_operations dictionary
#unit_name is first nested dictionary, so will be the key
#storing this as another variable so that the given unit_name can be used in the print string at the end 

    else:
        return('invalid input')
        
#returns "invalid_input" if the unit_name is not in the given dictionary 
#if print is used instead of return and the unit_name is not in unit_operations_data, the function will try to continue
#to the next if statement & throws an error because there is no key associated with the unit_name

    if parameter_name in key_1.keys():
        key_2 = key_1[parameter_name]
        
#looks for the given parameter_name key in the key from the unit_name because of the nested dictionary structure
#the unit_operations_data nested dictionary is {unit_name(key):parameter_name(also a key):index(the value, which is a list)
#also stores this as a new variable so the given parameter_name can be used in the print string at the end

    else:
        return('invalid input')
        
#returns "invalid_input" if the parameter_name is not in the given dictionary 
#if print is used instead of return, the function will try to continue
#to the next if statement & throws an error because there is no key associated with the unit_name

    if index in range(len(key_2)):
        index = str(key_2[index])

#looks for the given index which is given by the user as an element index in the values list of the parameter_name key
#also saves the value of the given list index as a string to use in the print string at the end
    
    else:
        return("out of range")

# returns out of range if the index given is not an index in the list

    print(unit_name + "_" + parameter_name + "_" + index)

#prints the given unit_name, parameter_name, and index value (not the index arg inputted to the function
#but the value from the index value list from the dictionary
#all of them are strings, so can just use + to add them together