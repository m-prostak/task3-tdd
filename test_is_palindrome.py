from main import is_palindrome

def test_is_palindrome_happy():
    assert is_palindrome("a") == True
    assert is_palindrome("aba") == True
    assert is_palindrome("abba") == True
    assert is_palindrome("12345654321") == True

def test_is_palindrome_unhappy():
    assert is_palindrome("ab") == False
    assert is_palindrome("abca") == False
    assert is_palindrome("abc") == False
    assert is_palindrome("abasdasdc") == False