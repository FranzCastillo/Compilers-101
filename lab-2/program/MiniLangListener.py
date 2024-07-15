# Generated from MiniLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete listener for a parse tree produced by MiniLangParser.
class MiniLangListener(ParseTreeListener):

    # Enter a parse tree produced by MiniLangParser#prog.
    def enterProg(self, ctx:MiniLangParser.ProgContext):
        pass

    # Exit a parse tree produced by MiniLangParser#prog.
    def exitProg(self, ctx:MiniLangParser.ProgContext):
        pass


    # Enter a parse tree produced by MiniLangParser#printExpr.
    def enterPrintExpr(self, ctx:MiniLangParser.PrintExprContext):
        pass

    # Exit a parse tree produced by MiniLangParser#printExpr.
    def exitPrintExpr(self, ctx:MiniLangParser.PrintExprContext):
        pass


    # Enter a parse tree produced by MiniLangParser#assign.
    def enterAssign(self, ctx:MiniLangParser.AssignContext):
        pass

    # Exit a parse tree produced by MiniLangParser#assign.
    def exitAssign(self, ctx:MiniLangParser.AssignContext):
        pass


    # Enter a parse tree produced by MiniLangParser#if.
    def enterIf(self, ctx:MiniLangParser.IfContext):
        pass

    # Exit a parse tree produced by MiniLangParser#if.
    def exitIf(self, ctx:MiniLangParser.IfContext):
        pass


    # Enter a parse tree produced by MiniLangParser#while.
    def enterWhile(self, ctx:MiniLangParser.WhileContext):
        pass

    # Exit a parse tree produced by MiniLangParser#while.
    def exitWhile(self, ctx:MiniLangParser.WhileContext):
        pass


    # Enter a parse tree produced by MiniLangParser#function.
    def enterFunction(self, ctx:MiniLangParser.FunctionContext):
        pass

    # Exit a parse tree produced by MiniLangParser#function.
    def exitFunction(self, ctx:MiniLangParser.FunctionContext):
        pass


    # Enter a parse tree produced by MiniLangParser#return.
    def enterReturn(self, ctx:MiniLangParser.ReturnContext):
        pass

    # Exit a parse tree produced by MiniLangParser#return.
    def exitReturn(self, ctx:MiniLangParser.ReturnContext):
        pass


    # Enter a parse tree produced by MiniLangParser#blank.
    def enterBlank(self, ctx:MiniLangParser.BlankContext):
        pass

    # Exit a parse tree produced by MiniLangParser#blank.
    def exitBlank(self, ctx:MiniLangParser.BlankContext):
        pass


    # Enter a parse tree produced by MiniLangParser#type.
    def enterType(self, ctx:MiniLangParser.TypeContext):
        pass

    # Exit a parse tree produced by MiniLangParser#type.
    def exitType(self, ctx:MiniLangParser.TypeContext):
        pass


    # Enter a parse tree produced by MiniLangParser#parens.
    def enterParens(self, ctx:MiniLangParser.ParensContext):
        pass

    # Exit a parse tree produced by MiniLangParser#parens.
    def exitParens(self, ctx:MiniLangParser.ParensContext):
        pass


    # Enter a parse tree produced by MiniLangParser#string.
    def enterString(self, ctx:MiniLangParser.StringContext):
        pass

    # Exit a parse tree produced by MiniLangParser#string.
    def exitString(self, ctx:MiniLangParser.StringContext):
        pass


    # Enter a parse tree produced by MiniLangParser#MulDiv.
    def enterMulDiv(self, ctx:MiniLangParser.MulDivContext):
        pass

    # Exit a parse tree produced by MiniLangParser#MulDiv.
    def exitMulDiv(self, ctx:MiniLangParser.MulDivContext):
        pass


    # Enter a parse tree produced by MiniLangParser#AddSub.
    def enterAddSub(self, ctx:MiniLangParser.AddSubContext):
        pass

    # Exit a parse tree produced by MiniLangParser#AddSub.
    def exitAddSub(self, ctx:MiniLangParser.AddSubContext):
        pass


    # Enter a parse tree produced by MiniLangParser#id.
    def enterId(self, ctx:MiniLangParser.IdContext):
        pass

    # Exit a parse tree produced by MiniLangParser#id.
    def exitId(self, ctx:MiniLangParser.IdContext):
        pass


    # Enter a parse tree produced by MiniLangParser#BoolOp.
    def enterBoolOp(self, ctx:MiniLangParser.BoolOpContext):
        pass

    # Exit a parse tree produced by MiniLangParser#BoolOp.
    def exitBoolOp(self, ctx:MiniLangParser.BoolOpContext):
        pass


    # Enter a parse tree produced by MiniLangParser#int.
    def enterInt(self, ctx:MiniLangParser.IntContext):
        pass

    # Exit a parse tree produced by MiniLangParser#int.
    def exitInt(self, ctx:MiniLangParser.IntContext):
        pass



del MiniLangParser