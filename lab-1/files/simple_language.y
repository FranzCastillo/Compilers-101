%{
#include <iostream>
#include <string>
#include <map>
#include <cstdio>
static std::map<std::string, int> vars;
inline void yyerror(const char *str) { std::cout << str << std::endl; }
int yylex();
%}

%union { int num; std::string *str; }

%token<num> NUMBER
%token<str> ID
%token INVALIDO
%type<num> expression
%type<num> assignment

%right '='
%left '+' '-'
%left '*' '/'

%%

program: statement_list
        ;

statement_list: statement
    | statement_list statement
    ;

statement: assignment
    | expression ':' { std::cout << $1 << std::endl; }
    | INVALIDO
    {
        std::cout << "Token Invalido" << std::endl;
    }
    ;

assignment: ID '=' expression
    { 
        std::cout << "Assign " << *$1 << " = " << $3 << std::endl;
        $$ = vars[*$1] = $3;
        delete $1;
    }
    ;

expression: NUMBER { $$ = $1; }
    | ID { $$ = vars[*$1]; delete $1; }
    | expression '+' expression { $$ = $1 + $3; }
    | expression '-' expression { $$ = $1 - $3; }
    | expression '*' expression { $$ = $1 * $3; }
    | expression '/' expression { $$ = $1 / $3; }
    ;

%%

int main() {
    yyparse();
    return 0;
}