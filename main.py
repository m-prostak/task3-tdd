def is_palindrome(word):
    for index in range(0, int(len(word)/2),1):
        if not word[index]==word[len(word)-1-index]:
            return False
    return True