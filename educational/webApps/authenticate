

brute force dictionary attack

sniper attact with burp

zap would not work , would change the post req to get 



re register attact

Let's understand this with the help of an example, say there is an existing user with the name admin and now we want to get access to their account so what we can do is try to re-register that username but with slight modification. We are going to enter " admin"(notice the space in the starting). Now when you enter that in the username field and enter other required information like email id or password and submit that data. It will actually register a new user but that user will have the same right as normal admin. And that new user will also be able to see all the content present under the user admin.



JSON web token

three parts

JWT can be divided into 3 parts separated by a dot(.)

1) Header:  This consists of the algorithm used and the type of the token.

{  "alg": "HS256", "typ": "JWT"}

alg could be HMAC, RSA, SHA256 or can even contain None value.

2) Payload: This is part that contains the access given to the certain user etc. This can vary from website to website, some can just have a simple username and some ID and others could have a lot of other details.

3) Signature: This is the part that is used to make sure that the integrity of the data was maintained while transferring it from a user's computer to the server and back. This is encrypted with whatever algorithm or alg that was passed in the header's value. And this can only be decrypted with a predefined secret(which should be difficult to)

Now to put all the 3 part together we base64 encode all of them separated by a dot(.) so it would look something like:

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c


we change the first part to none , so we don't need the signature,,, then manipulate the identity

{"typ":"JWT","alg":"HS256"}
becomes
{"typ":"JWT","alg":"NONE"}



{"exp":1586620929,"iat":1586620629,"nbf":1586620629,"identity":1}

becomes

{"exp":1586620929,"iat":1586620629,"nbf":1586620629,"identity":2}

admin would typically be 0

we hash it in base64

eyJ0eXAiOiJKV1QiLCJhbGciOiJOT05FIn0K.eyJleHAiOjE1ODY3MDUyOTUsImlhdCI6MTU4NjcwNDk5NSwibmJmIjoxNTg2NzA0OTk1LCJpZGVudGl0eSI6MH0K.


change the cookie, and that should switch users, 





no authorization


A lot of time on websites we see that when we register a user and login with our credentials we are given a certain id which either is completely a number or ends with a number. Most of the time developers secures their application but sometime in some places, it could happen that just by changing that number we are able to see some hidden or private data.


























