%option noyywrap

%{
    int broj_otvorenihZagrada = 0;
%}


%%
"(" {broj_otvorenihZagrada++;}
")" {
    if(broj_otvorenihZagrada>0){
        broj_otvorenihZagrada--;
    }
    else{
        printf("Zagrade nisu uparene!\n");
        return(-1);
    }
    }
.   {}
\n  {}

%%

int main(){
    
    if(yylex() == -1){
    exit(EXIT_FAILURE);
    
    }
    
    if(broj_otvorenihZagrada == 0){
        printf("Zagrade su uparene kako treba!\n");
    }
    else{
    printf("Zagrade nisu uparene kako treba!\n");
    }
    
    exit(EXIT_SUCCESS);
    }
