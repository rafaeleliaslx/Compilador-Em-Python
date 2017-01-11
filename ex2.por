PROG Teste2;
    INTEIRO I, N1, OPCAO;
    REAL SOMA;
    REPITA
        SOMA = 0;
        LEIA(N1);
        SE (N1 > 0) ENTAO
            PARA I DE 1 ATE N1 FACA
                SOMA = SOMA + I;
            FIM;
        SENAO
            PARA I DE N1 ATE 1 PASSO -1 FACA
                SOMA = SOMA + I;
            FIM;
        FIM;
        IMPRIMA (SOMA);
        IMPRIMA (“Deseja continuar? (-1 para Sair)”);
        LEIA (OPCAO);
    ATE (OPCAO == -1)
FIM.