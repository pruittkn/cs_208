import math

def print_all_race_outcomes(podium_list, racer_list, podium_size, race_count):
    if (len(podium_list) == podium_size):
        race_count[0] += 1
        print(f'Race #{race_count[0]}: ', end='')
        for k in range(podium_size - 1):
            print(f'#{(k + 1):n} {podium_list[k]}, ', end ='')
        print(f'#{podium_size:n} {podium_list[podium_size - 1]}')

    else:
        for i in range(len(racer_list)):
            tmpClosetList = racer_list.copy()
            temp = tmpClosetList.pop(i)
            podium_list.append(temp)
            print_all_race_outcomes(podium_list, tmpClosetList, podium_size, race_count)
            podium_list.pop(len(podium_list) - 1)



if __name__ == '__main__':

    racer_list = []
    podium_list = []
    race_count = [0]

    while True:
        try:
            racers_size = int(input("How many racers are there?\n"))
            if racers_size >= 1:
                break
            else:
                print("Invalid input. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    while True:
        try:
            podium_size = int(input("How many people can be on the podium?\n"))
            if (podium_size <= 0):
                print("Invalid input. Please enter a positive number.")
            elif (podium_size > racers_size):
                print("Invalid input. Please enter a number less than or equal to the number of racers.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Uses Fact 5.4.1 to count number of permutations
    combinations = math.factorial(racers_size) / math.factorial(racers_size - podium_size)

    print(f'You have {combinations:n} potential race outcomes')

    # Prints all permutations using recursion
    selection = input("Do you want to print all potential race outcomes? 1 to continue, any other key to quit (Not recommended for large selections)\n")
    if (selection == "1"):
        for i in range(0, racers_size):
            racer_list.append(input("Enter the next racer's name: \n"))

        print_all_race_outcomes(podium_list, racer_list, podium_size, race_count)
    else:
        print("Thanks for participating!")
        print("hi")