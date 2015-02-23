"""
This program takes as input a number (n) which represents the number of
ordered pairs in a relation. It then takes in those ordered pairs and outputs
the entire relation. It also outputs to the screen, formatted text representing
the domain and range of the given relation. Additionally, it tells the user
if the given relation represents a function.
"""

def getRelationLength():
    """
    Prompts the user for an input and returns it.
    """
    n = input("Enter the size of the relation: ")
    return n

def checkedRelationLength(n):
    """
    Checks if the parameter n is an integer.
    If n is not an integer prompt the user to enter
    an integer until she does.
    """
    correct = False
    while not correct:
        try:
            n = int(n)
            if n < 2:
                print("Input must be an integer greater than or equal to two (2).")
                n = getRelationLength()
                continue
            correct = True
        except:
            print("Input must be an integer greater than or equal to two (2).")
            n = getRelationLength()
    return n

def checkedValue(num, value_name):
    """"
    Checks to ensure that the given value is a number.
    Prompts user for a new value if previously inputted value
    is not a number until user inputs an valid value.
    """
    correct = False
    while not correct:
        try:
            num = float(num)
            correct = True
        except:
            print(value_name + "  must be a number.")
            num = input("Enter " + value_name + " : ")
    return num

def isFunction(relation):
    """
    Takes the parameter relation of type dict and checks
    if the given relation represents a function.
    """
    for key in relation.keys():
        if len(relation[key]) > 1:
            return False
        else:
            return True

def buildRelation(size):
    relation = {}
    for num in range(size):
            for i in range(2):
                if i == 0:
                    x_value = input("Enter x-value: ")
                    x_value = checkedValue(x_value, "x-value")
                else:
                    y_value = input("Enter y-value: ")
                    y_value = checkedValue(y_value, "y-value")

            if x_value in relation.keys():
                relation[x_value].append(y_value)
            else:
                relation[x_value] = []
                relation[x_value].append(y_value)
    return relation
        
if __name__ == "__main__":

    # get and verify length of the relation
    n = getRelationLength()
    n = checkedRelationLength(n)

    # build the relation
    relation = buildRelation(n)

    #Output relation, domain, and range
    print("\nRelation: ", relation) 
    print("Domain\t\tRange")
    for domain_element in relation.keys():
        if len(relation[domain_element]) > 1:
            for item in range(len(relation[domain_element])):
                print("{domain_element}\t\t{range_element}".format(domain_element=domain_element,
                                                                   range_element=relation[domain_element][item]))
        else:
            print("{domain_element}\t\t{range_element}".format(domain_element=domain_element,
                                                               range_element=relation[domain_element][0]))

    if isFunction(relation):
        print("This relation represents a function.")
    else:
        print("This relation does not represent a function.")
    
            
