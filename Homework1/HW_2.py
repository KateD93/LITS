str0 = '((((((((((((((2, 3)))))))))))))'

str1 = '((((((((((((((2, 3)))))))))))})'

str2 = '(([{(((((((((((2, 3)))))))))))))'

str3 = '{(((((((((((((2, 3))))))))))))}'

def bal(my_string):
    chars = ["{","}","[","]"]
    lst = list(my_string)
    lst = filter(lambda x: x not in chars, lst)
    counter_brackets_one = lst.count("(")
    counter_brackets_two = lst.count (")")
    #print counter_brackets_one, counter_brackets_two
    if counter_brackets_one < counter_brackets_two:
        diff_count_right = counter_brackets_two - counter_brackets_one
        print "You had {} extra brackets in right.".format(diff_count_right)
        lst.insert(0,"("*diff_count_right) 
        new_string = ''.join(lst)
    elif counter_brackets_two < counter_brackets_one:
        diff_count_left = counter_brackets_one - counter_brackets_two
        print "You had {} extra brackets in left.".format(diff_count_left)
        lst.extend(")"*diff_count_left)
        new_string = ''.join(lst)
    else:
    	print "Good. You have a balance between brackets."
        new_string = ''.join(lst)
    print "Your string after balance is %s" %(new_string)

print "For string str0"
bal(str0)

print "For string str1"
bal(str1)

print "For string str2"
bal(str2)

print "For string str3"
bal(str3)


