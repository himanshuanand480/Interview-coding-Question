"Write a programe to Obtain the last word from the given string"
arr=input("Enter the sentence: ").split()
def len_last_word(arr):
    size=len(arr)
    if size==1:
        print(arr)
    else:
        last_word=arr[-1]
        print(last_word)
len_last_word(arr)

#method2:-
arr=input("Enter the sentence: ").split()
def len_last_word(arr):
    last_word=arr[-1]
    print(last_word)
len_last_word(arr)
