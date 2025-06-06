[Saltar al contenido principal](#__docusaurus_skipToContent_fallback)

[![DoorDash Logo](/es-US/img/header/developer-logo.svg)![DoorDash Logo](/es-US/img/header/developer-logo.svg)](/es-US/)

Icon Loading

[Documentación](/es-US/docs/welcome)

[Referencia de API](#)

* [Drive](/es-US/api/drive)
* [Drive (clásico)](/es-US/api/drive_classic)
* [Marketplace](/es-US/api/marketplace)
* [Marketplace (legacy)](/es-US/api/marketplace_legacy)
* [Marketplace for Retailers](/es-US/api/marketplace_v2)
* [Reporting](/es-US/api/reporting)

[Blog](/es-US/blog)

[🇪🇸 español](#)

* [🇺🇸 English](/en-US/api/drive_classic)
* [🇫🇷 français](/fr-CA/api/drive_classic)
* [🇪🇸 español](/es-US/api/drive_classic)

[Portal para desarrolladores](https://developer.doordash.com/portal)

[![Doordash Drive](https://doordash-static.s3-us-west-2.amazonaws.com/media/drive/drive-logo.png)](https://www.doordash.com/drive/portal/discover)

* Delivery
  + postDelivery Estimate
  + postDelivery Validation
  + postDelivery Creation
  + getDelivery Details
  + patchUpdate Delivery
  + putCancel Delivery
* Business & Store
  + getGet Business
  + patchUpdate Business
  + postCreate Business
  + getList Businesses
  + getGet Store
  + patchUpdate Store
  + postCreate Store
  + getList Stores

[API docs by Redocly](https://redocly.com/redoc/)

# Drive (classic) API Specification (0.4.8)

# Delivery

## Delivery Estimate

Request time and fee estimates for the delivery. The Estimates API can also be used to check if an area is serviced.

##### Request Body schema: application/json

Request body for estimate endpoint

|  |  |
| --- | --- |
| pickup\_address | object (The address the delivery needs to be picked up from.)  The address the delivery needs to be picked up from. Required unless your request includes an `external_store_id` that you've already used in at least one successful delivery request. If both `pickup_address` and `external_store_id` are included, `pickup_address` is ignored in favor of the existing address associated with the store. |
| dropoff\_address required | object (The address where the delivery needs to be dropped off.)  The address where the delivery needs to be dropped off. |
| order\_value required | integer <int32>   >= 0  The subtotal for all items in the order, excluding tax/tip, in cents. i.e. $19.99 = 1999 |
| delivery\_time | string  The requested UTC date-time (in ISO-8601 format) at which the order should be delivered. If this field is specified, `pickup_time` cannot be specified.Must provide either a `pickup_time` or a `delivery_time` to pass validation. |
| pickup\_time | string  The requested UTC date-time (in ISO-8601 format) at which the order should be picked up. If this field is specified, `delivery_time` cannot be specified. Must provide either a `pickup_time` or a `delivery_time` to pass validation. |
| external\_business\_name | string  A name used to group stores under a particular owner. For example, John Smith's Franchise Business. Required if `pickup_address` object is not passed in. If `external_business_name` is used, `external_store_id` is required. Can't be used with `external_business_id`. |
| external\_business\_id | string/^[A-Za-z0-9\_-]{3,64}$/  An unique, caller-selected ID of the business. Required if pickup\_address object is not passed in. If `external_business_id` is used, `external_store_id` is required. Can't be used with `external_business_name`. |
| external\_store\_id | string  A unique identifier, defined by you, which can be used to track the specific store that the delivery is for. Required if `pickup_address` object is not passed in. If `external_store_id` is used, `external_business_name` is required. |
| promotion\_id | string  The ID of the promotion that you want to apply to the delivery. The quoted fee in the response will reflect the promotion if this ID is valid. If the ID is invalid, field error will be returned. Contact your account manager for any configured promotion IDs. |
| items | Array of objects (Item) |

### Responses

**200** 

Estimate returned for the delivery with the given parameters

**400** 

Bad request

**5XX** 

* Please retry all 50x response status codes as the error could be transient. We recommend up to 3 retries with some exponential backoff delay between requests.
* When providing a time to any of the below APIs (i.e. `pickup_time` or `delivery_time`), the format must be UTC.'

post/drive/v1/estimates

https://openapi.doordash.com/drive/v1/estimates

### Request samples

* Payload

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "pickup_address": {
  + "city": "San Francisco",
  + "state": "California",
  + "street": "101 Howard Street",
  + "unit": "Apt 301",
  + "zip_code": "94105",
  + "full_address": "901 Market Street 6th Floor, San Francisco, CA 94103"},
* "dropoff_address": {
  + "city": "San Francisco",
  + "state": "California",
  + "street": "901 Market Street",
  + "unit": "Suite #600",
  + "zip_code": "94105",
  + "full_address": "901 Market Street 6th Floor, San Francisco, CA 94103",
  + "location": {
    - "lat": 37.78,
    - "lng": -122.4}},
* "order_value": 1999,
* "delivery_time": "2018-08-22T17:21:28Z",
* "pickup_time": "2018-08-22T17:20:28Z",
* "external_business_name": "1443432456",
* "external_business_id": "a0720d55-7cbe-41ce-8185-58285b7985cd",
* "external_store_id": "mega-corp-2340593",
* "promotion_id": "ee680b87-0016-496e-ac3c-d3f33ab54c1c",
* "items": [
  + {
    - "name": "Mega Bean and Cheese Burrito",
    - "description": "Mega Burrito contains the biggest beans of the land with extra cheese.",
    - "barcode": "12342830041",
    - "quantity": 2,
    - "external_id": "123-123443434b",
    - "volume": 5.3,
    - "weight": 2.8,
    - "length": 2.8,
    - "width": 2.8,
    - "height": 2.8,
    - "price": 1000}]

}`

### Response samples

* 200
* 400

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "delivery_time": "2018-08-22T17:20:28Z",
* "fee": 1900,
* "fee_components": [
  + {
    - "type": "distance_based_fee",
    - "amount": 1900}],
* "tax": 520,
* "tax_components": [
  + {
    - "type": "gst_hst",
    - "amount": 520}],
* "pickup_time": "2018-08-22T18:10:58Z",
* "currency": "USD",
* "id": 48173944

}`

## Delivery Validation

Validates input parameters for delivery and checks if the area is serviceable. DoorDash recommends using the Estimates API instead.

##### Request Body schema: application/json

|  |  |
| --- | --- |
| pickup\_address | object (The address the delivery needs to be picked up from.)  The address the delivery needs to be picked up from. Required unless your request includes an `external_store_id` that you've already used in at least one successful delivery request. If both `pickup_address` and `external_store_id` are included, `pickup_address` is ignored in favor of the existing address associated with the store. |
| pickup\_phone\_number | string  The phone number for the Dasher to call, including country code, if there are any issues with the pick up. The phone number must be a valid phone number. Required unless your request includes an `external_store_id` that you've already used in at least one successful delivery request. If both `pickup_phone_number` and `external_store_id` are included, `pickup_phone_number` is ignored in favor of the existing phone number associated with the store. |
| pickup\_instructions | string  Instruction for the dasher for the pickup location. |
| dropoff\_address required | object (The address where the delivery needs to be dropped off.)  The address where the delivery needs to be dropped off. |
| customer required | object (The customer that ordered the delivery.)  The customer that ordered the delivery. |
| dropoff\_instructions | string  Instruction for the dasher for the drop off location. |
| order\_value required | integer <int32>   >= 0  The subtotal for all items in the order, excluding tax/tip, in cents. i.e. $19.99 = 1999 |
| tip | integer <int32>  The amount to tip the Dasher in cents i.e. $5.00 = 500 |
| pickup\_time | string  The requested UTC date-time (in ISO-8601 format) at which the order should be picked up. If this field is specified, `delivery_time` cannot be specified. |
| delivery\_time | string  The requested UTC date-time (in ISO-8601 format) at which the order should be delivered. If this field is specified, `pickup_time` cannot be specified. |
| external\_delivery\_id | string  A unique identifier across all store locations under a business, defined by the merchant, which can be used to track this specific delivery. |
| contains\_alcohol | boolean  Set this to true if the order contains alcohol. Default value is false. |
| barcode\_scanning\_required | boolean  Set this to true if barcode scanning at both pickup and dropoff is required to complete the delivery. Default value is false. |
| num\_items | integer <int32>  The total number of items in the order. |
| external\_business\_name | string  A name used to group stores under a particular owner. For example, John Smith's Franchise Business. Required if `pickup_address` object is not passed in. If `external_business_name` is used, `external_store_id` is required. Can't be used with `external_business_id`. |
| external\_business\_id | string/^[A-Za-z0-9\_-]{3,64}$/  An unique, caller-selected ID of the business. Required if pickup\_address object is not passed in. If `external_business_id` is used, `external_store_id` is required. Can't be used with `external_business_name`. |
| external\_store\_id | string  A unique identifier, defined by you, which can be used to track the specific store that the delivery is for. Required if `pickup_address` object is not passed in. If `external_store_id` is used, `external_business_name` is required. |
| signature\_required | boolean  Set this to true if signature is required. Default value is false. |
| promotion\_id | string  The ID of the promotion that you want to apply to the delivery. If the ID is invalid, field error will be returned. Contact your account manager for any configured promotion IDs. |
| order\_contains\_list | Array of arrays  Items Enum: "tobacco\_items" "hemp\_items" "otc\_items"  An object that specifies the restricted item(s) contained in this order. The values that can be specified are 'tobacco\_items' (delivery contains tobacco items, requires ID Verification), 'hemp\_items' (delivery contains hemp items, requires ID Verification), 'otc\_items' (delivery contains otc items, requires ID Verification) |

### Responses

**200** 

Validity of the delivery

**400** 

Bad request

**5XX** 

* Please retry all 50x response status codes as the error could be transient. We recommend up to 3 retries with some exponential backoff delay between requests.
* When providing a time to any of the below APIs (i.e. `pickup_time` or `delivery_time`), the format must be UTC.'

post/drive/v1/validations

https://openapi.doordash.com/drive/v1/validations

### Request samples

* Payload

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "pickup_address": {
  + "city": "San Francisco",
  + "state": "California",
  + "street": "101 Howard Street",
  + "unit": "Apt 301",
  + "zip_code": "94105",
  + "full_address": "901 Market Street 6th Floor, San Francisco, CA 94103"},
* "pickup_phone_number": "+15555555555",
* "pickup_instructions": "Use the back alley of the store for pickup",
* "dropoff_address": {
  + "city": "San Francisco",
  + "state": "California",
  + "street": "901 Market Street",
  + "unit": "Suite #600",
  + "zip_code": "94105",
  + "full_address": "901 Market Street 6th Floor, San Francisco, CA 94103",
  + "location": {
    - "lat": 37.78,
    - "lng": -122.4}},
* "customer": {
  + "phone_number": "+16505555555",
  + "business_name": "Mega Corp HQ",
  + "first_name": "Jane",
  + "last_name": "Goodall",
  + "email": "[email protected]",
  + "should_send_notifications": true,
  + "locale": "en-US"},
* "dropoff_instructions": "Use the access code 420 to get into the building.",
* "order_value": 1999,
* "tip": 500,
* "pickup_time": "2018-08-22T17:20:28Z",
* "delivery_time": "2018-08-22T17:21:28Z",
* "external_delivery_id": "1342666-2420",
* "contains_alcohol": true,
* "barcode_scanning_required": true,
* "num_items": 1,
* "external_business_name": "1443432456",
* "external_business_id": "a0720d55-7cbe-41ce-8185-58285b7985cd",
* "external_store_id": "mega-corp-2340593",
* "signature_required": true,
* "promotion_id": "ee680b87-0016-496e-ac3c-d3f33ab54c1c",
* "order_contains_list": [
  + "tobacco_items",
  + "hemp_items",
  + "otc_items"]

}`

### Response samples

* 200
* 400

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "valid": true,
* "errors": { }

}`

## Delivery Creation

Create a delivery

##### Request Body schema: application/json

|  |  |
| --- | --- |
| pickup\_address | object (The address the delivery needs to be picked up from. This field is not required for existing stores with a known `external\_store\_id`.)  The address the delivery needs to be picked up from. |
| pickup\_phone\_number | string  The phone number for the Dasher to call, including country code, if there are any issues with the pick up. The phone number must be a valid US phone number. This field is not required for existing stores with a known `external_store_id` |
| dropoff\_address required | object (The address where the delivery needs to be dropped off.)  The address where the delivery needs to be dropped off. |
| customer required | object (The customer that ordered the delivery.)  The customer that ordered the delivery. |
| order\_value required | integer <int32>   >= 0  The subtotal for all items in the order, excluding tax/tip, in cents. i.e. $19.99 = 1999 |
| pickup\_time | string  The requested UTC date-time (in ISO-8601 format) at which the order should be picked up. If this field is specified, `delivery_time` cannot be specified. |
| delivery\_time | string  The requested UTC date-time (in ISO-8601 format) at which the order should be delivered. If this field is specified, `pickup_time` cannot be specified. |
| pickup\_window\_start\_time | string  The UTC date-time (in ISO-8601 format) overrides `delivery_time` and `pickup_time` when all four parameters of the delivery window (i.e. `pickup_window_start_time` , `pickup_window_end_time` , `delivery_window_start_time` , `delivery_window_end_time` ) are provided. |
| pickup\_window\_end\_time | string  The UTC date-time (in ISO-8601 format) overrides `delivery_time` and `pickup_time` when all four parameters of the delivery window (i.e. `pickup_window_start_time` , `pickup_window_end_time` , `delivery_window_start_time` , `delivery_window_end_time` ) are provided. |
| delivery\_window\_start\_time | string  The UTC date-time (in ISO-8601 format) overrides `delivery_time` and `pickup_time` when all four parameters of the delivery window (i.e. `pickup_window_start_time` , `pickup_window_end_time` , `delivery_window_start_time` , `delivery_window_end_time` ) are provided. |
| delivery\_window\_end\_time | string  The UTC date-time (in ISO-8601 format) overrides `delivery_time` and `pickup_time` when all four parameters of the delivery window (i.e. `pickup_window_start_time` , `pickup_window_end_time` , `delivery_window_start_time` , `delivery_window_end_time` ) are provided. |
| items | Array of objects (Item) |
| team\_lift\_required | boolean  More than one dasher is required to complete the delivery |
| barcode\_scanning\_required | boolean  Barcode scanning at both pickup and dropoff is required to complete the delivery |
| pickup\_business\_name | string  The name of the business where the order should be picked up from. |
| pickup\_instructions | string  Instructions for the Dasher to follow upon pickup of the order. |
| dropoff\_instructions | string  Instructions for the Dasher to follow upon delivery of the order. |
| order\_volume | integer <int32>   >= 0  Only supported for specific use cases. Provide a list of `items` with `weight` and `volume` instead or contact support to discuss the use of `order_volume`. |
| tip | integer <int32>  The amount to tip the driver in cents i.e. $5.00 = 500 |
| external\_delivery\_id | string  A unique identifier across all store locations under a business, defined by the merchant, which can be used to track this specific delivery. |
| driver\_reference\_tag | string  The internal order identifier at the merchant, which the driver can use to pick up the order. One example of a value for this field is the number the cashier hands the customer at a counter-serve restaurant. |
| external\_business\_name | string  A name used to group stores under a particular owner. For example, John Smith's Franchise Business. Required if `pickup_address` object is not passed in. If `external_business_name` is used, `external_store_id` is required. Can't be used with `external_business_id`. |
| external\_business\_id | string/^[A-Za-z0-9\_-]{3,64}$/  An unique, caller-selected ID of the business. Required if pickup\_address object is not passed in. If `external_business_id` is used, `external_store_id` is required. Can't be used with `external_business_name`. |
| external\_store\_id | string  A unique identifier, defined by you, which can be used to track the specific store that the delivery is for. Required if `pickup_address` object is not passed in. If `external_store_id` is used, `external_business_name` is required. |
| contains\_alcohol | boolean  If true, flags the order as one that contains alcoholic beverages. This ensures that the driver will check the recipient's ID upon delivery. |
| requires\_catering\_setup | boolean  If true, flags the order as one that requires special setup at the consumer's location. |
| num\_items | integer <int32>  The total number of items in the order. |
| signature\_required | boolean  If true, flags the order as one that requires a signature from the consumer. Cannot be true if `allow_unattended_delivery` is true. |
| allow\_unattended\_delivery | boolean  If true, flags the order as one that does not require the customer to be present to receive the delivery. Cannot be true if `signature_required` is true and/or contains restricted items. |
| cash\_on\_delivery | integer  >= 0  Optional value in cents. Default is `None`. Cash orders must be contact not contactless orders and cash value must be greater than all fees. There maybe a limit up to a certain $ amount depending on Mx |
| delivery\_metadata | object  A JSON document that allows adding metadata about the delivery such as item weight, size, etc. |
| allowed\_vehicles | Array of arrays  Items Enum: "car" "bicycle" "walker"  An array of vehicles that are allowed to be used to complete this delivery. The only values that can be specified in the array are 'car', 'bicycle', or 'walker'. |
| is\_contactless\_delivery | boolean  Allows for order to be dropped off without physically handing delivery to consumer |
| promotion\_id | string  The ID of the promotion that you want to apply to the delivery. The fee in the response will reflect the promotion if this ID is valid. If the ID is invalid, field error will be returned. Contact your account manager for any configured promotion IDs. |
| order\_contains\_list | Array of arrays  Items Enum: "pharmacy\_items" "age\_restricted\_pharmacy\_items" "tobacco\_items" "hemp\_items" "otc\_items"  An object that specifies the restricted item(s) contained in this order. The values that can be specified are 'pharmacy\_items' (delivery contains pharmacy items), 'age\_restricted\_pharmacy\_items' (the order is an S3+ pharmacy order which requires ID Verification and can only be delivered to 18+ year olds), 'tobacco\_items' (delivery contains tobacco items, requires ID Verification), 'hemp\_items' (delivery contains hemp items, requires ID Verification), 'otc\_items' (delivery contains otc items, requires ID Verification) |
| pin\_code\_verification\_metadata | object  An object that contains dropoff pin code verification metadata. Please reach out to Doordash to enable this feature for your business. |

### Responses

**200**

**400** 

Bad request

**409**

**5XX** 

* Please retry all 50x response status codes as the error could be transient. We recommend up to 3 retries with some exponential backoff delay between requests.
* When providing a time to any of the below APIs (i.e. `pickup_time` or `delivery_time`), the format must be UTC.'

post/drive/v1/deliveries

https://openapi.doordash.com/drive/v1/deliveries

### Request samples

* Payload

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "pickup_address": {
  + "city": "San Francisco",
  + "state": "California",
  + "street": "101 Howard Street",
  + "unit": "Apt 301",
  + "zip_code": 94105,
  + "location": {
    - "lng": -122.431297,
    - "lat": 37.773972}},
* "pickup_phone_number": "+16505555555",
* "dropoff_address": {
  + "city": "San Francisco",
  + "state": "California",
  + "street": "901 Market Street",
  + "unit": "Suite #600",
  + "zip_code": "94105",
  + "full_address": "901 Market Street 6th Floor, San Francisco, CA 94103",
  + "location": {
    - "lat": 37.78,
    - "lng": -122.4}},
* "customer": {
  + "phone_number": "+16505555555",
  + "business_name": "Mega Corp HQ",
  + "first_name": "Jane",
  + "last_name": "Goodall",
  + "email": "[email protected]",
  + "should_send_notifications": true,
  + "locale": "en-US"},
* "order_value": 1999,
* "pickup_time": "2018-08-22T17:20:28Z",
* "delivery_time": "2018-08-22T17:21:28Z",
* "pickup_window_start_time": "2018-08-22T17:20:12Z",
* "pickup_window_end_time": "2018-08-22T17:40:28Z",
* "delivery_window_start_time": "2018-08-22T18:15:28Z",
* "delivery_window_end_time": "2018-08-22T18:35:28Z",
* "items": [
  + {
    - "name": "Mega Bean and Cheese Burrito",
    - "description": "Mega Burrito contains the biggest beans of the land with extra cheese.",
    - "barcode": "12342830041",
    - "quantity": 2,
    - "external_id": "123-123443434b",
    - "volume": 5.3,
    - "weight": 2.8,
    - "length": 2.8,
    - "width": 2.8,
    - "height": 2.8,
    - "price": 1000}],
* "team_lift_required": true,
* "barcode_scanning_required": false,
* "pickup_business_name": "Chipotle",
* "pickup_instructions": "Enter gate code 1234 on the callbox.",
* "dropoff_instructions": "Lock the front door after delivering the food.",
* "order_volume": 5,
* "tip": 500,
* "external_delivery_id": "1342666-2420",
* "driver_reference_tag": "1",
* "external_business_name": "1443432456",
* "external_business_id": "a0720d55-7cbe-41ce-8185-58285b7985cd",
* "external_store_id": "mega-corp-2340593",
* "contains_alcohol": false,
* "requires_catering_setup": true,
* "num_items": 1,
* "signature_required": false,
* "allow_unattended_delivery": true,
* "cash_on_delivery": 1000,
* "delivery_metadata": {
  + "foo": "bar"},
* "allowed_vehicles": [
  + "car",
  + "bicycle"],
* "is_contactless_delivery": false,
* "promotion_id": "ee680b87-0016-496e-ac3c-d3f33ab54c1c",
* "order_contains_list": [
  + "pharmacy_items",
  + "age_restricted_pharmacy_items",
  + "tobacco_items",
  + "hemp_items",
  + "otc_items"],
* "pin_code_verification_metadata": {
  + "pin_code_type": "customer_phone_number",
  + "pin_code_value": "1234"}

}`

### Response samples

* 200
* 400
* 409

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "rating": "string",
* "pickup_window_start_time": "2018-08-22T17:20:12Z",
* "pickup_window_end_time": "2018-08-22T17:40:28Z",
* "delivery_window_start_time": "2018-08-22T18:15:28Z",
* "delivery_window_end_time": "2018-08-22T18:35:28Z",
* "actual_return_time": "2018-08-22T18:35:28Z",
* "driver_reference_tag": "ABD13234",
* "contains_alcohol": true,
* "updated_at": "2018-08-22T18:35:28Z",
* "currency": "USD",
* "estimated_pickup_time": "2018-08-22T18:35:28Z",
* "order_volume": 3,
* "id": 0,
* "dasher_status": "unassigned",
* "estimated_delivery_time": "2018-08-22T18:35:28Z",
* "fee": 1900,
* "fee_components": [
  + {
    - "type": "distance_based_fee",
    - "amount": 1900}],
* "tax": 520,
* "tax_components": [
  + {
    - "type": "gst_hst",
    - "amount": 520}],
* "quoted_pickup_time": "2018-08-22T17:20:28Z",
* "dropoff_address": {
  + "city": "San Francisco",
  + "state": "California",
  + "street": "901 Market Street",
  + "unit": "Suite #600",
  + "zip_code": "94105",
  + "dasher_parking_details": "Parking Stall 1234"},
* "allow_unattended_delivery": false,
* "tip": 500,
* "team_lift_required": true,
* "external_store_id": "148767394",
* "pickup_instructions": "Use the back alley of the store for pickup",
* "dasher": {
  + "id": 1232142,
  + "first_name": "John",
  + "last_name": "Wick",
  + "phone_number": "+1-501-234-1343",
  + "dasher_phone_number_for_customer": "+1-501-234-1343",
  + "profile_image_url": "string",
  + "vehicle": {
    - "color": "",
    - "make": "Toyota",
    - "model": "Corolla",
    - "license_plate_number": "",
    - "year": "2006"},
  + "location": {
    - "lat": 123.1312343,
    - "lng": -37.2144343}},
* "status": "scheduled",
* "quoted_delivery_time": "2018-08-22T18:35:28Z",
* "actual_pickup_time": "2018-08-22T18:35:28Z",
* "signature_required": false,
* "pickup_address": {
  + "city": "San Francisco",
  + "state": "California",
  + "street": "101 Howard Street",
  + "unit": "Apt 301",
  + "zip_code": "94105",
  + "dasher_parking_details": "Parking Stall 1234"},
* "barcode_scanning_required": false,
* "delivery_tracking_url": "http://drd.sh/d035NtWrk/",
* "external_delivery_id": "1342666-2420",
* "customer": {
  + "phone_number": "+16505555555",
  + "business_name": "Mega Corp HQ",
  + "first_name": "Jane",
  + "last_name": "Goodall",
  + "email": "[email protected]",
  + "should_send_notifications": true,
  + "locale": "en-US"},
* "order_value": 14000,
* "items": [
  + {
    - "name": "Mega Bean and Cheese Burrito",
    - "description": "Mega Burrito contains the biggest beans of the land with extra cheese.",
    - "barcode": "12342830041",
    - "scan_status": "unknown",
    - "quantity": 2,
    - "external_id": "123-123443434b",
    - "volume": 5.3,
    - "weight": 2.8,
    - "price": 1000}],
* "dropoff_instructions": "Please call me to buzz you in",
* "actual_delivery_time": "string",
* "signature_image_url": "https://doordash-static.s3-us-west-2.amazonaws.com/media/drive/drive-logo.png",
* "quantity": 1,
* "delivery_verification_image_url": "https://doordash-static.s3-us-west-2.amazonaws.com/media/drive/drive-logo.png",
* "pickup_verification_image_url": "https://doordash-static.s3-us-west-2.amazonaws.com/media/drive/drive-logo.png",
* "relationship_type": "Self",
* "relationship_description": "Brother",
* "order_contains_list": [
  + "pharmacy_items",
  + "age_restricted_pharmacy_items",
  + "tobacco_items",
  + "hemp_items",
  + "otc_items"],
* "pin_code_verification_metadata": {
  + "pin_code_type": "customer_phone_number",
  + "pin_code_value": "1234"}

}`

## Delivery Details

Get details for a delivery

##### path Parameters

|  |  |
| --- | --- |
| delivery\_id required | string  Id of the delivery that was created via the Create Delivery API call. |

##### query Parameters

|  |  |
| --- | --- |
| extra | string  Value: "cash\_on\_delivery"  Optional parameter requesting any cash on delivery details |

### Responses

**200** 

Delivery object by id

**400** 

Bad request

**5XX** 

* Please retry all 50x response status codes as the error could be transient. We recommend up to 3 retries with some exponential backoff delay between requests.
* When providing a time to any of the below APIs (i.e. `pickup_time` or `delivery_time`), the format must be UTC.'

get/drive/v1/deliveries/{delivery\_id}

https://openapi.doordash.com/drive/v1/deliveries/{delivery\_id}

### Response samples

* 200
* 400

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "rating": "string",
* "pickup_window_start_time": "2018-08-22T17:20:12Z",
* "pickup_window_end_time": "2018-08-22T17:40:28Z",
* "delivery_window_start_time": "2018-08-22T18:15:28Z",
* "delivery_window_end_time": "2018-08-22T18:35:28Z",
* "actual_return_time": "2018-08-22T18:35:28Z",
* "driver_reference_tag": "ABD13234",
* "contains_alcohol": true,
* "updated_at": "2018-08-22T18:35:28Z",
* "currency": "USD",
* "estimated_pickup_time": "2018-08-22T18:35:28Z",
* "order_volume": 3,
* "id": 0,
* "dasher_status": "unassigned",
* "estimated_delivery_time": "2018-08-22T18:35:28Z",
* "fee": 1900,
* "fee_components": [
  + {
    - "type": "distance_based_fee",
    - "amount": 1900}],
* "tax": 520,
* "tax_components": [
  + {
    - "type": "gst_hst",
    - "amount": 520}],
* "quoted_pickup_time": "2018-08-22T17:20:28Z",
* "dropoff_address": {
  + "city": "San Francisco",
  + "state": "California",
  + "street": "901 Market Street",
  + "unit": "Suite #600",
  + "zip_code": "94105",
  + "dasher_parking_details": "Parking Stall 1234"},
* "allow_unattended_delivery": false,
* "tip": 500,
* "team_lift_required": true,
* "external_store_id": "148767394",
* "pickup_instructions": "Use the back alley of the store for pickup",
* "dasher": {
  + "id": 1232142,
  + "first_name": "John",
  + "last_name": "Wick",
  + "phone_number": "+1-501-234-1343",
  + "dasher_phone_number_for_customer": "+1-501-234-1343",
  + "profile_image_url": "string",
  + "vehicle": {
    - "color": "",
    - "make": "Toyota",
    - "model": "Corolla",
    - "license_plate_number": "",
    - "year": "2006"},
  + "location": {
    - "lat": 123.1312343,
    - "lng": -37.2144343}},
* "status": "scheduled",
* "quoted_delivery_time": "2018-08-22T18:35:28Z",
* "actual_pickup_time": "2018-08-22T18:35:28Z",
* "signature_required": false,
* "pickup_address": {
  + "city": "San Francisco",
  + "state": "California",
  + "street": "101 Howard Street",
  + "unit": "Apt 301",
  + "zip_code": "94105",
  + "dasher_parking_details": "Parking Stall 1234"},
* "barcode_scanning_required": false,
* "delivery_tracking_url": "http://drd.sh/d035NtWrk/",
* "external_delivery_id": "1342666-2420",
* "customer": {
  + "phone_number": "+16505555555",
  + "business_name": "Mega Corp HQ",
  + "first_name": "Jane",
  + "last_name": "Goodall",
  + "email": "[email protected]",
  + "should_send_notifications": true,
  + "locale": "en-US"},
* "order_value": 14000,
* "items": [
  + {
    - "name": "Mega Bean and Cheese Burrito",
    - "description": "Mega Burrito contains the biggest beans of the land with extra cheese.",
    - "barcode": "12342830041",
    - "scan_status": "unknown",
    - "quantity": 2,
    - "external_id": "123-123443434b",
    - "volume": 5.3,
    - "weight": 2.8,
    - "price": 1000}],
* "dropoff_instructions": "Please call me to buzz you in",
* "actual_delivery_time": "string",
* "signature_image_url": "https://doordash-static.s3-us-west-2.amazonaws.com/media/drive/drive-logo.png",
* "quantity": 1,
* "delivery_verification_image_url": "https://doordash-static.s3-us-west-2.amazonaws.com/media/drive/drive-logo.png",
* "pickup_verification_image_url": "https://doordash-static.s3-us-west-2.amazonaws.com/media/drive/drive-logo.png",
* "relationship_type": "Self",
* "relationship_description": "Brother",
* "order_contains_list": [
  + "pharmacy_items",
  + "age_restricted_pharmacy_items",
  + "tobacco_items",
  + "hemp_items",
  + "otc_items"],
* "pin_code_verification_metadata": {
  + "pin_code_type": "customer_phone_number",
  + "pin_code_value": "1234"}

}`

## Update Delivery

Update the time or address for a delivery

##### path Parameters

|  |  |
| --- | --- |
| delivery\_id required | string  Id of the delivery that was created via the Create Delivery API call. |

##### Request Body schema: application/json

|  |  |
| --- | --- |
| pickup\_business\_name | string  The name of the business where the order should be picked up from. |
| pickup\_instructions | string  Instructions for the Dasher to follow upon pickup of the order. |
| pickup\_phone\_number | string  The phone number for the Dasher to call, including country code, if there are any issues with the pick up. The phone number must be a valid US phone number. |
| quoted\_delivery\_time | string  The newly requested UTC date-time (in ISO-8601 format) at which the order should be delivered. If this field is specified, then `quoted_pickup_time` cannot be specified. |
| quoted\_pickup\_time | string  The newly requested UTC date-time (in ISO-8601 format) at which the order should be picked up. If this field is specified, then `quoted_delivery_time` cannot be specified. |
| pickup\_window\_start\_time | string  The UTC date-time (in ISO-8601 format) overrides `delivery_time` and `pickup_time` when all four parameters of the delivery window (i.e. `pickup_window_start_time`, `pickup_window_end_time`, `delivery_window_start_time`, `delivery_window_end_time`) are provided. |
| pickup\_window\_end\_time | string  The UTC date-time (in ISO-8601 format) overrides `delivery_time` and `pickup_time` when all four parameters of the delivery window (i.e. `pickup_window_start_time`, `pickup_window_end_time`, `delivery_window_start_time`, `delivery_window_end_time`) are provided. |
| delivery\_window\_start\_time | string  The UTC date-time (in ISO-8601 format) overrides `delivery_time` and `pickup_time` when all four parameters of the delivery window (i.e. `pickup_window_start_time`, `pickup_window_end_time`, `delivery_window_start_time`, `delivery_window_end_time`) are provided. |
| delivery\_window\_end\_time | string  The UTC date-time (in ISO-8601 format) overrides `delivery_time` and `pickup_time` when all four parameters of the delivery window (i.e. `pickup_window_start_time`, `pickup_window_end_time`, `delivery_window_start_time`, `delivery_window_end_time`) are provided. |
| dropoff\_address | object (The address where the delivery needs to be dropped off.)  The address where the delivery needs to be dropped off. |
| first\_name | string  The customer's updated first name. |
| last\_name | string  The customer's updated last name. |
| business\_name | string  The customer's new business name. |
| customer\_phone\_number | string  The customer's new phone number including the country code. |
| dropoff\_special\_instructions | string  New instructions for the driver to follow upon delivery of the order. |
| signature\_required | boolean  If true, flags the order as one that requires a signature from the consumer. Cannot be true if `allow_unattended_delivery` is true. |
| allow\_unattended\_delivery | boolean  If true, flags the order as one that does not require the customer to be present to receive the delivery. Cannot be true if `signature_required` is true and/or contain restricted items. |
| contains\_alcohol | boolean  If true, flags the order as one that contains alcoholic beverages. This ensures that the driver will check the recipient's ID upon delivery. |
| delivery\_metadata | object  A dictionary that allows adding metadata about the delivery such as item weight, size, etc. |
| allowed\_vehicles | Array of arrays  An array of vehicles that are allowed to be used to complete this delivery. The only values that can be specified in the array are 'car', 'bicycle', or 'walker'. |
| tip | integer <int32>  The tip (in cents) to be provided after the given delivery is completed. |
| order\_ready\_time | string  The UTC time at which the order was actually ready at the pickup location. |
| order\_contains\_list | Array of arrays  Items Enum: "tobacco\_items" "hemp\_items" "otc\_items"  An object that specifies the restricted item(s) contained in this order. The values that can be specified are 'tobacco\_items' (delivery contains tobacco items, requires ID Verification), 'hemp\_items' (delivery contains hemp items, requires ID Verification), 'otc\_items' (delivery contains otc items, requires ID Verification) |

### Responses

**200** 

Updated delivery object

**400** 

Bad Request.

**404** 

Delivery not found.

**5XX** 

* Please retry all 50x response status codes as the error could be transient. We recommend up to 3 retries with some exponential backoff delay between requests.
* When providing a time to any of the below APIs (i.e. `pickup_time` or `delivery_time`), the format must be UTC.'

patch/drive/v1/deliveries/{delivery\_id}

https://openapi.doordash.com/drive/v1/deliveries/{delivery\_id}

### Request samples

* Payload

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "pickup_business_name": "Chipotle",
* "pickup_instructions": "Enter gate code 1234 on the callbox.",
* "pickup_phone_number": "+15555555555",
* "quoted_delivery_time": "2018-08-22T17:21:28Z",
* "quoted_pickup_time": "2018-08-22T17:20:28Z",
* "pickup_window_start_time": "2018-08-22T17:20:28Z",
* "pickup_window_end_time": "2018-08-22T17:21:28Z",
* "delivery_window_start_time": "2018-08-22T17:22:28Z",
* "delivery_window_end_time": "2018-08-22T17:23:28Z",
* "dropoff_address": {
  + "city": "San Francisco",
  + "state": "California",
  + "street": "901 Market Street",
  + "unit": "Suite #600",
  + "zip_code": "94105",
  + "full_address": "901 Market Street 6th Floor, San Francisco, CA 94103",
  + "location": {
    - "lat": 37.78,
    - "lng": -122.4}},
* "first_name": "John",
* "last_name": "Smith",
* "business_name": "Some Company Inc",
* "customer_phone_number": "+15555555555",
* "dropoff_special_instructions": "Lock the front door after delivering the food.",
* "signature_required": false,
* "allow_unattended_delivery": false,
* "contains_alcohol": false,
* "delivery_metadata": {
  + "weight": "foo",
  + "volume": "bar",
  + "contains_batteries": true},
* "allowed_vehicles": [
  + "car",
  + "bicycle",
  + "walker"],
* "tip": 1300,
* "order_ready_time": "2018-08-22T17:20:28Z",
* "order_contains_list": [
  + "tobacco_items",
  + "hemp_items",
  + "otc_items"]

}`

### Response samples

* 200
* 400

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "rating": "string",
* "pickup_window_start_time": "2018-08-22T17:20:12Z",
* "pickup_window_end_time": "2018-08-22T17:40:28Z",
* "delivery_window_start_time": "2018-08-22T18:15:28Z",
* "delivery_window_end_time": "2018-08-22T18:35:28Z",
* "actual_return_time": "2018-08-22T18:35:28Z",
* "driver_reference_tag": "ABD13234",
* "contains_alcohol": true,
* "updated_at": "2018-08-22T18:35:28Z",
* "currency": "USD",
* "estimated_pickup_time": "2018-08-22T18:35:28Z",
* "order_volume": 3,
* "id": 0,
* "dasher_status": "unassigned",
* "estimated_delivery_time": "2018-08-22T18:35:28Z",
* "fee": 1900,
* "fee_components": [
  + {
    - "type": "distance_based_fee",
    - "amount": 1900}],
* "tax": 520,
* "tax_components": [
  + {
    - "type": "gst_hst",
    - "amount": 520}],
* "quoted_pickup_time": "2018-08-22T17:20:28Z",
* "dropoff_address": {
  + "city": "San Francisco",
  + "state": "California",
  + "street": "901 Market Street",
  + "unit": "Suite #600",
  + "zip_code": "94105",
  + "dasher_parking_details": "Parking Stall 1234"},
* "allow_unattended_delivery": false,
* "tip": 500,
* "team_lift_required": true,
* "external_store_id": "148767394",
* "pickup_instructions": "Use the back alley of the store for pickup",
* "dasher": {
  + "id": 1232142,
  + "first_name": "John",
  + "last_name": "Wick",
  + "phone_number": "+1-501-234-1343",
  + "dasher_phone_number_for_customer": "+1-501-234-1343",
  + "profile_image_url": "string",
  + "vehicle": {
    - "color": "",
    - "make": "Toyota",
    - "model": "Corolla",
    - "license_plate_number": "",
    - "year": "2006"},
  + "location": {
    - "lat": 123.1312343,
    - "lng": -37.2144343}},
* "status": "scheduled",
* "quoted_delivery_time": "2018-08-22T18:35:28Z",
* "actual_pickup_time": "2018-08-22T18:35:28Z",
* "signature_required": false,
* "pickup_address": {
  + "city": "San Francisco",
  + "state": "California",
  + "street": "101 Howard Street",
  + "unit": "Apt 301",
  + "zip_code": "94105",
  + "dasher_parking_details": "Parking Stall 1234"},
* "barcode_scanning_required": false,
* "delivery_tracking_url": "http://drd.sh/d035NtWrk/",
* "external_delivery_id": "1342666-2420",
* "customer": {
  + "phone_number": "+16505555555",
  + "business_name": "Mega Corp HQ",
  + "first_name": "Jane",
  + "last_name": "Goodall",
  + "email": "[email protected]",
  + "should_send_notifications": true,
  + "locale": "en-US"},
* "order_value": 14000,
* "items": [
  + {
    - "name": "Mega Bean and Cheese Burrito",
    - "description": "Mega Burrito contains the biggest beans of the land with extra cheese.",
    - "barcode": "12342830041",
    - "scan_status": "unknown",
    - "quantity": 2,
    - "external_id": "123-123443434b",
    - "volume": 5.3,
    - "weight": 2.8,
    - "price": 1000}],
* "dropoff_instructions": "Please call me to buzz you in",
* "actual_delivery_time": "string",
* "signature_image_url": "https://doordash-static.s3-us-west-2.amazonaws.com/media/drive/drive-logo.png",
* "quantity": 1,
* "delivery_verification_image_url": "https://doordash-static.s3-us-west-2.amazonaws.com/media/drive/drive-logo.png",
* "pickup_verification_image_url": "https://doordash-static.s3-us-west-2.amazonaws.com/media/drive/drive-logo.png",
* "relationship_type": "Self",
* "relationship_description": "Brother",
* "order_contains_list": [
  + "pharmacy_items",
  + "age_restricted_pharmacy_items",
  + "tobacco_items",
  + "hemp_items",
  + "otc_items"],
* "pin_code_verification_metadata": {
  + "pin_code_type": "customer_phone_number",
  + "pin_code_value": "1234"}

}`

## Cancel Delivery

Cancel OR initiate a return for a delivery

##### path Parameters

|  |  |
| --- | --- |
| delivery\_id required | string  Id of the delivery that was created via the Create Delivery API call. |

##### Request Body schema: application/json

OPTIONAL: should be left blank for normal cancellations. If cancelling for a specific reason, provide a return code (Ex: to create a cold chain return, return code should be "cold\_chain".)

|  |  |
| --- | --- |
| reason\_code | string  OPTIONAL: should be left blank for normal cancellations. If cancelling for a specific reason, provide a return code (Ex: to create a cold chain return, return code should be "cold\_chain".) |

### Responses

**200**

**400** 

Delivery cannot be cancelled due to the following reasons

* Delivery already confirmed by restaurant
* Delivery can not be cancelled so close to estimated pickup time

**404** 

Delivery not found

**5XX** 

* Please retry all 50x response status codes as the error could be transient. We recommend up to 3 retries with some exponential backoff delay between requests.
* When providing a time to any of the below APIs (i.e. `pickup_time` or `delivery_time`), the format must be UTC.'

put/drive/v1/deliveries/{delivery\_id}/cancel

https://openapi.doordash.com/drive/v1/deliveries/{delivery\_id}/cancel

### Request samples

* Payload

Content type

application/json

Copy

`{

* "reason_code": "cold_chain"

}`

### Response samples

* 200

Content type

application/json

Copy

`{

* "return_initiated": true,
* "cancelled_at": "string"

}`

# Business & Store

## Get Business

Get the details of a business.

##### path Parameters

|  |  |
| --- | --- |
| external\_business\_id required | string  Unique, caller-selected ID of the business. Validated using the following regular expression: `/^[A-Za-z0-9_-]{3,64}$/` . |

### Responses

**200** 

OK

**400** 

Request validation failed

**403** 

Operation not authorized

**404** 

Unknown external business ID

**500** 

Internal service failure, please try again later

get/developer/v1/businesses/{external\_business\_id}

https://openapi.doordash.com/developer/v1/businesses/{external\_business\_id}

### Response samples

* 200
* 400
* 403
* 404
* 500

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "name": "Neighborhood Deli",
* "description": "A neighborhood deli serving many tasty sandwiches and soups.",
* "external_business_id": "a0720d55-7cbe-41ce-8185-58285b7985cd",
* "activation_status": "active",
* "created_at": "2022-04-25T17:21:43Z",
* "last_updated_at": "2022-04-25T17:21:43Z",
* "is_test": false,
* "external_metadata": {
  + "number_of_stores": "10",
  + "client_email": "[email protected]",
  + "client_phone_number": "+12065551212",
  + "external_store_ids": [
    - null]}

}`

## Update Business

Update the attributes of a business.

##### path Parameters

|  |  |
| --- | --- |
| external\_business\_id required | string  Unique, caller-selected ID of the business. Validated using the following regular expression: `/^[A-Za-z0-9_-]{3,64}$/` . |

##### Request Body schema: application/json

|  |  |
| --- | --- |
| name | string (Business Name) Any non empty string  Human readable name for the business. Used when the details of a business are shown to a customer, Dasher, merchant, or support agent. |
| description | string (BusinessDescription) Any non empty string  Short description of the business. Used in the DoorDash Merchant Portal. Maximum length of description is 100 characters |
| activation\_status | string (BusinessActivationStatus)  Enum: "initiated" "pending\_external\_activation" "pending\_legal\_agreement" "abandoned" "failed" "active" "inactive"  Activation status of the business. Used primarily for the automatic self-serve onboarding flow. |

### Responses

**200** 

OK

**400** 

Request validation failed

**403** 

Operation not authorized

**404** 

Unknown external business ID

**500** 

Internal service failure, please try again later

patch/developer/v1/businesses/{external\_business\_id}

https://openapi.doordash.com/developer/v1/businesses/{external\_business\_id}

### Request samples

* Payload

Content type

application/json

Copy

`{

* "name": "Neighborhood Deli",
* "description": "A neighborhood deli serving many tasty sandwiches and soups.",
* "activation_status": "active"

}`

### Response samples

* 200
* 400
* 403
* 404
* 500

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "name": "Neighborhood Deli",
* "description": "A neighborhood deli serving many tasty sandwiches and soups.",
* "external_business_id": "a0720d55-7cbe-41ce-8185-58285b7985cd",
* "activation_status": "active",
* "created_at": "2022-04-25T17:21:43Z",
* "last_updated_at": "2022-04-25T17:21:43Z",
* "is_test": false,
* "external_metadata": {
  + "number_of_stores": "10",
  + "client_email": "[email protected]",
  + "client_phone_number": "+12065551212",
  + "external_store_ids": [
    - null]}

}`

## Create Business

Create a Drive business. You cannot create a business with string "default" as external\_business\_id. "default" is reserved for automatically created business during developer onboarding.

##### Request Body schema: application/json

|  |  |
| --- | --- |
| external\_business\_id required | string (BizExternalBusinessId) /^[A-Za-z0-9\_-]{3,64}$/  Unique, caller-selected ID of the business. |
| name required | string (Business Name) Any non empty string  Human readable name for the business. Used when the details of a business are shown to a customer, Dasher, merchant, or support agent. |
| description | string (BusinessDescription) Any non empty string  Short description of the business. Used in the DoorDash Merchant Portal. Maximum length of description is 100 characters |
| activation\_status | string (BusinessActivationStatus)  Enum: "initiated" "pending\_external\_activation" "pending\_legal\_agreement" "abandoned" "failed" "active" "inactive"  Activation status of the business. Used primarily for the automatic self-serve onboarding flow. |

### Responses

**200** 

OK

**400** 

Request validation failed

**403** 

Operation not authorized

**500** 

Internal service failure, please try again later

post/developer/v1/businesses

https://openapi.doordash.com/developer/v1/businesses

### Request samples

* Payload

Content type

application/json

Copy

`{

* "external_business_id": "a0720d55-7cbe-41ce-8185-58285b7985cd",
* "name": "Neighborhood Deli",
* "description": "A neighborhood deli serving many tasty sandwiches and soups.",
* "activation_status": "active"

}`

### Response samples

* 200
* 400
* 403
* 500

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "name": "Neighborhood Deli",
* "description": "A neighborhood deli serving many tasty sandwiches and soups.",
* "external_business_id": "a0720d55-7cbe-41ce-8185-58285b7985cd",
* "activation_status": "active",
* "created_at": "2022-04-25T17:21:43Z",
* "last_updated_at": "2022-04-25T17:21:43Z",
* "is_test": false,
* "external_metadata": {
  + "number_of_stores": "10",
  + "client_email": "[email protected]",
  + "client_phone_number": "+12065551212",
  + "external_store_ids": [
    - null]}

}`

## List Businesses

List the businesses owned by a developer.

##### query Parameters

|  |  |
| --- | --- |
| activationStatus | string (BusinessActivationStatus)  Enum: "initiated" "pending\_external\_activation" "pending\_legal\_agreement" "abandoned" "failed" "active" "inactive"  Example:  activationStatus=active  Activation status of the business. Used primarily for the automatic self-serve onboarding flow. |
| continuationToken | string  Opaque string that can be used to fetch next page of businesses, the token value will be null if there are no more businesses to fetch. Page size is 100 businesses. |

### Responses

**200** 

OK

**400** 

Request validation failed

**403** 

Operation not authorized

**500** 

Internal service failure, please try again later

get/developer/v1/businesses

https://openapi.doordash.com/developer/v1/businesses

### Response samples

* 200
* 400
* 403
* 500

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "result": [
  + {
    - "name": "Neighborhood Deli",
    - "description": "A neighborhood deli serving many tasty sandwiches and soups.",
    - "external_business_id": "a0720d55-7cbe-41ce-8185-58285b7985cd",
    - "activation_status": "active",
    - "created_at": "2022-04-25T17:21:43Z",
    - "last_updated_at": "2022-04-25T17:21:43Z",
    - "is_test": false,
    - "external_metadata": {
      * "number_of_stores": "10",
      * "client_email": "[email protected]",
      * "client_phone_number": "+12065551212",
      * "external_store_ids": [
        + null]}}],
* "continuation_token": "string",
* "result_count": 0

}`

## Get Store

Get the details of a store.

##### path Parameters

|  |  |
| --- | --- |
| external\_business\_id required | string  Unique, caller-selected ID of the business. Validated using the following regular expression: `/^[A-Za-z0-9_-]{3,64}$/` . |
| external\_store\_id required | string  Unique, caller-selected ID for the store. Validated using the following regular expression: `/^[A-Za-z0-9_-]{3,64}$/` . |

### Responses

**200** 

OK

**400** 

Request validation failed

**403** 

Operation not authorized

**404** 

Store not found under this external business ID

**500** 

Internal service failure, please try again later

get/developer/v1/businesses/{external\_business\_id}/stores/{external\_store\_id}

https://openapi.doordash.com/developer/v1/businesses/{external\_business\_id}/stores/{external\_store\_id}

### Response samples

* 200
* 400
* 403
* 404
* 500

Content type

application/json

Copy

`{

* "name": "Neighborhood Deli #10",
* "external_business_id": "a0720d55-7cbe-41ce-8185-58285b7985cd",
* "external_store_id": "ed178ef3-b486-4ce8-8baa-5bc9f0f3fa4a",
* "phone_number": "+12065551212",
* "address": "901 Market Street, 6th Floor, San Francisco, CA, 94103",
* "status": "active",
* "is_test": false,
* "created_at": "2022-04-25T17:21:43Z",
* "last_updated_at": "2022-04-25T17:21:43Z"

}`

## Update Store

Update the attributes of a store.

##### path Parameters

|  |  |
| --- | --- |
| external\_business\_id required | string  Unique, caller-selected ID of the business. Validated using the following regular expression: `/^[A-Za-z0-9_-]{3,64}$/` . |
| external\_store\_id required | string  Unique, caller-selected ID for the store. Validated using the following regular expression: `/^[A-Za-z0-9_-]{3,64}$/` . |

##### Request Body schema: application/json

|  |  |
| --- | --- |
| name | string (Store Name) Any non empty string  The name of the store. |
| phone\_number | string (StorePhoneNumber) Any non empty string, validated by country  Phone number of the store. Used when a customer, Dasher, or support agent needs to contact the store. |
| address | string (StoreAddress) Any non empty string  The full address of the store, in the order appropriate for your locale, with each element separated by a comma. |

### Responses

**200** 

Ok

**400** 

Request validation failed

**403** 

Operation not authorized

**404** 

Store not found under this external business ID

**500** 

Internal service failure, please try again later

patch/developer/v1/businesses/{external\_business\_id}/stores/{external\_store\_id}

https://openapi.doordash.com/developer/v1/businesses/{external\_business\_id}/stores/{external\_store\_id}

### Request samples

* Payload

Content type

application/json

Copy

`{

* "name": "Neighborhood Deli #10",
* "phone_number": "+12065551212",
* "address": "901 Market Street, 6th Floor, San Francisco, CA, 94103"

}`

### Response samples

* 200
* 400
* 403
* 404
* 500

Content type

application/json

Copy

`{

* "name": "Neighborhood Deli #10",
* "external_business_id": "a0720d55-7cbe-41ce-8185-58285b7985cd",
* "external_store_id": "ed178ef3-b486-4ce8-8baa-5bc9f0f3fa4a",
* "phone_number": "+12065551212",
* "address": "901 Market Street, 6th Floor, San Francisco, CA, 94103",
* "status": "active",
* "is_test": false,
* "created_at": "2022-04-25T17:21:43Z",
* "last_updated_at": "2022-04-25T17:21:43Z"

}`

## Create Store

Create a Drive store. To create a store for your developer's default business please create stores under "default" external\_business\_id. We recommend this route if you are either an enterprise or a developer who plan to manage only one business.

##### path Parameters

|  |  |
| --- | --- |
| external\_business\_id required | string  Unique, caller-selected ID of the business. Validated using the following regular expression: `/^[A-Za-z0-9_-]{3,64}$/` . |

##### Request Body schema: application/json

|  |  |
| --- | --- |
| external\_store\_id required | string (StoreExternalStoreId) /^[A-Za-z0-9\_-]{3,64}$/  A unique ID for the store, selected or generated by the API caller. |
| name required | string (Store Name) Any non empty string  The name of the store. |
| phone\_number | string (StorePhoneNumber) Any non empty string, validated by country  Phone number of the store. Used when a customer, Dasher, or support agent needs to contact the store. |
| address required | string (StoreAddress) Any non empty string  The full address of the store, in the order appropriate for your locale, with each element separated by a comma. |

### Responses

**200** 

OK

**400** 

Request validation failed

**403** 

Operation not authorized

**404** 

Unknown external business ID

**424** 

Missing dependency to set up stores

**500** 

Internal service failure, please try again later

post/developer/v1/businesses/{external\_business\_id}/stores

https://openapi.doordash.com/developer/v1/businesses/{external\_business\_id}/stores

### Request samples

* Payload

Content type

application/json

Copy

`{

* "external_store_id": "ed178ef3-b486-4ce8-8baa-5bc9f0f3fa4a",
* "name": "Neighborhood Deli #10",
* "phone_number": "+12065551212",
* "address": "901 Market Street, 6th Floor, San Francisco, CA, 94103"

}`

### Response samples

* 200
* 400
* 403
* 404
* 424
* 500

Content type

application/json

Copy

`{

* "name": "Neighborhood Deli #10",
* "external_business_id": "a0720d55-7cbe-41ce-8185-58285b7985cd",
* "external_store_id": "ed178ef3-b486-4ce8-8baa-5bc9f0f3fa4a",
* "phone_number": "+12065551212",
* "address": "901 Market Street, 6th Floor, San Francisco, CA, 94103",
* "status": "active",
* "is_test": false,
* "created_at": "2022-04-25T17:21:43Z",
* "last_updated_at": "2022-04-25T17:21:43Z"

}`

## List Stores

List the stores under a business.

##### path Parameters

|  |  |
| --- | --- |
| external\_business\_id required | string  Unique, caller-selected ID of the business. Validated using the following regular expression: `/^[A-Za-z0-9_-]{3,64}$/` . |

##### query Parameters

|  |  |
| --- | --- |
| activationStatus | string (StoreActivationStatus)  Enum: "active" "inactive"  Activation status of the store. |
| continuationToken | string  Opaque string that can be used to fetch next page of stores, the token value will be null if there are no more stores to fetch. Page size is 100 stores. |

### Responses

**200** 

OK

**400** 

Request validation failed

**403** 

Operation not authorized

**404** 

Unknown external business ID

**500** 

Internal service failure, please try again later

get/developer/v1/businesses/{external\_business\_id}/stores

https://openapi.doordash.com/developer/v1/businesses/{external\_business\_id}/stores

### Response samples

* 200
* 400
* 403
* 404
* 500

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "result": [
  + {
    - "name": "Neighborhood Deli #10",
    - "external_business_id": "a0720d55-7cbe-41ce-8185-58285b7985cd",
    - "external_store_id": "ed178ef3-b486-4ce8-8baa-5bc9f0f3fa4a",
    - "phone_number": "+12065551212",
    - "address": "901 Market Street, 6th Floor, San Francisco, CA, 94103",
    - "status": "active",
    - "is_test": false,
    - "created_at": "2022-04-25T17:21:43Z",
    - "last_updated_at": "2022-04-25T17:21:43Z"}],
* "continuation_token": "string",
* "result_count": 0

}`