# Fix_File.py
This code will change the magic bytes of your file to 50 4b 03 04.

README

This Python script, bless.py, allows the user to edit individual bytes of a binary file in a terminal interface. The user can input an address to edit and a new hexadecimal value for the byte at that address. The script also displays the data in a hexdump format, showing the hexadecimal and ASCII representation of the data.
Usage

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

To use this script, run the following command in a terminal:

python bless.py <file_path>

where <file_path> is the path to the binary file you want to edit.

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

OBS: The code has a section called : new_header = b'\x50\x4b\x03\x04', which will change your first bytes for: \x50\x4b\x03\x04.
You can ignore the commands and change manually in the code the first bytes. 


\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
After running the command, the script will display the data in hexdump format and prompt the user to input an address to edit. The user can then input a new hexadecimal value for the byte at that address. The hexdump will be updated to reflect the changes made. The user can continue editing bytes until they enter "q" to quit the program. The modified data will be written back to the original file.
Functions

The script contains the following functions:

    read_hex_string(hex_string): Converts a hexadecimal string to bytes.
    format_hex_byte(byte): Formats a byte as a hexadecimal string.
    format_ascii_byte(byte): Formats a byte as an ASCII character, replacing non-printable characters with periods.
    hexdump(data, address=0, bytes_per_line=16): Displays the data in hexdump format.
    edit_byte(data, address, new_value): Edits a byte in the data.

The main function, main(), reads in the file specified in the command line argument and uses the other functions to allow the user to edit individual bytes.
