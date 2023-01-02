from tkinter import *
 
window = Tk()
window.title("Apps Kriptografi")
window.geometry('350x300')

plaintext = "Sebuah pesan dari Dimas"
key = "12345"

judul1 = Label(window, text="Teks : ",anchor="e",width=20)
judul1.grid(column=0, row=0)
lText = Label(window, text= plaintext ,anchor="w",width=20)
lText.grid(column=1, row=0)

judul2 = Label(window, text="Kunci : ",anchor="e",width=20)
judul2.grid(column=0, row=1)
lKunci = Label(window, text=key ,anchor="w",width=20)
lKunci.grid(column=1, row=1)

judul3 = Label(window, text="Plaintext : ",anchor="e",width=20)
judul3.grid(column=0, row=2)
lPlaintext = Label(window, text="o",anchor="w",width=20)
lPlaintext.grid(column=1, row=2)

judul4 = Label(window, text="Cyphertext : ",anchor="e",width=20)
judul4.grid(column=0, row=3)
lCyphertext = Label(window, text="o",anchor="w",width=20)
lCyphertext.grid(column=1, row=3)

# Menggunakan XOR untuk enkripsi
def encrypt(plaintext, key):
  ciphertext = ""
  for i in range(len(plaintext)):
    ciphertext += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
  return ciphertext

# Menggunakan XOR untuk deskripsi
def decrypt(ciphertext, key):
  plaintext = ""
  for i in range(len(ciphertext)):
    plaintext += chr(ord(ciphertext[i]) ^ ord(key[i % len(key)]))
  return plaintext


ciphertext = encrypt(plaintext, key)
decrypted = decrypt(ciphertext, key)

def work():    
    lCyphertext.configure(ciphertext)
    lPlaintext.configure(decrypted)

btn = Button(window, text="Generate", command=work)
btn.grid(column=1, row=4)

window.mainloop()
