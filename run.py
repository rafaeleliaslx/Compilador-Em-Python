# -*- coding: utf-8 -*-
import sys
from antlr4 import *
from grammar.PortugolLexer import PortugolLexer
from grammar.PortugolParser import PortugolParser
from grammar.PortugolListener import PortugolListener
from antlr4.tree.Trees import Trees
from antlr4.error.ErrorListener import ErrorListener

from models import AcoesSemanticas, Variavel


class MyErrorListener( ErrorListener ):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print( str(line) + ":" + str(column) + ": sintax ERROR, " + str(msg))
        print( "Terminating Translation")
        # sys.exit()

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print( "Ambiguity ERROR, " + str(configs))
        # sys.exit()

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass
        # print( "Attempting full context ERROR, " + str(configs))
        # sys.exit()

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print( "Context ERROR, " + str(configs))
        # sys.exit()


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

    try:
        if argv[2] == 'p':
            print_arvore(Trees.toStringTree(tree, None, parser))
    except:
        pass

if __name__ == '__main__':
    main(sys.argv)