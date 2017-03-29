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

def Bool_stmt():
    if(Imply_term(s.pop())):
        return True
    else:
        return False

def Imply_term(current_token):
    if(Or_term(current_token) and Imply_tail(s.pop())):
        return True
    else:
        return False

def Or_term(current_token):
    if(And_term(current_token) and Or_tail(s.pop())):
        return True
    else:
        return False

def And_term(current_token):
    if(Literal(current_token) and And_tail(current_token)):
        return True
    else:
        return False

def Imply_tail(current_token):
    if(current_token == "->" and Or_term(s.pop()) and Imply_tail(s.pop())):
        return True
    elif(current_token == ""):
        return True
    else:
        return False

def Or_tail(current_token):
    if(current_token == "v" and And_term(s.pop()) and Or_tail(s.pop())):
        return True
    elif(toks == ""):
        return True
    else:
        return False

def And_tail(current_token):
    if(current_token == "^" and Literal(s.pop()) and And_tail(s.pop())):
        return True
    elif(toks == ""):
        return True
    else:
        return False

def Literal(current_token):
    if(Atom(current_token)):
        return True
    elif(current_token == "~" and Literal(s.pop())):
        return True
    else:
        return False

def Atom(current_token):
    if(current_token == "T"):
        return True
    elif(current_token == "F"):
        return True
    elif(current_token == "("):
        if(Imply_term(s.pop())):
            if(s.pop() == ")"):
                True
            else:
                False
        else:
            False
    else:
<<<<<<< HEAD
        print("Expecting '(', 'T', or 'F'")
=======
        print("error: expecting 'T', 'F', or '()'")
>>>>>>> origin/master
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

def put_stack(tokens):
    for i in reversed(tokens):
        s.push(i)



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

s = Stack()

def run():
    n = 0

    filename = input("enter file name: ")
    data = open_file(filename) # gets data from file input
    toks = lex(data) # lexes data
    put_stack(toks)
    if(Bool_stmt):
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


run()
