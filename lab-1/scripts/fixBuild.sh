tr -d '\r' < buildLanguage.sh > newBuildLanguage.sh
tr -d '\r' < p/p1.txt > p1.txt
tr -d '\r' < p/p2.txt > p2.txt
tr -d '\r' < p/p3.txt > p3.txt
tr -d '\r' < p/p4.txt > p4.txt
tr -d '\r' < p/p5.txt > p5.txt
sh newBuildLanguage.sh