#!/usr/bin/python3
"""
    HBNBCommand class for the console
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
        console.py that contains the entry point 
        of the command interpreter
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """
            quit: command to exit the program
        """
        
        return True

    def do_EOF(self, line):
        """
            function to handle EOF
        """
       
        print()
        return True

    def emptyline(self):
        """
            function to handle enter when empty line
        """
       
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
