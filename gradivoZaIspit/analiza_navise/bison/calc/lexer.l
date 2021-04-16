%option noyywrap

%{

#include "parser.tab.h"

%}

%%

print {return PRINT;}
[a-zA-Z][a-zA-Z0-9]* {
						yylval.ime = strdup(yytext);
						
						if (yylval.ime == NULL) {
							
							fprintf(stderr,"Alokacija");
							exit(EXIT_FAILURE);
						}
						
						return ID;
					}
[0-9]+(\.[0-9]*)?	{
						yylval.v = atof(yytext);
						return BROJ;
					}
"<="	{return LEQ;}
">="	{return GEQ;}
"=="	{return EQ;}
"!="	{return NEQ;}
[+*/()<=>;-]	{return *yytext; }
[ \t\n]	{ }
.		{
			fprintf(stderr, "Leksicka greska: %s\n", yytext);
			exit(EXIT_FAILURE);
		}

%%