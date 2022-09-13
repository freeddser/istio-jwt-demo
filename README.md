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


##### test with token
    
    #curl --location --request GET 'http://abc.test.com/api/test' \
    --header 'Authorization: Bearer $token'
    ok