import datetime

# --- Logic Section ---
def inverse_initial_permutation(hex_64bit_string):
    """
    Performs the DES Inverse Initial Permutation (IP^-1) on a 64-bit input.
    """
    # IP^-1 Table (1-based indices)
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
    
    # 1. Convert hex to integer
    try:
        val = int(hex_64bit_string, 16)
    except ValueError:
        return "Error"

    # 2. Convert to binary string (64 bits)
    input_bits = bin(val)[2:].zfill(64)

    # 3. Permute
    output_bits_list = []
    for position in IP_INVERSE_TABLE:
        original_index = position - 1
        output_bits_list.append(input_bits[original_index])

    output_bits_str = "".join(output_bits_list)
    output_int = int(output_bits_str, 2)
    
    # 4. Return formatted hex
    return f"0x{output_int:016X}"


def log(message, file_obj=None):
    """Prints to console and appends to file."""
    print(message)
    if file_obj:
        file_obj.write(str(message) + "\n")

def get_valid_half_input(prompt_text, file_obj):
    """
    Asks for one half (Left or Right). 
    Strictly enforces 8 hex digits to match '32-bit' requirement.
    Returns None if error occurs (so we can stop).
    """
    user_input = input(prompt_text).strip()
    
    
    if file_obj:
        file_obj.write(f"{prompt_text} {user_input}\n")

    # Error Messages
    if len(user_input) > 8:
        log("Error input too long", file_obj)
        return None
    
    if len(user_input) < 8:
        log("Error input too short", file_obj)
        return None

    # Invalid Hex Characters Check
    try:
        int(user_input, 16)
    except ValueError:
        log("Error", file_obj)
        return None

    return user_input


if __name__ == "__main__":
 
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    output_filename = "des_output.txt"
    
    with open(output_filename, "w") as f:
        log(f"Run Timestamp: {current_time}", f)
        log("==========================================", f)
        log("Q8: DES Inverse Initial Permutation (IP^-1)", f)
        log("Input: 32-bit L and 32-bit R (hex)", f)
        log("==========================================", f)

        # 2. Get Left Half
        left_input = get_valid_half_input("Enter 32-bit Left  (L) hex (8 digits): ", f)
        
        if left_input is not None:
            log("NEXT", f)
            # 3. Get Right Half ( if Left was valid)
            right_input = get_valid_half_input("Enter 32-bit Right (R) hex (8 digits): ", f)
            
            if right_input is not None:
                log("NEXT", f)
                
                # 4. Combine as R || L (Swap logic for IP^-1)
                combined_hex = right_input + left_input
                
                log("", f)
                log("--- Results ---", f)
                log(f"Combined (R||L)           : 0x{combined_hex.upper()}", f)
                
                # 5. Run Logic
                cipher_text = inverse_initial_permutation(combined_hex)
                log(f"Ciphertext (after IP^-1)  : {cipher_text}", f)
        
        log("------------------------------------------", f)
        log(f"Log saved to {output_filename}", f)
