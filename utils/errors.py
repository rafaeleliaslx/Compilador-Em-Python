# -*- coding: utf-8 -*-


class CompilaError(Exception):
    """docstring for CompilaError"""

class JaDeclaradoError(CompilaError):

    def __init__(self, classe, nome, pai, linha):
        self.classe = classe
        self.nome = nome
        self.parent = pai
        self.linha = linha
        Exception.__init__(self,
            '{} "{}" já declarado(a) em {} - Linha {}'.format(
            self.classe,
            self.nome,
            self.parent,
            self.linha
            ))

class JaDeclaradoParametroError(CompilaError):

    def __init__(self, classe, nome, pai, linha):
        self.classe = classe
        self.nome = nome
        self.parent = pai
        self.linha = linha
        Exception.__init__(self,
            '{} "{}" já declarado(a) como parâmetro em {}  - Linha {}'.format(
            self.classe,
            self.nome,
            self.parent,
            self.linha
            ))

class NaoDeclaradaError(CompilaError):

    def __init__(self, classe, nome, pai, linha):
        self.classe = classe
        self.nome = nome
        self.parent = pai
        self.linha = linha
        Exception.__init__(self,
            '{} "{}" não declarado(a). - Linha {}'.format(
            self.classe,
            self.nome,
            self.linha
            ))

class FuncaoSemParametros(CompilaError):
    def __init__(self,nome, linha):
        self.nome = nome
        self.linha = linha
        Exception.__init__(self,
            'A função "{}" precisa de parâmetros. - Linha {}'.format(self.nome,self.linha))

class ParametroIncompaivel(CompilaError):
    def __init__(self,nome, linha):
        self.nome = nome
        self.linha = linha
        Exception.__init__(self,
            'Parametro(s) incompatíveis na chamada da função "{}". - Linha {}'.format(self.nome, self.linha))

class EraEsperado(CompilaError):
    def __init__(self,tipo, linha):
        self.tipo = tipo
        self.linha = linha
        Exception.__init__(self,
            'Variável de tipo "{}" era esperado(a). - Linha {}'.format(self.tipo, self.linha))

class AtribuicaoErro(CompilaError):
    def __init__(self,tipo, tipo2, linha):
        self.tipo = tipo
        self.tipo2 = tipo2
        self.linha = linha
        Exception.__init__(self,
            'Atribuição incorreta de tipos: "{}" recebendo "{}". - Linha {}'.format(self.tipo, self.tipo2, self.linha))