def inputAndPrintListAndTuple():
    input_text = input()
    my_list = input_text.split(",")
    my_tuple = tuple(my_list)

    print(my_list)
    print(my_tuple)

inputAndPrintListAndTuple()