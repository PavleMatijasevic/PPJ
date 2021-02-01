%option noyywrap

%{

%}

%%

"{"[^}]*"}" { }
"(*"[^)]*"*)" { }

%%


int main(){

    yylex();


    exit(EXIT_SUCCESS);
    
}
