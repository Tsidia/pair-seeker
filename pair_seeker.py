#3 3 5 7 9 9
#The task is to collect pairs of numbers that sum to 12, no duplicates.

def pair_seeker(number_list):
    no_duplicates = list(dict.fromkeys(number_list)) # Remove duplicate numbers.
    output = "" #This is where we store valid pairs
    i = 0
    for number in no_duplicates: #Take every number in the list
        i += 1
        for compared_number in no_duplicates: #And compare it with every number in the list
            if number != compared_number and number + compared_number == 12: #Make sure a number doesn't pair with itself. Check if the numbers sum to target
                output += "\n" + str(number) + ":" + str(compared_number)
        no_duplicates = no_duplicates[i:] #Remove the number from list when all of its pairs are found
    return output

print(pair_seeker([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 8, 9, 10]))
