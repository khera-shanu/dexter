from interpreter.scanner.tokens import Token, TokenType
from interpreter.parser.expr import Binary, Unary, Grouping, Literal
from interpreter.parser.ast_printer import AstPrinter


#(123 + 456) * (-2)  (*  (+ 123 456) (-2))

sum_123_456 = Binary(
                        Literal(123),
                        Token(TokenType.PLUS, "+", None, 1),
                        Literal(456)
                    )

negative_2 = Unary(
                    Token(TokenType.MINUS, "-", None, 1),
                    Literal(2)
                  )

multiplication = Binary(
                         Grouping(sum_123_456),
                         Token(TokenType.STAR, "*", None, 1),
                         Grouping(negative_2)
                       )

print(AstPrinter().print(multiplication));
