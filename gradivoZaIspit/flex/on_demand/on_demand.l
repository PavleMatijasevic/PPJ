%option noyywrap


%{
    #define I_CONST (1)
    #define F_CONST (2)
%}
DIGIT [0-9]


%%

[+\-]?{DIGIT}+  {return I_CONST;}
[+\-]?{DIGIT}+\.{DIGIT}*([Ee][+\-]?{DIGIT}+)? {return F_CONST;}
.   {   }
\n  {   }


%%


int main(){
    
    int token = 0;
    while(token = yylex()){
        switch(token){
            case I_CONST:
            printf("Pronadjen je ceo broj!\n");
            break;
            case F_CONST:
            printf("Pronadjen je realan broj!\n");
            break;
        }
    }
    

    exit(EXIT_SUCCESS);
    }
