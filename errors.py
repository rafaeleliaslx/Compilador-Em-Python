# -*- coding: utf-8 -*-


class CompilaError(Exception):
    """docstring for CompilaError"""

class VariavelDeclaradaError(CompilaError):

    def __init__(self, classe, nome, tipo):
        self.classe = classe
        self.nome = nome
        self.tipo = tipo
        Exception.__init__(self,
            '{0} - {1} - {2} já foi declarado.'.format(
            self.classe,
            self.nome,
            self.tipo
            ))
        
class VariavelDeclaradaGlobalError(CompilaError):

    def __init__(self, classe, nome, tipo):
        self.classe = classe
        self.nome = nome
        self.tipo = tipo
        Exception.__init__(self,
            '{0} - {1} - {2} já foi declarado como global.'.format(
            self.classe,
            self.nome,
            self.tipo
            ))
