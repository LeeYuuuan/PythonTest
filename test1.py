# test py

def decx_init_add(func1):
    def rex():
        func1(3, 4)
        
    return rex

@decx_init_add    
def funcf(a, b):
    print(f"This is decorator {a + b}.")

funcf()