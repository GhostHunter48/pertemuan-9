# Nama:Fikri Raditya Hutama
# Kelas: RPL 1A
# NIM: 2408727
def login():
    user = "Daspro2023"
    pwd = "Latihan"
    tries = 3

    while tries > 0:
        u_input = input("Username: ")
        p_input = input("Password: ")

        if u_input == user and p_input == pwd:
            print("Login berhasil!")
            break
        else:
            tries -= 1
            print("Login gagal. Sisa kesempatan:", tries)

    if tries == 0:
        print("Anda dikeluarkan dari sistem.")

# Menjalankan login
login()
