## HW#36 Regular Expressions + LTR Evaluation. 

### Functions are changed to operate on floats

### Function __checkArithmeticExpr
#### takes: expression
#### calls:
    - __checkExpressionIsFine(expression) - taking expression as argument and matching it against regex to check that only allowed characters are used; if any unsupported characters are found, function raises ValueError.

    - __checkExpression(expression) - taking expression as argument and checking that it does not:
        - start with operator - except for minus sign
        - ends with operator
        - has two operators in a row - except for pow and minus sign
        - has operator after opening parentheses - except for minus sign
        - has operand before opening parentheses
        - has operand after closing parentheses
    
    - __countParentheses(expression) - taking expression as argument and checking that the count of opening and closing parentheses is equal; if not, function raises ValueError.

#### Tests are implemeted to check evaluation of expressions with floats.
