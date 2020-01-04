package main

type struct Scanner{
    start, current, line int64,
    source string,
    hadError bool,
    tokens []*Token,
}

func (scanner* Scanner) ScanTokens(){
    var err error;
    for !scanner.atEnd(){
        start = current
        err = scanner.scanToken()
    }
    if err!=nil{
        return scanner.tokens, err
    }
    append(scanner.tokens, &Token(EOF, "", nil, scanner.line))
    return scanner.tokens, nil
}

func (scanner* Scanner) atEnd(){
    return scanner.current >= len(scanner.source)
}

func (scanner* Scanner) scanToken(){
    c := scanner.advance()
    switch c {
        case '(':
            scanner.addToken(LEFT_PAREN)
        case ')':
            scanner.addToken(RIGHT_PAREN)
        case '{':
            scanner.addToken(LEFT_BRACE)
        case '}':
            scanner.addToken(RIGHT_BRACE)
        case ',':
            scanner.addToken(COMMA)
        case '.':
            scanner.addToken(DOT)
        case '-':
            scanner.addToken(MINUS)
        case '+':
            scanner.addToken(PLUS)
        case ';':
            scanner.addToken(SEMICOLON)
        case '*':
            scanner.addToken(STAR)
    }
}

func (scanner* Scanner) advance(){
    scanner.current += 1
    return source[scanner.current-1]
}

func (scanner* Scanner) addToken(Type TokenType){
    scanner.addTokenAndLiteral(Type, nil)
}

func (scanner* Scanner) addTokenAndLiteral(Type TokenType, Literal interface{}){

}
