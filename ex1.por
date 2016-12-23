PROG Teste1;
    INTEIRO N1, N2;

    FUNCAO MEDIA(REAL S1,S2,S3):REAL;
        INTEIRO N1;
        RETORNE (S1+S2+S3)/3;
    FIM;

    REPITA
        LEIA (N1, N2);
        SE (N2 == 0) ENTAO
            SAIR;
        SENAO
            IMPRIMA (N1/N2);
        FIM;
    ATE (1);
FIM.