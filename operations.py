def find_common_elem(list1, list2):
    common_elem = []
    for item in list1:
        if item in list2:
            common_elem.append(item)
    return common_elem
