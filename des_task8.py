def inverse_initial_permutation(input_hex_string):
    """
    Performs the DES Inverse Initial Permutation (IP^-1) on a 64-bit input.
    
    Args:
        input_hex_string (str): A 64-bit hex string (e.g., "0x0000000000000000")
                                Representing the combined 32-bit Left and Right halves.
    
    Returns:
        str: The final 64-bit Ciphertext in hex format.
    """
    
    IP_INVERSE_TABLE = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]

    # Convert hex string to an integer
    try:
        val = int(input_hex_string, 16)
    except ValueError:
        return "Error: Invalid Hex Input"

    # Convert integer to a binary string of exactly 64 bits.
    input_bits = bin(val)[2:].zfill(64)

    # Ensure we only have 64 bits and handles overflow (in case it happens)
    if len(input_bits) > 64:
        print("Warning: Input was larger than 64 bits. Truncating to last 64.")
        input_bits = input_bits[-64:]

    # Build the output string bit by bit based on the table.
    output_bits_list = []
    
    for position in IP_INVERSE_TABLE:
        original_index = position - 1
        output_bits_list.append(input_bits[original_index])

    # combines list of bits into string
    output_bits_str = "".join(output_bits_list)

    #output formation
    output_int = int(output_bits_str, 2)
    
    # Format as hex, uppercase, with 0x prefix, padded to 16 hex chars (64 bits)
    # The '016X' format specifier handles the padding and uppercase.
    output_hex = f"0x{output_int:016X}"

    return output_hex

# User view
if __name__ == "__main__":
    print("DES Task 8: Inverse Initial Permutation")

    test_input = "0x0000000000000000" 
    
    print(f"Input  (Hex): {test_input}")
    
    # Run the function
    cipher_text = inverse_initial_permutation(test_input)
    
    print(f"Output (Hex): {cipher_text}")
    print("-----------------------------------------------")

def run_tests():
    print("Running Verification Tests...")
    
    # Define our test cases: (Input, Expected Output)
    test_cases = [
        ("0x00000000FFFFFFFF", "0xAAAAAAAAAAAAAAAA"),
        ("0xFFFFFFFF00000000", "0x5555555555555555")
    ]
    
    all_passed = True
    
    for input_val, expected in test_cases:
        result = inverse_initial_permutation(input_val)
        
        # validating match
        if result == expected:
            print(f"[PASS] Input: {input_val} -> Output: {result}")
        else:
            print(f"[FAIL] Input: {input_val}")
            print(f"       Expected: {expected}")
            print(f"       Got:      {result}")
            all_passed = False
            
    if all_passed:
        print("\nSUCCESS: All logic checks passed! Your code is ready.")
    else:
        print("\nWARNING: Some tests failed. Check your IP_INVERSE_TABLE values.")

# Run the tests
if __name__ == "__main__":
    run_tests()