def greatest(list):
    my_list =[ ]
    i=0
    k = int(input("enter a number"))
    for i in range(len(my_list)):
        if my_list[i] > k:
           greatest = my_list[i]
        else:
            print("greatest does not exist")
    return greatest