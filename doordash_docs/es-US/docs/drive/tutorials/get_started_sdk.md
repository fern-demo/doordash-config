En esta página

# Comenzar (Node.js)

Con esta API, puedes aprovechar nuestra plataforma de logística bajo demanda para entregar tus productos de forma rápida y sencilla sin la molestia de tener tu propia flota de entrega. La API de Drive se ha diseñado para ser la forma más sencilla de completar tus entregas.

### Un flujo típico:[​](#un-flujo-típico "Enlace directo al encabezado")

* Solicita un presupuesto (opcional). Esto te indicará la hora del retiro estimada y el costo de tu entrega.
* Solicita una entrega o acepta un presupuesto.
* Se realiza la entrega.

### Cómo crear una entrega[​](#cómo-crear-una-entrega "Enlace directo al encabezado")

Antes de comenzar, asegúrate de [crear una clave de acceso](/es-US/docs/drive/how_to/manage_credentials) y [generar un JWT](/es-US/docs/drive/how_to/JWTs).

* JavaScript
* Python
* PHP
* Kotlin
* C#

```
const axios = require('axios')  
const { v4: uuidv4 } = require('uuid')  
  
const body = JSON.stringify({  
  external_delivery_id: uuidv4(), // keep track of the generated id here or in the response  
  pickup_address: '901 Market Street 6th Floor San Francisco, CA 94103',  
  pickup_business_name: 'Wells Fargo SF Downtown',  
  pickup_phone_number: '+16505555555',  
  pickup_instructions: 'Enter gate code 1234 on the callbox.',  
  dropoff_address: '901 Market Street 6th Floor San Francisco, CA 94103',  
  dropoff_business_name: 'Wells Fargo SF Downtown',  
  dropoff_phone_number: '+16505555555',  
  dropoff_instructions: 'Enter gate code 1234 on the callbox.',  
  order_value: 1999,  
})  
  
axios  
  .post('https://openapi.doordash.com/drive/v2/deliveries', body, {  
    headers: {  
      Authorization: 'Bearer ' + token,  
      'Content-Type': 'application/json',  
    },  
  })  
  .then(function (response) {  
    console.log(response.data)  
  })  
  .catch(function (error) {  
    console.log(error)  
  })  

```

```
import requests  
import uuid  
  
endpoint = "https://openapi.doordash.com/drive/v2/deliveries/" # DRIVE API V2  
  
headers = {"Authorization": "Bearer " + token,  
            "Content-Type": "application/json"}  
  
delivery_id = str(uuid.uuid4()) # Randomly generated UUID4  
  
request_body = { # Modify pickup and drop off addresses below  
    "external_delivery_id": delivery_id,  
    "pickup_address": "901 Market Street 6th Floor San Francisco, CA 94103",  
    "pickup_business_name": "Wells Fargo SF Downtown",  
    "pickup_phone_number": "+16505555555",  
    "pickup_instructions": "Enter gate code 1234 on the callbox.",  
    "dropoff_address": "901 Market Street 6th Floor San Francisco, CA 94103",  
    "dropoff_business_name": "Wells Fargo SF Downtown",  
    "dropoff_phone_number": "+16505555555",  
    "dropoff_instructions": "Enter gate code 1234 on the callbox.",  
    "order_value": 1999  
}  
  
create_delivery = requests.post(endpoint, headers=headers, json=request_body) # Create POST request  
  
  
print(create_delivery.status_code)  
print(create_delivery.text)  
print(create_delivery.reason)  

```

```
$jwt = "Refer to How To > Get Started With JWTs"  
  
// Modify pickup and drop off addresses below  
$request_body = json_encode([  
  "external_delivery_id" => "{Generate_your_own_id}",  
  "pickup_address"=> "901 Market Street 6th Floor San Francisco, CA 94103",  
  "pickup_business_name"=> "Wells Fargo SF Downtown",  
  "pickup_phone_number"=> "+16505555555",  
  "pickup_instructions"=> "Enter gate code 1234 on the callbox.",  
  "dropoff_address"=> "901 Market Street 6th Floor San Francisco, CA 94103",  
  "dropoff_business_name"=> "Wells Fargo SF Downtown",  
  "dropoff_phone_number"=> "+16505555555",  
  "dropoff_instructions"=> "Enter gate code 1234 on the callbox.",  
  "order_value"=> 1999  
]);  
  
$headers = array(  
  "Content-type: application/json",  
  "Authorization: Bearer ".$jwt  
);  
  
$ch = curl_init();  
curl_setopt($ch, CURLOPT_URL, "https://openapi.doordash.com/drive/v2/deliveries/");  
curl_setopt($ch, CURLOPT_POST, 1);  
curl_setopt($ch, CURLOPT_POSTFIELDS, $request_body);  
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);  
$result = curl_exec($ch);  
echo($result)  
  

```

