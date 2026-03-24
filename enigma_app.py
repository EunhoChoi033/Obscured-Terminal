# enigma_app.py



from enigma import Enigma
import tkinter



_DEFAULT_FONT = ('Helvetica', 11)
_DEFAULT_BOLD_FONT = ('Helvetica', 12, 'bold')



class EnigmaApp:
    def __init__(self):
        self._enigma = Enigma()
        
        self._root_window = tkinter.Tk()
        self._root_window.geometry('800x500')
        self._root_window.title('Obscured M1')  
        self._root_window.configure(padx = 30, pady = 30)

        self._message_label = tkinter.Label(self._root_window, text = 'Message:', font = _DEFAULT_BOLD_FONT, anchor = 'w')
        self._message_label.pack(fill = 'x', pady = (0, 5))

        self._message_box = tkinter.Text(self._root_window, height = 4, font = _DEFAULT_FONT, highlightthickness = 2, highlightbackground = 'black', highlightcolor = 'black')
        self._message_box.pack(fill = 'x', pady = (0, 40))
        
        self._encrypt_button = tkinter.Button(self._root_window, text = 'Encrypt', font = _DEFAULT_BOLD_FONT, cursor = 'hand2', command = lambda: [self._get_input_message(), self._set_enigma_output()])
        self._encrypt_button.pack(pady=(0, 20))

        self._output_label = tkinter.Label(self._root_window, text = 'Output:', font = _DEFAULT_BOLD_FONT, anchor = 'w')
        self._output_label.pack(fill = 'x', pady = (0, 5))

        self._output_box = tkinter.Label(self._root_window, height = 4, font = _DEFAULT_FONT, highlightthickness = 2, highlightbackground = 'black', highlightcolor = 'black', text = '', fg='black')
        self._output_box.pack(fill = 'x', pady = (0, 20))

        self._copy_button = tkinter.Button(self._root_window, text = 'Copy to Clipboard', font = _DEFAULT_BOLD_FONT, cursor = 'hand2', command = self._copy_output_to_clipboard)
        self._copy_button.pack(pady = 10)
        
        self._reset_button = tkinter.Button(self._root_window, text = 'Reset', font = _DEFAULT_BOLD_FONT, cursor = 'hand2', command = self._reset)
        self._reset_button.pack(pady = 10, anchor = tkinter.E)
    
    
    def run(self):
        '''Executes the GUI'''
        self._root_window.mainloop()


    def _get_input_message(self):
        '''Provides the enigma with the message'''
        self._enigma.set_message(self._message_box.get('1.0', 'end-1c'))
        
        
    def _set_enigma_output(self):
        '''Gets the output given from the Enigma'''
        self._output_box.config(text = ''.join(self._enigma.process_message()))
    
    
    def _present_output(self, output: str) -> None:
        '''If the Enigma produces an output, then display that output into the output box'''
        self._output_box.config(text = output)
        
        
    def _copy_output_to_clipboard(self) -> None:
        '''Copies the Enigma\'s result to the user\'s clipboard'''
        self._root_window.clipboard_append(self._output_box.cget('text'))
        
    
    def _reset(self) -> None:
        '''Resets the Enigma'''
        self._message_box.delete("1.0", tkinter.END)
        self._output_box.config(text = '')
        self._enigma = Enigma()
    
    
    
if __name__ == '__main__':
    able = EnigmaApp()
    able.run()