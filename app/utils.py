import bcrypt


def hash_password(password):
    hashed_password_bytes = bcrypt.hashpw(
        password.encode('utf-8'), bcrypt.gensalt())
    hashed_password_str = hashed_password_bytes.decode('utf-8')
    return hashed_password_str


def verify_password(hashed_password, input_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8'))
