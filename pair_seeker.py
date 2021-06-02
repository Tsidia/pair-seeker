import sys

target = int(sys.argv[1])
number_list = list(map(int, sys.argv[2].split(" ")))

def pair_seeker(target, number_list):
    no_duplicates = list(dict.fromkeys(number_list)) # Remove duplicate numbers.
    output = "" #This is where we store valid pairs
    i = 0
    for number in no_duplicates: #Take every number in the list
        i += 1
        for compared_number in no_duplicates: #And compare it with every number in the list
            if number != compared_number and number + compared_number == target: #Make sure a number doesn't pair with itself. Check if the numbers sum to target
                output += "\n" + str(number) + ":" + str(compared_number)
        no_duplicates = no_duplicates[i:] #Remove the number from list when all of its pairs are found
    return output

print(pair_seeker(target, number_list))
