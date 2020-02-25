from abc import ABC, abstractmethod
from interpreter.scanner.tokens import Token

class Expr(ABC):
    @abstractmethod
    def accept(visitor):
        pass

class ExprVisitor(ABC):
    @abstractmethod
    def visitBinary(self, binary_expr) -> None:
        pass

    @abstractmethod
    def visitGrouping(self, grouping_expr) -> None:
        pass

    @abstractmethod
    def visitLiteral(self, unary_expr) -> None:
        pass

    @abstractmethod
    def visitUnary(self, literal_value) -> None:
        pass

class Binary(Expr):
    def __init__(self, left:Expr, operator: Token, right:Expr) -> None:
        self.left = left
        self.operator = operator
        self.right = right

    def accept(self, visitor:ExprVisitor) -> None:
        return visitor.visitBinary(self)

class Grouping(Expr):
    def __init__(self, expression:Expr) -> None:
        self.expression = expression

    def accept(self, visitor:ExprVisitor) -> None:
        return visitor.visitGrouping(self)

class Literal(Expr):
    def __init__(self, value:object) -> None:
        self.value = value

    def accept(self, visitor:ExprVisitor) -> None:
        return visitor.visitLiteral(self)

class Unary(Expr):
    def __init__(self, operator:Token, right:Expr) -> None:
        self.operator = operator
        self.right = right

    def accept(self, visitor:ExprVisitor) -> None:
        return visitor.visitUnary(self)
