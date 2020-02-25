from interpreter.parser.expr import ExprVisitor, Expr

class AstPrinter(ExprVisitor):
    def print(self, expr: Expr) -> str:
        return expr.accept(self)

    def visitBinary(self, expr) -> str:
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visitGrouping(self, expr) -> str:
        return self.parenthesize("group", expr.expression)

    def visitLiteral(self, expr) -> str:
        if (expr.value == None):
            return "nil"
        return str(expr.value)

    def visitUnary(self, expr) -> str:
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def parenthesize(self, name, *exprs):
        to_return =f"( {name}";
        for expr in exprs:
            to_return += " " + expr.accept(self)
        return to_return + ")"
