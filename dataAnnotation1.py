import time

#1:3
#2:2
#3:4
#4:4

def is_palindrome(string):
    return string == string[::-1]

def find_next_instance(string, current_index, val):
    index = string[current_index+1:].find(val)
    return index + 1 + current_index if index>-1 else -1

# uses scanning window and verifies window is palindrome
# finds minimum length palindrome example: is_interesting('abcba') -> 'bcb'
def is_interesting(string=None):
    # verify input
    if not string or not isinstance(string, str):
        return None
    if len(string) <= 2:
        return string[0]

    # initialize variables
    start = 0
    size = int(len(string)/2)+(len(string)%2>0)
    end = size
    window = string[start:end]

    # do twice for odd and even length palindromes
    for i in range(2):
        while True:
            if is_palindrome(window.lower()):
                return window
            else:
                start+=1
                end+=1
                if end > len(string):
                    break
                else:
                    window = string[start:end]
        size += 1
        end = size
        start = 0
    return False

def is_interesting2(string=None): # broken
    if not string:
        return None
    # if string is <= 2 char is length half string is single letter which is same
    # forwards and backwards
    if len(string) <= 2:
        return string[0]

    min_len = int(len(string)/2)+(len(string)%2>0)
    # start at beginning of string
    first_i = 0
    # find the next character in string that matches first
    next_i = 0
    # var to hold min length string must be

    while first_i <= min_len:
        # find next character in string that matches first val.
        next_i = find_next_instance(string, first_i, string[first_i])
        # while there is another value that matches fist value
        while next_i > -1:
            # determine if it is a palindrome
            if next_i-first_i+1 >= min_len and is_palindrome(string[first_i:next_i+1].lower()):
                # if so return True
                return string[first_i:next_i+1]
            else:
                next_i = find_next_instance(string, next_i, string[first_i])
        # if no palindrome found incriment first value to next index of string
        first_i += 1
    return False

def is_interesting3(string: str): # dosnt work for even if window odd or odd if windwo even.
    if not string or not isinstance(string, str):
        return None
    if len(string)<=2:
        return string[0]

    start = 0
    end = len(string)//2 + (len(string)%2>0)
    window = string[start:end]

    while True:
        if is_palindrome(window.lower()):
            return window
        else:
            start += 1
            end += 1
        if end > len(string):
            break
        else:
            window = string[start:end]

    return False


def is_palindrome_root(string, index_s, index_e):
    if index_s < 0 or index_e > len(string)-1:
        return False
    if string[index_s] != string[index_e]:
        return False
    if  index_s == 0:
        if index_s == index_e:
            return False
        elif string[index_s] != string[index_e]:
            return False

    start = index_s - 1
    end = index_e + 1

    while start >= 0 and end < len(string):
        if string[start] != string[end]:
            if (end-1) - (start+1) > 0:
                return {'start':start+1, 'end':end}
            else:
                return False
        start -= 1
        end += 1
    return {'start':start+1, 'end':end}


# get chr, move out by one on upper and lower, check if ==, yes->do agian else incriment char by 1
# go until find to char, incriment out by one, check if ==, yes-> do again else incrment char
def is_interesting4(string:str):
    if not string or not isinstance(string, str):
        return None
    if len(string)<=2:
        return string[0]

    start = 0
    end = 0
    min_length = len(string)//2 + (len(string)%2>0)

    for val in string:
        # check for even palindrome first since will be longer than odd
        rsp = is_palindrome_root(string.lower(), start, end+1)
        if rsp and rsp['end']-rsp['start'] >= min_length:
            return string[rsp['start']:rsp['end']]
        else:
            # check for odd palindrome if no even palindrome
            rsp = is_palindrome_root(string.lower(), start, end)
            if rsp and rsp['end']-rsp['start'] >= min_length:
                return string[rsp['start']:rsp['end']]
        start += 1
        end = start

    return False


def test_Is_Palindrome_root():
    test_cases = [('aba', 0, 0), ('aba', 1, 1), ('aba', 2, 2),('abac', 2, 2),
                  ('caba', 2, 2), ('cabaz', 2, 2), ('cghabar', 4, 4),
                  ('aabc', 0, 0), ('aabc', 0, 1), ('abcc', 2, 3),('zzz', 1, 1),
                  ('abbaz', 1, 2)]

    for test in test_cases:
        print(test, is_palindrome_root(test[0], test[1], test[2]))

