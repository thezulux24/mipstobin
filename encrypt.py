from cryptography.fernet import Fernet
import base64

# Clave de cifrado proporcionada
clave_original = 0
clave = base64.urlsafe_b64encode(clave_original.ljust(32)[:32].encode())

cipher_suite = Fernet(clave)

# Leer el contenido del archivo main.py
with open('main.py', 'rb') as file:
    file_data = file.read()

# Encriptar el contenido del archivo
encrypted_data = cipher_suite.encrypt(file_data)

# Guardar el contenido encriptado en un nuevo archivo
with open('main_encrypted.py', 'wb') as file:
    file.write(encrypted_data)

print('Archivo encriptado y guardado como main_encrypted.py')