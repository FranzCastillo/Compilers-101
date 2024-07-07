flex files/simple_language.l
yacc -dtv files/simple_language_6.y
g++ -c lex.yy.c 
g++ -c y.tab.c
g++ -o calc y.tab.o lex.yy.o

tr -d '\r' < buildLanguage.sh > newBuildLanguage.sh
tr -d '\r' < p/p1.txt > p1.txt
tr -d '\r' < p/p2.txt > p2.txt
tr -d '\r' < p/p3.txt > p3.txt
tr -d '\r' < p/p4.txt > p4.txt
tr -d '\r' < p/p5.txt > p5.txt
sh newBuildLanguage.sh