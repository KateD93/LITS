old_list = ['1', ['2', '3'], '4', [['6','7']]]
new_list = [x for y in old_list for z in y for x in z]
print new_list


