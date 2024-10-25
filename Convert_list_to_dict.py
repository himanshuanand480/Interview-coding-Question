"""Write a program to convert list to dictionary"""

def list_to_dict():
    keys=[1,2,3]
    values=["one","two","three"]
    res=dict(zip(keys,values))
    print(res)

list_to_dict()
print()
def dict_to_tuple():
    keys=[1,2,3]
    values=["one","two","three"]
    x=dict(zip(keys,values))
    for i in x.items():
        print(i)
dict_to_tuple()
