def find_common_elem(list1, list2):
    common_elem = []
    for item in list1:
        if item in list2:
            common_elem.append(item)
    return common_elem

def find_disjoint_elem(list1, list2):

    disjoint_elem = []
    for item in list1:
        if item not in list2:
            disjoint_elem.append(item)
    return disjoint_elem

def freq_table(list1):
    table = {}
    for item in list1:
        if item not in table:
            table[item] = 1
        else:
            table[item] += 1
    return table