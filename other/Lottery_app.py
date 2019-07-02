import random

#User can pic 6 numbers

def menu():
    #ask player for number
    user_numbers = get_player_numbers()
    #calculate lottery numbers
    lottery_numbers = create_lottery_numbers()
    #print out the winnings
    matches_numbers = user_numbers.intersection(lottery_numbers)
    print("You matched {}. You won ${}!".format(matches_numbers, 100**len(matches_numbers)))


def get_player_numbers():
    number_csv = input("Enter you 6 numbers separeted by commas: ")
    #print(number_csv)
    #Now I want to create a set of integers from this number_csv
    number_list = number_csv.split(",") #['1', '2', '3']
    #print(number_list)
    integer_set = {int(number) for number in number_list}
    return integer_set

#Lottery calculates 6 random numbers (between 1 and 20)
def create_lottery_numbers():
    values = set() # Cannot initialise like so: {}
    while len(values) < 6: #range in [0,1,2,3,4,5]
        values.add(random.randint(1,20))
    return values

menu()
