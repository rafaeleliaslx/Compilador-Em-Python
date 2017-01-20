# -*- coding: utf-8 -*-


class CompilaError(Exception):
    """docstring for CompilaError"""

class JaDeclaradoError(CompilaError):

    def __init__(self, classe, nome, pai):
        self.classe = classe
        self.nome = nome
        self.parent = pai
        Exception.__init__(self,
            '{} {} já declarado(a) em {}'.format(
            self.classe,
            self.nome,
            self.parent
            ))

class JaDeclaradoParametroError(CompilaError):

    def __init__(self, classe, nome, pai):
        self.classe = classe
        self.nome = nome
        self.parent = pai
        Exception.__init__(self,
            '{} {} já declarado(a) como parâmetro em {}'.format(
            self.classe,
            self.nome,
            self.parent
            ))

