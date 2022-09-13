import rsa

public_key, private_key = rsa.newkeys(2048)

# create public pem
public_key_bytes = public_key.save_pkcs1()
with open('public.pem', 'wb')as f:
    f.write(public_key_bytes)

# create public key
private_key_bytes = private_key.save_pkcs1()
with open('private.key', 'wb')as f:
    f.write(private_key_bytes)