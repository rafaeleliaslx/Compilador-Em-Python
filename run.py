# -*- coding: utf-8 -*-
import sys
from antlr4 import *
from grammar.PortugolLexer import PortugolLexer
from grammar.PortugolParser import PortugolParser
from grammar.PortugolListener import PortugolListener
from antlr4.tree.Trees import Trees

from models import AcoesSemanticas, Variavel

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
    arq = FileStream(argv[1])
    lexer = PortugolLexer(arq)
    stream = CommonTokenStream(lexer)
    parser = PortugolParser(stream)
    tree = parser.programa()

    acoes = AcoesSemanticas()
    walker = ParseTreeWalker()
    walker.walk(acoes, tree)

    try:
        if argv[2] == 'p':
            print_arvore(Trees.toStringTree(tree, None, parser))
    except:
        pass

if __name__ == '__main__':
    main(sys.argv)