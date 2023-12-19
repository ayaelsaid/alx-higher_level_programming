#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for j in range(list_length):
        try:
            div_res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            division_result = 0
        except (TypeError, ValueError):
            print("wrong type")
            div_res = 0
        except IndexError:
            print("out of range")
            break
        finally:
            result.append(div_res)
    return result
