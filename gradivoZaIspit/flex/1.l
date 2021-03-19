%option noyywrap

%{
    int brojLinija = 0;
    int brojKaraktera = 0;

%}

%%

\n  { brojKaraktera++; brojLinija++;}
.   {brojKaraktera++;}


%%


int main(){
    yylex();
    
    printf("Broj redova je: %d\n", brojLinija);
    printf("Broj karaktera je: %d\n", brojKaraktera);
    

    exit(EXIT_SUCCESS);
}
