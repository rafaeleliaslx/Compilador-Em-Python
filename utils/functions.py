# -*- coding: utf-8 -*-
from . import vartipo
from .errors import *


def check_boolean(boolean, parent, acoes):
    if len(boolean.children)==1:
        ret = check_join(boolean.children[0], parent, acoes)
        return ret

    booleano = check_boolean(boolean.children[0], parent, acoes)
    junta = check_join(boolean.children[2], parent, acoes)
    if junta == vartipo.BOOL and booleano == vartipo.BOOL:
        return vartipo.BOOL
    else:
        raise EraEsperado(vartipo.BOOL+' e '+vartipo.BOOL, join.stop.line)


def check_join(join, parent, acoes):
    if len(join.children)==1:
        ret = check_equality(join.children[0], parent, acoes)
        return ret

    junta = check_join(join.children[0], parent, acoes)
    igual = check_equality(join.children[2], parent, acoes)

    if junta == vartipo.BOOL and igual == vartipo.BOOL:
        return vartipo.BOOL
    else:
        raise EraEsperado(vartipo.BOOL+' e '+vartipo.BOOL, join.stop.line)


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
        raise EraEsperado(vartipo.INT+' ou '+vartipo.FLOAT, rel.stop.line)


def check_expr(expr, parent, acoes):
    if len(expr.children)==1:
        ret = check_term(expr.children[0], parent, acoes)
        import pdb; pdb.set_trace()
        return ret

    expressao = check_expr(expr.children[0], parent, acoes)
    termo = check_term(expr.children[2], parent, acoes)

    if termo not in vartipo.NUM or expressao not in vartipo.NUM:
        raise EraEsperado(vartipo.INT+' ou '+vartipo.FLOAT, term.stop.line)


def check_term(term, parent, acoes):
    if len(term.children)==1:
        ret = check_unary(term.children[0], parent, acoes)
        return ret

    termo = check_term(term.children[0], parent, acoes)
    unario = check_unary(term.children[2], parent, acoes)

    if termo not in vartipo.NUM or unario not in vartipo.NUM:
        raise EraEsperado(vartipo.INT+' ou '+vartipo.FLOAT, term.stop.line)


def check_unary(unary, parent, acoes):
    if len(unary.children)==1:
        ret = check_factor(unary.children[0], parent, acoes)
        return ret

    signal = unary.children[0].getText()
    retorno = check_unary(unary.children[1], parent, acoes)

    if signal == '!' and retorno == vartipo.BOOL:
        return vartipo.BOOL
    else:
        raise EraEsperado(vartipo.BOOL, unary.stop.line);
    if signal == '-' and retorno in vartipo.NUM:
        return retorno
    else:
        raise EraEsperado(vartipo.INT+' ou '+vartipo.FLOAT, unary.stop.line)


def check_factor(factor, parent, acoes):
    if len(factor.children) == 3:
        return check_boolean(factor.children[1], parent, acoes)

    if class_name(factor.children[0]).startswith('Chamada'):
        return check_chamada_func_simples(factor.children[0], parent, acoes)

    f_txt = factor.children[0].getText()

    if f_txt == 'true' or f_txt == 'false':
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

    return check_ID(f_txt, parent, acoes, factor.stop.line)


def check_chamada_func_simples(chamada, parent, acoes):
    f = check_ID_func(chamada.children[0].getText(), parent, acoes, chamada.stop.line)
    if len(f.parametros)>0:
        if len(chamada.children)==3:
            raise FuncaoSemParametros(f.nome, chamada.stop.line)
        if check_lista_parametros(acoes, parent, f.parametros, chamada.children[2].children, 0):
            return f.tipo
        else:
            raise ParametroIncompaivel(f.nome, chamada.stop.line)
    else:
        return f.tipo

def check_lista_parametros(acoes, parent, parametros, lista, indice):
    first = lista[0]
    if class_name(first).startswith('Boolean'):
        if parametros[indice].tipo == check_boolean(first, parent, acoes):
            return True if len(lista) == 1 else check_lista_parametros(acoes, parent, parametros, lista[2], indice+1)
        else:
            return False
    if class_name(first).startswith('Chamada'):
        if parametros[indice].tipo == check_chamada_func_simples(first, parent, acoes):
            return True if len(lista) == 1 else check_lista_parametros(acoes, parent, parametros, lista[2], indice+1)
        else:
            return False
    if class_name(first).startswith('Terminal'):
        if parametros[indice].tipo == vartipo.STRING:
            return True if len(lista) == 1 else check_lista_parametros(acoes, parent, parametros, lista[2], indice+1)
        else:
            return False

def check_ID_func(id, parent, acoes, linha):
    f = contains(acoes.funcs_list, lambda func: func.nome == id)
    if f:
        return f
    else:
        raise NaoDeclaradaError('Função', id, parent, linha)

def class_name(item):
    return item.__class__.__name__

def check_ID(id, parent, acoes, linha):
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
    raise NaoDeclaradaError('Variável', id, parent, linha)


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