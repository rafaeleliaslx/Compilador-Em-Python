import sys
from antlr4 import *
from PortugolLexer import PortugolLexer
from PortugolParser import PortugolParser
from PortugolListener import PortugolListener
from antlr4.tree.Trees import Trees

class Variavel():
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def __str__(self):
        return "Nome: "+self.nome+" - Tipo: "+self.tipo

    def getText(self):
        return str(self)

class AcoesSemanticas(PortugolListener):
    tab_simb = {}

    def enterVariavel(self, ctx:PortugolParser.VariavelContext):
        # import pdb; pdb.set_trace()

        tipo = ctx.tipo().getText()

        vars_nomes = [v for v in ctx.lista_ids().getText().split(',')]

        for var_nome in vars_nomes:
            if not self.tab_simb.get(var_nome):
                variavel = Variavel(var_nome, tipo)
                self.tab_simb[var_nome] = variavel
            else:
                print('Variável já declarada: '+self.tab_simb[var_nome].getText())


    def exitPrograma(self, ctx:PortugolParser.ProgramaContext):
        print("\n"+"*"*10+" MAPA DE MEMORIA"+"*"*10)
        for k,v in self.tab_simb.items():
            print(k+': '+v.getText())


def print_arvore(arv):
    tabs = 0
    new_arv = ''
    for i in arv:
        if i == '(':
            tabs = tabs+1
            new_arv+=i+'\n'+(tabs*'\t')
        elif i == ')':
            new_arv+='\n'+(tabs*'\t')+i+'\n'+(tabs*'\t')
            tabs = tabs-1
        else:
            new_arv +=i
    print(new_arv)


def main(argv):
    input = FileStream(argv[1])
    lexer = PortugolLexer(input)
    stream = CommonTokenStream(lexer)
    parser = PortugolParser(stream)
    tree = parser.programa()

    acoes = AcoesSemanticas()
    walker = ParseTreeWalker()
    walker.walk(acoes, tree)
    
    print("\n"+"*"*15+" ÁRVORE "+"*"*15)
    print_arvore(Trees.toStringTree(tree, None, parser))

if __name__ == '__main__':
    main(sys.argv)