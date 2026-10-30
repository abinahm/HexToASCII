# Hex to ASCII Converter

A small, dependency-free Python script that converts hexadecimal strings into readable ASCII text. It accepts several common hex formats, so you can paste data straight from a debugger, hex dump, packet capture, or shellcode listing without cleaning it up first.

## Features

- Converts hex to text with no external libraries
- Handles multiple input formats automatically (see below)
- Tolerates extra whitespace, newlines, tabs, and commas
- Raises a clear error on odd-length contiguous hex strings

## Supported Input Formats

| Format | Example |
|---|---|
| Contiguous hex | `48656c6c6f` |
| Space-separated | `48 65 6c 6c 6f` |
| `0x`-prefixed | `0x48, 0x65, 0x6c, 0x6c, 0x6f` |
| `\x` escaped | `\x48\x65\x6c\x6c\x6f` |
| Multi-line / tab-separated | Any of the above split across lines or tabs |

All of the examples above decode to `Hello`.

## Usage

1. Open the script and paste your hex data into the `data` variable inside the `if __name__ == '__main__':` block:

   ```python
   if __name__ == '__main__':
       data = """
       48 65 6c 6c 6f 20 57 6f 72 6c 64
       """
       print(hex_to_ascii(data))
   ```

2. Run it:

   ```bash
   python3 Main.py
   ```

3. Output:

   ```
   Hello World
   ```

You can also import the function into your own code:

```python
from hex_to_ascii import hex_to_ascii

print(hex_to_ascii("0x48,0x69"))  # Hi
```

## How It Works

1. **Normalize** – Strips whitespace and replaces `\x`, `0x`, `0X`, commas, newlines, and tabs with spaces.
2. **Split** – Splits the cleaned string into tokens.
3. **Parse** – Two cases:
   - **Multiple tokens:** each token is parsed as its own hex value.
   - **Single token:** the string is split into 2-character pairs (one byte each) and each pair is parsed. An odd-length string raises a `ValueError`.
4. **Decode** – Converts each value to a character with `chr()` and joins them into the final string.

## Notes and Limitations

- **Token size matters.** When the input contains separators, each token is treated as a single character code. For example, `48 65` gives `He`, but `4865` (as one token between spaces) is read as the single code point `0x4865`, not two bytes. For byte-by-byte decoding, use separated two-digit values (`48 65`) or one contiguous string (`4865`) with nothing else in the input.
- **Invalid hex** characters raise a `ValueError` from Python's `int()`.
- **Non-ASCII output:** values above `0x7F` are still converted with `chr()`, so they produce the matching Unicode character rather than raw bytes. This is not a UTF-8 decoder, so multi-byte UTF-8 sequences will not be reassembled.
- **Empty input** returns an empty string.

## Requirements

- Python 3.6+
