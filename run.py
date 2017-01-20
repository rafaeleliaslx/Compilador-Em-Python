# -*- coding: utf-8 -*-
import sys
from antlr4 import *
from grammar.PortugolLexer import PortugolLexer
from grammar.PortugolParser import PortugolParser
from grammar.PortugolListener import PortugolListener
from antlr4.tree.Trees import Trees
import traceback
from models import AcoesSemanticas, Variavel, MyErrorListener
import os


def print_arvore(arv):
    tabs = 0
    new_arv = ''
    for i in arv:
        if i == '(':
            tabs = tabs+1
            new_arv+=i+'\n'+(tabs*' ')
        elif i == ')':
            new_arv+='\n'+(tabs*' ')+i+'\n'+(tabs*' ')
            tabs = tabs-1
        else:
            new_arv +=i
    print(new_arv)


def main(argv):
    try:
        errors = MyErrorListener()

        arq = FileStream(argv[1])
        # arq2 = io.TextIOWrapper(write_through=False)
        arq2 = open('temp.por', 'w')
        arq2.write(arq.strdata.upper())
        arq2.close()

        arq = FileStream('temp.por')
        lexer = PortugolLexer(arq)
        stream = CommonTokenStream(lexer)
        parser = PortugolParser(stream)
        
        parser._listeners = [errors]
        
        tree = parser.programa()

        acoes = AcoesSemanticas()
        walker = ParseTreeWalker()
        walker.walk(acoes, tree)
    except Exception as err:
        print(err)
    # traceback.print_exc()

    try:
        if argv[2] == 'p':
            print_arvore(Trees.toStringTree(tree, None, parser))
    except:
        pass

if __name__ == '__main__':
    main(sys.argv)