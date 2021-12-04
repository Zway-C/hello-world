
nouns = [ "cat", "food", "table"]
input = input("please type a noun:")

def isNoun(word):
    if input in nouns: 
        return True
    return False
        
result = isNoun(word)
print(f"result:{result}")
