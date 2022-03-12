from base64 import encode
import sha3

pesan = input("Masukan Pesan: ")
print("Pesan sebelum di hash: ", pesan)
encoded = pesan.encode()
obj_encoded = sha3.keccak_256(encoded)
print("Pesan setelah di hash: ", obj_encoded.hexdigest())

