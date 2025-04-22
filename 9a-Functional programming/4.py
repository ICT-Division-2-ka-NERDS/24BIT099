lst = ['madam','Python',"malayalam",12321]
def palindrome(s:str):
    return True if s==s[::-1] else False
print(list(filter(palindrome,lst)))