%{
#include <cstdlib>
#include <string>
#include <cstdio>
#include "y.tab.h"
%}

%%

[a-zA-Z][a-zA-Z0-9]*    { yylval.str = new std::string(yytext); return ID; }
[0-9]+                  { yylval.num = strtol(yytext, NULL, 10); return NUMBER; }
"+"                     { return '+'; }
"-"                     { return '-'; }
"*"                     { return '*'; }
"/"                     { return '/'; }
"="                     { return '='; }
":"                     { return ':'; }
[ \t\n]                 ;  // skip whitespace
.                       { return INVALIDO; }

%%

int yywrap() {
    return 1;
}

void yyerror(const char* s) {
    fprintf(stderr, "Error: %s\n", s);
}
