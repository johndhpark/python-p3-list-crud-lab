def create_an_empty_list():
    res = []

    return res

def create_a_list():
    return [0] * 4

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l):
    l.pop()

    return l

def remove_element_from_start_of_list(l):
    l.pop(0)

    return l

def retrieve_first_element_from_list(l):
    return l[0]

def retrieve_element_from_index(l, index):
    if index >= len(l): return None

    return l[index]

def retrieve_last_element_from_list(l):
    return l[-1]
