'''
Objective: Brute-force algorithm to find all occurrences of a pattern in a given text using slicing.


Author: Sarju S
Date: 28-10-2024
'''

def brute_force_string_matching(text, pattern):
    """
    Parameters:
    text (str): The string to search within.
    pattern (str): The string to search for.

    Returns:
    Nothing
    """
    # Get lengths of the text and pattern
    text_length = len(text)
    pattern_length = len(pattern)

    # Traverse the text from 0 to text_length - pattern_length
    for i in range(text_length - pattern_length + 1):
        # Use slicing to extract the substring and compare it with the pattern
        if text[i:i + pattern_length] == pattern:
            print(f"Pattern found at index {i}")  # Pattern found, print the index

# Example Usage
text = "ABABABCABABABCAB"
pattern = "ABABC"
brute_force_string_matching(text, pattern)

