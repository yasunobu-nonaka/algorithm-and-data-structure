def is_valid_parentheses(text):
    stack = []

    for char in text:
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    print(is_valid_parentheses("()"))
    print(is_valid_parentheses("()()"))
    print(is_valid_parentheses("(()"))
    print(is_valid_parentheses("())("))
