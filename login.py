#Penulis Kresna
import pandas as pd

df_user = pd.read_csv("user.csv")


def login():
    while True:

        print("=== Selamat Datang ===")
        print()
        usernameInput = input("Masukkan Username: ")
        passwordInput = input("Masukkan Password: ")

        user = df_user[
            (df_user["username"] == usernameInput) &
            (df_user["password"] == passwordInput)
        ]
        
        if not user.empty:
            role = int(user.iloc[0]["role"])
            print("\nLogin Berhasil\n")
            
            if role == 2:
                print("Role: Admin")
                break
            elif role == 1:
                print("Role: User")
                break
            else:
                print("Username atau Password salah. Silahkan coba lagi\n")
                
login()