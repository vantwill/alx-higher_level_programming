#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    reslt = []
    for t in range(list_length):
        try:
            reslt.append(my_list_1[t] / my_list_2[t])
            continue
        except ZeroDivisionError:
            print("division by 0")
            reslt.append(0)
        except TypeError:
            print("wrong type")
            reslt.append(0)
        except IndexError:
            print("out of range")
            reslt.append(0)
        finally:
            pass
    return reslt
