%option noyywrap

%{
    int brojOtvorenihZagrada = 0;
%}


%%
"(" {brojOtvorenihZagrada++; ECHO;}
")" {
    ECHO;
    if(brojOtvorenihZagrada > 0){
        brojOtvorenihZagrada--;
        }
    else{
        printf("Zagrade nisu dobro uparene!\n");
        return (-1);
        }
    }
.   {ECHO;}
\n  {ECHO;} 


%%

int main(){

    if(yylex() == -1)
        exit(EXIT_FAILURE);
    if(brojOtvorenihZagrada == 0)
        printf("Zagrade su dobro uparene!\n");
    else
        printf("Zagrade nisu dobro uparene!\n");

    exit(EXIT_SUCCESS);
}
