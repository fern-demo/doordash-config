Sur cette page

# Créer des JWT (JSON Web Tokens)

API: Drive

Ce document traite de l’API Drive. Si vous utilisez l’API Drive (classique), consultez le [guide pratique pour les JWT Drive (classique)](/fr-CA/docs/drive_classic/how_to/JWTs).

## Conditions préalables[​](#conditions-préalables "Lien direct vers le titre")

Avant de commencer, assurez-vous d'avoir créé et enregistré une clé d'accès à partir du Portail des développeurs.

Pour continuer, vous aurez besoin de : **developer\_id** , **key\_id** et **signature\_secret**

* JavaScript
* Python
* Kotlin
* C#

```
npm install jsonwebtoken  

```

```
pip install pyjwt  

```

```
gradle.properties:  
  
    # JWT  
    jjwtVersion=0.10.6  
  
build.gradle.kts:  
  
    dependencies {  
        testImplementation(kotlin("test"))  
        val jjwtVersion: String by project  
        implementation("io.jsonwebtoken:jjwt-api:$jjwtVersion")  
        implementation("io.jsonwebtoken:jjwt-impl:$jjwtVersion")  
        implementation("io.jsonwebtoken:jjwt-jackson:$jjwtVersion")  
    }  
  

```

```
dotnet add package System.IdentityModel.Tokens.Jwt  

```

## Comment générer un JWT[​](#comment-générer-un-jwt "Lien direct vers le titre")

* JavaScript
* Python
* PHP
* Kotlin
* C#

```
const jwt = require('jsonwebtoken')  
  
const data = {  
  aud: 'doordash',  
  iss: '{developer_id}',  
  kid: '{key_id}',  
  exp: Math.floor(Date.now() / 1000 + 300),  
  iat: Math.floor(Date.now() / 1000),  
}  
  
const headers = { algorithm: 'HS256', header: { 'dd-ver': 'DD-JWT-V1' } }  
  
const token = jwt.sign(data, Buffer.from('{signing_secret}', 'base64'), headers)  

```

```
import jwt.utils  
import time  
import math  
  
token = jwt.encode(  
    {  
        "aud": "doordash",  
        "iss": "{developer_id}",  
        "kid": "{key_id}",  
        "exp": str(math.floor(time.time() + 300)),  
        "iat": str(math.floor(time.time())),  
    },  
    jwt.utils.base64url_decode("{signing_secret}"),  
    algorithm="HS256",  
    headers={"dd-ver": "DD-JWT-V1"})  

```

```
function base64UrlEncode(string $data): string  
{  
    $base64Url = strtr(base64_encode($data), '+/', '-_');  
  
    return rtrim($base64Url, '=');  
}  
  
function base64UrlDecode(string $base64Url): string  
{  
    return base64_decode(strtr($base64Url, '-_', '+/'));  
}  
  
$header = json_encode([  
    'alg' => 'HS256',  
    'typ' => 'JWT',  
    'dd-ver' => 'DD-JWT-V1'  
]);  
  
$payload = json_encode([  
    'aud' => 'doordash',  
    'iss' => '{developer_id}',  
    'kid' => '{key_id}',  
    'exp' => time() + 300,  
    'iat' => time()  
]);  
  
$base64UrlHeader = base64UrlEncode($header);  
$base64UrlPayload = base64UrlEncode($payload);  
  
$signature = hash_hmac('sha256', $base64UrlHeader . "." . $base64UrlPayload, base64UrlDecode({signing_secret}), true);  
$base64UrlSignature = base64UrlEncode($signature);  
  
$jwt = $base64UrlHeader . "." . $base64UrlPayload . "." . $base64UrlSignature;  

```

```
import io.jsonwebtoken.Header  
import io.jsonwebtoken.Jwts  
import io.jsonwebtoken.io.Decoders  
import io.jsonwebtoken.security.Keys  
import java.security.Key  
import java.time.ZoneOffset  
import java.time.ZonedDateTime  
import kotlin.collections.HashMap  
  
val claims = HashMap<String, Any?>();  
  
claims["aud"] = "doordash";  
claims["iss"] = "{developer_id}";  
claims["kid"] = "{key_id}";  
claims["exp"] = ZonedDateTime.now(ZoneOffset.UTC).plusMinutes(5).toEpochSecond()  
claims["iat"] = ZonedDateTime.now(ZoneOffset.UTC).toEpochSecond();  
  
val keyBytes = Decoders.BASE64URL.decode("{signing_secret}")  
val key: Key = Keys.hmacShaKeyFor(keyBytes)  
  
val jwt: String = Jwts.builder()  
    .setHeaderParam("dd-ver", "DD-JWT-V1")  
    .setHeaderParam("typ", "JWT")  
    .setClaims(claims)  
    .signWith(key)  
    .compact();  
  

```

```
using Microsoft.IdentityModel.Tokens;  
using System.IdentityModel.Tokens.Jwt;  
using System.Security.Claims;  
  
var decodedSecret = Base64UrlEncoder.DecodeBytes("{signing_secret}");  
var securityKey = new SymmetricSecurityKey(decodedSecret);  
var credentials = new SigningCredentials(securityKey, SecurityAlgorithms.HmacSha256);  
var header = new JwtHeader(credentials);  
header["dd-ver"] = "DD-JWT-V1";  
  
var payload = new JwtPayload(  
    issuer: "{developer_id}",  
    audience: "doordash",  
    claims: new List<Claim> { new Claim("kid", "{key_id}") },  
    notBefore: null,  
    expires: System.DateTime.UtcNow.AddSeconds(300),  
    issuedAt: System.DateTime.UtcNow);  
  
var securityToken = new JwtSecurityToken(header, payload);  
var token = new JwtSecurityTokenHandler().WriteToken(securityToken);  

```

[Précédent

Configure SMS delivery updates](/fr-CA/docs/drive/how_to/configure_sms)[Suivant

Recevoir des mises à jour de livraison par le point d’ancrage Web](/fr-CA/docs/drive/how_to/webhooks)

* [Conditions préalables](#conditions-préalables)
* [Comment générer un JWT](#comment-générer-un-jwt)