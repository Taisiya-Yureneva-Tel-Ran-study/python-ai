## HW#36 Regular Expressions + LTR Evaluation. 

### Functions are changed to operate on floats

### TODO:
Implement pow (**) operator.

### Function __checkArithmeticExpr
#### takes: expression
#### calls:
    - __checkExpressionIsFine(expression) - taking expression as argument and matching it against regex to check that only allowed characters are used; if any unsupported characters are found, function raises ValueError.

    - __checkExpression(expression) - taking expression as argument and checking that it does not:
        - starts with operator
        - ends with operator
        - has two operators in a row
        - has two operands in a row
        - has operator before opening parentheses
        - has operator after closing parentheses
        - has operand before opening parentheses
        - has operand after closing parentheses
    
    - __countParentheses(expression) - taking expression as argument and checking that the count of opening and closing parentheses is equal; if not, function raises ValueError.

#### Tests are implemeted to check evaluation of expressions with floats.
