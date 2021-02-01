%option noyywrap
//radi kako treba!
%{
#define KLJUCNA_REC (1)
#define ID (2)
#define I_CONST (3)
#define R_CONST (4)
#define OPERACIJE (5)
#define VECE_MANJE_JEDNAKO (6)
#define INTERPUNKCIJA (7)
#define DODELA (8)
#define OTVORENA_ZAGRADA (9)
#define ZATVORENA_ZAGRADA (10)
#define NESTO_DRUGO (11)
%}
DIGIT [0-9] // iz nekog razloga nece

%%
if|else|begin|var|integer|then|end  {return KLJUCNA_REC;}
[A-Za-z][A-Za-z0-9]* {return ID;}
[0-9]+  {return I_CONST;}
[0-9]+\.[0-9]*  {return R_CONST;}
[+/*-] {return OPERACIJE;}
[><=]|">="|"<=" {return VECE_MANJE_JEDNAKO;}
[,;:\.] {return INTERPUNKCIJA;}
":="    {return DODELA;}
"("     {return OTVORENA_ZAGRADA;}
")"     {return ZATVORENA_ZAGRADA;}
[ \t\n]  {   }  // ako se ovde ne stavi i razmak bude skroz pogresan rad!!!
.   {return NESTO_DRUGO;}

%%


int main(int argc, char** argv){

    int token = 0;
    if(argc > 1){
        yyin = fopen(argv[1], "r");
        if(yyin == NULL)
            exit(EXIT_FAILURE);
    }
    else{
    yyin = stdin;
    }
    
    while(token = yylex()){
        switch(token){
        case KLJUCNA_REC:
        printf("KLJUCNA_REC: %s\n",yytext);
        break;
        case ID:
        printf("ID: %s\n", yytext);
        break;
        case I_CONST:
        printf("I_CONST: %s\n",yytext);
        break;
        case R_CONST:
        printf("R_CONST: %s\n", yytext);
        break;
        case OPERACIJE:
        printf("OPERACIJE: %s\n",yytext);
        break;
        case VECE_MANJE_JEDNAKO:
        printf("VECE_MANJE_JEDNAKO: %s\n", yytext);
        break;
        case INTERPUNKCIJA:
        printf("INTERPUNKCIJA: %s\n",yytext);
        break;
        case DODELA:
        printf("DODELA: %s\n", yytext);
        break;
        case OTVORENA_ZAGRADA:
        printf("OTVORENA_ZAGRADA: %s\n",yytext);
        break;
        case ZATVORENA_ZAGRADA:
        printf("ZATVORENA_ZAGRADA: %s\n",yytext);
        break;
        case NESTO_DRUGO:
        printf("Prijatelju ovde si pogresio: %s\n",yytext);
        break;
        exit(EXIT_FAILURE);
        
        }
    }


    exit(EXIT_SUCCESS);
    }
