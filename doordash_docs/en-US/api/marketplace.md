[Skip to main content](#__docusaurus_skipToContent_fallback)

[![DoorDash Logo](/en-US/img/header/developer-logo.svg)![DoorDash Logo](/en-US/img/header/developer-logo.svg)](/en-US/)

Icon Loading

[Documentation](/en-US/docs/welcome)

[API Reference](#)

* [Drive](/en-US/api/drive)
* [Drive (classic)](/en-US/api/drive_classic)
* [Marketplace](/en-US/api/marketplace)
* [Marketplace (legacy)](/en-US/api/marketplace_legacy)
* [Marketplace for Retailers](/en-US/api/marketplace_v2)
* [Reporting](/en-US/api/reporting)

[Blog](/en-US/blog)

[🇺🇸 English](#)

* [🇺🇸 English](/en-US/api/marketplace)
* [🇫🇷 français](/fr-CA/api/marketplace)
* [🇪🇸 español](/es-US/api/marketplace)

[Developer Portal](https://developer.doordash.com/portal)

[![Doordash Marketplace](https://cdn.doordash.com/static/img/merchant/logo-red@3x.png)](https://developer.doordash.com/)

* Note
* Caution
* Authentication
* Menu Endpoints
  + postCreate Menu
  + patchUpdate Menu
* Order Endpoints
  + patchConfirm Order
  + patchCancel/Adjust/Substitute Items
  + patchCancel Order
  + patchOrder Events
* Store Endpoints
  + getStore Info
  + putActivate/Deactivate Store
  + putActivate/Deactivate Item
  + putActivate/Deactivate Item Options
  + getGet Store Menu Details
  + getGet Store Menu Jsons
* Models
  + StoreMenu
  + Order
  + MerchantOrderRecord
  + StoreConfirmOrderReadyForPickupRecord
  + ItemActivation
  + ItemOptionActivation
  + StoreActivationStatus
  + MxOrderAdjustRecord

[API docs by Redocly](https://redocly.com/redoc/)

# Marketplace API Specification (1.0.0)

URL: <https://openapi.doordash.com/marketplace>

# Note

API Reference: Marketplace

This is the Marketplace API Reference page. If you're an existing customer
using the Marketplace (legacy) API, see the
[Marketplace (legacy) API Reference](/api/marketplace_legacy).

  

You can tell which API you're using by checking the URL. If your API URL
is `https://openapi.doordash.com/marketplace`, you're using the
Marketplace API.

# Caution

Caution

Our Marketplace integration pipeline is currently at capacity. We are not
accepting new partners at the moment while we develop self-serve tooling
for merchant onboarding. Please fill in the
[Marketplace integration interest form](https://docs.google.com/forms/d/e/1FAIpQLSfggU_NjGWCdi9vyWUicrnzJmtu9vC4zgbfSC3ROwSvW4eV2g/viewform)
to get in touch with DoorDash **before** building your
integration.

# Authentication

See [JWT Token](/docs/marketplace/how_to/JWTs) guide

# Menu Endpoints

Endpoints for updating and creating menus

## Create Menu

##### Request Body schema: application/json

|  |  |
| --- | --- |
| reference | string |
| store required | object (Store) |
| open\_hours required | Array of objects (StoreOpenHour) |
| special\_hours required | Array of objects (StoreSpecialHour) |
| menu | object (Menu) |

### Responses

**200** 

Success

**400** 

Bad Request

**403** 

Forbidden

**404** 

Not Found

**422** 

Request Entity Too Large

**429** 

Request is rate limited

**500** 

Internal Server Error

post/api/v1/menus

https://openapi.doordash.com/marketplace/api/v1/menus

### Request samples

* Payload

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "reference": "string",
* "store": {
  + "merchant_supplied_id": "1dfa934a-190c-43a9-b2e0-449e5b8cccde",
  + "provider_type": "positouch"},
* "open_hours": [
  + {
    - "day_index": "MON",
    - "start_time": "13:00:00",
    - "end_time": "18:00:00"}],
* "special_hours": [
  + {
    - "date": "2021-12-11",
    - "closed": true,
    - "start_time": "13:00:00",
    - "end_time": "18:00:00"}],
* "menu": {
  + "name": "string",
  + "subtitle": "string",
  + "merchant_supplied_id": "string",
  + "active": true,
  + "experience": "voice",
  + "categories": [
    - {
      * "name": "string",
      * "subtitle": "string",
      * "merchant_supplied_id": "string",
      * "active": true,
      * "sort_id": 0,
      * "items": [
        + {
          - "name": "string",
          - "description": "string",
          - "merchant_supplied_id": "string",
          - "active": true,
          - "is_alcohol": true,
          - "is_bike_friendly": true,
          - "sort_id": 0,
          - "price": 0,
          - "base_price": 0,
          - "item_special_hours": [
            * {
              + "day_index": "MON",
              + "start_time": "13:00:00",
              + "end_time": "18:00:00",
              + "start_date": "string",
              + "end_date": "string"}],
          - "extras": [
            * {
              + "name": "string",
              + "merchant_supplied_id": "string",
              + "active": true,
              + "sort_id": 0,
              + "min_num_options": 0,
              + "max_num_options": 0,
              + "num_free_options": 0,
              + "min_option_choice_quantity": 0,
              + "max_option_choice_quantity": 0,
              + "min_aggregate_options_quantity": 0,
              + "max_aggregate_options_quantity": 0,
              + "options": [
                - {
                  * "name": null,
                  * "merchant_supplied_id": null,
                  * "active": null,
                  * "price": null,
                  * "base_price": null,
                  * "default": null,
                  * "sort_id": null,
                  * "tax_rate": null,
                  * "tax_category": null,
                  * "item_extra_option_special_hours": [ ],
                  * "operation_context": [ ],
                  * "quantity_info": { },
                  * "dish_info": { },
                  * "extras": [ ]}]}],
          - "tax_rate": "string",
          - "tax_category": "string",
          - "original_image_url": "string",
          - "operation_context": [
            * "string"],
          - "dish_info": {
            * "nutritional_info": {
              + "calorific_info": {
                - "display_type": "string",
                - "lower_range": 0,
                - "higher_range": 0}},
            * "classification_info": {
              + "has_side": true,
              + "is_hot": true,
              + "is_entree": true,
              + "has_alcoholic_items": true,
              + "service_types": [
                - "string"],
              + "classification_tags": [
                - "TAG_KEY_DIETARY_VEGETARIAN"]}}}]}]}

}`

### Response samples

* 200

Content type

application/json

Copy

`{

* "reference": null,
* "status": "string"

}`

## Update Menu

##### path Parameters

|  |  |
| --- | --- |
| id required | string  A Menu UUID |

##### Request Body schema: application/json

|  |  |
| --- | --- |
| reference | string |
| store required | object (Store) |
| open\_hours required | Array of objects (StoreOpenHour) |
| special\_hours required | Array of objects (StoreSpecialHour) |
| menu | object (Menu) |

### Responses

**200** 

Success

**400** 

Bad Request

**403** 

Forbidden

**404** 

Not Found

**422** 

Request Entity Too Large

**429** 

Request is rate limited

**500** 

Internal Server Error

patch/api/v1/menus/{id}

https://openapi.doordash.com/marketplace/api/v1/menus/{id}

### Request samples

* Payload

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "reference": "string",
* "store": {
  + "merchant_supplied_id": "1dfa934a-190c-43a9-b2e0-449e5b8cccde",
  + "provider_type": "positouch"},
* "open_hours": [
  + {
    - "day_index": "MON",
    - "start_time": "13:00:00",
    - "end_time": "18:00:00"}],
* "special_hours": [
  + {
    - "date": "2021-12-11",
    - "closed": true,
    - "start_time": "13:00:00",
    - "end_time": "18:00:00"}],
* "menu": {
  + "name": "string",
  + "subtitle": "string",
  + "merchant_supplied_id": "string",
  + "active": true,
  + "experience": "voice",
  + "categories": [
    - {
      * "name": "string",
      * "subtitle": "string",
      * "merchant_supplied_id": "string",
      * "active": true,
      * "sort_id": 0,
      * "items": [
        + {
          - "name": "string",
          - "description": "string",
          - "merchant_supplied_id": "string",
          - "active": true,
          - "is_alcohol": true,
          - "is_bike_friendly": true,
          - "sort_id": 0,
          - "price": 0,
          - "base_price": 0,
          - "item_special_hours": [
            * {
              + "day_index": "MON",
              + "start_time": "13:00:00",
              + "end_time": "18:00:00",
              + "start_date": "string",
              + "end_date": "string"}],
          - "extras": [
            * {
              + "name": "string",
              + "merchant_supplied_id": "string",
              + "active": true,
              + "sort_id": 0,
              + "min_num_options": 0,
              + "max_num_options": 0,
              + "num_free_options": 0,
              + "min_option_choice_quantity": 0,
              + "max_option_choice_quantity": 0,
              + "min_aggregate_options_quantity": 0,
              + "max_aggregate_options_quantity": 0,
              + "options": [
                - {
                  * "name": null,
                  * "merchant_supplied_id": null,
                  * "active": null,
                  * "price": null,
                  * "base_price": null,
                  * "default": null,
                  * "sort_id": null,
                  * "tax_rate": null,
                  * "tax_category": null,
                  * "item_extra_option_special_hours": [ ],
                  * "operation_context": [ ],
                  * "quantity_info": { },
                  * "dish_info": { },
                  * "extras": [ ]}]}],
          - "tax_rate": "string",
          - "tax_category": "string",
          - "original_image_url": "string",
          - "operation_context": [
            * "string"],
          - "dish_info": {
            * "nutritional_info": {
              + "calorific_info": {
                - "display_type": "string",
                - "lower_range": 0,
                - "higher_range": 0}},
            * "classification_info": {
              + "has_side": true,
              + "is_hot": true,
              + "is_entree": true,
              + "has_alcoholic_items": true,
              + "service_types": [
                - "string"],
              + "classification_tags": [
                - "TAG_KEY_DIETARY_VEGETARIAN"]}}}]}]}

}`

### Response samples

* 200

Content type

application/json

Copy

`{

* "reference": null,
* "status": "string"

}`

# Order Endpoints

Endpoints for retrieving and confirming success of orders

## Confirm Order

Webhook to confirm an order

##### path Parameters

|  |  |
| --- | --- |
| id required | string  Order ID |

##### Request Body schema: application/json

|  |  |
| --- | --- |
| merchant\_supplied\_id required | string  Order ID in your system |
| order\_status required | string  Enum: "success" "fail" |
| failure\_reason | string  Reason why order can't be fulfilled. Omit if order\_status = success |
| prep\_time | string  Estimated time by which order should be ready for pickup. It should be in UTC timezone |
| pickup\_instructions | string  <= 128 characters  Pickup instructions for dasher |

### Responses

**202** 

OK

**400** 

Order has already been processed or order has expired

**401** 

Request is unauthenticated

**403** 

Access is denied

**404** 

Order with provided ID does not exist

**429** 

Request is rate limited

**500** 

Internal Server Error

patch/api/v1/orders/{id}

https://openapi.doordash.com/marketplace/api/v1/orders/{id}

### Request samples

* Payload

Content type

application/json

Copy

`{

* "merchant_supplied_id": "1dfa934a-190c-43a9-b2e0-449e5b8cccde",
* "order_status": "success",
* "failure_reason": "The store is offline and cannot accept the order",
* "prep_time": "2021-07-20T21:43:47.324Z",
* "pickup_instructions": "Use the back alley of the store for pickup"

}`

## Cancel/Adjust/Substitute Items

Endpoint for merchants to cancel items, adjust item/option quantities or substitute items

##### path Parameters

|  |  |
| --- | --- |
| id required | string  Order ID |

##### Request Body schema: application/json

|  |  |
| --- | --- |
| items required | Array of items |
| |  |  | | --- | --- | | [0] | object (LineItemForUpdate) | | [1] | object (LineItemForRemove) | | [2] | object (LineItemForSubstitute) | | |

### Responses

**202** 

OK

**400** 

Order is not confirmed or has been cancelled

**404** 

Order, item, or option with provided ID does not exist

**500** 

Internal Server Error

patch/api/v1/orders/{id}/adjustment

https://openapi.doordash.com/marketplace/api/v1/orders/{id}/adjustment

### Request samples

* Payload

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "items": [
  + {
    - "line_item_id": "94b653e4-e394-4330-a714-43e764aergjn",
    - "adjustment_type": "ITEM_UPDATE",
    - "quantity": 2,
    - "substituted_item": { },
    - "options": [
      * {
        + "line_option_id": "94b653e4-e394-4330-a714-43e764aergjn",
        + "adjustment_type": "ITEM_UPDATE",
        + "quantity": 1}]},
  + {
    - "line_item_id": "94b653e4-e394-4330-a714-43e764a223",
    - "adjustment_type": "ITEM_REMOVE",
    - "substituted_item": { },
    - "options": [ ]},
  + {
    - "line_item_id": "94b653e4-e394-4330-a714-43e764ab113",
    - "adjustment_type": "ITEM_SUBSTITUTE",
    - "substituted_item": {
      * "name": "Diet Coke",
      * "merchant_supplied_id": "179",
      * "price": 2,
      * "quantity": 1},
    - "options": [ ]}]

}`

## Cancel Order

Endpoint for merchants to cancel an order

##### path Parameters

|  |  |
| --- | --- |
| id required | string  Order ID |

##### Request Body schema: application/json

|  |  |
| --- | --- |
| cancel\_reason required | string  Enum: "ITEM\_OUT\_OF\_STOCK" "STORE\_CLOSED" "KITCHEN\_BUSY" "OTHER" |
| cancel\_details | string  Reason why the order has to be cancelled |

### Responses

**202** 

OK

**400** 

Order is not confirmed or has already been cancelled

**401** 

Request is unauthenticated

**403** 

Access is denied

**404** 

Order with provided ID does not exist

**429** 

Request is rate limited

**500** 

Internal Server Error

patch/api/v1/orders/{id}/cancellation

https://openapi.doordash.com/marketplace/api/v1/orders/{id}/cancellation

### Request samples

* Payload

Content type

application/json

Copy

`{

* "cancel_reason": "STORE_CLOSED",
* "cancel_details": "The store is offline and cannot accept the order"

}`

## Order Events

Endpoint for order events. In order to use `patch_order_events`, separate token is required.

##### path Parameters

|  |  |
| --- | --- |
| id required | string  Order ID |
| event\_type required | string  Supported event types: `order_ready_for_pickup` |

##### Request Body schema: application/json

|  |  |
| --- | --- |
| merchant\_supplied\_id | string  Order ID in your system |

### Responses

**202** 

OK

**400** 

Order has expired

**401** 

Request is unauthenticated

**403** 

Access is denied

**404** 

Order with provided ID does not exist

**429** 

Request is rate limited

**500** 

Internal Server Error

patch/api/v1/orders/{id}/events/{event\_type}

https://openapi.doordash.com/marketplace/api/v1/orders/{id}/events/{event\_type}

### Request samples

* Payload

Content type

application/json

Copy

`{

* "merchant_supplied_id": "1dfa934a-190c-43a9-b2e0-449e5b8cccde"

}`

# Store Endpoints

Endpoints for store based operations

## Store Info

Get the summary information of the given store

##### path Parameters

|  |  |
| --- | --- |
| location\_id required | string  Store location id |

### Responses

**200** 

Successfully retrieved store details

**400** 

Request contains invalid arguments

**401** 

Request is unauthenticated

**403** 

Access is denied

**404** 

Store does not exist

**429** 

Request is rate limited

**500** 

Internal Server Error

get/api/v1/stores/{location\_id}/store\_details

https://openapi.doordash.com/marketplace/api/v1/stores/{location\_id}/store\_details

### Response samples

* 200

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "provider_name": "square",
* "merchant_supplied_id": "1dfa934a-190c-43a9-b2e0-449e5b8cccde",
* "is_order_protocol_pos": true,
* "auto_release_enabled": true,
* "auto_release_distance": 0,
* "special_instructions_max_length": 0,
* "current_deactivations": [
  + {
    - "reason": "Merchant operational issues",
    - "notes": "store deactivated",
    - "created_at": "2020-08-14T02:13:56.121734Z",
    - "end_time": "2021-08-20T07:00:17Z",
    - "experience": "ANY_EXPERIENCE"}]

}`

## Activate/Deactivate Store

##### path Parameters

|  |  |
| --- | --- |
| location\_id required | string  Store location id |

##### Request Body schema: application/json

|  |  |
| --- | --- |
| is\_active required | boolean  Should store be deactivated/activated. If store is being deactivated i.e. `is_active: false`, then the `reason` field in request body is required. |
| reason | string  Enum: "out\_of\_business" "operational\_issues" "delete\_store" "payment\_issue" "store\_self\_disabled\_in\_their\_POS\_portal" "store\_pos\_connectivity\_issues" |
| notes | string |
| merchant\_supplied\_id | string |
| end\_time | string  Deactivation end time in format YYYY-MM-DDTHH:MM:SS+HH:MM. |
| duration\_in\_hours | integer  Duration of the temporary deactivation in hours. Use with duration\_in\_secs. |
| duration\_in\_secs | integer  Duration of the temporary deactivation in seconds. Use with duration\_in\_hours. |

### Responses

**200** 

Successfully updated store activation status

**400** 

Request contains invalid arguments

**401** 

Request is unauthenticated

**403** 

Access is denied

**404** 

Store does not exist

**429** 

Request is rate limited

**500** 

Internal Server Error

put/api/v1/stores/{location\_id}/status

https://openapi.doordash.com/marketplace/api/v1/stores/{location\_id}/status

### Request samples

* Payload

Content type

application/json

Copy

`{

* "is_active": true,
* "reason": "operational_issues",
* "notes": "The store is offline due to operational issues",
* "merchant_supplied_id": "1dfa934a-190c-43a9-b2e0-449e5b8cccde",
* "end_time": "string",
* "duration_in_hours": 0,
* "duration_in_secs": 0

}`

## Activate/Deactivate Item

Webhook to stock in/out items for a given store

##### path Parameters

|  |  |
| --- | --- |
| merchant\_supplied\_id required | string  Store location id |

##### Request Body schema: application/json

Array

|  |  |
| --- | --- |
| merchant\_supplied\_id required | string |
| is\_active required | boolean |

### Responses

**200** 

Success

**400** 

Bad Request (If one of the item option fails to update, 400 should be returned)

**401** 

Request is unauthenticated

**403** 

Not Allowed to modify this store

**404** 

Store Not Found

**413** 

Request Entity Too Large

**429** 

Request is rate limited

**500** 

Internal Server Error

put/api/v1/stores/{merchant\_supplied\_id}/items/status

https://openapi.doordash.com/marketplace/api/v1/stores/{merchant\_supplied\_id}/items/status

### Request samples

* Payload

Content type

application/json

Copy

 Expand all  Collapse all

`[

* {
  + "merchant_supplied_id": "string",
  + "is_active": true}

]`

## Activate/Deactivate Item Options

Webhook to stock in/out item options for a given store

##### path Parameters

|  |  |
| --- | --- |
| merchant\_supplied\_id required | string  Store location id |

##### Request Body schema: application/json

Array

|  |  |
| --- | --- |
| merchant\_supplied\_id required | string |
| is\_active required | boolean |

### Responses

**200** 

Success

**400** 

Bad Request (If one of the item option fails to update, 400 should be returned)

**401** 

Request is unauthenticated

**403** 

Not Allowed to modify this store

**404** 

Store Not Found

**413** 

Request Entity Too Large

**429** 

Request is rate limited

**500** 

Internal Server Error

put/api/v1/stores/{merchant\_supplied\_id}/item\_options/status

https://openapi.doordash.com/marketplace/api/v1/stores/{merchant\_supplied\_id}/item\_options/status

### Request samples

* Payload

Content type

application/json

Copy

 Expand all  Collapse all

`[

* {
  + "merchant_supplied_id": "string",
  + "is_active": true}

]`

## Get Store Menu Details

Get the menu details of the given store

##### path Parameters

|  |  |
| --- | --- |
| merchant\_supplied\_id required | string  Store location id |

### Responses

**200** 

Successfully retrieved store menu details

**400** 

Request contains invalid arguments

**401** 

Request is unauthenticated

**403** 

Access is denied

**404** 

Store does not exist

**429** 

Request is rate limited

**500** 

Internal Server Error

get/api/v1/stores/{merchant\_supplied\_id}/menu\_details

https://openapi.doordash.com/marketplace/api/v1/stores/{merchant\_supplied\_id}/menu\_details

### Response samples

* 200

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "provider_name": "square",
* "merchant_supplied_id": "1dfa934a-190c-43a9-b2e0-449e5b8cccde",
* "menu": [
  + {
    - "menu_id": "string",
    - "name": "string",
    - "subtitle": "string",
    - "is_active": true,
    - "is_pos_menu": true,
    - "latest_menu_update": {
      * "created_at": "2019-08-24T14:15:22Z",
      * "status": "PENDING"},
    - "last_successful_menu_update_at": "2019-08-24T14:15:22Z",
    - "url": "string",
    - "open_hours": [
      * {
        + "day_index": "MON",
        + "start_time": "13:00:00",
        + "end_time": "18:00:00"}],
    - "special_hours": [
      * {
        + "date": "2021-12-11",
        + "closed": true,
        + "start_time": "13:00:00",
        + "end_time": "18:00:00"}]}]

}`

## Get Store Menu Jsons

Get the menu jsons of the given store

##### Authorizations:

None

##### path Parameters

|  |  |
| --- | --- |
| merchant\_supplied\_id required | string  Store location id |

### Responses

**200** 

Successfully retrieved store menu jsons

**400** 

Request contains invalid arguments

**401** 

Request is unauthenticated

**403** 

Access is denied

**404** 

Store does not exist

**429** 

Request is rate limited

**500** 

Internal Server Error

get/api/v1/stores/{merchant\_supplied\_id}/store\_menu

https://openapi.doordash.com/marketplace/api/v1/stores/{merchant\_supplied\_id}/store\_menu

### Response samples

* 200

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "reference": "string",
* "store": {
  + "merchant_supplied_id": "1dfa934a-190c-43a9-b2e0-449e5b8cccde",
  + "provider_type": "positouch"},
* "open_hours": [
  + {
    - "day_index": "MON",
    - "start_time": "13:00:00",
    - "end_time": "18:00:00"}],
* "special_hours": [
  + {
    - "date": "2021-12-11",
    - "closed": true,
    - "start_time": "13:00:00",
    - "end_time": "18:00:00"}],
* "menu": {
  + "name": "string",
  + "subtitle": "string",
  + "merchant_supplied_id": "string",
  + "active": true,
  + "experience": "voice",
  + "categories": [
    - {
      * "name": "string",
      * "subtitle": "string",
      * "merchant_supplied_id": "string",
      * "active": true,
      * "sort_id": 0,
      * "items": [
        + {
          - "name": "string",
          - "description": "string",
          - "merchant_supplied_id": "string",
          - "active": true,
          - "is_alcohol": true,
          - "is_bike_friendly": true,
          - "sort_id": 0,
          - "price": 0,
          - "base_price": 0,
          - "item_special_hours": [
            * {
              + "day_index": "MON",
              + "start_time": "13:00:00",
              + "end_time": "18:00:00",
              + "start_date": "string",
              + "end_date": "string"}],
          - "extras": [
            * {
              + "name": "string",
              + "merchant_supplied_id": "string",
              + "active": true,
              + "sort_id": 0,
              + "min_num_options": 0,
              + "max_num_options": 0,
              + "num_free_options": 0,
              + "min_option_choice_quantity": 0,
              + "max_option_choice_quantity": 0,
              + "min_aggregate_options_quantity": 0,
              + "max_aggregate_options_quantity": 0,
              + "options": [
                - {
                  * "name": null,
                  * "merchant_supplied_id": null,
                  * "active": null,
                  * "price": null,
                  * "base_price": null,
                  * "default": null,
                  * "sort_id": null,
                  * "tax_rate": null,
                  * "tax_category": null,
                  * "item_extra_option_special_hours": [ ],
                  * "operation_context": [ ],
                  * "quantity_info": { },
                  * "dish_info": { },
                  * "extras": [ ]}]}],
          - "tax_rate": "string",
          - "tax_category": "string",
          - "original_image_url": "string",
          - "operation_context": [
            * "string"],
          - "dish_info": {
            * "nutritional_info": {
              + "calorific_info": {
                - "display_type": "string",
                - "lower_range": 0,
                - "higher_range": 0}},
            * "classification_info": {
              + "has_side": true,
              + "is_hot": true,
              + "is_entree": true,
              + "has_alcoholic_items": true,
              + "service_types": [
                - "string"],
              + "classification_tags": [
                - "TAG_KEY_DIETARY_VEGETARIAN"]}}}]}]}

}`

# Models

## StoreMenu

|  |  |
| --- | --- |
| reference | string |
| store required | object (Store) |
| open\_hours required | Array of objects (StoreOpenHour) |
| special\_hours required | Array of objects (StoreSpecialHour) |
| menu | object (Menu) |

Copy

 Expand all  Collapse all

`{

* "reference": "string",
* "store": {
  + "merchant_supplied_id": "1dfa934a-190c-43a9-b2e0-449e5b8cccde",
  + "provider_type": "positouch"},
* "open_hours": [
  + {
    - "day_index": "MON",
    - "start_time": "13:00:00",
    - "end_time": "18:00:00"}],
* "special_hours": [
  + {
    - "date": "2021-12-11",
    - "closed": true,
    - "start_time": "13:00:00",
    - "end_time": "18:00:00"}],
* "menu": {
  + "name": "string",
  + "subtitle": "string",
  + "merchant_supplied_id": "string",
  + "active": true,
  + "experience": "voice",
  + "categories": [
    - {
      * "name": "string",
      * "subtitle": "string",
      * "merchant_supplied_id": "string",
      * "active": true,
      * "sort_id": 0,
      * "items": [
        + {
          - "name": "string",
          - "description": "string",
          - "merchant_supplied_id": "string",
          - "active": true,
          - "is_alcohol": true,
          - "is_bike_friendly": true,
          - "sort_id": 0,
          - "price": 0,
          - "base_price": 0,
          - "item_special_hours": [
            * {
              + "day_index": "MON",
              + "start_time": "13:00:00",
              + "end_time": "18:00:00",
              + "start_date": "string",
              + "end_date": "string"}],
          - "extras": [
            * {
              + "name": "string",
              + "merchant_supplied_id": "string",
              + "active": true,
              + "sort_id": 0,
              + "min_num_options": 0,
              + "max_num_options": 0,
              + "num_free_options": 0,
              + "min_option_choice_quantity": 0,
              + "max_option_choice_quantity": 0,
              + "min_aggregate_options_quantity": 0,
              + "max_aggregate_options_quantity": 0,
              + "options": [
                - {
                  * "name": null,
                  * "merchant_supplied_id": null,
                  * "active": null,
                  * "price": null,
                  * "base_price": null,
                  * "default": null,
                  * "sort_id": null,
                  * "tax_rate": null,
                  * "tax_category": null,
                  * "item_extra_option_special_hours": [ ],
                  * "operation_context": [ ],
                  * "quantity_info": { },
                  * "dish_info": { },
                  * "extras": [ ]}]}],
          - "tax_rate": "string",
          - "tax_category": "string",
          - "original_image_url": "string",
          - "operation_context": [
            * "string"],
          - "dish_info": {
            * "nutritional_info": {
              + "calorific_info": {
                - "display_type": "string",
                - "lower_range": 0,
                - "higher_range": 0}},
            * "classification_info": {
              + "has_side": true,
              + "is_hot": true,
              + "is_entree": true,
              + "has_alcoholic_items": true,
              + "service_types": [
                - "string"],
              + "classification_tags": [
                - "TAG_KEY_DIETARY_VEGETARIAN"]}}}]}]}

}`

## Order

|  |  |
| --- | --- |
| id | string |
| consumer | object (Consumer) |
| store | object (Store) |
| subtotal | integer |
| tax | integer |
| estimated\_pickup\_time | string <date-time> |
| is\_pickup | boolean |
| categories | Array of objects (OrderMenuCategory) |
| is\_tax\_remitted\_by\_doordash | boolean |
| tax\_amount\_remitted\_by\_doordash | integer |
| commission\_type | string  Enum: "regular" "dashpass" |
| delivery\_short\_code | string  short code for dasher to identify an order |
| fulfillment\_type | string  Enum: "dx\_delivery" "pickup" "mx\_fleet\_delivery"  order type of fulfillment. dx\_delivery- DoorDash delivery, pickup- consumer pickup, mx\_fleet\_delivery- merchant delivery |
| merchant\_tip\_amount | integer  tip amount for merchant staff |
| experience | string  Enum: "DOORDASH" "CAVIAR" "STOREFRONT" "WHITE\_LABELED" "DOORDASH\_CHECKOUT" "ANY\_EXPERIENCE"  experience on which the order is placed. DOORDASH- order placed on doordash, CAVIAR- order placed on caviar, STOREFRONT- order placed on storefront |
| is\_plastic\_ware\_option\_selected | boolean  Flag determining if the customer has opted for plasticware (or utensils) to be sent as part of the order |
| tip\_amount | number  Delivery tip amount. This is only sent for Self Delivery orders |

Copy

 Expand all  Collapse all

`{

* "id": "string",
* "consumer": {
  + "id": 0,
  + "email": "string",
  + "first_name": "string",
  + "last_name": "string",
  + "phone": "string"},
* "store": {
  + "merchant_supplied_id": "1dfa934a-190c-43a9-b2e0-449e5b8cccde",
  + "provider_type": "positouch"},
* "subtotal": 0,
* "tax": 0,
* "estimated_pickup_time": "2019-08-24T14:15:22Z",
* "is_pickup": true,
* "categories": [
  + {
    - "name": "string",
    - "merchant_supplied_id": "string",
    - "items": [
      * {
        + "name": "string",
        + "merchant_supplied_id": "string",
        + "price": 0,
        + "quantity": 0,
        + "extras": [
          - {
            * "name": "string",
            * "merchant_supplied_id": "string",
            * "options": [
              + {
                - "name": "string",
                - "merchant_supplied_id": "string",
                - "price": 0,
                - "quantity": 0,
                - "extras": [
                  * null],
                - "line_option_id": "string"}]}],
        + "consumer_name": "string",
        + "special_instructions": "string",
        + "line_item_id": "string"}]}],
* "is_tax_remitted_by_doordash": true,
* "tax_amount_remitted_by_doordash": 0,
* "commission_type": "regular",
* "delivery_short_code": "string",
* "fulfillment_type": "dx_delivery",
* "merchant_tip_amount": 0,
* "experience": "DOORDASH",
* "is_plastic_ware_option_selected": true,
* "tip_amount": 0

}`

## MerchantOrderRecord

|  |  |
| --- | --- |
| merchant\_supplied\_id required | string  Order ID in your system |
| order\_status required | string  Enum: "success" "fail" |
| failure\_reason | string  Reason why order can't be fulfilled. Omit if order\_status = success |
| prep\_time | string <date-time>  Estimated time by which order should be ready for pickup. It should be in UTC timezone |

Copy

`{

* "merchant_supplied_id": "string",
* "order_status": "success",
* "failure_reason": "string",
* "prep_time": "2019-08-24T14:15:22Z"

}`

## StoreConfirmOrderReadyForPickupRecord

|  |  |
| --- | --- |
| merchant\_supplied\_id | string  Order ID in your system |

Copy

`{

* "merchant_supplied_id": "string"

}`

## ItemActivation

|  |  |
| --- | --- |
| merchant\_supplied\_id required | string |
| is\_active required | boolean |

Copy

`{

* "merchant_supplied_id": "string",
* "is_active": true

}`

## ItemOptionActivation

|  |  |
| --- | --- |
| merchant\_supplied\_id required | string |
| is\_active required | boolean |

Copy

`{

* "merchant_supplied_id": "string",
* "is_active": true

}`

## StoreActivationStatus

|  |  |
| --- | --- |
| is\_active required | boolean  Should store be deactivated/activated. If store is being deactivated i.e. `"is_active": false`, then the `reason` field in request body is required |
| reason | string  Enum: "out\_of\_business" "delete\_store" "payment\_issue" "operational\_issues" "store\_self\_disabled\_in\_their\_POS\_portal" "store\_pos\_connectivity\_issues"  If store is being deactivated, then this is a required field. For store activation, this is not required. |
| notes | string |

Copy

`{

* "is_active": true,
* "reason": "out_of_business",
* "notes": "string"

}`

## MxOrderAdjustRecord

|  |  |
| --- | --- |
| items | Array of items |
| |  |  | | --- | --- | | [0] | object (LineItemForUpdate) | | [1] | object (LineItemForRemove) | | [2] | object (LineItemForSubstitute) | | |

Copy

 Expand all  Collapse all

`{

* "items": [
  + {
    - "line_item_id": "94b653e4-e394-4330-a714-43e764aergjn",
    - "adjustment_type": "ITEM_UPDATE",
    - "quantity": 2,
    - "substituted_item": { },
    - "options": [
      * {
        + "line_option_id": "94b653e4-e394-4330-a714-43e764aergjn",
        + "adjustment_type": "ITEM_UPDATE",
        + "quantity": 1}]},
  + {
    - "line_item_id": "94b653e4-e394-4330-a714-43e764a223",
    - "adjustment_type": "ITEM_REMOVE",
    - "substituted_item": { },
    - "options": [ ]},
  + {
    - "line_item_id": "94b653e4-e394-4330-a714-43e764ab113",
    - "adjustment_type": "ITEM_SUBSTITUTE",
    - "substituted_item": {
      * "name": "Diet Coke",
      * "merchant_supplied_id": "179",
      * "price": 2,
      * "quantity": 1},
    - "options": [ ]}]

}`