with open ("book1.txt") as file:
    import re
    data = re.findall('\w+', file.read().lower())

    def unique_words1(data):
        """Specifies the unique word using set comprehensions"""
        return {word for line in data for word in line.split()}

    def unique_words2(data):
        """Specifies the unique word using Collections"""
        from collections import Counter
        return Counter(data).keys()

    def unique_words3(data):
        """Specifies the unique word using dict comprehensions"""
        return {k: data.count(k) for k in data}.keys()

    def unique_words4(data):
        """Specifies the unique word using for loop """
        words = []
        for word in data:
            if word not in words:
                words.append(word)
        return words

    def unique_gen(iterable, seen=None):
        """Specifies the unique word using generator"""
        seen = set(seen or [])
        for item in iterable:
            if item not in seen:
                seen.add(item)
                yield item

def runtime(script):
    """Specifies the performance features"""
    import timeit
    run_time = timeit.Timer(setup=script).repeat(10)
    return sum(run_time)/len(run_time)

list_func = [unique_words1(data), unique_words2(data), unique_words3(data), unique_words4(data), list(unique_gen(data))]
times = [runtime(str(item)) for item in list_func]

print "Runtime for use Set comprehension is {} sec ".format(times[0])
print "Runtime for use Collections is {} sec".format(times[1])
print "Runtime for use Dict comprehensions is {} sec".format(times[2])
print "Runtime for use For loop is {} sec".format(times[3])
print "Runtime for use Generator is {} sec\n".format(times[4])

print "Best runtime is {} sec" .format(min(times))