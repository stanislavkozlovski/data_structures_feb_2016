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