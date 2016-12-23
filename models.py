# -*- coding: utf-8 -*-

from grammar.PortugolListener import PortugolListener
from grammar.PortugolParser import PortugolParser
from errors import *


class AcoesSemanticas(PortugolListener):
    tab_simb = {}
    tab_simb_global = {}
    tab_func = {}

    def enterVariavel(self, ctx:PortugolParser.VariavelContext):

        if class_name(ctx.parentCtx.parentCtx).startswith('Programa'):
            global_var = True
        else:
            global_var = False

        tipo = ctx.tipo().getText()

        vars_nomes = [v for v in ctx.lista_ids().getText().split(',')]

        for var_nome in vars_nomes:
            variavel = Variavel(var_nome, tipo)
            try:
                if global_var:
                    if var_nome not in self.tab_simb_global:
                        self.tab_simb_global[var_nome] = variavel
                    else:
                        raise VariavelDeclaradaError(class_name(variavel), var_nome, tipo)
                else:
                    if var_nome in self.tab_simb_global:
                        raise VariavelDeclaradaGlobalError(class_name(variavel), var_nome, tipo)
                    elif var_nome not in self.tab_simb:
                        self.tab_simb[var_nome] = variavel
                    else:
                        raise VariavelDeclaradaError(class_name(variavel), var_nome, tipo)
            except Exception as err:
                print(err)

    def enterDec_func(self, ctx:PortugolParser.Dec_funcContext):

        funcs = [f for f in ctx.func()]



    def exitPrograma(self, ctx:PortugolParser.ProgramaContext):
        print("\n"+"*"*10+" GLOBAIS "+"*"*10)
        for k,v in self.tab_simb_global.items():
            print(k+': '+v.getText())
        print("\n"+"*"*10+" LOCAIS "+"*"*10)
        for k,v in self.tab_simb.items():
            print(k+': '+v.getText())


class Variavel():
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def __str__(self):
        return "Nome: "+self.nome+" - Tipo: "+self.tipo

    def getText(self):
        return str(self)

def class_name(item):
    return item.__class__.__name__