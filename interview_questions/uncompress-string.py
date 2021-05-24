
def expand(): 
   compressed = "[ab[c]]" 
   s = stack()  
   factor = 1
   for char in compressed: 
       if char != ‘]’: 
           s.push(char) ['[', 'a', 'b','[', 'c']
        elif char == "]" : 
            temp = list   
            # S # [‘A’, ‘2’, ’[‘, ‘b’, ‘c’] 
            while s.peek() != ‘[‘:
                temp.append(s.pop()) # ['c'] 
                # S # [‘A’, ‘2’, ’[‘] 
                temp.reverse() 
                # Temp # ['a', ‘b’, ‘c’] 
                s.pop() # pops left ‘[‘ 
                factor  = isdigit(s.peek())?; s.pop(): 1 
                intermediate_obj = "".join(temp)*factor #  
                s.push(intermediate_obj) #  ['[', 'a', 'b','c']

                # [a,b,c] 
    
    return  "".join(s)


if __name__ == '__main__':
    expand()