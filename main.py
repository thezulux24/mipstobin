import streamlit as st
from cryptography.fernet import Fernet
import base64


# Clave de cifrado proporcionada
clave_original = st.secrets["KEY"]
clave = base64.urlsafe_b64encode(clave_original.ljust(32)[:32].encode())

cipher_suite = Fernet(clave)

try:
    # Leer el contenido del archivo main_encrypted.py
    with open('main_encrypted.py', 'rb') as file:
        encrypted_data = file.read()

    # Desencriptar el contenido del archivo
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    # Guardar el contenido desencriptado temporalmente
    with open('main_decrypted_temp.py', 'wb') as file:
        file.write(decrypted_data)

    # Importar el contenido desencriptado
    import main_decrypted_temp as main_decrypted

except Exception as e:
    st.error(f"Error al desencriptar o importar el archivo: {e}")
    st.stop()

# Streamlit interface
st.title("MIPS a Binario Traductor")
codigo_mips = st.text_area("Ingrese el código MIPS aquí:", height=300)
if st.button("Traducir"):
    try:
        codigo_binario = main_decrypted.traducir_mips_a_binario(codigo_mips)
        st.text_area("Código Binario:", value=codigo_binario, height=300)
    except AttributeError as e:
        st.error(f"Error al traducir el código MIPS: {e}")