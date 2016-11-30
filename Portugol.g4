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
listaIDs[int tip]: ( ID | atribuicao ) (',' ( ID | atribuicao ) )*
        ;

decFunc: 'FUNCAO' ID '(' listaParamentros? ')' ( ':' tipo ) ? ';' decVars? 
         blocoPrincipal ( 'retorne' expr)? 'FIM' ';'
       ;

listaParamentros: (decVars)(';' decVars)*
                ; 

blocoPrincipal: comandos+
              ;

comandos: decVars
		    | atribuicao ';'
        | leitura
        | impressao
        | condicional
    ;

atribuicao: ID '=' expr (',' ID '=' expr)*
          ;

leitura: 'LEIA' '(' listaIDs[0] ')' ';'
       ;

impressao: 'IMPRIMA' '(' listaExprs ')' ';'
         ;

condicional: 'SE' '(' condicao ')' 'ENTAO' blocoPrincipal ('SENAO' blocoPrincipal)? 'FIM' ';'
            ;

condicao: ID
        | '!'ID
        | ID '&' ID
        | ID '|' ID
        | expr '>' expr
        | expr '<' expr
        | expr '>=' expr
        | expr '<=' expr
        | expr '==' expr
        | expr '!=' expr
        ;

expr: expr op=('+'|'-') term
    | term
    ;

term: term op=('*'|'/') fator
    | fator
    ;

fator:  NUM
      | ID
      | '-' fator
      | '!' fator
      ;

listaExprs: expr (',' expr)*
          ;

ID: [a-zA-Z][a-zA-Z0-9]*
  ;

NUM: [0-9]+('.'[0-9]+)?
   ;

WS: [ \t\r\n] -> skip;
