import random

options = ["Rock", "Paper", "Scissors"]


def main():
    comp_choice = random.choice(options)
    my_choice = options[int(input("0 - Rock; 1 - Paper; 2 - Scissors\nYour turn: "))]
    print(f"{my_choice} vs {comp_choice}")
    if comp_choice == my_choice:
        print("Draw!")
    elif (comp_choice == "Rock" and my_choice == "Scissors") or (comp_choice == "Paper" and my_choice == "Rock") \
            or (comp_choice == "Scissors" and my_choice == "Paper"):
        print("Computer wins this round!")
    else:
        print("You won!")


if __name__ == '__main__':
    main()
