# ==============================================================================
# (Kai)
# Cryptography & Data Security Assignment 2025/2026
# Task 4: DES Encryption Process - Initial Permutation to ready for Fiestel Function
# ==============================================================================
# INPUT:  64 bit plaintext in format of 0x1122334455667788
# OUTPUT: 32 Bits Left (L0), 32 Bits Right (R0), Ready for Fiestel Function
# ==============================================================================
IP_TABLE = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]
# note that IP table is fixed

def hex_to_bin64(hex_input: str) -> str:
# convert hex string to 64-bit binary string
    value = int(hex_input, 16)
    return format(value, '064b')


def initial_permutation(bin64: str) -> str:
# apply DES initial permutation
    return ''.join(bin64[i - 1] for i in IP_TABLE)


def des_ip_split(hex_plaintext: str):
    # run everything and perform 
    # DES Initial Permutation and split into L0 and R0
    # return left and right half, both 32 bits long
    bin64 = hex_to_bin64(hex_plaintext)
    permuted = initial_permutation(bin64)

    L0 = permuted[:32]
    R0 = permuted[32:]

    return L0, R0


# actually running the thing here. plaintext input, 
# permuted 32 bits on teh left and right for output, ready for fiestel function
if __name__ == "__main__":
    plaintext = "0x1122334455667788"
    L0, R0 = des_ip_split(plaintext)

    print("L0 (32 bits):", L0)
    print("R0 (32 bits):", R0)
    
# kind of simple and straight forward, huh?