# -*- coding: utf-8 -*-
from . import vartipo
from .errors import *
import resource, sys


def check_lista_ids(lista_ids, parent, acoes):
    pass

def check_STRING(string, parent, acoes):
    txt = string.getText()
    if txt[0] == '"' and txt[len(txt)-1]:
        return vartipo.STRING
    else:
        raise CustomError("String inválida.",string.start.line, string.start.column)

def check_boolean(boolean, parent, acoes):
    if len(boolean.children)==1:
        ret = check_join(boolean.children[0], parent, acoes)
        return ret

    booleano = check_boolean(boolean.children[0], parent, acoes)
    junta = check_join(boolean.children[2], parent, acoes)
    if junta == vartipo.BOOL and booleano == vartipo.BOOL:
        return vartipo.BOOL
    else:
        raise EraEsperado(vartipo.BOOL+' e '+vartipo.BOOL, boolean.start.line, boolean.start.column)


def check_join(join, parent, acoes):
    if len(join.children)==1:
        ret = check_equality(join.children[0], parent, acoes)
        return ret

    junta = check_join(join.children[0], parent, acoes)
    igual = check_equality(join.children[2], parent, acoes)

    if junta == vartipo.BOOL and igual == vartipo.BOOL:
        return vartipo.BOOL
    else:
        raise EraEsperado(vartipo.BOOL+' e '+vartipo.BOOL, join.start.line, join.start.column)


def check_equality(equality, parent, acoes):
    if len(equality.children)==1:
        ret = check_rel(equality.children[0], parent, acoes)
        return ret

    igualdade = check_equality(equality.children[0], parent, acoes)
    relac = check_rel(equality.children[2], parent, acoes)
    return vartipo.BOOL


def check_rel(rel, parent, acoes):
    if len(rel.children)==1:
        ret = check_expr(rel.children[0], parent, acoes)
        return ret

    expr1 = check_expr(rel.children[0], parent, acoes)
    expr2 = check_expr(rel.children[2], parent, acoes)

    if expr1 in vartipo.NUM and expr2 in vartipo.NUM:
        return vartipo.BOOL
    else:
        raise EraEsperado(vartipo.INT+'" ou "'+vartipo.FLOAT, rel.start.line, rel.start.column)


def check_expr(expr, parent, acoes):
    if len(expr.children)==1:
        ret = check_term(expr.children[0], parent, acoes)
        return ret

    expressao = check_expr(expr.children[0], parent, acoes)
    termo = check_term(expr.children[2], parent, acoes)

    if termo not in vartipo.NUM or expressao not in vartipo.NUM:
        raise EraEsperado(vartipo.INT+'" ou "'+vartipo.FLOAT, expr.start.line, expr.start.column)
    return vartipo.FLOAT if expressao == vartipo.FLOAT or \
    termo == vartipo.FLOAT else vartipo.INT


def check_term(term, parent, acoes):
    if len(term.children)==1:
        ret = check_unary(term.children[0], parent, acoes)
        return ret

    termo = check_term(term.children[0], parent, acoes)
    unario = check_unary(term.children[2], parent, acoes)

    if termo not in vartipo.NUM or unario not in vartipo.NUM:
        raise EraEsperado(vartipo.INT+'" ou "'+vartipo.FLOAT, term.start.line, term.start.column)
    return vartipo.FLOAT if termo == vartipo.FLOAT or \
    unario == vartipo.FLOAT else vartipo.INT

def check_unary(unary, parent, acoes):
    if len(unary.children)==1:
        ret = check_factor(unary.children[0], parent, acoes)
        return ret

    signal = unary.children[0].getText().upper()
    retorno = check_unary(unary.children[1], parent, acoes)

    if signal == '!': 
        if retorno == vartipo.BOOL:
            return vartipo.BOOL
        else:
            raise EraEsperado(vartipo.BOOL, unary.start.line, unary.start.column);
    if signal == '-' and retorno in vartipo.NUM:
        return retorno
    else:
        raise EraEsperado(vartipo.INT+'" ou "'+vartipo.FLOAT, unary.start.line, unary.start.column)


