import pyAesCrypt
from os import stat, remove
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "foopassword"


# encrypt
with open("raspberry.tar.gz", "rb") as fIn:
    with open("raspberry.aes", "wb") as fOut:
        pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)

# get encrypted file size
encFileSize = stat("raspberry.aes").st_size

# decrypt
with open("raspberry.aes", "rb") as fIn:
    try:
        with open("raspberry_out.tar.gz", "wb") as fOut:
            # decrypt file stream
            pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
    except ValueError:
        # remove output file on error
        remove("dataout.txt")
