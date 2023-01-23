def palindrome(string: str):
    if len(string) <= 1:
        return True
    
    return string[0] == string[-1] and palindrome(string[1:-1]) # does NOT include the last letter

def palindrome_2(string: str):
    return string == string[::-1]