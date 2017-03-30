from sys import *

tokens = []


def __open_file__(filename):
    data = open(filename, "r").read()
    return data


def __lex__(filecontents):
    tok = ""
    filecontents = list(filecontents)
    for char in filecontents:  # cycle threw and add each char to the last
        tok += char   # add the previous char(s) to the current char
        if tok == " ":   # ignore spaces
            tok = ""
        elif tok == "T":
            tokens.append("T")
            tok = ""
        elif tok == "F":
            tokens.append("F")
            tok = ""
        elif tok == "~":
            tokens.append("~")
            tok = ""
        elif tok == "->":
            tokens.append("->")
            tok = ""
        elif tok == ".":
            tokens.append(".")
            tok = ""
        elif tok == "^":
            tokens.append("^")
            tok = ""
        elif tok == "v":
            tokens.append("v")
            tok = ""
        elif tok == "\n":
            tok = ""
        # TODO put in the case for "()"!!!!!!!!!!
        else:
            print("error")
            return "error"
    # print(tokens)
    return tokens


"""
def parse(toks):
    # print(toks)
    i = 0
    while(i < len(toks)):
        if (toks[i] ):
            i += 1
"""


def __Bool_stmt__():
    if(__Imply_term__(s.pop())):
        return True
    else:
        return False


def __Imply_term__(current_token):
    if(__Or_term__(current_token) and __Imply_tail__(s.pop())):
        return True
    else:
        return False


def __Or_term__(current_token):
    if(__And_term__(current_token) and __Or_tail__(s.pop())):
        return True
    else:
        return False


def __And_term__(current_token):
    if(__Literal__(current_token) and __And_tail__(current_token)):
        return True
    else:
        return False


def __Imply_tail__(current_token):
    if(current_token == "->" and __Or_term__(s.pop()) and __Imply_tail__(s.pop())):
        return True
    elif(current_token == ""):
        return True
    else:
        return False


def __Or_tail__(current_token):
    if(current_token == "v" and __And_term__(s.pop()) and __Or_tail__(s.pop())):
        return True
    elif(current_token == ""):
        return True
    else:
        return False


def __And_tail__(current_token):
    if(current_token == "^" and __Literal__(s.pop()) and __And_tail__(s.pop())):
        return True
    elif(current_token == ""):
        return True
    else:
        return False


def __Literal__(current_token):
    if(__Atom__(current_token)):
        return True
    elif(current_token == "~" and __Literal__(s.pop())):
        return True
    else:
        return False


def __Atom__(current_token):
    if(current_token == "T"):
        return True
    elif(current_token == "F"):
        return True
    elif(current_token == "("):
        if(__Imply_term__(s.pop())):
            if(s.pop() == ")"):
                True
            else:
                False
        else:
            False
    else:
        print("error: expecting 'T', 'F', or '()'")
        return False


"""
def get_next(toks, num):
    count = 0
    new = 0
    if(count == 0):
        count += 1
        return toks[0]
    else:
        new = toks[count + num]
        count += 1
        return new
"""


def __put_stack__(tokens):
    for i in reversed(tokens):
        s.push(i)


class __Stack__:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printstack(self):
        for items in reversed(self.items):
            print(items)


s = __Stack__()


def __run__():
    filename = input("enter file name: ")
    data = __open_file__(filename)  # gets data from file input
    toks = __lex__(data)  # lexes data
    __put_stack__(toks)
    if(__Bool_stmt__):
        print("valid")
    else:
        print("invalid")

    """ easy to debug stack
    print(toks)
    print("")
    s.printstack()
    print("")
    print(s.pop())
    #s.printstack()
    # token_cmd = parse(toks)
"""


__run__()
