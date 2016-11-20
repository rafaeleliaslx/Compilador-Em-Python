grammar Portugol;

programa: 'PROG' ID ';' decVars* decFunc? blocoPrincipal 'FIM' '.'
        ;

decVars: tipo listaIDs[$tipo.tip] ';'
       ;
tipo returns [int tip]
    : 'INTEIRO'  {$tip=1;}
    | 'REAL'     {$tip=2;}
    | 'BOOLEANO' {$tip=3;}
    | 'STRING'   {$tip=4;}
    ;
listaIDs[int tip]: ID (',' ID)*
        ;

decFunc: 'FUNCAO' ID '(' listaParamentros? ')' ( ':' tipo ) ? ';' decVars? 
         blocoPrincipal ( 'retorne' expr)? 'FIM' ';'
       ;

listaParamentros: (decVars)(';' decVars)*
                ; 

blocoPrincipal: comandos+
              ;

comandos: atribuicao
        | leitura
        | impressao
    ;

atribuicao: ID '=' expr ';'
          ;

leitura: 'LEIA' '(' listaIDs[0] ')' ';'
       ;

impressao: 'IMPRIMA' '(' listaExprs ')' ';'
         ;

expr: expr op=('+'|'-') term
    | term
    ;

term: term op=('*'|'/') fator
    | fator
    ;

fator:NUM
    | ID;

listaExprs: expr (',' expr)*
          ;

ID: [a-zA-Z][a-zA-Z0-9]*
  ;

NUM: [0-9]+('.'[0-9]+)?
   ;

WS: [ \t\r\n] -> skip;
