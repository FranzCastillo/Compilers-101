grammar MiniLang;

prog:   {print("Accepted!");} stat+ ;

stat:   expr NEWLINE                 # printExpr
    |   ID '=' expr NEWLINE          # assign
    |   'if' expr 'then' stat+ ('else' stat+)? 'end' NEWLINE # if
    |   'while' expr 'do' stat+ 'end' NEWLINE# while
    |   'function' ID '(' (ID (',' ID)*)? ')' 'do' stat+ 'end' NEWLINE # function
    |   NEWLINE                      # blank
    ;

expr:   expr op=('*'|'/') expr       # MulDiv
    |   expr op=('+'|'-') expr       # AddSub
    |   expr op=('=='|'!='|'>'|'<'|'>='|'<='|'&&'|'||') expr  # BoolOp
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

EQ  : '==';
NEQ : '!=';
GT  : '>';
LT  : '<';
GTE : '>=';
LTE : '<=';

NEWLINE:'\r'? '\n' ; // return newlines to parser (is end-statement signal)
WS  : [ \t]+ -> skip ; // toss out whitespace
COMMENT: '//' ~[\r\n]* -> skip ; // toss out comments

ERROR : . { print("No defined token for: '{0}'".format(self.text)) } ;