def test_is_interesting(test_cases, func):
    print(f'*******{func.__name__}*******')
    for test in test_cases:
        timer = time.process_time_ns()
        rsp = func(test[0])
        print(f'Test Case: {test}, {rsp}, time: {(time.process_time_ns()-timer)/1e9}')



if __name__ == '__main__':

    test_cases = ['a', 'ab', 'abc', 'aabc', 'Aabc', 'abcc', 'abcC', 'abcba', 'abccba','', 123,
                  'TrsgAbbBbba', 'jfldjhadljkfhlakjsdhflkjahsdfljahsldfjkhaljksdhfljahdsflkjahldsjkfhlakjdhflkjahsdf',
                  'tiuaejfkhlvfd;kjadfjkha;kjdfhuhn;vskjghsflgkjhsdlfbglsjkfhgljsfhlghs;kfghlsjkdfhg;shdflgjkhsldkfghlskjdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfhgljshdflgjhslkfjghlkjshgfjkhslfgnslkjgnlskjfnglksjndfgjnslkfjgnlksjnfglksndflgjnslkdfjglksjdnfglkjsndflgjnlbgfdrtlugoyugdf',
                  'tiuaejfkhlvfd;kjadfabcdefgfdecbaakdlfj;akdsjf;klajdsf;kljad;slkfj;kldjfdfslkajflkjsdfjkha;kjdfhuhn;vskjghsflgkjhsdlfbglsjkfhgljsfhlghs;kfghlsjkdfhg;shdflgjkhsldkfghlskjdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfhgljshdflgjhslkfjghlkjshgfjkhslfgnslkjgnlskjfnglksjndfgjnslkfjgnlksjnfglksndflgjnslkdfjglksjdnfglkjsndflgjnlbgfdrtlugoyugdf',
                  'dfgsdfgsfgqwertyuioplkjhgfdsasdfghjklpoiuytrewq',
                  'dfhlakjdhlaaaaaaaaaa',
                  'zyxwddddddddzyxw', 'zyxwdddddddzyxw']

    test_cases2 = [('a', 'a'), ('ab', 'a'), ('abc', False), ('aabc', 'aa'), ('Aabc', 'Aa'), ('abcc', 'cc'), ('abcC', 'cC'), ('abcba', 'abcba'), ('abccba', 'abccba'),('', None), (123, None),
                  ('TrsgAbbBbba', 'AbbBbba'), ('jfldjhadljkfhlakjsdhflkjahsdfljahsldfjkhaljksdhfljahdsflkjahldsjkfhlakjdhflkjahsdf', False),
                  ('tiuaejfkhlvfd;kjadfjkha;kjdfhuhn;vskjghsflgkjhsdlfbglsjkfhgljsfhlghs;kfghlsjkdfhg;shdflgjkhsldkfghlskjdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfhgljshdflgjhslkfjghlkjshgfjk hslfgnslkjgnlskjfnglksjndfgjnslkfjgnlksjnfglksndflgjnslkdfjglksjdnfglkjsndflgjnlbgfdrtlugoyugdf', 'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'),
                  ('tiuaejfkhlvfd;kjadfabcdefgfdecbaakdlfj;akdsjf;klajdsf;kljad;slkfj;kldjfdfslkajflkjsdfjkha;kjdfhuhn;vskjghsflgkjhsdlfbglsjkfhgljsfhlghs;kfghlsjkdfhg;shdflgjkhsldkfghlskjdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfhgljshdflgjhslkfjghlkjshgfjkhslfgnslkjgnlskjfnglksjndfgjnslkfjgnlksjnfglksndflgjnslkdfjglksjdnfglkjsndflgjnlbgfdrtlugoyugdf', 'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'),
                  ('dfgsdfgsfgqwertyuioplkjhgfdsasdfghjklpoiuytrewq', 'qwertyuioplkjhgfdsasdfghjklpoiuytrewq'),
                  ('dfhlakjdhlaaaaaaaaaa', 'aaaaaaaaaa'),
                  ('zyxwddddddddzyxw', 'dddddddd'), ('zyxwdddddddzyxw', False)]

    test_is_interesting(test_cases2, is_interesting)
    test_is_interesting(test_cases2, is_interesting4)