def check_factor(factor, parent, acoes):
    if len(factor.children) == 3:
        return check_boolean(factor.children[1], parent, acoes)

    if class_name(factor.children[0]).startswith('Chamada'):
        return check_chamada_func_simples(factor.children[0], parent, acoes)

    f_txt = factor.children[0].getText().upper()

    if f_txt == 'TRUE' or f_txt == 'FALSE':
        return vartipo.BOOL

    try:
        num = int(f_txt)
        return vartipo.INT
    except:
        pass

    try:
        num = float(f_txt)
        return vartipo.FLOAT
    except:
        pass

    return check_ID(f_txt, parent, acoes, factor.start.line, factor.start.column)


def check_chamada_func_simples(chamada, parent, acoes):
    f = check_ID_func(chamada.children[0].getText().upper(), parent, acoes, chamada.start.line, chamada.start.column)
    if len(f.parametros)>0:
        if len(chamada.children)==3:
            raise FuncaoSemParametros(f.nome, chamada.start.line, chamada.start.column)

        if check_lista_parametros(chamada.children[2].children, f.nome, acoes, f.parametros, 0):
            return f.tipo    
    else:
        return f.tipo

def check_lista_parametros(lista, parent, acoes, parametros=None, indice=None):
    first = lista[0]
    if class_name(first).startswith('Boolean'):
        check = check_boolean(first, parent, acoes)
        if parametros == None and indice == None:
            return check
        if parametros[indice].tipo == check:
            return True if len(lista) == 1 else check_lista_parametros(lista[2].children, parent, acoes, parametros, indice+1)
        else:
            raise ParametroIncompaivel(parent, parametros[indice].tipo, check, indice+1, first.start.line, first.start.column)
    if class_name(first).startswith('Chamada'):
        check = check_chamada_func_simples(first, parent, acoes)
        if parametros == None and indice == None:
            return check
        if parametros[indice].tipo == check:
            return True if len(lista) == 1 else check_lista_parametros(lista[2].children, parent, acoes, parametros, indice+1)
        else:
            raise ParametroIncompaivel(parent, parametros[indice].tipo, check, indice+1, first.start.line, first.start.column)
    if class_name(first).startswith('Terminal'):
        if parametros == None and indice == None:
            return check_STRING(first, parent, acoes)
        if parametros[indice].tipo == vartipo.STRING:
            return True if len(lista) == 1 else check_lista_parametros(lista[2].children, parent, acoes, parametros, indice+1)
        else:
            raise ParametroIncompaivel(parent, parametros[indice].tipo, check, indice+1, first.start.line, first.start.column)

def check_ID_func(id, parent, acoes, linha, coluna):
    f = contains(acoes.funcs_list, lambda func: func.nome == id)
    if f:
        return f
    else:
        raise NaoDeclaradaError('Função', id, parent, linha, coluna)

def class_name(item):
    return item.__class__.__name__

def check_ID(id, parent, acoes, linha, coluna):
    pai = get_from_id(parent, acoes.funcs_list)
    if pai:
        var = contains(pai.parametros, lambda var: var.nome == id)
        if var:
            return var.tipo
        var = contains(acoes.vars_list, lambda var: var.nome == id and var.parent == pai.nome)
        if var:
            return var.tipo
    var = contains(acoes.vars_list, lambda var: var.nome == id and var.parent == acoes.prog_name)
    if var:
        return var.tipo
    raise NaoDeclaradaError('Variável', id, parent, linha, coluna)


def contains(list, filter):
    for x in list:
        if filter(x):
            return x
    return False

def get_from_id(id, _list):
    for i in _list:
        if i.nome == id:
            return i
    else:
        return False

def get_parent(ctx):
    if hasattr(ctx.parentCtx,'ID'):
        return ctx.parentCtx.ID().getText().upper()
    else:
        return get_parent(ctx.parentCtx)

def search_return(ctx):
    if class_name(ctx).startswith('Retorno'):
        return ctx
    else:
        if hasattr(ctx, 'children'):
            for c in ctx.children:
                if search_return(c) != None:
                    return search_return(c)
    return None
