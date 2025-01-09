#!/usr/bin/python3
"""AirBnB Command Interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB objects"""
    prompt = "(hbnb) "

    def do_quit(self, _):
        """
        Quit command to exit the program.
        
        Usage: quit
        """
        return True

    def do_eof(self, _):
        """
        EOF command to exit the program (e.g., Ctrl+D).
        
        Usage: EOF or press Ctrl+D
        """
        print()  # Print a newline for clean exit
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        
        Overrides the default behavior to prevent repeating the last command.
        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
