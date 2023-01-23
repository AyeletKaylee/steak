def print_vertically(word: str):
    if len(word) <= 1:
        print(word)
    
    else:
        print(word[0])
        print_vertically(word[1:]) # the word from index 1 and on = remove the first item
        
        
print_vertically("Hello")