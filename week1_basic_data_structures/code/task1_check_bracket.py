# python3

'''
Input: 
Input contains one string 𝑆 which consists of big and small latin letters, digits, punctuation
marks and brackets from the set []{}().

Output: 
If the code in 𝑆 uses brackets correctly, output “Success" (without the quotes). Otherwise,
output the 1-based index of the first unmatched closing bracket (right), and if there are no unmatched closing
brackets (left), output the 1-based index of the first unmatched opening bracket.

'''

from collections import namedtuple

def find_mismatch(text):

    opening_brackets_stack = []
    
    for i, char in enumerate(text):
        
        if char in "([{":
            # update the node and index of each openning bracket -- create the stack here
            opening_brackets_stack.append((char,i)) # like 'top'

        if char in ")]}":
            if not opening_brackets_stack: # if stack is empty -- no openning bracket
            
                return (i+1)

            last_stack, _ = opening_brackets_stack.pop() # return the last one 'pop' and to compare with closing term
            
            if char == ")" and last_stack != "(" or \
               char == "]" and last_stack != "[" or \
               char == "}" and last_stack != "{": 
                
                return (i+1) # as 1-based index
            # output the index of first closing bracket in case there is no closing bracket
            # if always match, the stack will be popped to empty, rather than return the index but goes to return False

    if opening_brackets_stack: # if stack is not empty
        _, i = opening_brackets_stack.pop()
        
        return (i+1) # as 1-based index
    # output the index of first openning bracket in case there is no closing bracket -- 
    # IF "if next in ")]}"" is False then return only the index of unmatched openning bracket

    return opening_brackets_stack     
            

if __name__ == "__main__":
    #text = "{[}"
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if not mismatch: # if stack is empty after popping -- which means all paired
        print ("Success")
    else:
        print (mismatch)
    
    


