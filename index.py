#XOR untuk enkripsi
def encrypt(teks, kunci):
  ciphertext = ""
  for i in range(len(teks)):
    ciphertext += chr(ord(teks[i]) ^ ord(kunci[i % len(kunci)]))
  return ciphertext

#XOR untuk deskripsi
def decrypt(ciphertext, kunci):
  teks = ""
  for i in range(len(ciphertext)):
    teks += chr(ord(ciphertext[i]) ^ ord(kunci[i % len(kunci)]))
  return teks

# Trial enkripsi dan deskripsi
teks = "Sebuah Pesan dari Dimas"
kunci = "12345"

print("--Mini Apps Kripto--")
print("Plaintext : ", teks)
ciphertext = encrypt(teks, kunci)
print("Teks Enkripsi :", ciphertext)
decrypted = decrypt(ciphertext, kunci)
print("Teks Dekripsi :", decrypted)