from datetime import timedelta


def first_last_name():
    user_fname = str(input("Enter first name: "))
    user_lname = str(input("Enter last name: "))
    return f"{user_lname} {user_fname}"


def text_x_3():
    user_input = str(input("Enter text: "))
    return user_input * 3


def sum_n():
    user_input = str(input("Enter number: "))
    num_1 = user_input
    num_2 = user_input * 2
    num_3 = user_input * 3
    result = int(num_1) + int(num_2) + int(num_3)
    equation = f"{num_1}+{num_2}+{num_3}={result}"
    return equation


def cylinder_darius():
    height = int(input("Enter the height: "))
    radius = int(input("Enter the radius: "))

    volume = 3.14 * radius * radius * height
    area = 2 * (3.14 * radius * radius) + height * (2 * 3.14 * radius)

    print(f"Volume: {volume}")
    print(f"Area: {area}")


def seconds():
    user_input = int(input("Seconds: "))
    sec = timedelta(seconds=user_input)
    str_sec = str(sec).split(":")

    if "days" in str_sec[0]:
        str_yr = str_sec[0].split(", ")[0]
        str_hr = str_sec[0].split(", ")[1]
        return f"{str_yr} {str_hr} hours {str_sec[1]} minutes {str_sec[2]} seconds"
    else:
        return f"{str_sec[0]} hours {str_sec[1]} minutes {str_sec[2]} seconds"


def main():
    first_task = first_last_name()
    print(first_task)

    second_task = text_x_3()
    print(second_task)

    third_task = sum_n()
    print(third_task)

    fourth_task = seconds()
    print(fourth_task)


if __name__ == "__main__":
    main()
