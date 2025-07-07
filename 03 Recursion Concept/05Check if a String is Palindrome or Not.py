#Check if a String is Palindrome or Not


s1="racecar"

def palindrome(s1,st,end):
    if st>=end:
        return True
    
    if s1[st]!=s1[end]:
        return False
    
    return palindrome(s1,st+1,end-1)

checkpalin=palindrome(s1,0,len(s1)-1)
if checkpalin:
    print("Palindrome")
else:
    print("Not Plaindrome")


#TC-> o(N/2) -> o(N)