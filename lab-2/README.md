# Laboratorio 2

## ¿Cómo correr?
En el root de lab-2 se corre el ambiente (desde Command Promt) como:
  ```
  docker build --rm . -t lab2-image && docker run --rm -ti -v "%cd%\program":/program lab2-image
  ```
Luego, se deben generar los archivos de Lexer y Parser de ANTLR con el siguiente comando:
  ```
  antlr4 -Dlanguage=Python3 MiniLang.g4
  ```
Luego, usar el Driver para analizar el archivo de prueba:
  ```
  python3 Driver.py program_test.txt
  ```
* Si el archivo se encuentra sintácticamente correcto, no verán un output en la consola. Por el contrario si hay un error sintáctico/léxico, ANTLR se los hará saber.
* Y listo, con esto ya tienen un playground inicial para probar archivos con ANTLR.
* Para sus proyectos, se recomienda que extiendan este ambiente para sostener una arquitectura más robusta, este solo es un ejemplo básico.
