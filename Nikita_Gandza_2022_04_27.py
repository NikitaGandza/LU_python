

def half_pyramid():
    num = int(input("Enter number: "))
    n = 1
    for _ in range(num):
        print(str(n) * n)
        n += 1


def dividers():
    start = int(input("Start: "))
    end = int(input("End: "))
    divider = int(input("Divider: "))

    counter = 0
    for i in range(start, end+1):
        if i % divider == 0:
            counter += 1
    print(f"{counter} number between {start} and {end} can be divided by {divider}")


def multiplication_table():
    num = int(input("Enter number: "))
    multipl = 1
    for i in range(1, 11):
        print(f"{num}*{multipl}={num*multipl}")
        multipl += 1


def fourth_task():
    # start = int(input("Start: "))
    # end = int(input("End: "))
    # start = 234
    # end = 1541
    # start = 896
    # end = 35673
    # final_sum = 0
    # for i in range(start, end+1):
    #     if len(str(i)) == 4 and i % 7 == 0 and i % 1000 == 0:
    #         break
    #     elif (i % 13 == 0 or i % 4 == 0) and len(str(i)) == 3:
    #         continue
    #     else:
    #         final_sum += i
    # print(final_sum)
    "Not clear task"


def print_p():
    p = """
****
*   *
*   *
****
*
*
*
    """
    print(p)

def main():
    # half_pyramid()
    # dividers()
    # multiplication_table()
    fourth_task()
    # print_p()

    # print(len(str(20)))
if __name__ == '__main__':
    main()