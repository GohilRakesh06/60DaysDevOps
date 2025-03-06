import subprocess

username = input("Enter User Name: ")
default_passwd = '123'

subprocess.run(['sudo', 'useradd', username])


subprocess.run(['echo', f"{username}:{default_passwd}"], stdout=subprocess.PIPE)
subprocess.run(['sudo', 'chpasswd'], input=f"{username}:{default_passwd}".encode())
print(f"User '{username}' added with default password.")
