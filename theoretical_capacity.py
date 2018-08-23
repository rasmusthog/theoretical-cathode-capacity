# List of molecular weights of relevant elements, from period table from the Royal Society of Chemistry http://www.rsc.org/periodic-table
molecular_weights = {"Li": 6.94, "Na": 22.99, # Alkali metals
                    "Sc": 44.956, "Ti": 47.867, "V": 50.942, "Cr": 51.996, "Mn": 54.938, "Fe": 55.845, "Co": 58.933, "Ni": 58.693, "Cu": 63.546, "Zn": 65.38, # 3d metals
                    "O": 15.999, "F": 18.998, "P": 30.974, "S": 32.06} # p-block

faradays_constant = 96485.3365 # [F] = C mol^-1 = As mol^-1
seconds_per_hour = 3600 # s h^-1
f = faradays_constant / seconds_per_hour * 1000.0 # [f] = mAh mol^-1


reading = True
element_list = []

while reading == True:
    element = input("Enter element ('q' to quit): ")

    if element == "q":
        reading = False
        break

    number_of_element = input("Enter number of %s atoms: " %element)

    element_tuple = (element, number_of_element)

    element_list.append(element_tuple)

n_cc = input("Enter number of charge carriers per formula unit: ")

molecular_weight = 0
compound_name = ""

for element in element_list:
    molecular_weight += molecular_weights[element[0]] * float(element[1])
    compound_name += element[0]
    if element[1] != "1":
        compound_name += element[1]

theoretical_capacity = (float(n_cc) * f) / molecular_weight

print("The theoretical capacity of " + compound_name + " is: " + str(round(theoretical_capacity, 2)) + " mAh g^-1")
