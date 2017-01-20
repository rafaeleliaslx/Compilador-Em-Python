grammar Portugol;

programa: 'PROG' ID ';' 
    dec_vars? 
    dec_func? 
    bloco_principal 'FIM' '.'
    ;

dec_vars: (variavel ';')+
    ;

variavel: tipo lista_ids
    ;

tipo: 'INTEIRO' 
    | 'REAL'    
    | 'BOOLEANO'
    | 'STRING'  
    ;

lista_ids: ID (',' ID)*
    ;

dec_func: (func)+
    ;

func: 'FUNCAO' ID '(' dec_parametros? ')' ( ':' tipo ) ? ';' 
    dec_vars? 
    bloco_principal 
    retorno? 
    'FIM' ';'
    ;

chamada_func: ID '(' lista_parametros? ')' ';'
    | leitura
    | impressao
    ;

chamada_func_simples: ID '(' lista_parametros? ')'
    ;

lista_parametros: (STRING|boolean|chamada_func_simples) (',' lista_parametros)*
    ;

retorno: 'RETORNE' (boolean|STRING|chamada_func_simples) ';'
    ;

dec_parametros: variavel (';' variavel)*
    ; 

bloco_principal: (comandos)*
    ;

atribuicao: ID '=' (boolean|STRING) ';'
    ;

leitura: 'LEIA' '(' lista_parametros ')' ';'
    ;

impressao: 'IMPRIMA' '(' lista_parametros ')' ';'
    ;

condicional: 'SE' '(' boolean ')' 
    'ENTAO' bloco_principal 
    ('SENAO' bloco_principal)? 
    'FIM' ';'
    ;

laco_repita: 'REPITA' bloco_principal 
    'ATE' '(' boolean ')' ';'
    ;

laco_enquanto: 'ENQUANTO' '(' boolean ')' 
    'FACA' bloco_principal 
    'FIM' ';'
    ;

laco_para: 'PARA' ID '=' (boolean|chamada_func_simples) 
    'ATE' (boolean|chamada_func_simples) 
    ('PASSO' (boolean|chamada_func_simples))? 
    'FACA' bloco_principal 'FIM' ';'
    ;

comandos: atribuicao
    | chamada_func
    | condicional
    | laco_repita
    | laco_enquanto
    | laco_para
    | sair
    | COMMENT
    | LINE_COMMENT
    ;

COMMENT
    : '/*' .*? '*/' -> skip
;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
;

sair: 'SAIR' ';'
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
    | 'true'
    | 'false'
    ;

ID: [a-zA-Z][a-zA-Z0-9]*
    ;


NUM: [0-9]+('.'[0-9]+)?
    ;

STRING: '"' (~['"']|WS)* '"'
    ;

WS: [ \t\r\n] -> skip
    ;