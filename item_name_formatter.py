exceptions = ["of", "the", "an", "a"]

def format(string):
    string = str(string)
    string = string.lower()
    words = string.split(" ")

    output = ""

    i = 0
    while i < len(words):
        if i == 0 or i == len(words) or words[i] not in exceptions:
            words[i] = words[i].capitalize()
        if i == len(words) - 1:
            output += words[i]
        else:
            output += f'{words[i]} '
        
        i += 1
    
    return output

print(format("test"))

