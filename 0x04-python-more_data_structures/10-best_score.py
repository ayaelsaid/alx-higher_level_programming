#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        score = 0
        the_highest = ""
        items = list(a_dictionary.keys())
        for key in items:
            if a_dictionary[key] > score:
                score = a_dictionary[key]
                the_highest = key
        return the_highest
    else:
        return None
