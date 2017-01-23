# -*- coding: utf-8 -*-
from antlr4.error.ErrorListener import ErrorListener

class CompilaError(Exception):
    """docstring for CompilaError"""

class JaDeclaradoError(CompilaError):

    def __init__(self, classe, nome, pai, linha, coluna):
        self.classe = classe
        self.nome = nome
        self.parent = pai
        self.linha = linha
        self.coluna = coluna
        Exception.__init__(self,
            '{} "{}" já declarado(a) em {}. Linha {} - Coluna {}'.format(
            self.classe,
            self.nome,
            self.parent,
            self.linha,
            self.coluna
            ))

class JaDeclaradoParametroError(CompilaError):

    def __init__(self, classe, nome, pai, linha, coluna):
        self.classe = classe
        self.nome = nome
        self.parent = pai
        self.linha = linha
        self.coluna = coluna
        Exception.__init__(self,
            '{} "{}" já declarado(a) como parâmetro em {}. Linha {} - Coluna {}'.format(
            self.classe,
            self.nome,
            self.parent,
            self.linha,
            self.coluna
            ))

class NaoDeclaradaError(CompilaError):

    def __init__(self, classe, nome, pai, linha, coluna):
        self.classe = classe
        self.nome = nome
        self.parent = pai
        self.linha = linha
        self.coluna = coluna
        Exception.__init__(self,
            '{} "{}" não declarado(a). Linha {} - Coluna {}'.format(
            self.classe,
            self.nome,
            self.linha,
            self.coluna
            ))

class FuncaoSemParametros(CompilaError):
    def __init__(self,nome, linha, coluna):
        self.nome = nome
        self.linha = linha
        self.coluna = coluna
        Exception.__init__(self,
            'A função "{}" precisa de parâmetros. Linha {} - Coluna {}'.format(self.nome,self.linha, self.coluna))

class ParametroIncompaivel(CompilaError):
    def __init__(self,nome, param, param_err, indice, linha, coluna):
        Exception.__init__(self,
            'Tipo incompatível no {}º parâmentro da chamada da função "{}", um(a) "{}" era esperado(a), porém foi atribuído um(a) "{}". Linha {} - Coluna {}'.format(
                indice, nome, param, param_err, linha, coluna))

class EraEsperado(CompilaError):
    def __init__(self,tipo, linha, coluna):
        self.tipo = tipo
        self.linha = linha
        self.coluna = coluna
        Exception.__init__(self,
            'Variável de tipo "{}" era esperado(a). Linha {} - Coluna {}'.format(self.tipo, self.linha, self.coluna))

class AtribuicaoErro(CompilaError):
    def __init__(self,tipo, tipo2, linha, coluna):
        self.tipo = tipo
        self.tipo2 = tipo2
        self.linha = linha
        self.coluna = coluna
        Exception.__init__(self,
            'Atribuição incorreta de tipos: "{}" recebendo "{}". Linha {} - Coluna {}'.format(self.tipo, self.tipo2, self.linha, self.coluna))

class CustomError(CompilaError):
    def __init__(self,msg, linha, coluna):
        Exception.__init__(self,msg+" Linha {} - Coluna {}".format(linha, coluna))

class MyErrorListener( ErrorListener ):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("Erro de sintaxe na linha "+str(line) + ", coluna " + str(column) + ".")
        # print( "Terminating Translation")
        # sys.exit()

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        # print( "Ambiguity ERROR, " + str(configs))
        # print( "Erro de ambiguidade.")
        # sys.exit()
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass
        # print( "Attempting full context ERROR, " + str(configs))
        # sys.exit()

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        # print( "Context ERROR, " + str(configs))
        # print( "Erro de contexto")
        # sys.exit()
        pass
