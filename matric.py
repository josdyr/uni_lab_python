list_of_groups = []

while True:
    tutor_group = []
    group_name = input("What is the name of the tutor group?\n> ")
    while True:
        print("'q' for quit")
        student_matric = input('add a student matric number to {}: '.format(group_name))
        if student_matric == 'q':
            print('You have added students: ', tutor_group, " to {}".format(group_name))
            break
        else:
            tutor_group.append(student_matric)
    list_of_groups.append(tutor_group)
    answer = input('Do you want to add any more groups? (yes/no)')
    if answer != 'yes':
        print("You have successfully added {} group(s): {}".format(
            len(list_of_groups), list_of_groups))
        break
    else:
        continue
