file = input("Masukan nama file : ") # meminta input file dari pengguna
handle = open(file) # membuka file
dicto = dict() 

for barisan in handle: # untuk barisan di handle
    if barisan.startswith("From "): # jika barisan dimulai dari from
        kat = barisan.split() # split setiap barisam
        email = kat[1] 

        dicto[email] = dicto.get(email, 0) + 1
    
print(dicto) # memunculkan variabel untuk dictionery
handle.close() # menutup 