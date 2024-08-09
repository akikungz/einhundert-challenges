from expression_evaluator_with_variables import ecaluate_expression

def test_expression_evaluator_with_variables():
    expression = "x = 3 + 5 * (2 - 1)"
    variables = {}
    assert ecaluate_expression(expression, variables) == 8
    
    expression = "y = x + 4"
    variables = {"x": 8}
    assert ecaluate_expression(expression, variables) == 12
    
    expression = "z = (x + y) * 2"
    variables = {"x": 3, "y": 5}
    assert ecaluate_expression(expression, variables) == 16