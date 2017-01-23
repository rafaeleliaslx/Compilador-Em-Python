grammar Portugol;

programa: ('PROG'|'prog') ID ';' 
    dec_vars? 
    dec_func? 
    bloco_principal ('FIM'|'fim') '.'
    ;

dec_vars: (variavel ';')+
    ;

variavel: tipo lista_ids
    ;

tipo: ('INTEIRO' |   'inteiro'  )
    | ('REAL'    |   'real'     )
    | ('BOOLEANO'|   'booleano' )
    | ('STRING'  |   'string'   )
    ;

lista_ids: ID (',' ID)*
    ;

dec_func: (func)+
    ;

func: ('FUNCAO'|'funcao') ID '(' dec_parametros? ')' ( ':' tipo ) ? ';' 
    dec_vars? 
    bloco_principal 
    retorno? 
    ('FIM'|'fim') ';'
    ;

chamada_func: ID '(' lista_parametros? ')' ';'
    | leitura
    | impressao
    ;

chamada_func_simples: ID '(' lista_parametros? ')'
    ;

lista_parametros: (STRING|boolean|chamada_func_simples) (',' lista_parametros)*
    ;

retorno: ('RETORNE'|'retorne') (boolean|STRING|chamada_func_simples)? ';'
    ;

dec_parametros: variavel (';' variavel)*
    ; 

bloco_principal: (comandos)*
    ;

atribuicao: ID '=' (boolean|STRING|chamada_func_simples) ';'
    ;

leitura: ('LEIA'|'leia') '(' lista_ids ')' ';'
    ;

impressao: ('IMPRIMA'|'imprima') '(' lista_parametros ')' ';'
    ;

condicional: ('SE'|'se') '(' boolean ')' 
    ('ENTAO'|'entao') bloco_principal 
    (('SENAO'|'senao') bloco_principal)? 
    ('FIM'|'fim') ';'
    ;

laco_repita: ('REPITA'|'repita') bloco_principal 
    ('ATE'|'ate') '(' boolean ')' ';'
    ;

laco_enquanto: ('ENQUANTO'|'enquanto') '(' boolean ')' 
    ('FACA'|'faca') bloco_principal 
    ('FIM'|'fim') ';'
    ;

laco_para: ('PARA'|'para') ID '=' (boolean|chamada_func_simples) 
    ('ATE'|'ate') (boolean|chamada_func_simples) 
    (('PASSO'|'passo') (boolean|chamada_func_simples))? 
    ('FACA'|'faca') bloco_principal ('FIM'|'fim') ';'
    ;

comandos: atribuicao
    | chamada_func
    | condicional
    | laco_repita
    | laco_enquanto
    | laco_para
    | sair
    | retorno
    | COMMENT
    | LINE_COMMENT
    ;

COMMENT
    : '/*' .*? '*/' -> skip
;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
;

sair: ('SAIR'|'sair') ';'
    ;

boolean returns [String _tipo]
    : boolean '|' join 
    | join
    ;

join returns [String _tipo]
    : join '&' equality 
    | equality
    ;

equality returns [String _tipo]
    : equality '==' rel 
    | equality '!=' rel
    | rel
    ;

rel returns [String _tipo]
    : expr '>' expr
    | expr '<' expr
    | expr '>=' expr
    | expr '<=' expr 
    | expr
    ;

expr returns [String _tipo]
    : expr op=('+'|'-') term
    | term
    ;

term returns [String _tipo]
    : term op=('*'|'/') unary
    | unary
    ;

unary returns [String _tipo]
    : '!' unary
    | '-' unary
    | factor
    ;

factor: NUM
    | ID
    | '(' boolean ')'
    | chamada_func_simples
    | ('TRUE'   |   'true'  )
    | ('FALSE'  |   'false' )
    ;

ID: [a-zA-Z][a-zA-Z0-9]*
    ;


NUM: [0-9]+('.'[0-9]+)?
    ;

STRING: '"' (~['"']|WS)* '"'
    ;

WS: [ \t\r\n] -> skip
    ;