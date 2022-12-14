from pwn import xor
print("\n")
password = input("enter the password text")
secret = input("enter the secret text")
hash = xor(password,secret)
print("\n")
print(hash)
