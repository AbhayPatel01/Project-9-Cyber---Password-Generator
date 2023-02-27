# Idea 2: Using Dataclasses.
    # More Functionality, than idea 1. 
    # UML (used minimally, 5 mins for data class construction)
    # Programming.(OOP/Procedural mix) 
    # Debugging and Testing. (Used pdb, testing done manually.) 

from dataclasses import dataclass, field 
import string 
import secrets
import pdb 

from tkinter import  ttk
from tkinter import  messagebox
from tkinter import  *
import os


@dataclass
class Password():
    length: int 
    alphabet_uppercase: bool = True
    alphabet_lowercase: bool = True  
    punctuation_characters: bool = True 
    digits: bool = True
    as_sentence : bool = False 
    _pwd: str = field(init = False, repr = False )
    
    def __post_init__(self):
        if not any((self.alphabet_uppercase, self.alphabet_lowercase, self.punctuation_characters)): 
            raise ValueError('Must Contain At Least One Of: alphabet lowercase, alphabet uppercase or punctuation characters')

        _semantics = ''
        if self.alphabet_uppercase: 
            _semantics += string.ascii_uppercase 
        if self.alphabet_lowercase: 
            _semantics += string.ascii_lowercase
        if self.punctuation_characters: 
            _semantics += string.punctuation 
        if self.digits: 
            _semantics += string.digits


        out = ''
        if not self.as_sentence:
            for x in range(self.length): 
                out += secrets.choice(_semantics)
        else: 
            for x in range(1,self.length + self.length // 5): 
                if x % 6 == 0: 
                    out += ' '
                else: 
                    out += secrets.choice(_semantics)
            
        self._pwd = out
    
    def get_password(self):
        return self._pwd

spaces = lambda num_spaces,text: num_spaces * ' ' + text + num_spaces * ' '
    
if __name__ == '__main__':  
   
    root = Tk()
    root.title('Simple Password Generator')
     
    root.geometry('400x250')
    mainframe = ttk.Frame(root, padding = (4, 5, 12, 12 ))
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) 
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1, uniform = True)
    root.resizable(0,0)    

    length_label = ttk.Label(mainframe, text=spaces(7,"Length"))
    length_variable = StringVar()
    length_input  = ttk.Entry(mainframe,textvariable=length_variable, width=10)
    
    length_input.configure(justify = 'right')    
    length_input.configure()
     
    uppercase_label = ttk.Label(mainframe, text=spaces(5,"Uppercase"))
    is_uppercase = StringVar() 
    uppercase_yes = ttk.Radiobutton(mainframe, text='Yes', variable=is_uppercase, value=True)
    uppercase_no = ttk.Radiobutton(mainframe, text='No', variable=is_uppercase, value=False)

    punctuation_label = ttk.Label(mainframe, text=spaces(5,"Punctuation"))
    allow_punctuation = StringVar()
    punctuation_yes = ttk.Radiobutton(mainframe, text='Yes', variable=allow_punctuation, value=True)
    punctuation_no = ttk.Radiobutton(mainframe, text='No', variable=allow_punctuation, value=False)

    digit_label = ttk.Label(mainframe, text=spaces(5,"Digits"))
    allow_digits = StringVar()
    digit_yes = ttk.Radiobutton(mainframe, text='Yes', variable=allow_digits, value=True)
    digit_no = ttk.Radiobutton(mainframe, text='No', variable=allow_digits, value=False)
    
    sentence_label = ttk.Label(mainframe, text=spaces(5,"Sentence"))
    allow_sentence = StringVar()
    sentence_yes = ttk.Radiobutton(mainframe, text='Yes', variable=allow_sentence, value=True)
    sentence_no  = ttk.Radiobutton(mainframe, text='No', variable=allow_sentence, value=False)
    
    is_uppercase.set(True)
    allow_digits.set(True) 
    allow_punctuation.set(True) 
    allow_sentence.set(True) 
    
    def gen_password():
        try: 
            _len = int(length_variable.get())  
            if _len == 0: 
                messagebox.showerror(title = 'Error', message="Can't Be Zero!")
                length_variable.set('')
                return
            elif _len < 0: 
                messagebox.showerror(title = 'Error', message="Can't Be Negative!")
                length_variable.set('')
                return
            elif _len >= 1 and _len <= 7: 
                messagebox.showwarning(title='Warning',message= 'Recommended: At least 8 characters.')

        except ValueError: 
            messagebox.showwarning(title = 'Incorrect Input in Length Box', message='Must Be An Integer')
            length_variable.set('')
            return
        # pdb.set_trace() 
        conv = {'1':True, '0':False}
        p1  =  Password(_len, conv[is_uppercase.get()],True, conv[allow_punctuation.get()], conv[allow_digits.get()], conv[allow_sentence.get()]) 
        # Find Secure way, Storage. 
        messagebox.showinfo(title ='Password Generated Based On Specification', message=p1.get_password())
        return       
    
    generate_password_button = ttk.Button(mainframe,text  = 'Generate Password', command = gen_password)
    root.bind('<Return>', lambda e: generate_password_button.invoke())



    length_label.grid(column  = 1, row= 1, sticky = (N,E,S,W))
    length_input.grid(column = 2, row= 1, sticky = E, pady = 5)   

    uppercase_label.grid(column = 1, row =  2)
    uppercase_yes.grid(column = 2, row = 2, sticky = W)
    uppercase_no.grid(column = 3, row = 2, sticky = W, pady = 10)

    punctuation_label.grid(column = 1, row =  3)
    punctuation_yes.grid(column = 2, row = 3, sticky = W)
    punctuation_no.grid(column = 3, row = 3, sticky = W, pady = 10)

    digit_label.grid(column = 1, row =  4)
    digit_yes.grid(column = 2, row =4, sticky = W)
    digit_no.grid(column = 3, row = 4, sticky = W, pady = 10)

    sentence_label.grid(column = 1, row =  5)
    sentence_yes.grid(column = 2, row =5, sticky = W)
    sentence_no.grid(column = 3, row = 5, sticky = W, pady = 10)

    generate_password_button.grid(column = 2,row = 6)
    

    root.mainloop() 

     




