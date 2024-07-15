grammar MiniLang;

prog:   stat+ ;

stat:   expr NEWLINE                 # printExpr
    |   ID '=' expr NEWLINE          # assign
    |   NEWLINE                      # blank
    ;

expr:   expr op=('*'|'/') expr       # MulDiv
    |   expr op=('+'|'-') expr       # AddSub
    |   INT                          # int
    |   ID                           # id
    |   '(' expr ')'                 # parens
    ;

MUL : '*' ; // define token for multiplication
DIV : '/' ; // define token for division
ADD : '+' ; // define token for addition
SUB : '-' ; // define token for subtraction
ID  : [a-zA-Z]+ ; // match identifiers
INT : [0-9]+ ; // match integers
NEWLINE:'\r'? '\n' ; // return newlines to parser (is end-statement signal)
WS  : [ \t]+ -> skip ; // toss out whitespace
COMMENT: '//' ~[\r\n]* -> skip ; // toss out comments

ERROR : . { print("No defined token for: '{0}'".format(self.text)) } ;
