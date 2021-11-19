

# Searchs for individual axioms
def sentSearch(axiom) -> str:   
    for index, x in enumerate(kb, start = 1):
        if x[-1] == axiom:
            return x
    return "Null"

# Searchs for full sentences
def truthSearch(axiom) -> str:
    for index, x in enumerate(kb, start = 1):
        if x == axiom and len(x) == 1:
            return x
    return "Null"

# Removes extra chars from sentence
def splitter(sentence) -> list:

    sentence = sentence.replace('=','')
    sentence = sentence.replace('>',' ')
    sentence = sentence.replace('v',' ')
    sentence = sentence.replace('^',' ')
    split = sentence.split()

    return split

# Main loop 
def loop(inital):
    print(inital)
    
    x = truthSearch(inital)

    if x != "Null":
        print (f'\nProve: {x}, returns 1')
        return 1
    else:
        y = prove(sentSearch(inital))
    
    print (f'\nProve: {inital}, returns {y}')

# Recursive function that handles the return values
def prove(axiom) -> bool:
    
    # Uncomment this if you want to see the search tree
    #print(axiom)

    # Handles the basic and/or sentences 
    if axiom.find("^") >= 0 or axiom.find("v") >= 0:
        global count    
        count += 1
        if count > 100:
            return 0
        q = []
        key = ""
        if axiom.find("^") >= 0:
            key = "and"
        else:
            key = "or"

        x = splitter(axiom)

        for y in x[:-1]:
            z = sentSearch(y)
            q.append(prove(z))

        a = q.count(0)
        b = q.count(1)

        # Finds the amount of trues and falses and returns a value based off that
        if key == "and":
            if a >= 1:
                return 0
            else:
                return 1
        else:
            if b >= 1:
                return 1
            else:
                return 0

    # Handles single imply sentences
    elif axiom.find("=>") >= 0:

        x = splitter(axiom)
        x = x[:-1]
        z = sentSearch(x[0])
 

        if prove(z) == 1:
            return 1
        else:
            return 0

    # Handles the end of a sentence
    else:        
        q = truthSearch(axiom)
        if q == "Null":
            return 0
        else: 
            return 1

# User input
temp = ""

# Recursion timeout
count = 0

# Knowledge base
kb = []

print("\nSentence format")
print("\nAvBvC=>D")
print("A^B^C=>D")
print("A=>D")
print("A")

# Main program loop
while 1:
    # Grabs the knowledge base from standard input
    while temp != "nil": 
        temp = input("Enter the kb (nil to finish)")
        kb.append(temp)
    del kb[-1] 
    # Loops for the searches
    while 1:
        tested = input("\nTest KB\n")
        loop(tested)  
        count == 0
