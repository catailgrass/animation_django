from django.contrib.auth.hashers import make_password

if __name__ == '__main__':
    pwd_hash = make_password('Ab123145')
    print(pwd_hash)