from keys import Keys

def encrypt(public_key, data):
    encrypted_data = []

    for t in data:
        c = pow(t, public_key['e'], public_key['n'])
        encrypted_data.append(c)

    return encrypted_data


def decrypt(private_key, data):
    decrypted_data = []

    for c in data:
        t = pow(c, private_key['d'], private_key['n'])
        decrypted_data.append(t)

    return decrypted_data

results = [6, 2, 3, 5, 3, 6, 6, 6, 7, 8, 9, 9, 12, 455]
keys = Keys()
public_key = keys.generate_public_key()
private_key = keys.generate_private_key()

data = encrypt(public_key,results)

print(data)

data = decrypt(private_key, data)

print(data)

