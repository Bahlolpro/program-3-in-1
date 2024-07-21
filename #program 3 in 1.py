#program 3 in 1
#program ini walau 3 tapi beranak ya ges :v

import requests


def convert_currency(amount, to_currency, from_currency):
    # API url
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    # Make request
    response = requests.get(url)
    data = response.json()

    # Extract conversion rate
    exchange_rate = data['rates'].get(to_currency)  # Use .get() in case the key doesn't exist

    # Calculate converted amount
    converted_amount = amount * exchange_rate

    return converted_amount

def curbaliik():
    print ("---- jeda program ----")
    print (" ingin mengkonfersi mata uang lain??")
    print ("1. iya ")
    print ("2. tidak")
    curlagi = int(input("pilih opsi 1/2 = "))
    if curlagi == 1:
        cur()
    if curlagi == 2:
        konvbalik()
    else:
        novalid()


def cur():
    clearScreen()
    print ("---program mengkonversi mata uang----")
    print (" SEMUA MATA UANG TERSEDIA  (list dibawah hanya mempermudah)")
    print (" 1. USD (dolar amerika)")
    print (" 2. EUR (euro)")
    print (" 3. IDR (rupiah indonesia)")
    print (" 4. SAR (riyal saudi arabia)") 
    print (" 5. GBP (pound ingris )") 
    print (" 6. JPY (yen jepang)") 
    print (" 7. CNY (yuan cina)") 
    print (" 8. SGD (dolar singapura)") 
    print (" 9. EGP (pound mesir)") 
    print (" 10. KRW (won korea selatan)")
    print (" jika memang mengetahui code mata uang negara lain dipersilahkan")   
    print ("-------------------------------------------------------------------")
    amount = float(input("masukan besaran uang = "))
    from_currency = input("masukan nama mata uang pertama = ")
    to_currency = input("masukan nama mata uang ke dua = ")
    converted_amount = convert_currency(amount, to_currency, from_currency)
    print(f"{amount} {from_currency} sama dengan {converted_amount} {to_currency}")
    curbaliik()



import os 
def clearScreen() : # def ini fungsi 
    os.system('cls') #windows


#fungsi dlu
def awalmasuk():
    clearScreen()
    print ("-------- selamat datang --------")
    print ("pilih program yang ingin kamu pakai")
    print ("1. kalkulator sederhana")
    print ("2. menghitung luass ")
    print ("3.  konversi satuan")
    print ("4. tutup prgram")
    
def balikmasuk():
    awalmasuk()
    
    
def close():
    clearScreen()
    print ("-------- terima kasih --------")
    print ("terimakasih sudah mencoba program yang saya buat")
    print ("semoga program ini dapat bermanfaat")

def novalid():
    clearScreen()
    print ("-------- program tertutup --------")
    print ("mohon maaf program ini terpaksa tertutup karena input yanng tidak valid")
    print ("mohon masukan input yang sesuai dengan opsi yanng ada")
    print ("-------- terima kasih --------")
    print ("ingin mengulang progfram ? y/n")
    mau = 'y'
    mau = input (" pilih y/n : ")
    if mau == 'y':
        jalan()
    else:
        close()

def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

def kalkulator():
    print("Select operation.")
    print("1.tambah")
    print("2.kurang")
    print("3.kali")
    print("4.bagi")
    print("5.kembali")

    
def kalkubalik():
    print ("apakah anda ingin kembali?")
    print ("1. operasi lain")
    print ("2. kembali ")
    balikkalku = int(input("pillih opsi : "))
    if balikkalku == 1:
        kalkulagi()
    elif balikkalku == 2:
        jalan()
    else: 
        novalid()
     
