def first_task():
    my_dict = {
        "value1": "key1",
        "value2": "key2",
        "value3": "key3",
        "value4": "key4",
    }
    my_dict["value1"] = "key11"
    my_dict["value5"] = "key5"
    my_dict.pop("value4")
    print(my_dict)


def second_task():
    lst = ["one", "one", "two", "three", "four", "four"]
    lst = list(dict.fromkeys(lst))
    print(lst)


def third_task(words):
    for word in words:
        if "a" in word or "A" in word:
            print(word)


def fourth_task(words):
    for word in words:
        print(f"{words.index(word)+1}: {word}")


def fifth_task(lst):
    greatest = 0
    for num in lst:
        if num > greatest:
            greatest = num

    return greatest


def main():
    words = ["pythonA", "java", "javascript", "ruby", "c"]
    num_lst = [1, 2.5, 0, 333, 494, 234.6]
    # first_task()
    # second_task()
    # third_task(words)
    # fourth_task(words)
    fifth_task(num_lst)


if __name__ == '__main__':
    main()