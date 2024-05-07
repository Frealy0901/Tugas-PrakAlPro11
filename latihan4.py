file = input("Masukan nama file : ") # meminta input file pengguna 
handle = open(file) # membuka file yang sudah dimasukan
dicto = dict() # membuat dictionary

for baris in handle: # untuk barisan di handle
    if baris.startswith("From "): # jika baris dimulai dari from
        kat = baris.split() # di split perbaris
        email = kat[1]

        smbol = email.find('@') # menemukan simbol @
        domain= email[smbol + 1:] 

        dicto[domain] = dicto.get(domain, 0) + 1

print(dict) # memunculkan dictionarynya
handle.close() # menutup file