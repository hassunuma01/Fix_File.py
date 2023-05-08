import sys

def read_hex_string(hex_string):
    """
    Converte uma string hexadecimal em bytes.
    """
    hex_string = hex_string.replace(" ", "")  # Remove espaços em branco
    if len(hex_string) % 2 != 0:  # Certifica-se que a string tem um número par de caracteres
        hex_string = "0" + hex_string
    return bytes.fromhex(hex_string)

def format_hex_byte(byte):
    """
    Formata um byte como uma string hexadecimal.
    """
    return "{:02x}".format(byte)

def format_ascii_byte(byte):
    """
    Formata um byte como um caractere ASCII, substituindo caracteres não-imprimíveis por pontos.
    """
    if byte >= 32 and byte <= 126:  # Caractere imprimível
        return chr(byte)
    else:  # Caractere não-imprimível
        return "."

def hexdump(data, address=0, bytes_per_line=16):
    """
    Exibe os dados em formato hexadecimal e ASCII.
    """
    for i in range(0, len(data), bytes_per_line):
        chunk = data[i:i+bytes_per_line]
        hex_line = " ".join([format_hex_byte(b) for b in chunk])
        ascii_line = "".join([format_ascii_byte(b) for b in chunk])
        print("{:08x}  {:48}  {}".format(address+i, hex_line, ascii_line))

def edit_byte(data, address, new_value):
    """
    Edita um byte no dado.
    """
    new_data = data[:address] + bytes([new_value]) + data[address+1:]
    return new_data

def main():
    if len(sys.argv) != 2:
        print("Uso: python bless.py arquivo.bin")
        return

    file_path = sys.argv[1]

    with open(file_path, "rb") as f:
        data = f.read()

    # Substitui os primeiros 4 bytes pela sequência 01 02 03 04
    new_header = b'\x50\x4b\x03\x04'
    data = new_header + data[4:]

    while True:
        print("Endereço\tHexadecimal\tASCII")
        hexdump(data)

        user_input = input("Digite o endereço para editar (ou 'q' para sair): ")
        if user_input == "q":
            break

        try:
            address = int(user_input, 16)
            if address < 0 or address >= len(data):
                raise ValueError()
        except ValueError:
            print("Endereço inválido.")
            continue

        user_input = input("Digite o novo valor em hexadecimal: ")
        try:
            new_value = int(user_input, 16)
            if new_value < 0 or new_value > 255:
                raise ValueError()
        except ValueError:
            print("Valor inválido.")
            continue

        data = edit_byte(data, address, new_value)

    with open(file_path, "wb") as f:
        f.write(data)

if __name__ == "__main__":
    main()
