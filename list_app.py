# LIST APP #

list = []

def add_item(item):
    list.append(item)

def remove_item(item):
    list.remove(item)

def remove_all():
    list.remove_all()

def print_list(list):
    for item in list:
        print(list)
