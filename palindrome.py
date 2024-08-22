s = str(input())

def Palindrome(s):
    for i in range(0, len(s)//2):
        if s[i] != s[len(s) - 1]:
            return False
        return True
print(Palindrome(s))