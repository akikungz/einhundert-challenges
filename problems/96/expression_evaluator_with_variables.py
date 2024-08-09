def ecaluate_expression(expression: str, variables: dict = None) -> int:
    # Write your code here
    pass

def main():
    expression = "x = 3 + 5 * (2 - 1)"
    variables = {}
    print(ecaluate_expression(expression, variables))  # 8
    
    expression = "y = x + 4"
    variables = {"x": 8}
    print(ecaluate_expression(expression, variables))  # 12
    
    expression = "z = (x + y) * 2"
    variables = {"x": 3, "y": 5}
    print(ecaluate_expression(expression, variables))  # 16