PROG FATORIAL;
    INTEIRO I, X, RESULTADO, OPCAO;
    REPITA
        RESULTADO = 1;
        LEIA(X);
        SE (X < 0) ENTAO
        	IMPRIMA ("DIGITE UM NUMERO NAO NEGATIVO");
        SENAO
        	SE (X > 0) ENTAO
            	PARA I = 1 ATE X FACA
                	RESULTADO = RESULTADO * I;
                FIM;
        	FIM;
        	SE (X == 0) ENTAO
        		RESULTADO = 1;
        	FIM;
        	IMPRIMA (RESULTADO);
        FIM;
        IMPRIMA ("Deseja continuar? (-1 para Sair)");
        LEIA (OPCAO);
    ATE (OPCAO == -1);
FIM.