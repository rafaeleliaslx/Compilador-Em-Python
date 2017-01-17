# -*- coding: utf-8 -*-

from grammar.PortugolListener import PortugolListener
from grammar.PortugolParser import PortugolParser
from errors import *


class AcoesSemanticas(PortugolListener):
    tab_simb = {}
    tab_simb_global = {}
    tab_func = {}

    vars_list = []
    funcs_list = []

    def enterVariavel(self, ctx:PortugolParser.VariavelContext):

        if class_name(ctx.parentCtx.parentCtx).startswith('Programa'):
            global_var = True
        else:
            global_var = False
            
        parent = ctx.parentCtx.parentCtx.ID().getText()
        tipo = ctx.tipo().getText()

        vars_nomes = [v for v in ctx.lista_ids().getText().split(',')]

        for var_nome in vars_nomes:
            variavel = Variavel(var_nome, tipo, parent)
            try:
                if contains(self.vars_list, lambda var: var.nome == var_nome and var.parent == parent):
                    raise JaDeclaradoError(class_name(variavel), var_nome, parent)
                # elif contains(self.func_list, lambda var: var.nome == var_nome and var.parent == parent):
                    # raise VariavelDeclaradaError(class_name(variavel), var_nome, tipo, parent)
                else:
                    self.vars_list.append(variavel)                    
            except Exception as err:
                print(err)

    def enterFunc(self, ctx:PortugolParser.Dec_funcContext):
        parametros = []
        parent = ctx.parentCtx.parentCtx.ID().getText()
        func = ctx
        func_name = func.ID().getText()
        retorno = func.tipo().getText() if func.tipo() else ""

        try:
            if contains(self.funcs_list, lambda fun: fun.nome == func_name):
                raise JaDeclaradoError('Função', func_name, parent)
                import pdb; pdb.set_trace()
            else:
                for list_pars in func.dec_parametros().variavel():
                    tipo = list_pars.tipo().getText()
                    for par_name in list_pars.lista_ids().getText().split(','):
                        parametros.append(Variavel(par_name, tipo, func_name))

                self.funcs_list.append(Funcao(func_name, retorno, parametros))
        except Exception as err:
            print(err)



    def exitFactor(self, ctx:PortugolParser.FactorContext):
        pass

    def exitPrograma(self, ctx:PortugolParser.ProgramaContext):
        print("\n"+"*"*10+" GLOBAIS "+"*"*10)
        for i in self.funcs_list:
            print(i)
        print("\n"+"*"*10+" LOCAIS "+"*"*10)
        for k,v in self.tab_simb.items():
            print(k+': '+v.getText())


class Variavel():
    def __init__(self, nome, tipo, pai):
        self.nome = nome
        self.tipo = tipo
        self.parent = pai

    def __str__(self):
        return "Nome: "+self.nome+" - Tipo: "+self.tipo

    def getText(self):
        return str(self)

class Funcao():
    def __init__(self, nome, tipo, params):
        self.nome = nome
        self.tipo = tipo
        self.parametros = params

    def __str__(self):
        return "Nome: "+self.nome+" - Tipo: "+self.tipo

    def getText(self):
        return str(self)


def class_name(item):
    return item.__class__.__name__

def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False
