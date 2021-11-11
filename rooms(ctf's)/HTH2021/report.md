During trivia decided to finally start ctf

started with pwned 1

went to r2 and couln't really get it, 

Intro flag, a pdf file, look at the index as hint says and you see certain letters in bold, line them up and ca boom we get flat

Web Challenges:

1- cookie manipulation- change cookie to admin:1 , then funny thing is that refresh doesn't work, you have to actually login admin:admin and we get flat
# HTH{int0_th3_und3rgr0und}
2- JSON web token 
We get a new cookie with JSON, 
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJOZXh4dXMiLCJpYXQiOjE2MzUxMjI3OTUsImV4cCI6MTY2NjY1ODc5NSwiYXVkIjoiTkRSIGFkbWlucyIsInN1YiI6IkFjY2VzcyBjb2RlIGZvciBzZW5zaXRpdmUgZGF0YSIsIkFjY2Vzc0NvZGUiOiI2MjYwIn0.CjORA2THjMe71itx26iQ12xEPVXeI0nMPdGL3qNLUOA
Payload,
{
  "iss": "Nexxus",
  "iat": 1635122795,
  "exp": 1666658795,
  "aud": "NDR admins",
  "sub": "Access code for sensitive data",
  "AccessCode": "6260"
}
HTH{i_dont_think_thats_how_you_use_jwts}

3- RCE   ;cd flag;cat therealflag.txt
HTH{injecting_some_minor_details}

