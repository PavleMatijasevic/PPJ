%option noyywrap

%{
//zaglavlja
#include<iostream>
#include "parser.tab.hpp"

using namespace std;
    
%}

%%

"print"     {return PRINT_T;}
"$"[a-zA-Z0-9_]+ {
        yylval.niska = new string(yytext);
        return ID_T;
        }
[0-9]+  {
    yylval.niska = new string(yytext);
    return CONST_T;
}
\"[^\"]*\" {
        yylval.niska = new string(yytext+1, strlen(yytext)-2);
        return CONST_T;
        }

[+*=()x\[\],.;/-]    {return *yytext;}
[ \t\n]             {   }
.   {
    cerr << "Leksicka greska!" << endl;
    exit(EXIT_FAILURE);
}


%%