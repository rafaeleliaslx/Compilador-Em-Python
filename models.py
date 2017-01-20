# -*- coding: utf-8 -*-

from grammar.PortugolListener import PortugolListener
from grammar.PortugolParser import PortugolParser
from antlr4.error.ErrorListener import ErrorListener
from utils.functions import *
from utils import vartipo
from utils.errors import *


class AcoesSemanticas(PortugolListener):

    vars_list = []
    funcs_list = []

    ERRORS = []

    def enterPrograma(self, ctx:PortugolParser.ProgramaContext):
        self.prog_name = ctx.children[1].getText()

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
                        raise JaDeclaradoParametroError(class_name(variavel), var_nome, parent, ctx.stop.line)
                    else:
                        raise JaDeclaradoError(class_name(variavel), var_nome, parent, ctx.stop.line)
                self.vars_list.append(variavel)                    
            except Exception as err:
                print(err)
                self.ERRORS.append(err)

    def enterFunc(self, ctx:PortugolParser.Dec_funcContext):
        parametros = []
        parent = get_parent(ctx)
        func = ctx
        func_name = func.ID().getText()
        retorno = func.tipo().getText() if func.tipo() else ""

        try:
            if contains(self.funcs_list, lambda fun: fun.nome == func_name):
                raise JaDeclaradoError('Função', func_name, parent, ctx.stop.line)
            else:
                for list_pars in func.dec_parametros().variavel():
                    tipo = list_pars.tipo().getText()
                    for par_name in list_pars.lista_ids().getText().split(','):
                        parametros.append(Variavel(par_name, tipo, func_name))

                self.funcs_list.append(Funcao(func_name, retorno, parametros))
        except Exception as err:
            print(err)
            self.ERRORS.append(err)

    def exitAtribuicao(self, ctx:PortugolParser.AtribuicaoContext):
        parent = get_parent(ctx)
        tipo = check_ID(ctx.children[0].getText(), parent, self, ctx.stop.line)
        tipo_attr = ''
        if class_name(ctx.children[2]).startswith('Boolean'):
            tipo_attr = check_boolean(ctx.children[2], parent, self)
        if class_name(ctx.children[2]).startswith('Chama'):
            tipo_attr = check_chamada_func_simples(ctx.children[2], parent, self)
        if tipo == tipo_attr or (tipo==vartipo.FLOAT and tipo_attr==vartipo.INT):
            return
        else:
            raise AtribuicaoErro(tipo, tipo_attr, ctx.stop.line)

        if tipo == vartipo.STRING:
            return
        else:
            raise AtribuicaoErro(tipo, vartipo.STRING, ctx.stop.line)

    def exitRetorno(self, ctx:PortugolParser.RetornoContext):
        parent = get_parent(ctx)
        parent_obj = get_from_id(parent, self.funcs_list)
        tipo = parent_obj.tipo
        # tipo = check_ID(ctx.children[0].getText(), parent, self, ctx.stop.line)
        tipo_attr = ''
        if class_name(ctx.children[1]).startswith('Boolean'):
            tipo_attr = check_boolean(ctx.children[1], parent, self)
        if class_name(ctx.children[1]).startswith('Chama'):
            tipo_attr = check_chamada_func_simples(ctx.children[1], parent, self)
        if tipo == tipo_attr or (tipo==vartipo.FLOAT and tipo_attr==vartipo.INT):
            return
        else:
            raise AtribuicaoErro(tipo, tipo_attr, ctx.stop.line)

        if tipo == vartipo.STRING:
            return
        else:
            raise AtribuicaoErro(tipo, vartipo.STRING, ctx.stop.line)

    def exitChamada_func(self, ctx:PortugolParser.Chamada_funcContext):
        import pdb; pdb.set_trace()


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


class MyErrorListener( ErrorListener ):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print( str(line) + ":" + str(column) + ": sintax ERROR, " + str(msg))
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
