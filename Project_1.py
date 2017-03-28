from sys import *

tokens = []


def open_file(filename):
    data = open(filename, "r").read()
    return data


def lex(filecontents):
    tok = ""
    filecontents = list(filecontents)
    for char in filecontents:
        tok += char
        if tok == " ":
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
        #put in the case for "()"!!!!!!!!!!!
    #print(tokens)
    return tokens

def parse(toks):
    #print(toks)
    i = 0
    while(i < len(toks)):
        if toks[i]
        i += 1

def Bool_stmt(toks):
    if(Imply_term(toks)):
        return true
    else:
        return false

def Imply_term(toks):
    if(Or_term(toks) and Imply_tail(toks)):
        return true
    else:
        return false

def Or_term(toks):
    if(And_term(toks) and Or_tail(toks)):
        return true
    else:
        return false

def And_term(toks):
    if(Literal(toks) and And_tail(toks)):
        return true
    elif(toks ##################################)

def Imply_tail(toks):
    if(toks == "->" and Or_term(toks) and Imply_tail(toks)):
        return true
    elif(toks == ""):
        return true
    else:
        return false



def run():
    filename = input("enter file name: ")
    data = open_file(filename)
    toks = lex(data)
    parse(toks)

run()
