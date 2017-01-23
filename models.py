# -*- coding: utf-8 -*-

from grammar.PortugolListener import PortugolListener
from grammar.PortugolParser import PortugolParser
from utils.functions import *
from utils import vartipo
from utils.errors import *


class AcoesSemanticas(PortugolListener):

    vars_list = []
    funcs_list = []

    ERRORS = []

    def enterPrograma(self, ctx:PortugolParser.ProgramaContext):
        self.prog_name = ctx.children[1].getText().upper()

    def enterVariavel(self, ctx:PortugolParser.VariavelContext):

        if class_name(ctx.parentCtx.parentCtx).startswith('Programa'):
            global_var = True
        else:
            global_var = False
            
        parent = ctx.parentCtx.parentCtx.ID().getText().upper()
        tipo = ctx.tipo().getText().upper()

        vars_nomes = [v for v in ctx.lista_ids().getText().upper().split(',')]

        for var_nome in vars_nomes:
            variavel = Variavel(var_nome, tipo, parent)
            try:
                ja_dec = contains(self.vars_list, lambda var: var.nome == var_nome and var.parent == parent)
                if ja_dec:
                    if not global_var and contains(get_from_id(parent, self.funcs_list).parametros,\
                        lambda var: var.nome == var_nome) and not class_name(ctx.parentCtx).startswith('Dec_parametros'):
                        raise JaDeclaradoParametroError(class_name(variavel), var_nome, parent, ctx.start.line, ctx.start.column)
                    else:
                        raise JaDeclaradoError(class_name(variavel), var_nome, parent, ctx.start.line, ctx.start.column)
                self.vars_list.append(variavel)                    
            except Exception as err:
                print(err)
                self.ERRORS.append(err)

    def enterFunc(self, ctx:PortugolParser.Dec_funcContext):
        parametros = []
        parent = get_parent(ctx)
        func = ctx
        func_name = func.ID().getText().upper()
        retorno = func.tipo().getText().upper() if func.tipo() else ""

        if retorno != "" and search_return(ctx) == None:
            raise CustomError("Função '{}' deve retornar '{}', mas não possui retorno.".format(func_name, retorno),
                            ctx.start.line, ctx.start.column)

        try:
            if contains(self.funcs_list, lambda fun: fun.nome == func_name):
                raise JaDeclaradoError('Função', func_name, parent, ctx.start.line, ctx.start.column)
            else:
                for list_pars in func.dec_parametros().variavel():
                    tipo = list_pars.tipo().getText().upper()
                    for par_name in list_pars.lista_ids().getText().upper().split(','):
                        parametros.append(Variavel(par_name, tipo, func_name))

                self.funcs_list.append(Funcao(func_name, retorno, parametros))
        except Exception as err:
            print(err)
            self.ERRORS.append(err)

    def exitAtribuicao(self, ctx:PortugolParser.AtribuicaoContext):
        parent = get_parent(ctx)
        tipo = check_ID(ctx.children[0].getText().upper(), parent, self, ctx.start.line, ctx.start.column)
        tipo_attr = ''
       
        if class_name(ctx.children[2]).startswith('Terminal'):
            tipo_attr = check_STRING(ctx.children[2], parent, self)
        if class_name(ctx.children[2]).startswith('Boolean'):
            tipo_attr = check_boolean(ctx.children[2], parent, self)
        if class_name(ctx.children[2]).startswith('Chama'):
            tipo_attr = check_chamada_func_simples(ctx.children[2], parent, self)
        if tipo == tipo_attr or (tipo==vartipo.FLOAT and tipo_attr==vartipo.INT):
            return
        else:
            raise AtribuicaoErro(tipo, tipo_attr, ctx.start.line, ctx.start.column)


    def exitRetorno(self, ctx:PortugolParser.RetornoContext):
        parent = get_parent(ctx)

        if parent == self.prog_name:
            return
        
        parent_obj = get_from_id(parent, self.funcs_list)
        tipo = parent_obj.tipo

        if tipo == '' and ctx.getChildCount() == 2:
            return
        if tipo != '' and ctx.getChildCount() == 2:
            raise CustomError("Função '{}' deveria retornar '{}', porém, está retornando nada.".format(parent, tipo),
                ctx.start.line, ctx.start.column)
        
        tipo_attr = ''
        
        if class_name(ctx.children[1]).startswith('Terminal'):
            tipo_attr = check_STRING(ctx.children[1], parent, self)
        if class_name(ctx.children[1]).startswith('Boolean'):
            tipo_attr = check_boolean(ctx.children[1], parent, self)
        if class_name(ctx.children[1]).startswith('Chama'):
            tipo_attr = check_chamada_func_simples(ctx.children[1], parent, self)
        if tipo == '' and tipo_attr != '':
            raise CustomError("Função '{}' foi declarada sem tipo de retorno, porém, está retornando algo do tipo '{}'.".format(parent, tipo_attr),
                ctx.start.line, ctx.start.column)
        if tipo == tipo_attr or (tipo==vartipo.FLOAT and tipo_attr==vartipo.INT):
            return
        else:
            raise AtribuicaoErro(tipo, tipo_attr, ctx.start.line, ctx.start.column)

    def exitChamada_func(self, ctx:PortugolParser.Chamada_funcContext):
        if len(ctx.children) == 1:
            func = ctx.children[0]
            if class_name(func).startswith('Leitura'):
                check_lista_ids(func.children[2], get_parent(ctx), self)
            else:
                check_lista_parametros(func.children[2].children, get_parent(ctx), self)
        else:
            check_chamada_func_simples(ctx, get_parent(ctx), self)

    def exitCondicional(self, ctx:PortugolParser.CondicionalContext):
        parent = get_parent(ctx)
        check = check_boolean(ctx.children[2], parent, self)
        if (not (check == vartipo.BOOL)) and (check not in vartipo.NUM):
            raise CustomError("Condição do comando 'SE' não retorna um valor booleano.", ctx.start.line, ctx.start.column)

    def exitLaco_repita(self, ctx:PortugolParser.Laco_repitaContext):
        parent = get_parent(ctx)
        check = check_boolean(ctx.children[4], parent, self)
        if (not check == vartipo.BOOL) and (check not in vartipo.NUM):
            raise CustomError("Condição em 'ATE' do comando 'REPITA' não retorna um valor booleano.", ctx.start.line, ctx.start.column)

    def exitLaco_enquanto(self, ctx:PortugolParser.Laco_enquantoContext):
        parent = get_parent(ctx)
        check = check_boolean(ctx.children[2], parent, self)
        if (not (check == vartipo.BOOL)) and (check not in vartipo.NUM):
            raise CustomError("Condição do comando 'ENQUANTO' não retorna um valor booleano.", ctx.start.line, ctx.start.column)

    def exitPrograma(self, ctx:PortugolParser.ProgramaContext):
        # import pdb; pdb.set_trace()
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

