"""
You have to implement a string editor that starts from empty string and executes sequence of commands:
    APPEND some_string – appends given string at the end of the text. Print "OK" on success
        .
    INSERT some_string position – inserts given string at given position.
        Print "OK" on success. Print "ERROR" in case of invalid position.
    DELETE start_index count – deletes the specified substring.
        Print "OK" on success. Print "ERROR" in case of invalid substring.
    REPLACE start_index count some_string – replaces the specified substring with the specified string.
        Print "OK" on success. Print "ERROR" in case of invalid substring.
    PRINT –
        prints the string in the editor.
    END – stops the program execution. Passed as last command in the input. Does not print anything.
        .

Ensure your programs runs efficiently for tens of thousands of commands.
"""
from rope import Rope


class StringEditor:
    PRINT_COMMAND = "PRINT"
    APPEND_COMMAND = "APPEND"
    DELETE_COMMAND = "DELETE"
    INSERT_COMMAND = "INSERT"
    REPLACE_COMMAND = "REPLACE"
    AVAILABLE_COMMANDS = [PRINT_COMMAND, APPEND_COMMAND, DELETE_COMMAND, INSERT_COMMAND, REPLACE_COMMAND]

    def __init__(self, value=''):
        self.content = Rope(value)
        self.commands_to_function = {
            self.PRINT_COMMAND: self.print_string,
            self.INSERT_COMMAND: self.insert_string,
            self.DELETE_COMMAND: self.delete_string,
            self.APPEND_COMMAND: self.append_string,
            self.REPLACE_COMMAND: self.replace_string
        }

    def command_controller(self):
        """ Take a command and act on it """
        command = input()
        while not self._validate_command(command):
            print("Command is invalid! Valid commands are:\n\t{}".format('\n\t'.join(self.AVAILABLE_COMMANDS)))
            command = input()
        arguments = command.split()
        command = arguments[0]
        if command == 'END':
            return True
        args = arguments[1:]
        self.commands_to_function[command](args)

    def insert_string(self, *args):
        """ inserts given string at front of the text. Print "OK" as command result. """
        str_to_insert = args[0][0]
        self.content.insert(0, str_to_insert)
        print('OK')

    def append_string(self, *args):
        """ append a given string to the end of the text. Print "OK" as command result. """
        str_to_append = args[0][0]
        self.content.insert(len(self.content), str_to_append)
        print('OK')

    def replace_string(self, *args):
        arguments = args[0]
        start = int(arguments[0])
        count = int(arguments[1])
        string = arguments[2]
        self.content.remove(start, start + count)
        self.content.insert(start, string)
        print('OK')

    def delete_string(self, *args):
        """ deletes the specified substring. Print "OK" as command result in case of success.
        Print "ERROR" in case of invalid substring. """
        try:
            start = int(args[0][0])
            end = start + int(args[0][1])
            self.content.remove(start, end)
            print('OK')
        except:
            print('ERROR')

    def print_string(self, *args):
        print(self.content)

    def _validate_command(self, command: str) -> bool:
        """ return a boolean indicating if the command is valid """
        for valid_command in self.AVAILABLE_COMMANDS:
            if command.startswith(valid_command):
                return True

        return False


def main():
    str_editor = StringEditor()
    to_stop = False
    while not to_stop:
        to_stop = str_editor.command_controller()

if __name__ == '__main__':
    main()