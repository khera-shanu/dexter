from .tokens import Token, TokenType, keywords

class Scanner:
    def __init__(self, source):
        self.tokens = []
        self.source = source
        self.start = 0
        self.current = 0
        self.line = 1

    def scan_tokens(self):
        while not self._at_end():
            self.start = self.current
            self._scan_token()
        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def _at_end(self):
        return self.current >= len(self.source)

    def _scan_token(self):
        c = self._advance()
        if   c == '(': self._add_token(TokenType.LEFT_PARAM)
        elif c == ')': self._add_token(TokenType.RIGHT_PARAM)
        elif c == '{': self._add_token(TokenType.LEFT_BRACE)
        elif c == '}': self._add_token(TokenType.RIGHT_BRACE)
        elif c == ',': self._add_token(TokenType.COMMA)
        elif c == '.': self._add_token(TokenType.DOT)
        elif c == '-': self._add_token(TokenType.MINUS)
        elif c == '+': self._add_token(TokenType.PLUS)
        elif c == ';': self._add_token(TokenType.SEMICOLON)
        elif c == '*': self._add_token(TokenType.STAR)
        elif c == '!': self._add_token(TokenType.BANG_EQUAL if self._match('=') else TokenType.BANG)
        elif c == '=': self._add_token(TokenType.EQUAL_EQUAL if self._match('=') else TokenType.EQUAL)
        elif c == '<': self._add_token(TokenType.LESS_EQUAL if self._match('=') else TokenType.LESS)
        elif c == '>': self._add_token(TokenType.GREATER_EQUAL if self._match('=') else TokenType.GREATER)
        elif c == '/':
            if self._match('/'):
                while self._peek() != '\n' and not self._at_end(): self._advance()
            else:
                self._add_token(TokenType.SLASH)
        elif c in (' ', '\r', '\t'): pass #ignore
        elif c == '\n': self.line += 1
        elif c == '"': self._string() #double quoted string
        elif c.isdigit(): self._number()
        elif c.isalnum(): self._identifier()
        else:
            print("Error in _scan_token")
            pass #Dexter._print_error here ?

    def _peek(self):
        if self._at_end(): return '\0'
        return self.source[self.current]

    def _advance(self):
        self.current += 1
        return self.source[self.current-1]

    def _match(self, char):
        if self._at_end(): return False
        if self.source[self.current] != char: return False
        self.current += 1
        return True

    def _string(self):
        while self._peek() != '"' and not self._at_end():
            if self._peek() == '\n': self.line += 1
            self._advance()
        if self._at_end():
            #show error here - unterminated string
            return
        self._advance() # the closing "
        value = self.source[self.start+1:self.current-1]
        self.__add_token(TokenType.STRING, value)

    def _number(self):
        while self._peek().isdigit(): self._advance()
        if self._peek() == '.' and self._peek_next().isdigit():
            self._advance()
            while self._peek().isdigit(): self._advance()
        self.__add_token(TokenType.NUMBER, float(self.source[self.start:self.current]))

    def _identifier(self):
        while self._peek().isalnum(): self._advance()
        text = self.source[self.start:self.current]
        _type = keywords.get(text, TokenType.IDENTIFIER)
        self._add_token(_type)

    def _peek_next(self):
        if self.current + 1 > len(self.source): return '\0'
        return source[current+1]

    def _add_token(self, token_type):
        self.__add_token(token_type, None)

    def __add_token(self, token_type, literal):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))
