def is_palindrome(text):
    revtext = text[::-1]
    if revtext == text:
        return True
    else:
        return False


print(is_palindrome('УЛЫБОК ТЕБЕ ДЕД МАКАР'))
