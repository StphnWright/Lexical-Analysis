"""
A program that prompts a user string input 
to center and print in a box. 
"""

py = "Python\nRocks\n!"

def print_box(s):
    if '\n' in s:
        li= s.split("\n")
        longest_word=0
        n=0
        li_strip=[]
        for word in li:
            li_strip.append(word.strip( ))
            
        for word in li_strip:
            len(li_strip[n])
            if len(li_strip[n])>longest_word:
                longest_word=len(li_strip[n])
              

            n+=1
        
        
        if longest_word%2==0:
            t=0
            print('*'*(longest_word+4))
            for word in li_strip:
                x=((longest_word+2)-len(li_strip[t]))//2
                if len(word)%2!=0:
                    print('*'+' '*x+li_strip[t]+' '*(x+1)+'*')
                else:
                    print('*'+' '*x+li_strip[t]+' '*(x)+'*')
                t+=1
            print('*'*(longest_word+4))
            
        else:
            t=0
            print('*'*(longest_word+4))
            for word in li_strip:
                x=((longest_word+2)-len(li_strip[t]))//2
                if len(word)%2!=0:
                    print('*'+' '*x+li_strip[t]+' '*x+'*')
                else:
                    print('*'+' '*x+li_strip[t]+' '*(x+1)+'*')
                t+=1
            print('*'*(longest_word+4))
          
     
    else:
        s=s.strip()
        print('*'*(len(s)+4)+'\n* '+s+' *\n'+'*'*(len(s)+4))
    
user_input=input("Type something and press enter to print (include \\n for new line): ")

if '\\n' in user_input:
    li_multi= user_input.split("\\n")
    multiline_string=""
    p=0
    for word in li_multi:
        if p<len(li_multi)-1:
            multiline_string +=word+"\n"
        elif p==len(li_multi)-1:
            multiline_string +=word
        p+=1
    print_box(multiline_string)
    
else:
    print_box(py)
