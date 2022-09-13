from jwcrypto import jwk

# key = jwk.JWK.generate(kty='RSA', size=2048,  kid='12345')
# public_key = key.export_public()
# private_key = key.export_private()
#
# print(key)
# print(private_key)
# print(public_key)

with open("public.pem", "rb") as pemfile:  #doctest: +SKIP
    key = jwk.JWK.from_pem(pemfile.read())
    # print("!!!!",key)
    print('{"keys":['+key.export_public()+']}')
    # print(key.export_private())

