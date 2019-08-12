# Import module
import base64

# Convert to base64 encoded string
def to_base64_string(guid):
    # Convert to base64 encoded byte
    encoded_byte = base64.b64encode(guid.encode('utf-8'))
    # Convert to base64 encoded string
    encoded_string = str(encoded_byte, 'utf-8')
    return encoded_string
