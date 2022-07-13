import re

data = ""

def funct():
    pattern = r'(?P<username>\w+)@(?P<organization>\w+)\.'
    my_matches = []
    with open("StackOverflow/assets/logdata.txt", mode="r") as file:
        rawdata = file.read()
        #Substitution of linebreaks for spaces
        finaldata=rawdata.replace('\n', ' ').replace('\r', '')
        matches = re.finditer(pattern, finaldata, re.IGNORECASE)
        for match in matches:
           my_matches.append(match.groupdict())
    
    print(my_matches)

def test():
    pattern = r'\b(?:9|[a-z]{3,5})\w*'
    search_string = 'This is Mation 9akdjfklad Cation string'
    match = re.finditer(pattern, search_string)
    print(list(match))


funct()
test()