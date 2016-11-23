import sys
from antlr4 import *
from PortugolLexer import PortugolLexer
from PortugolParser import PortugolParser
from PortugolListener import PortugolListener
from antlr4.tree.Trees import Trees
from pprint import pprint

class AcoesSemanticas(PortugolListener):
	tab_simb = {}

	def exitTipo(self, ctx:PortugolParser.TipoContext):
		if ctx.getText() == 'INTEIRO':
			ctx.tip = 1
		elif ctx.getText() == 'REAL':
			ctx.tip = 2
		elif ctx.getText() == 'BOOLEANO':
			ctx.tip = 3
		elif ctx.getText() == 'STRING':
			ctx.tip = 4

	def exitListaIDs(self, ctx:PortugolParser.ListaIDsContext):
		if ctx.tip != 0:
			for id in ctx.ID():
				if not id.getText().lower() in self.tab_simb.keys():
					self.tab_simb[id.getText().lower()] = ctx.tip
				else:
					print('Variavel duplicada: '+str(id))

	def enterBlocoPrincipal(self, ctx:PortugolParser.BlocoPrincipalContext):
		print("\n"+"*"*10+" MAPA DE MEMORIA"+"*"*10)
		pprint(self.tab_simb)



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
    pprint(Trees.toStringTree(tree, None, parser))

if __name__ == '__main__':
    main(sys.argv)