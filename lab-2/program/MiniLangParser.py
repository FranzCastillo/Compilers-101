# Generated from MiniLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,109,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,4,0,11,8,0,11,
        0,12,0,12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,27,
        8,1,11,1,12,1,28,1,1,1,1,4,1,33,8,1,11,1,12,1,34,3,1,37,8,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,4,1,46,8,1,11,1,12,1,47,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,5,1,59,8,1,10,1,12,1,62,9,1,3,1,64,8,1,1,1,1,
        1,1,1,4,1,69,8,1,11,1,12,1,70,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,81,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,93,8,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,104,8,3,10,3,12,3,107,9,3,1,
        3,0,1,6,4,0,2,4,6,0,4,1,0,13,14,1,0,17,18,1,0,19,20,2,0,15,16,24,
        29,124,0,8,1,0,0,0,2,80,1,0,0,0,4,82,1,0,0,0,6,92,1,0,0,0,8,10,6,
        0,-1,0,9,11,3,2,1,0,10,9,1,0,0,0,11,12,1,0,0,0,12,10,1,0,0,0,12,
        13,1,0,0,0,13,1,1,0,0,0,14,15,3,6,3,0,15,16,5,30,0,0,16,81,1,0,0,
        0,17,18,5,21,0,0,18,19,5,1,0,0,19,20,3,6,3,0,20,21,5,30,0,0,21,81,
        1,0,0,0,22,23,5,2,0,0,23,24,3,6,3,0,24,26,5,3,0,0,25,27,3,2,1,0,
        26,25,1,0,0,0,27,28,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,36,1,
        0,0,0,30,32,5,4,0,0,31,33,3,2,1,0,32,31,1,0,0,0,33,34,1,0,0,0,34,
        32,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,30,1,0,0,0,36,37,1,0,0,
        0,37,38,1,0,0,0,38,39,5,5,0,0,39,40,5,30,0,0,40,81,1,0,0,0,41,42,
        5,6,0,0,42,43,3,6,3,0,43,45,5,7,0,0,44,46,3,2,1,0,45,44,1,0,0,0,
        46,47,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,50,5,
        5,0,0,50,51,5,30,0,0,51,81,1,0,0,0,52,53,5,8,0,0,53,54,5,21,0,0,
        54,63,5,9,0,0,55,60,5,21,0,0,56,57,5,10,0,0,57,59,5,21,0,0,58,56,
        1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,64,1,0,0,0,
        62,60,1,0,0,0,63,55,1,0,0,0,63,64,1,0,0,0,64,65,1,0,0,0,65,66,5,
        11,0,0,66,68,5,7,0,0,67,69,3,2,1,0,68,67,1,0,0,0,69,70,1,0,0,0,70,
        68,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,73,5,5,0,0,73,74,5,30,
        0,0,74,81,1,0,0,0,75,76,5,12,0,0,76,77,3,6,3,0,77,78,5,30,0,0,78,
        81,1,0,0,0,79,81,5,30,0,0,80,14,1,0,0,0,80,17,1,0,0,0,80,22,1,0,
        0,0,80,41,1,0,0,0,80,52,1,0,0,0,80,75,1,0,0,0,80,79,1,0,0,0,81,3,
        1,0,0,0,82,83,7,0,0,0,83,5,1,0,0,0,84,85,6,3,-1,0,85,93,5,22,0,0,
        86,93,5,23,0,0,87,93,5,21,0,0,88,89,5,9,0,0,89,90,3,6,3,0,90,91,
        5,11,0,0,91,93,1,0,0,0,92,84,1,0,0,0,92,86,1,0,0,0,92,87,1,0,0,0,
        92,88,1,0,0,0,93,105,1,0,0,0,94,95,10,7,0,0,95,96,7,1,0,0,96,104,
        3,6,3,8,97,98,10,6,0,0,98,99,7,2,0,0,99,104,3,6,3,7,100,101,10,5,
        0,0,101,102,7,3,0,0,102,104,3,6,3,6,103,94,1,0,0,0,103,97,1,0,0,
        0,103,100,1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,
        0,106,7,1,0,0,0,107,105,1,0,0,0,12,12,28,34,36,47,60,63,70,80,92,
        103,105
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'if'", "'then'", "'else'", "'end'", 
                     "'while'", "'do'", "'function'", "'('", "','", "')'", 
                     "'return'", "'int'", "'string'", "'&&'", "'||'", "'*'", 
                     "'/'", "'+'", "'-'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'=='", "'!='", "'>'", "'<'", "'>='", "'<='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "MUL", "DIV", "ADD", "SUB", "ID", "INT", 
                      "STRING", "EQ", "NEQ", "GT", "LT", "GTE", "LTE", "NEWLINE", 
                      "WS", "COMMENT", "ERROR" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_type = 2
    RULE_expr = 3

    ruleNames =  [ "prog", "stat", "type", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    MUL=17
    DIV=18
    ADD=19
    SUB=20
    ID=21
    INT=22
    STRING=23
    EQ=24
    NEQ=25
    GT=26
    LT=27
    GTE=28
    LTE=29
    NEWLINE=30
    WS=31
    COMMENT=32
    ERROR=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = MiniLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            print("Accepted!");
            self.state = 10 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 9
                self.stat()
                self.state = 12 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1088426820) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)


    class FunctionContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.ID)
            else:
                return self.getToken(MiniLangParser.ID, i)
        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)
        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)


    class WhileContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)
        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)


    class IfContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)
        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)


    class ReturnContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def stat(self):

        localctx = MiniLangParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = MiniLangParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.expr(0)
                self.state = 15
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = MiniLangParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.match(MiniLangParser.ID)
                self.state = 18
                self.match(MiniLangParser.T__0)
                self.state = 19
                self.expr(0)
                self.state = 20
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = MiniLangParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.match(MiniLangParser.T__1)
                self.state = 23
                self.expr(0)
                self.state = 24
                self.match(MiniLangParser.T__2)
                self.state = 26 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 25
                    self.stat()
                    self.state = 28 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1088426820) != 0)):
                        break

                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 30
                    self.match(MiniLangParser.T__3)
                    self.state = 32 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 31
                        self.stat()
                        self.state = 34 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1088426820) != 0)):
                            break



                self.state = 38
                self.match(MiniLangParser.T__4)
                self.state = 39
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 4:
                localctx = MiniLangParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 41
                self.match(MiniLangParser.T__5)
                self.state = 42
                self.expr(0)
                self.state = 43
                self.match(MiniLangParser.T__6)
                self.state = 45 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 44
                    self.stat()
                    self.state = 47 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1088426820) != 0)):
                        break

                self.state = 49
                self.match(MiniLangParser.T__4)
                self.state = 50
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 5:
                localctx = MiniLangParser.FunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 52
                self.match(MiniLangParser.T__7)
                self.state = 53
                self.match(MiniLangParser.ID)
                self.state = 54
                self.match(MiniLangParser.T__8)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 55
                    self.match(MiniLangParser.ID)
                    self.state = 60
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==10:
                        self.state = 56
                        self.match(MiniLangParser.T__9)
                        self.state = 57
                        self.match(MiniLangParser.ID)
                        self.state = 62
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 65
                self.match(MiniLangParser.T__10)
                self.state = 66
                self.match(MiniLangParser.T__6)
                self.state = 68 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 67
                    self.stat()
                    self.state = 70 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1088426820) != 0)):
                        break

                self.state = 72
                self.match(MiniLangParser.T__4)
                self.state = 73
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 6:
                localctx = MiniLangParser.ReturnContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 75
                self.match(MiniLangParser.T__11)
                self.state = 76
                self.expr(0)
                self.state = 77
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 7:
                localctx = MiniLangParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 79
                self.match(MiniLangParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = MiniLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(MiniLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def MUL(self):
            return self.getToken(MiniLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(MiniLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def ADD(self):
            return self.getToken(MiniLangParser.ADD, 0)
        def SUB(self):
            return self.getToken(MiniLangParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class BoolOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def EQ(self):
            return self.getToken(MiniLangParser.EQ, 0)
        def NEQ(self):
            return self.getToken(MiniLangParser.NEQ, 0)
        def GT(self):
            return self.getToken(MiniLangParser.GT, 0)
        def LT(self):
            return self.getToken(MiniLangParser.LT, 0)
        def GTE(self):
            return self.getToken(MiniLangParser.GTE, 0)
        def LTE(self):
            return self.getToken(MiniLangParser.LTE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolOp" ):
                listener.enterBoolOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolOp" ):
                listener.exitBoolOp(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MiniLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                localctx = MiniLangParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 85
                self.match(MiniLangParser.INT)
                pass
            elif token in [23]:
                localctx = MiniLangParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 86
                self.match(MiniLangParser.STRING)
                pass
            elif token in [21]:
                localctx = MiniLangParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 87
                self.match(MiniLangParser.ID)
                pass
            elif token in [9]:
                localctx = MiniLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 88
                self.match(MiniLangParser.T__8)
                self.state = 89
                self.expr(0)
                self.state = 90
                self.match(MiniLangParser.T__10)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 103
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.MulDivContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 94
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 95
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 96
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.AddSubContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 97
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 98
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 99
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = MiniLangParser.BoolOpContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 100
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 101
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1057062912) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 102
                        self.expr(6)
                        pass

             
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




