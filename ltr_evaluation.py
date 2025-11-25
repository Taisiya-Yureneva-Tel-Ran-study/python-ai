import operator as op
import re

__ops: dict = {
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.truediv,
    "**": op.pow
}

def __binCompute(op1: float, op2: float, oper: str) -> int:
    operator = __ops.get(oper)
    if not operator:
        raise ValueError(f"Unsupported operator: {oper}")
    return operator(op1, op2)

def __ltrEvalWOParentheses(expr: str) -> float:
    operators: list[str] = re.findall(r"[+/]|(?<=\d|\.)\-|\*{1,2}", expr) 
    operands = re.findall(r"(?<=[^\d\.\()])\-\d+\.?\d*|(?:\d+\.?\d*)", expr)
    
    res = float(operands[0])
    for i in range(1, len(operators)+1):
        res = __binCompute(res, float(operands[i]), operators[i-1])
    return res

def __checkExpression(expr: str) -> bool:
    # We check if the expression is valid trying to find errors
    # It can be really useful to help the user to fix the expression
    patCannotStartWith = r"(\A[*/+)])" # Expression cannot start with operands or closing parenthesis - except for "-"
    patNoOperationAfterOpenParenthesis = r"(\([+*/])" # No operation after opening parenthesis - except for "-"
    patNoOperationBeforeCloseParenthesis = r"([+*/-]\))" # No operation before closing parenthesis
    patNoDigitsBeforeOpenParenthesis = r"((\d|\.)\()" # No digits or dots before opening parenthesis
    
    # No duplicate operators - keeping in mind that there is "**" and negative numbers that can be
    # at the beginning of the expression, after any operator and after an opening parenthesis 
    patNoDuplicateOperators = r"[/+]{2,}|[^\d\)\*]\*|((?<=[^\d/*+\.])\-)"   #([+/]{2,})|()" 
    
    patNoDigitsAfterCloseParenthesis = r"(\)(\d|\.))" # No digits after closing parenthesis
    patCannotEndWith = r"([+*/(-]\Z)" # Expression cannot end with operators or opening parenthesis
    pattern = fr"{patCannotStartWith}|{patNoOperationAfterOpenParenthesis}|{patNoOperationBeforeCloseParenthesis}|{patNoDigitsBeforeOpenParenthesis}|{patNoDuplicateOperators}|{patNoDigitsAfterCloseParenthesis}|{patCannotEndWith}"
    res = re.search(pattern, expr)
    return res is None

def __checkExpressionIsFine(expr: str):
    finePattern = r"^[\d+*/.()-]+$"
    if re.fullmatch(finePattern, expr) is None:
        raise ValueError("The expression contains invalid characters. The expression should only contain digits and the operators +, -, *, /, (, )")
    
def __countParentheses(expr: str):
    res = expr.count("(") - expr.count(")")
    if res != 0:
        raise ValueError("The expression contains unbalanced parentheses.")
 
def __checkArithmeticExpr(expr: str):
    __checkExpressionIsFine(expr)
    if not __checkExpression(expr):
        raise ValueError("The expression contains errors and cannot be evaluated.") 
    __countParentheses(expr)
    
def eval(expr: str) -> int:
    expr = expr.replace(" ", "") # Clean spaces
    __checkArithmeticExpr(expr)
    # find expressions in parentheses and evaluate them
    while  par := re.search(r"\([^()]+\)", expr):
        res = __ltrEvalWOParentheses(par.group()[1:-1])
        expr = expr[:par.start()] + str(res) + expr[par.end():]
    return __ltrEvalWOParentheses(expr)

