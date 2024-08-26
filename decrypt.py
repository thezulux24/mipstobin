from cryptography.fernet import Fernet
import base64

# Clave de cifrado proporcionada
clave_original = 'ashFA433FW#21='
clave = base64.urlsafe_b64encode(clave_original.ljust(32)[:32].encode())

cipher_suite = Fernet(clave)

# Leer el contenido del archivo main_encrypted.py
with open('main_encrypted.py', 'rb') as file:
    encrypted_data = file.read()

# Desencriptar el contenido del archivo
decrypted_data = cipher_suite.decrypt(encrypted_data)

# Guardar el contenido desencriptado en un nuevo archivo
with open('main_decrypted.py', 'wb') as file:
    file.write(decrypted_data)

print('Archivo desencriptado y guardado como main_decrypted.py')