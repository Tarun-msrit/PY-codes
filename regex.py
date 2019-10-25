import re
def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")
test_phrase="sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd"
test_patterns =['sd*'] #0 or more d's
multi_re_find(test_patterns,test_phrase)

test_patterns =['sd{3}']
multi_re_find(test_patterns,test_phrase)

test_phrase2="This is a string! But is has punctuation. How can we remove it?"
test_patterns2=['[^!.?]+']
multi_re_find(test_patterns2,test_phrase2)

test_phrase3 = 'This is a string with numbers 12312 and a symbol #hashtag'
test_patterns3=[r'\d+']
multi_re_find(test_patterns3,test_phrase3)