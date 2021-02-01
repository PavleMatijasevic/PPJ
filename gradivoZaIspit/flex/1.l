%option noyywrap

%{
    int brojLinija = 0;
    int brojKaraktera = 0;

%}


%%

\n  {brojLinija++; brojKaraktera++;}
.   {brojKaraktera++;}

%%


int main(){
    yylex();
    
    printf("Broj linija: %d\n", brojLinija);
    printf("Broj karaktera: %d\n", brojKaraktera);

    exit(EXIT_SUCCESS);
}
