"""Q.Find the common letter between two string"""

str1=input("Enter the 1st string: ")
str2=input("Enter the 2st string: ")
def common_letter(str1,str2):
    s1=set(str1)
    s2=set(str2)
    char=s1 & s2
    print("The common letter: ",char)   
common_letter(str1,str2)    