```
import java.net.URI  
import java.net.http.HttpClient  
import java.net.http.HttpRequest  
import java.net.http.HttpResponse  
import java.util.*  
  
val body = """{  
    "external_delivery_id": "${UUID.randomUUID()}",  
    "pickup_address": "901 Market Street 6th Floor San Francisco, CA 94103",  
    "pickup_business_name": "Wells Fargo SF Downtown",  
    "pickup_phone_number": "+16505555555",  
    "pickup_instructions": "Enter gate code 1234 on the callbox.",  
    "dropoff_address": "901 Market Street 6th Floor San Francisco, CA 94103",  
    "dropoff_business_name": "Wells Fargo SF Downtown",  
    "dropoff_phone_number": "+16505555555",  
    "dropoff_instructions": "Enter gate code 1234 on the callbox.",  
    "order_value": 1999  
}"""  
  
val client = HttpClient.newBuilder().build();  
val request = HttpRequest.newBuilder()  
    .uri(URI.create("https://openapi.doordash.com/drive/v2/deliveries/"))  
    .header("Authorization", "Bearer $jwt")  
    .header("Content-Type", "application/json")  
    .POST(HttpRequest.BodyPublishers.ofString(body))  
    .build();  
  
val response = client.send(request, HttpResponse.BodyHandlers.ofString());  
println(response.body())  

```

```
using System.Text;  
using System.Text.Json;  
  
var jsonContent = JsonSerializer.Serialize(new {  
    external_delivery_id = Guid.NewGuid().ToString(),  
    pickup_address = "901 Market Street 6th Floor San Francisco, CA 94103",  
    pickup_business_name = "Wells Fargo SF Downtown",  
    pickup_phone_number = "+16505555555",  
    pickup_instructions = "Enter gate code 1234 on the callbox.",  
    pickup_reference_tag = "Order number 61",  
    dropoff_address = "901 Market Street 6th Floor San Francisco, CA 94103",  
    dropoff_business_name = "Wells Fargo SF Downtown",  
    dropoff_phone_number = "+16505555555",  
    dropoff_instructions = "Enter gate code 1234 on the callbox."  
});  
var content = new StringContent(jsonContent, Encoding.UTF8, "application/json");  
  
HttpClient client = new HttpClient();  
client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", token);  
var result = await client.PostAsync("https://openapi.doordash.com/drive/v2/deliveries", content);  
  
var status = result.StatusCode;  
var resultString = await result.Content.ReadAsStringAsync();  

```

### Cómo obtener el estado de una entrega[​](#cómo-obtener-el-estado-de-una-entrega "Enlace directo al encabezado")

* JavaScript
* Python
* PHP
* Kotlin
* C#

```
const axios = require('axios')  
  
axios  
  .get(  
    'https://openapi.doordash.com/drive/v2/deliveries/{external_delivery_id}',  
    {  
      headers: {  
        Authorization: 'Bearer ' + token,  
        'Content-Type': 'application/json',  
      },  
    },  
  )  
  .then(function (response) {  
    console.log(response.data)  
  })  
  .catch(function (error) {  
    console.log(error)  
  })  

```

```
import requests  
import uuid  
  
endpoint = "https://openapi.doordash.com/drive/v2/deliveries/" # DRIVE API V2  
  
headers = {"Authorization": "Bearer " + token,  
            "Content-Type": "application/json"}  
  
get_delivery = requests.get(endpoint + '{external_delivery_id}', headers=headers) # Create GET request  
  
print(get_delivery.status_code)  
print(get_delivery.text)  
print(get_delivery.url)  

```

```
$jwt = "Refer to How To > Get Started With JWTs"  
  
$headers = array(  
  "Content-type: application/json",  
  "Authorization: Bearer ".$jwt  
);  
  
$ch = curl_init();  
curl_setopt($ch, CURLOPT_URL, "https://openapi.doordash.com/drive/v2/deliveries/{external_id_used_in_creation}");  
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);  
$result = curl_exec($ch);  
echo($result)  
  

```

```
import java.net.URI  
import java.net.http.HttpClient  
import java.net.http.HttpRequest  
import java.net.http.HttpResponse  
import java.util.*  
  
val client = HttpClient.newBuilder().build();  
val request = HttpRequest.newBuilder()  
    .uri(URI.create("https://openapi.doordash.com/drive/v2/deliveries/{external_delivery_id}"))  
    .header("Authorization", "Bearer $jwt")  
    .build();  
  
val response = client.send(request, HttpResponse.BodyHandlers.ofString());  
println(response.body())  

```

```
HttpClient client = new HttpClient();  
client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", token);  
var result = await client.GetAsync($"https://openapi.doordash.com/drive/v2/deliveries/{external_delivery_id}", content);  
  
var status = result.StatusCode;  
var resultString = await result.Content.ReadAsStringAsync();  

```

### Observaciones importantes:[​](#observaciones-importantes "Enlace directo al encabezado")

Vuelve a probar todos los códigos de estado de respuesta 50x, ya que el error podría ser transitorio. Recomendamos hasta 3 reintentos con un cierto retardo exponencial entre solicitudes.

[Anterior

Comenzar (API)](/es-US/docs/drive/tutorials/get_started)[Siguiente

Get started (Postman)](/es-US/docs/drive/tutorials/get_started_postman)

* [Un flujo típico:](#un-flujo-típico)
* [Cómo crear una entrega](#cómo-crear-una-entrega)
* [Cómo obtener el estado de una entrega](#cómo-obtener-el-estado-de-una-entrega)
* [Observaciones importantes:](#observaciones-importantes)