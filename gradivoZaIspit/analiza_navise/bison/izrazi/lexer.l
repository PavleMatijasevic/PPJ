%option noyywrap

%{

#include "parser.tab.h"

%}

%%

[0-9]+		{ 
				yylval.vrednost = atoi(yytext);
				return BROJ; 
			}
[*+();]		{ return *yytext;}
[ \t\n]		{	}
.			{
				fprintf(stderr,"Lekscika greska: %s\n", yytext);
				exit(EXIT_FAILURE);
			}

%%
