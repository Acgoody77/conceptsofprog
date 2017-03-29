from sys import *

tokens = []


def open_file(filename):
    data = open(filename, "r").read()
    return data


def lex(filecontents):
    tok = ""
    filecontents = list(filecontents)
    for char in filecontents: # cycle threw and add each char to the last collection of characters
        tok += char # add the previous char(s) to the current char
        if tok == " ": # ignore spaces
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

def Bool_stmt(toks):
    if(Imply_term(toks)):
        return True
    else:
        return False

def Imply_term(toks):
    if(Or_term(toks) and Imply_tail(toks)):
        return True
    else:
        return False

def Or_term(toks):
    if(And_term(toks) and Or_tail(toks)):
        return True
    else:
        return False

def And_term(toks):
    if(Literal(toks) and And_tail(toks)):
        return True
    else:
        return False

def Imply_tail(toks):
    if(toks == "->" and Or_term(toks) and Imply_tail(toks)):
        return True
    elif(toks == ""):
        return True
    else:
        return False

def Or_tail(toks):
    if(toks == "v" and And_term(toks) and Or_tail(toks)):
        return True
    elif(toks == ""):
        return True
    else:
        return False

def And_tail(toks):
    if(toks == "^" and Literal(toks) and And_tail(toks)):
        return True
    elif(toks == ""):
        return True
    else:
        return False

def Literal(toks):
    if(Atom(toks)):
        return True
    elif(toks == "~" and Literal(toks)):
        return True
    else:
        return False

def Atom(toks):
    if(toks == "T"):
        return True
    elif(toks == "F"):
        return False
        # TODO do this when ( is done!!! elif(toks == "()")
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


class Stack:
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


def run():
    n = 0
    s = Stack()
    filename = input("enter file name: ")
    data = open_file(filename) # gets data from file input
    toks = lex(data) # lexes data
    # token_cmd = parse(toks)



run()
