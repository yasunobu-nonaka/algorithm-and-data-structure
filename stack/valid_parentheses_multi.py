def is_valid_parentheses(text):
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    for char in text:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    print(is_valid_parentheses("()"))
    print(is_valid_parentheses("[()]"))
    print(is_valid_parentheses("{[()]}"))
    print(is_valid_parentheses("[{}()]"))
    print(is_valid_parentheses("[{}())"))
    print(is_valid_parentheses("{{))"))
