# istio-jwt-demo
    https://istio.io/latest/docs/tasks/security/authentication/authn-policy/
    https://istio.io/latest/docs/tasks/security/authentication/jwt-route/

### istio yaml
    jwksUri: "https://raw.githubusercontent.com/freeddser/istio-jwt-demo/master/jwks.json"
    or use your jwks link with your RSA public key

### create new RSA file
    python create-rsa-files.py
    you will get new public.pem and private.key
    you also can use your local RSA file replace those pem file
##### Covert RSA public key to jwks.json
    #https://jwcrypto.readthedocs.io/en/latest/jwk.html

    python get-jwks.py > jwks.json


       
##### get new token
    python gen-jwt.py  private.key --expire=3000000 --iss "testing@secure.istio.io" > demo.jwt

##### check token with jwt.io
    https://jwt.io/
![img.png](img.png)
##### test with token
    you can use this demo key:
    https://raw.githubusercontent.com/freeddser/istio-jwt-demo/master/demo.jwt
    eyJhbGciOiJSUzI1NiIsImtpZCI6InlvYmh1dW00S2pQdno3Znc1UjBqVXhQZkY5N2FwdGRYaklfdXQtcnpaR2MiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2NjYwNDk5NjcsImlhdCI6MTY2MzA0OTk2NywiaXNzIjoidGVzdGluZ0BzZWN1cmUuaXN0aW8uaW8iLCJzdWIiOiJ0ZXN0aW5nQHNlY3VyZS5pc3Rpby5pbyJ9.WYWzOooQdggf5j7mhjtA2IWWMuCGhs-I5AfSv5ul2o597evxD9SCjt3aX-Bh8ZjOTaxw2PDFhwzWLNyWVAzMiRufaaWJVejku3vdyLflRGb5PRjDs0uv6KiBx4v0pKpO6lPJSalIX4iZ1Q9wJZtBmpniDxPyS_Yv7E1d3FFGlHfbljZxVSKduQziDndJy1L3pl5Bxdv0cZynn0FaX8Xw8HHzwwxWzH2KWoSRBK1Ca6coNfVm1fqgW3CuRYaEqFsYk8eqaYoBfFc2LfZomhHhda-oY7V2yMqrcRgRykM746ylW7UYrzR84GzQP4z2AvzXFK_E1JtTv9BpOdmo1f74ig

    #curl --location --request GET 'http://abc.test.com/api/test' \
    --header 'Authorization: Bearer $token'
    ok