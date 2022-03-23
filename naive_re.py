#!/usr/bin/env python3
def match(regexp: str, text: str) -> bool:
    # Добавим признак конца строки
    text += '\0'
    regexp += '\0'
    if regexp[0] == '^':
        return matchhere(regexp[1:], text)
    for i in range(len(text)):
        if matchhere(regexp, text[i:]):
            return True
    return False


def matchhere(regexp: str, text: str) -> bool:
    if regexp[0] == '\0':
        return True
    if regexp[1] == '*':
        return matchstar(regexp[0], regexp[2:], text)
    if regexp[0] == '$' and regexp[1] == '\0':
        return text == '\0'
    if text != '\0' and (regexp[0] == '.' or regexp[0] == text[0]):
        return matchhere(regexp[1:], text[1:])
    return False


def matchstar(c: str, regexp: str, text: str) -> bool:
    i = 0
    # * может быть и для 0 вхождений
    if matchhere(regexp, text[i:]):
        return True
    while text[i] != '\0' and (text == c or c == '.'):
        i += 1
        if matchhere(regexp, text[i:]):
            return True
    return False

print(match("abc", "abc"))
print(match("abc$", "xyzabc"))
print(match("^abc", "xyzabc"))
print(match("^abc", "abcx"))
print(match("a*b", "bcd"))
print(match("a*b", "aaaaabcd"))
