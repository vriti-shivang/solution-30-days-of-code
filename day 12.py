print_object = print

def print(*items_to_print):
    if 'Grade: ' in items_to_print:
        items_to_print = map(str, items_to_print)
        
        print_object(''.join(items_to_print))
    else:
        print_object(*items_to_print)
