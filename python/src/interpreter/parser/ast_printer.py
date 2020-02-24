from interpreter.parser.expr import ExprVisitor, Expr

class AstPrinter(ExprVisitor):
    def print(self, expr: Expr) -> str:
        return expr.accept(self)

    def visitBinary(binary_expr) -> str:
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visitGrouping(grouping_expr) -> str:
        return self.parenthesize("group", expr.expression)

    def visitLiteral(unary_expr) -> str:
        if (expr.value == None):
            return "nil"
        return str(expr.value)

    def visitUnary(literal_value) -> str:
        return self.parenthesize(expr.operator.lexeme, expr.right)
