# -*- coding: utf-8 -*-

from grammar.PortugolListener import PortugolListener
from grammar.PortugolParser import PortugolParser
from antlr4.error.ErrorListener import ErrorListener
from errors import *


class AcoesSemanticas(PortugolListener):
    tab_simb = {}
    tab_simb_global = {}
    tab_func = {}

    vars_list = []
    funcs_list = []

    ERRORS = []

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
                ja_dec = contains(self.vars_list, lambda var: var.nome == var_nome and var.parent == parent)
                if ja_dec:
                    if not global_var and contains(get_from_id(parent, self.funcs_list).parametros,\
                        lambda var: var.nome == var_nome) and not class_name(ctx.parentCtx).startswith('Dec_parametros'):
                        raise JaDeclaradoParametroError(class_name(variavel), var_nome, parent)
                    else:
                        raise JaDeclaradoError(class_name(variavel), var_nome, parent)
                self.vars_list.append(variavel)                    
            except Exception as err:
                print(err)
                self.ERRORS.append(err)

    def enterFunc(self, ctx:PortugolParser.Dec_funcContext):
        parametros = []
        parent = ctx.parentCtx.parentCtx.ID().getText()
        func = ctx
        func_name = func.ID().getText()
        retorno = func.tipo().getText() if func.tipo() else ""

        try:
            if contains(self.funcs_list, lambda fun: fun.nome == func_name):
                raise JaDeclaradoError('Função', func_name, parent)
            else:
                for list_pars in func.dec_parametros().variavel():
                    tipo = list_pars.tipo().getText()
                    for par_name in list_pars.lista_ids().getText().split(','):
                        parametros.append(Variavel(par_name, tipo, func_name))

                self.funcs_list.append(Funcao(func_name, retorno, parametros))
        except Exception as err:
            print(err)
            self.ERRORS.append(err)



    def exitFactor(self, ctx:PortugolParser.FactorContext):
        pass

    def exitPrograma(self, ctx:PortugolParser.ProgramaContext):
        pass


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

def get_from_id(id, _list):
    for i in _list:
        if i.nome == id:
            return i
    else:
        return False

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
        # print( "Context ERROR, " + str(configs))
        print( "Context ERROR")
        # sys.exit()
