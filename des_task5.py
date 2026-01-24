# ==============================================================================
# (Nafis Aiman Bin Razalee)
# Cryptography & Data Security Assignment 2025/2026
# Task 5: DES Encryption - DES Expansion + XOR with Key
# ==============================================================================
# INPUT:  48 Bits Round Key, 32 Bits Right (R0)
# OUTPUT: 48 Bits to S-Box
# ==============================================================================

# DES Expansion Table (E-table)
E_TABLE = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# Convert hex string to binary string
def hex_to_bin(hex_str, bits):
    return bin(int(hex_str, 16))[2:].zfill(bits)

# Convert binary string to hex string
def bin_to_hex(bin_str):
    return hex(int(bin_str, 2))[2:].upper().zfill(len(bin_str) // 4)

# Perform DES Expansion (32 bits -> 48 bits)
def des_expansion(right_32bits):
    expanded = ""
    for position in E_TABLE:
        expanded += right_32bits[position - 1]
    return expanded

# XOR two binary strings
def xor_bits(a, b):
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))

# Main program
def main():
    print("DES Question 5: Expansion + XOR\n")

    # Input
    round_key_hex = input("Enter 48-bit Round Key (hex, e.g. 0x112233445566): ")
    right_half_hex = input("Enter 32-bit Right Half (hex, e.g. 0x80668066): ")

    # Convert inputs to binary
    round_key_bin = hex_to_bin(round_key_hex, 48)
    right_half_bin = hex_to_bin(right_half_hex, 32)

    # DES Expansion
    expanded_right = des_expansion(right_half_bin)

    # XOR with round key
    xor_result = xor_bits(expanded_right, round_key_bin)

    # Output
    output_hex = bin_to_hex(xor_result)

    output_text = (
        "--------------------------------------------------\n"
        "DES Question 5: Expansion + XOR\n"
        f"Round Key (48-bit): {round_key_hex}\n"
        f"Right Half (32-bit): {right_half_hex}\n"
        f"48-bit Output to S-Box (Task 6): 0x{output_hex}\n"
        "--------------------------------------------------\n"
        "Ready for Task 6 input.\n"
    )

    # Print to terminal
    print("\n" + output_text)

    # Write to text file
    with open("task5_output.txt", "w") as file:
        file.write(output_text)

    print("Output successfully saved to task5_output.txt")

if __name__ == "__main__":
    main()

