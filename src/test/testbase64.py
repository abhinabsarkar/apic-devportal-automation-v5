import base64
devorgid = "5d5181bde4b0d60664f78116"
encoded_byte = base64.b64encode(devorgid.encode('utf-8'))
encoded_string = str(encoded_byte, 'utf-8')
print(encoded_string)
