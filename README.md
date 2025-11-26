## HW#36 Regular Expressions + LTR Evaluation. 

### Functions are changed to operate on floats

### Function __checkArithmeticExpr
#### takes: expression
Expression may contain:

    - numbers, floating point separator is dot ("."), number cannot start or end with dot; numbers can be negative;
    - parentheses, 
    - operators +, -, *, /, ** (power) and spaces.
Expression cannot start with an operator (except for minus sign) or end with operator.

A workaround is implemented: to ease processing of operators, the "^" is used for pow in the code, and the "**" is substituted with "^" in the initial expression.

#### calls:
    - __checkFullMatch(expression) - taking expression as argument and matching it against numbers, operators and parentheses rules groups. Found groups are substituted with empty string; if any part of the expression is not matching any group, it is not substituted and a ValueError is raised.

    - __countParentheses(expression) - taking expression as argument and checking that the count of opening and closing parentheses is equal; if not, function raises ValueError.

#### Tests are implemeted to check evaluation of expressions with floats.
