
def first_task():
    num_str = "34.24"
    num_str_len = len(num_str)  # Atgriež teksta garumu
    num_float = float(num_str)  # Pārverš tekstu par float
    num_round = round(num_float, 1)  # noapaļo skaitli, 1: 1 cipars aiz komata, 2: 2 cipari aiz komata
    print(num_round)


def second_task():
    pigs = int(input("Amount of pigs: ")) #20
    cows = int(input("Amount of cows: ")) #12
    chickens = int(input("Amount of chickens: ")) # 4
    legs = pigs * 4 + cows * 4 + chickens * 2
    return legs


def third_task(a, b):
    if a > b:
        return "first is bigger"
    elif b > a:
        return "second is bigger"
    else:
        return "they are equal"


def fourth_task(num):
    reversed = int(str(num)[::-1])
    return reversed


def fifth_task():
    dalderi = int(input('Dālderi: '))
    grasi = int(input('Graši: '))
    santimi = int(input('Santīmi: '))

    new_santimi = (dalderi * 37 * 162) + (grasi * 162) + santimi
    new_dalderi = new_santimi // 100

    print(f'Jauni dalderi: {new_dalderi}')
    print(f'Jauni santimi: {new_santimi - (new_dalderi * 100)}')


def main():
    # first_task()
    #
    # print(second_task())
    #
    # a = int(input("Enter first number: "))
    # b = int(input("Enter second number: "))
    # print(third_task(a, b))

    number = int(input("Enter a number to reverse it: "))
    print(fourth_task(number))

    # fifth_task()


if __name__ == '__main__':
    main()

