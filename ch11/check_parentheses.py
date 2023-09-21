def check_parentheses(check_str):
    stack = []
    for c in check_str:
        if c == '(' or c == '{':
            stack.append(c)
        if (c == ')' or c == '}'
            ) and len(stack) == 0:
                return False
        if c == ')' and stack.pop() != '(':
            return False
        if c == '}' and stack.pop() != '{':
            return False
                
    return len(stack) == 0


if __name__ == '__main__':
    invalid_bracket = """
    fn test(param: &str, arg: &str) {
        println!("fn test((}, {})", param, arg);
    }"""
    assert not check_parentheses(invalid_bracket)
