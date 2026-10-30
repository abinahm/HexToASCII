def hex_to_ascii(hex_string):
    s = hex_string.strip()

    s = s.replace('\\x', ' ').replace('0x', ' ').replace('0X', ' ')
    s = s.replace(',', ' ').replace('\n', ' ').replace('\t', ' ')

    parts = s.split()

    if len(parts) > 1:      
        codepoints = [int(p, 16) for p in parts if p]
    else:      
        token = parts[0] if parts else ''
        if len(token) % 2 != 0:
            raise ValueError(f"Odd-length hex string: {token!r}")
        codepoints = [int(token[i:i+2], 16) for i in range(0, len(token), 2)]

    return ''.join(chr(c) for c in codepoints)


if __name__ == '__main__':   
    data = 
    """
    
    """
    print(hex_to_ascii(data))