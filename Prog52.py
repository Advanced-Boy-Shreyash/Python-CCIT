# Function Returning Function

def test():
    def message():
        return "Welcome to CCIT"
    return (message)


result = test()
print(result())
