# Import module
import base64

# Convert to base64 encoded string
def to_base64_string(input_string):
    # Convert to base64 encoded byte
    encoded_byte = base64.b64encode(input_string.encode('utf-8'))
    # Convert to base64 encoded string
    encoded_string = str(encoded_byte, 'utf-8')
    return encoded_string

# Decode base64 encoded string
def decode_base64_string(encoded_string):
    # Convert base64 encoding to byte
    encoded_byte = base64.b64decode(encoded_string)
    return encoded_byte
