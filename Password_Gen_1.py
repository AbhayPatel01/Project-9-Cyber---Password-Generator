# Mini Program 
# Idea 1: Typical, style function, 'No Thinking'/UML/design/Algo + DS/Tradeoffs/Efficienctly. 

import secrets  
import string

semantics = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

def generate_password(length:int,sentence:bool) -> None: 
    '''Generates a Password of legth as a single sentence or a word.''' 
    quotient, rem = divmod(length,5)  # 5: as common word length ~ depends/based on text type, etc..  
   
    if sentence: 
        out = '' 
        for x in range(quotient):
            for x in range(5): 
                out += secrets.choice(semantics)
            out += ' '
        for x in range(rem): 
            out += secrets.choice(semantics)
        print(out)
            
    else:
        print(''.join([secrets.choice(semantics) for x in range(length)]))

def gen_password_idea_1(): 
    try:   
        print('--- Password Generator ---') 
        length = input('Enter Password Length (int): ') 
        sentence = input('Enter \'y\'/\'n\' for Sentence (char strictly): ') 
        length = int(length)  
        if sentence.lower() == 'y': 
            generate_password(length,True)
        elif sentence.lower() == 'n':
            generate_password(length, False)
        else: 
            raise ValueError
    except ValueError: 
        print("Ensure input is valid:\n-Length Should be an Integer\n-Character Should: 'y' or 'n' ") 
        return        
    except: 
        print('Some Error Occured!')
        return 

    print('Password Generated Exiting.') 


if __name__ == '__main__': 
    gen_password_idea_1()














