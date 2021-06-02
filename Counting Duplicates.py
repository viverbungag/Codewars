def duplicate_count(text):
    return sum([1 for x in set(text.lower()) if text.lower().count(x) > 1])


print (duplicate_count("abcdeaB"))

