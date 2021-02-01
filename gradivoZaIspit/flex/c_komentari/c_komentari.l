%option noyywrap

%{
    int broj_linija = 0;
%}

%x comment

%%

"/*"    { BEGIN(comment); }

<comment>[^*\n]*    {   }
<comment>"*"*       {   }
<comment>\n         {broj_linija++;}
<comment>\*+"/"     {BEGIN(INITIAL);}

\n                  {broj_linija++; ECHO;}
.                   {ECHO;}

%%

int main(int argc, char** argv) {

if (argc > 1) {

    yyin = fopen(argv[1], "r");
		if (yyin == NULL) {
			exit(EXIT_FAILURE);
		}
	}
	else {
		yyin = stdin;
	}
	
	if (argc > 2) {
		
		yyout = fopen(argv[2], "w");
		if (yyout == NULL) {
			exit(EXIT_FAILURE);
		}
	}
	else {
		
		yyout = stdout;
	}

	yylex();
	
	if (yyin != stdin)
		fclose(yyin);
		
	if (yyout != stdout) {
		fclose(yyout);
	}
	
	
	exit(EXIT_SUCCESS);
}
