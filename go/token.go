package main

import  "fmt"

type TokenType int

const (
    EOF TokenType = iota + 1

    //Single-character tokens.  
    LEFT_PAREN
    RIGHT_PAREN
    LEFT_BRACE
    RIGHT_BRACE
    COMMA
    DOT
    MINUS
    PLUS
    SEMICOLON
    SLASH
    STAR

    //One or two character tokens.                  
    BANG
    BANG_EQUAL
    EQUAL
    EQUAL_EQUAL
    GREATER
    GREATER_EQUAL
    LESS
    LESS_EQUAL

    // Literals.                                     
    IDENTIFIER
    STRING
    NUMBER

    // Keywords.                                     
    AND
    CLASS
    ELSE
    FALSE
    FUN
    FOR
    IF
    NIL
    OR
    PRINT
    RETURN
    SUPER
    THIS
    TRUE
    VAR
    WHILE
)

type struct Token{
    Type TokenType,
    Lexeme string,
    Literal interface{},
    Line int64
}

func (t* Token) String() string{
    return Sprintf("TOKEN<%d %s %s>", t.Type, t.Lexeme, t.Literal)
}
