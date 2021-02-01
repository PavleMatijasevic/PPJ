%option noyywrap

%{
#define I_CONST (1)
#define R_CONST (2)
%}
DIGIT [0-9]

%%

[+\-]?{DIGIT}+  {return I_CONST;}
[+\-]?{DIGIT}+\.{DIGIT}*([Ee][+\-]?{DIGIT}+)?   {return R_CONST;}
.   {   }
\n  {   }

%%

int main(int argc, char** argv){
    int token = 0;
    
   if(argc > 1 && (yyin = fopen(argv[1], "r"))!= NULL)
   ;
   else
   yyin = stdin;
   if(argc > 2 &&(yyout = fopen(argv[2],"w"))!=NULL)
   ;
   else
   yyout = stdout;
   
   while(token = yylex()){
        switch(token){
        case I_CONST:
        printf("Ceo broj je pronadjen!\n");
        break;
        case R_CONST:
        printf("Realan broj je pronadjen!\n");
        break;
        }
   }

    exit(EXIT_SUCCESS);
}
