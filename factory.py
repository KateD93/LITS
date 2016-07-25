str0 = '((((((((((((((2, 3)))))))))))))'

str1 = '((((((((((((((2, 3)))))))))))})'

str2 = '(([{(((((((((((2, 3)))))))))))))'

str3 = '{(((((((((((((2, 3))))))))))))}'

def bal(my_string, debug = False):
    def counter(lst):
        chars = ["{","}","[","]"]
        lst = list(my_string)
        lst = filter(lambda x: x not in chars, lst)
        new_lst =''.join(lst)
        if debug:
            counter_brackets_one = lst.count("(")
            counter_brackets_two = lst.count(")")
            if counter_brackets_one < counter_brackets_two:
                diff_count_right = counter_brackets_two - counter_brackets_one
                print "You had {} extra brackets in right.".format(diff_count_right)
                lst.insert(0, "(" * diff_count_right)
                new_lst = ''.join(lst)
            elif counter_brackets_two < counter_brackets_one:
                diff_count_left = counter_brackets_one - counter_brackets_two
                print "You had {} extra brackets in left.".format(diff_count_left)
                lst.extend(")" * diff_count_left)
                new_lst = ''.join(lst)
            else:
                print "Good. You have a balance between brackets."
                new_lst = ''.join(lst)
        return new_lst
    return counter