def kalkulagi():
    clearScreen()
    kalkulator()
    choice = input("pilih opsi  (1/2/3/4/5): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("masukan angka pertama: "))
            num2 = float(input("masukan angka ke dua: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            kalkubalik()

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            kalkubalik()

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            kalkubalik()


        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            kalkubalik()
            
    elif choice == '5':
            kalkubalik()
        
    else:
            novalid()   
            
            
# fungsi luas 

def HitungLuas():
   clearScreen()


def Display_menuLuas():
    clearScreen()
    print ("---program menghitung luas----")
    print ("1. persegi ")
    print ("2. segitiga")
    print ("3. persegi panjang")
    print ("4. lingkaran")
    print ("5. tutup")



def ulang():
    Display_menuLuas()
    menu = int (input ("pilih nomor menu :  "))
    if menu == 1:
         persegi()
    elif menu == 2: 
         segitiga()
    elif menu == 3: 
          persegiPanjang()
    elif menu == 4: 
           lingkaran()
    elif menu == 5: 
           balikmasuk()
    else :
         novalid()

def balik():
    print ("apakah anda ingin kembali?")
    print ("1. operasi lain")
    print ("2. kembali")
    jawab = int(input("pilih menu :  "))
    if jawab == 1:
        ulang()
    elif jawab == 2:
        jalan()
    else:
        novalid()
    

def persegi():
    clearScreen()
    print ("----- luas persegi ------")
    
    sisi = int(input("masukan panjang sisi :"))
    
    luas = sisi * sisi 
    print ("luasnya adalah : ", luas)
    print ("")
    
    balik()

def segitiga():
    clearScreen()
    print ("----- luas segitiga ------")
    
    sisi = int(input("masukan panjang sisi :"))
    
    luas = sisi * sisi * sisi
    print ("luasnya adalah : ", luas)
    
    balik()
    
def persegiPanjang():
    clearScreen()
    print ("----- luas persegi panjang ------")
    
    panjang = int(input("masukan panjang  : "))
    lebar = int(input("masukan lebar  : "))

    
    luas = panjang * lebar 
    print ("luasnya adalah : ", luas)
    
    balik()
    
def lingkaran():
    clearScreen()
    print ("----- luas lingkaran  ------")
    
    jariJari = int(input("masukan jari jari lingkaran :"))
    
    luas =  3.14 * jariJari * jariJari 
    print ("luasnya adalah : ", luas)
    
    balik()

def ulanglagi():
    Display_menuLuas()
    menu = int (input ("pilih nomor menu : "))
    if menu == 1:
         persegi()
    elif menu == 2: 
         segitiga()
    elif menu == 3: 
          persegiPanjang()
    elif menu == 4: 
           lingkaran()
    elif menu == 5: 
           jalan()
    else :
          novalid()

def jalan():
    balikmasuk()
    pilihProgram = int (input(" masukan nomor menu yang ingin dipakai :  "))
    if pilihProgram == 1:
        kalkulagi()
    elif pilihProgram == 2:
        ulanglagi()
    elif pilihProgram == 3:
        konvulang()
    elif pilihProgram == 4:
        close()
    else:
       novalid()
       
# fungsi konversi

def konvsatuan():
    clearScreen()
    print ("---program mengkonversi satuan----")
    print ("1. panjang ")
    print ("2. berat ")
    print ("3. suhu")
    print ("4. kurs mata uang")
    print ("5. tutup")
    
def konvulang():
    konvsatuan()
    menukonv = int (input ("pilih nomor menu :  "))
    if menukonv == 1:
         panjang()
    elif menukonv == 2: 
         berat()
    elif menukonv == 3: 
          konvsuhu()
    elif menukonv == 4: 
           cur()
    elif menukonv == 5:
           jalan()
    else :
         novalid()
    
def konvbalik():
    print ("apakah anda ingin kembali?")
    print ("1. operasi lain")
    print ("2. kembali ")
    konvbalik = int(input("pillih opsi : "))
    if konvbalik == 1:
        konvulang()
    elif konvbalik == 2:
        jalan()
    else: 
        novalid()

def konvngarang():
    clearScreen()
    print ("-------- program tertutup --------")
    print ("mohon maaf program ini terpaksa tertutup karena input yang tidak valid/tersedia")
    print ("mohon masukan input yang sesuai dengan yang ada")
    print ("-------- terima kasih --------")
    print ("ingin mengulang progfram ? y/n")
    mau = 'y'
    mau = input (" pilih y/n : ")
    if mau == 'y':
        konvbalik()
    else:
        close()

#konv panjang

def panjang():
    clearScreen()
    print ("---program mengkonversi panjang----")
    print (" satuan yg tersedia")
    print (" 1. cm")
    print (" 2. m")
    print (" 3. mm")
    print (" 4. km")
    numA = input("masukan satuan awal = ")
    numB = input("masukan satuan tujuan = ")
    value = int (input("masukan besaran satuan =  "))
    if numA == "cm" and numB == "m":
        print ( value, numA, "=",float(value)/100,numB )
        print("----------------------------------")
        konvbalik()
        
    elif numA == "m" and numB == "cm":     
        print (value, numA, "=",float(value)*100,numB)
        print("----------------------------------")
        konvbalik()
       
    elif numA == "mm" and numB == "cm":     
        print (value, numA, "=",float(value)/10,numB)
        print("----------------------------------")
        konvbalik()


    elif numA == "cm" and numB == "mm":     
        print (value, numA, "=",float(value)*10,numB  )
        print("----------------------------------")
        konvbalik()

    elif numA == "mm" and numB == "m":     
        print (value, numA, "=",float(value)/1000,numB)
        print("----------------------------------")
        konvbalik()

    elif numA == "m" and numB == "mm":     
        print (value, numA, "=",float(value)*1000,numB)
        print("----------------------------------")
        konvbalik()

    elif numA == "km" and numB == "m":     
        print (value, numA, "=",float(value)/100,numB)
        print("----------------------------------")
        konvbalik()

    elif numA == "m" and numB == "km":     
        print (value, numA, "=",float(value)/1000,numB)
        print("----------------------------------")
        konvbalik()

    elif numA == "mm" and numB == "km":     
        print (value, numA, "=",float(value)/1000000,numB)
        print("----------------------------------")
        konvbalik()
        
    elif numA == "km" and numB == "mm":     
        print (value, numA, "=",float(value)*1000000,numB)
        print("----------------------------------")
        konvbalik()

    elif numA == "km" and numB == "cm":     
        print (value, numA, "=",float(value)*100000,numB)
        print("----------------------------------")
        konvbalik()  
              
    elif numA == "cm" and numB == "km":     
        print (value, numA, "=",float(value)*1000000,numB)
        print("----------------------------------")
        konvbalik()   
        
    else:
        konvngarang()
  
# konv berat 
     
def berat():
    clearScreen()
    print ("---program mengkonversi berat----")
    print (" satuan yg tersedia")
    print (" 1. kg")
    print (" 2. g")
    print (" 3. lb(pound)")
    print (" 4. oz(ons)")
    numA = input("masukan satuan awal = ")
    numB = input("masukan satuan tujuan = ")
    value = int (input("masukan besaran massa =  "))
    if numA == "g" and numB == "kg":
        print ( value, numA, "=",float(value)/1000,numB )
        print("----------------------------------")
        konvbalik()
        
    elif numA == "kg" and numB == "g":     
        print (value, numA, "=",float(value)*1000,numB)
        print("----------------------------------")
        konvbalik()
       
    elif numA == "lb" and numB == "kg":     
        print (value, numA, "=",float(value)*0.453592,numB)
        print("----------------------------------")
        konvbalik()


    elif numA == "kg" and numB == "lb":     
        print (value, numA, "=",float(value)/0.453592,numB  )
        print("----------------------------------")
        konvbalik()

    elif numA == "oz" and numB == "g":     
        print (value, numA, "=",float(value)*28.3495,numB)
        print("----------------------------------")
        konvbalik()

    elif numA == "g" and numB == "0z":     
        print (value, numA, "=",float(value)/28.3495,numB)
        print("----------------------------------")
        konvbalik()

    elif numA == "g" and numB == "lb":     
        print (value, numA, "=",float(value)/453.6,numB)
        print("----------------------------------")
        konvbalik()

    elif numA == "lb" and numB == "g":     
        print (value, numA, "=",float(value)*453.6,numB)
        print("----------------------------------")
        konvbalik()

    elif numA == "0z" and numB == "kg":     
        print (value, numA, "=",float(value)/35.274,numB)
        print("----------------------------------")
        konvbalik()
        
    elif numA == "kg" and numB == "0z":     
        print (value, numA, "=",float(value)*35.274,numB)
        print("----------------------------------")
        konvbalik()
        
    elif numA == "lb" and numB == "0z":     
        print (value, numA, "=",float(value)*16,numB)
        print("----------------------------------")
        konvbalik()
        
    elif numA == "oz" and numB == "lb":     
        print (value, numA, "=",float(value)/16,numB)
        print("----------------------------------")
        konvbalik()   
    else:
        konvngarang()
        
# konv suhu 
       
def suhu():
    clearScreen()
    print ("---program mengkonversi suhu----")
    print ("1. celcius ")
    print ("2. reamur ")
    print ("3. fahrenheit")
    print ("4. kelvin")
    print ("5. tutup")
    
def konvsuhu():
    suhu()
    suhukonv = int (input ("pilih nomor menu :  "))
    if suhukonv == 1:
         celci()
    elif suhukonv == 2: 
         reamr()
    elif suhukonv == 3: 
        fahren()
    elif suhukonv == 4: 
           kelv()
    elif suhukonv == 5:
           jalan()
    else :
         novalid()
         
def konvbaliksuhu():
    print ("apakah anda ingin kembali?")
    print ("1. konversi suhu lain")
    print ("2. kembali ")
    baliksuhu = int(input("pillih opsi : "))
    if baliksuhu == 1:
        konvsuhu()
    elif baliksuhu == 2:
        konvbalik()
    else: 
        novalid()

def celci():
    print ("---- program konversi celcius ----")
    celcius = float (input ("masukan suhu dalam celcius = "))
    print(" suhu celcius = ", celcius, "C")
    reamur = (4/5)* celcius
    print("suhu celcuis dalam reamur = ", reamur, "R")
    fahrenhite = ((9/5)*celcius) +32
    print("suhu celcius dalam fahrenhit = ", fahrenhite, "F")
    kelvin = celcius + 273
    print ("suhu celcius dalam kelvin = ", kelvin, "K")
    print("----------------------------------")
    konvbaliksuhu()
    
def reamr():
    print ("---- program konversi reamur ----")
    reamur = float (input ("masukan suhu dalam reamur = "))
    print(" suhu reamur = ", reamur, "R")
    celcius = (5/4)* reamur
    print("suhu reamur dalam celcius = ", celcius, "C")
    fahrenhite = ((9/4)*reamur) +32
    print("suhu reamur dalam fahrenhit = ", fahrenhite, "F")
    kelvin = ((5/4)* reamur)+ 273
    print ("suhu reamur dalam kelvin = ", kelvin, "K")
    print("----------------------------------")
    konvbaliksuhu()
    
def fahren():
    print ("---- program konversi fahrenheit ----")
    fahrenheit = float (input ("masukan suhu dalam fahrenheit = "))
    print(" suhu fahrenheit = ", fahrenheit, "F")
    reamur = (4/9)*(fahrenheit - 32)
    print("suhu fahrenheit dalam reamur = ", reamur, "R")
    celcius = (5/9)*(fahrenheit - 32)
    print("suhu fahrenheit dalam celsius = ", celcius, "C")
    kelvin = (5/9)*(fahrenheit - 32) + 273
    print ("suhu fahrenheit dalam kelvin = ", kelvin, "K")
    print("----------------------------------")
    konvbaliksuhu()
    
def kelv():
    print ("---- program konversi kelvin ----")
    kelvin = float (input ("masukan suhu dalam kelvin = "))
    print(" suhu celcius = ", kelvin, "K")
    reamur = (4/5)* (kelvin -273)
    print("suhu kelvin dalam reamur = ", reamur, "R")
    fahrenhite = ((4/5)*(kelvin - 273)) +32
    print("suhu celcius dalam fahrenhit = ", fahrenhite, "F")
    celcius = ((9/5)*(kelvin - 273)) +32
    print ("suhu celcius dalam kelvin = ", celcius, "C")
    print("----------------------------------")
    konvbaliksuhu()

# konv mata uang 





# ini baru jalan
jalan()