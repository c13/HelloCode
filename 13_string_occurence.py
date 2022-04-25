# The user specifies two strings. Determine the number of occurrences of one string in another.

def text_find(a,b):
    """
    Function will find occurence of word in the text
    """
    count = 0
    i = 0
    while i <= len(a):
        if b in a[i: i+len(b)]:
            #print("Found repeating string number", count+1)
            count += 1
            i += len(b)
        else:
            i += 1
    return count

a = "a test test taaattt test"
b = "test"

print(f"Count of first word in second phrase: {text_find(a,b)}")
print(f"Count of first string in second phrase: {text_find('aaaaaaaaaa','aa')}")

