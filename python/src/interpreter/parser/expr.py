from abc import ABC
from interpreter.scanner.tokens import Token


class Expr(ABC):
    pass

class Binary(Expr):
    def __init__(self, left:Expr, operator: Token, right:Expr) -> None:
        self.left = left
        self.operator = operator
        self.right = right

class Grouping(Expr):
    def __init__(self, expression:Expr) -> None:
        self.expression = expression

class Literal(Expr):
    def __init__(self, value:object) -> None:
        self.value = value

class Unary(Expr):
    def __init__(self, operator:Token, right:Expr) -> None:
        self.right = Expr
