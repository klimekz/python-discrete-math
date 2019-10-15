# function returns the degree sequence of a graph as an ordered list
def degree_sequence(graph):
    # list representing the degree sequence
    deg_seq = []
    # iterates through dictionary of graph to look at each vertex
    for key in graph:
        # counts the number of connections by finding the lenghth of the
        # list containing points connected to the verted
        deg_seq.append(len(graph[key]))
    # uses sort() to order in non-increasing order
    deg_seq.sort(reverse = True)
    # returns the new list containing the graph's degree sequence
    return deg_seq

# returns the boolean result of the Havel-Hakimi algorithm passed as
# a list of integeres as input
def Havel_Hakimi(integers):
    # iterates until the list only has 2 elements
    while(len(integers) >= 2):
        # upon each iteration, sorts list in non-increasing order
        integers.sort(reverse = True)
        index_zero = integers[0]
        placeholder = []
        # creates a placeholder list containing all but the first element
        for item in integers[1:]:
            placeholder.append(item)
        # return True if both elements are equal to 0, False otherwise
        if len(integers) == 2:
            if integers[0] != 0 or integers[1] != 0:
                return False
            else:
                return True
        # returns false if the first value is greater than the length of the list
        elif integers[0] >= len(integers):
            return False
        else:
        # if reached, subtracts one from n elements in the placeholder list where
        # n equals the value of the first (0th) index of the list
            for item in range(index_zero):
                placeholder[item] -= 1
            # sets the actual array equal to the placeholder array for
            # the next iteration
            integers = placeholder

# test cases    
ds_1 = {"A" : ["B", "C"], "B" : ["A", "C"], "C" : ["A", "B"]}
ds_2 = {"A": ["B", "C"], "B":["A", "C"], "C":["A", "B", "D"], "D": ["C"]}
hh_1 = [3,3,3,3,3]
hh_2 = [3,3,2,2,2,2]


print("Testing: \n")

print("Degree Sequence:")
print(str("Expected Return: [2,2,2]\n   " + str(degree_sequence(ds_1)) + "\n"))
print(str("Expected Return: [3,2,2,1]\n   " + str(degree_sequence(ds_2)) + "\n"))

print("\nHavel-Hakimi:")
print(str("Expected Return: False\n   " + str(Havel_Hakimi(hh_1)) + "\n"))
print(str("Expected Return: True\n   " + str(Havel_Hakimi(hh_2)) + "\n"))

