from bisect import bisect_left
import timeit

def remove_duplicates_new_array(data):
    hold = dict.fromkeys(data)
    print(hold)
    return list(dict.fromkeys(data))

def find_index(sorted_data, target):
    for i, v in enumerate(sorted_data):
        if v >= target: 
            return i 
    return len(sorted_data)

def find_index2(sorted_data, target):
    return bisect_left(sorted_data, target)

def find_index_test():
    print(timeit.timeit(lambda: find_index([1,3,5,6], 5)))
    print(timeit.timeit(lambda: find_index2([1,3,5,6], 5)))

def lengthOfLastWord(sentence):
    return len(sentence.strip('!?:.; ').split(' ')[-1])

def lengthOfLastWord2(sentence):
    word = ''
    sentence = sentence.strip()
    sentence = sentence.replace('!?:.;', '')

    while True and sentence: 
        space_index = sentence.find(' ')
        if space_index >= 0:
            word = sentence[0:space_index]
            sentence = sentence[space_index+1:]
        else: 
            word = sentence[0:]
            print(word)
            return len(word)

def lengthOfLastWord3(s):
    return 


def lenfthOfLastWord_test():
    sentences = ['Hello World', '    fly me  to  the moon ', 'luffy is still joyboy']
    for sentence in sentences: 
        print(lengthOfLastWord(sentence))  


class plusOneClass:

    @staticmethod
    def digitArrayToNum(d):
        return int(''.join(map(str,d)))

    @staticmethod
    def numberToDigitArray(val):
        return [int(c) for c in str(val)]

    @classmethod
    def plusOne(cls, digits):
        number = cls().digitArrayToNum(digits) + 1
        return cls().numberToDigitArray(number)


def plusOne_Test():
    print(plusOneClass.digitArrayToNum([1,2,3]))
    print(plusOneClass.numberToDigitArray(123))
    print(plusOneClass.plusOne([9,9,9]))


if __name__ == '__main__':
    plusOne_Test()