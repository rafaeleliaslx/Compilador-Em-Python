# Generated from Portugol.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PortugolParser import PortugolParser
else:
    from PortugolParser import PortugolParser

# This class defines a complete generic visitor for a parse tree produced by PortugolParser.

class PortugolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PortugolParser#programa.
    def visitPrograma(self, ctx:PortugolParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#dec_vars.
    def visitDec_vars(self, ctx:PortugolParser.Dec_varsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#variavel.
    def visitVariavel(self, ctx:PortugolParser.VariavelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#tipo.
    def visitTipo(self, ctx:PortugolParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#lista_ids.
    def visitLista_ids(self, ctx:PortugolParser.Lista_idsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#dec_func.
    def visitDec_func(self, ctx:PortugolParser.Dec_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#func.
    def visitFunc(self, ctx:PortugolParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#chamada_func.
    def visitChamada_func(self, ctx:PortugolParser.Chamada_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#chamada_func_simples.
    def visitChamada_func_simples(self, ctx:PortugolParser.Chamada_func_simplesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#lista_parametros.
    def visitLista_parametros(self, ctx:PortugolParser.Lista_parametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#teste_logico.
    def visitTeste_logico(self, ctx:PortugolParser.Teste_logicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#retorno.
    def visitRetorno(self, ctx:PortugolParser.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#dec_parametros.
    def visitDec_parametros(self, ctx:PortugolParser.Dec_parametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#bloco_principal.
    def visitBloco_principal(self, ctx:PortugolParser.Bloco_principalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#atribuicao.
    def visitAtribuicao(self, ctx:PortugolParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#leitura.
    def visitLeitura(self, ctx:PortugolParser.LeituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#impressao.
    def visitImpressao(self, ctx:PortugolParser.ImpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#condicional.
    def visitCondicional(self, ctx:PortugolParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#laco_repita.
    def visitLaco_repita(self, ctx:PortugolParser.Laco_repitaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#laco_enquanto.
    def visitLaco_enquanto(self, ctx:PortugolParser.Laco_enquantoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#laco_para.
    def visitLaco_para(self, ctx:PortugolParser.Laco_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#comandos.
    def visitComandos(self, ctx:PortugolParser.ComandosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#expr.
    def visitExpr(self, ctx:PortugolParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#term.
    def visitTerm(self, ctx:PortugolParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PortugolParser#fator.
    def visitFator(self, ctx:PortugolParser.FatorContext):
        return self.visitChildren(ctx)



del PortugolParser