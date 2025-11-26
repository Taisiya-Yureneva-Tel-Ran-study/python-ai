import operator as op
import re
from functools import reduce

__ops: dict = {
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.truediv,
    "^": op.pow
}

__operators = reduce(lambda res, el: res + "\\" + el, __ops.keys(), "")
# groups to match numbers, operators and parentheses
__numberPattern = r"(?<![\d)])\-\d+\.?\d*|\d+\.?\d*" # numbers including negative numbers
__operatorPattern = fr"(?<=\d|\))([{__operators}])(?=[\d(-])"  # operators are taken only if they are after a number or closing parenthesis
# opening parenthesis shoud not be preceded by a digit
# closing parenthesis should be preceded by a digit or closing parenthesis
__parenthesesPattern = r"(?<!\d)\(|(?<=[\d)])\)"

# pattern to match the initial expression, including numbers, operators and boundary conditions
__fullExprPatternCompiled = re.compile(fr"{__numberPattern}|{__operatorPattern}|{__parenthesesPattern}")

__numberPatternCompiled = re.compile(__numberPattern)
__operatorPatternCompiled = re.compile(__operatorPattern)
__parenthesesCompiled = re.compile(r"\([^()]+\)")

def __binCompute(op1: float, op2: float, oper: str) -> int:
    operator = __ops.get(oper)
    if not operator:
        raise ValueError(f"Unsupported operator: {oper}")
    return operator(op1, op2)

def __ltrEvalWOParentheses(expr: str) -> float:
    operators: list[str] = __operatorPatternCompiled.findall(expr) 
    operands = __numberPatternCompiled.findall(expr)
    
    res = float(operands[0])
    for i in range(1, len(operators)+1):
        res = __binCompute(res, float(operands[i]), operators[i-1])
    return res

def __checkFullMatch(expr: str):
    res = __fullExprPatternCompiled.sub("", expr)
    if res != "":
        raise ValueError("The expression is malformed.")

def __countParentheses(expr: str):
    res = 0
    for c in expr:
        res += 1 if c == "(" else -1 if c == ")" else 0
        if res < 0: # if there is closing parenthesis without opening one - raise immediately
            raise ValueError("The expression contains unbalanced parentheses.")
    if res > 0:
        raise ValueError("The expression contains unbalanced parentheses.")
 
def __checkArithmeticExpr(expr: str):
    __checkFullMatch(expr)
    __countParentheses(expr)
    
def eval(expr: str) -> int:
    expr = expr.replace(" ", "").replace("**", "^") # Clean spaces and a workaround to ease pow processing
    __checkArithmeticExpr(expr)
    # find expressions in parentheses and evaluate them
    while  par := __parenthesesCompiled.search(expr):
        res = __ltrEvalWOParentheses(par.group()[1:-1])
        expr = expr[:par.start()] + str(res) + expr[par.end():]
    return __ltrEvalWOParentheses(expr)

