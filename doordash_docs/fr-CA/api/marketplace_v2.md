[Aller au contenu principal](#__docusaurus_skipToContent_fallback)

[![DoorDash Logo](/fr-CA/img/header/developer-logo.svg)![DoorDash Logo](/fr-CA/img/header/developer-logo.svg)](/fr-CA/)

Icon Loading

[Documentation](/fr-CA/docs/welcome)

[Référence de l'API](#)

* [Drive](/fr-CA/api/drive)
* [Drive (classique)](/fr-CA/api/drive_classic)
* [Marketplace](/fr-CA/api/marketplace)
* [Marketplace (legacy)](/fr-CA/api/marketplace_legacy)
* [Marketplace for Retailers](/fr-CA/api/marketplace_v2)
* [Reporting](/fr-CA/api/reporting)

[Blogue](/fr-CA/blog)

[🇫🇷 français](#)

* [🇺🇸 English](/en-US/api/marketplace_v2)
* [🇫🇷 français](/fr-CA/api/marketplace_v2)
* [🇪🇸 español](/es-US/api/marketplace_v2)

[Portail des développeurs](https://developer.doordash.com/portal)

[![Doordash Marketplace](https://cdn.doordash.com/static/img/merchant/logo-red@3x.png)](https://developer.doordash.com/)

* Item Management Endpoints
  + postAdd new items
  + patchUpdate existing items
* Store Management Endpoints
  + patchUpdate existing store
* Inventory/Pricing Management Endpoints
  + postAdd inventory/pricing and other in-store attributes of new item that is made available for sale in the store.
  + patchUpdate inventory/pricing and other in-store attributes of item that is already sold in the store.
* Job Management endpoints
  + postCreate jobs to trigger various pull request flows. Job parameters should confirm to the schema defined for specific job.
* Promotion Management Endpoints
  + postCreate new promotion for store
  + patchUpdate promotions in store
* Models
  + Item
  + Store
  + StoreItem
  + Promotion
  + BatchAddOrUpdateItemRequest
  + BatchAddOrUpdateStoreItemRequest
  + CreateJobRequest
  + CreatePullStoreItemsJobParameters
  + BatchAddOrUpdatePromotionRequest

[API docs by Redocly](https://redocly.com/redoc/)

# Doordash Item management API Specification (2.0)

API to manage item catalog, inventory, pricing and other attributes.

# Item Management Endpoints

Endpoints for item management

## Add new items

Add new items managed by business. Items sold across all stores must be added to business first. Items must be uniquely identifiable across stores. As of now, only one businessId must be specified. Request validation will fail if no businessId or multiple businessIds are specified.

##### Request Body schema: application/json

|  |  |
| --- | --- |
| scope | object |
| items | Array of objects (Item) |

### Responses

**201** 

Ok

**400** 

Request Validation Failed

**401** 

Request unauthorized

**403** 

Forbidden

**404** 

Not Found

**422** 

Request Entity Too Large

**429** 

Request is rate limited

**500** 

Internal service failure, please try again later

post/api/v2/items

https://openapi.doordash.com/marketplace/api/v2/items

### Request samples

* Payload

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "scope": {
  + "business_ids": [
    - "string"]},
* "items": [
  + {
    - "merchant_supplied_item_id": "string",
    - "name": "string",
    - "description": "string",
    - "product_traits": [
      * "ALCOHOL"],
    - "other_identifiers": [
      * {
        + "identifier_type": "UPC",
        + "identifier_value": "string"}],
    - "images": [
      * {
        + "url": "string",
        + "sort_id": 0}],
    - "size": {
      * "details": {
        + "dimensions": {
          - "length": {
            * "value": 0,
            * "unit": "inch"},
          - "width": {
            * "value": 0,
            * "unit": "inch"},
          - "height": {
            * "value": 0,
            * "unit": "inch"}},
        + "weight": {
          - "value": 0,
          - "unit": "lbs"},
        + "volume": {
          - "value": 0,
          - "unit": "oz"},
        + "product_specific_size_definition": {
          - "value": "string",
          - "description": "string"}},
      * "pack_size_details": {
        + "count_per_pack": 0,
        + "per_item_size_details": {
          - "dimensions": {
            * "length": {
              + "value": 0,
              + "unit": "inch"},
            * "width": {
              + "value": 0,
              + "unit": "inch"},
            * "height": {
              + "value": 0,
              + "unit": "inch"}},
          - "weight": {
            * "value": 0,
            * "unit": "lbs"},
          - "volume": {
            * "value": 0,
            * "unit": "oz"},
          - "product_specific_size_definition": {
            * "value": "string",
            * "description": "string"}}}},
    - "weighted_item_info": {
      * "average_weight_per_each": 0,
      * "average_weight_measurement_unit": "ea",
      * "shop_by_measurement_unit": "kg",
      * "price_by_measurement_unit": "kg"},
    - "brand_info": {
      * "name": "string"},
    - "program_eligibility": [
      * "SNAP"],
    - "item_categorizations": [
      * {
        + "category": {
          - "name": "string",
          - "sub_category": { }}}],
    - "product_attributes": [
      * {
        + "attribute_name": "string",
        + "attribute_value": {
          - "single_select_bool": true}}]}]

}`

### Response samples

* 201
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{

* "operation_id": "string",
* "operation_status": "QUEUED",
* "message": "string"

}`

## Update existing items

Update existing items managed by business.

##### Request Body schema: application/json

|  |  |
| --- | --- |
| scope | object |
| items | Array of objects (Item) |

### Responses

**200** 

Ok

**400** 

Request Validation Failed

**401** 

Request unauthorized

**403** 

Forbidden

**404** 

Not Found

**422** 

Request Entity Too Large

**429** 

Request is rate limited

**500** 

Internal service failure, please try again later

patch/api/v2/items

https://openapi.doordash.com/marketplace/api/v2/items

### Request samples

* Payload

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "scope": {
  + "business_ids": [
    - "string"]},
* "items": [
  + {
    - "merchant_supplied_item_id": "string",
    - "name": "string",
    - "description": "string",
    - "product_traits": [
      * "ALCOHOL"],
    - "other_identifiers": [
      * {
        + "identifier_type": "UPC",
        + "identifier_value": "string"}],
    - "images": [
      * {
        + "url": "string",
        + "sort_id": 0}],
    - "size": {
      * "details": {
        + "dimensions": {
          - "length": {
            * "value": 0,
            * "unit": "inch"},
          - "width": {
            * "value": 0,
            * "unit": "inch"},
          - "height": {
            * "value": 0,
            * "unit": "inch"}},
        + "weight": {
          - "value": 0,
          - "unit": "lbs"},
        + "volume": {
          - "value": 0,
          - "unit": "oz"},
        + "product_specific_size_definition": {
          - "value": "string",
          - "description": "string"}},
      * "pack_size_details": {
        + "count_per_pack": 0,
        + "per_item_size_details": {
          - "dimensions": {
            * "length": {
              + "value": 0,
              + "unit": "inch"},
            * "width": {
              + "value": 0,
              + "unit": "inch"},
            * "height": {
              + "value": 0,
              + "unit": "inch"}},
          - "weight": {
            * "value": 0,
            * "unit": "lbs"},
          - "volume": {
            * "value": 0,
            * "unit": "oz"},
          - "product_specific_size_definition": {
            * "value": "string",
            * "description": "string"}}}},
    - "weighted_item_info": {
      * "average_weight_per_each": 0,
      * "average_weight_measurement_unit": "ea",
      * "shop_by_measurement_unit": "kg",
      * "price_by_measurement_unit": "kg"},
    - "brand_info": {
      * "name": "string"},
    - "program_eligibility": [
      * "SNAP"],
    - "item_categorizations": [
      * {
        + "category": {
          - "name": "string",
          - "sub_category": { }}}],
    - "product_attributes": [
      * {
        + "attribute_name": "string",
        + "attribute_value": {
          - "single_select_bool": true}}]}]

}`

### Response samples

* 200
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{

* "operation_id": "string",
* "operation_status": "QUEUED",
* "message": "string"

}`

# Store Management Endpoints

Endpoints for managing stores

## Update existing store

##### path Parameters

|  |  |
| --- | --- |
| store\_location\_id required | string <string>  ID of store to be updated |

##### Request Body schema: application/json

update existing store

|  |  |
| --- | --- |
| merchant\_supplied\_store\_id | string |
| open\_hours | Array of objects |
| special\_hours | Array of objects |

### Responses

**200** 

store updated successfully

**400** 

Request Validation Failed

**401** 

Request unauthorized

**403** 

Forbidden

**404** 

Not Found

**422** 

Request Entity Too Large

**429** 

Request is rate limited

**500** 

Internal service failure, please try again later

patch/api/v2/stores/{store\_location\_id}

https://openapi.doordash.com/marketplace/api/v2/stores/{store\_location\_id}

### Request samples

* Payload

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "merchant_supplied_store_id": "string",
* "open_hours": [
  + {
    - "day_index": "MON",
    - "start_time": "string",
    - "end_time": "string"}],
* "special_hours": [
  + {
    - "date": "string",
    - "start_time": "string",
    - "end_time": "string",
    - "closed": true}]

}`

### Response samples

* 200
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "merchant_supplied_store_id": "string",
* "open_hours": [
  + {
    - "day_index": "MON",
    - "start_time": "string",
    - "end_time": "string"}],
* "special_hours": [
  + {
    - "date": "string",
    - "start_time": "string",
    - "end_time": "string",
    - "closed": true}]

}`

# Inventory/Pricing Management Endpoints

Endpoints to manage inventory/pricing and other item attributes specific to this store

## Add inventory/pricing and other in-store attributes of new item that is made available for sale in the store.

Add inventory/pricing and other in-store attributes of new item that is made available for sale in the store. base\_price and status must be specified first time when an item is made available for sale in a store. At this time, item with extras/options is supported only via job management endpoint. Request validation will fail if extras/options are present in POST/PATCH.

##### path Parameters

|  |  |
| --- | --- |
| store\_location\_id required | string <string>  ID of store where the item is physically sourced. |

##### Request Body schema: application/json

|  |  |
| --- | --- |
| meta | object  Only need this information when you use paginated pull workflow |
| items | Array of objects (StoreItem) |

### Responses

**202** 

operation successfully queued

**400** 

Request Validation Failed

**401** 

Request unauthorized

**403** 

Forbidden

**404** 

Not Found

**422** 

Request Entity Too Large

**429** 

Request is rate limited

**500** 

Internal service failure, please try again later

post/api/v2/stores/{store\_location\_id}/items

https://openapi.doordash.com/marketplace/api/v2/stores/{store\_location\_id}/items

### Request samples

* Payload

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "meta": {
  + "current_page": 0,
  + "page_size": 0,
  + "total_page": 0},
* "items": [
  + {
    - "merchant_supplied_item_id": "string",
    - "item_availability": "ACTIVE",
    - "balance_on_hand": 0,
    - "last_sold_datetime": "string",
    - "price_info": {
      * "base_price": 0,
      * "sale_price": 0,
      * "tax_rate": 0,
      * "bottle_fee_deposit": 0,
      * "base_price_per_measurement_unit": 0,
      * "loyalty_price": 0,
      * "loyalty_price_per_measurement_unit": 0},
    - "location": {
      * "aisle": "string",
      * "zone": "string",
      * "shelf": "string",
      * "side": "string",
      * "additional_details": "string",
      * "coordinates": {
        + "x": 0,
        + "y": 0},
      * "raw_text": "string",
      * "section": "string"},
    - "item_special_hours": [
      * {
        + "day_index": "MON",
        + "start_time": "string",
        + "end_time": "string",
        + "start_date": "string",
        + "end_date": "string"}],
    - "extras": [
      * {
        + "name": "string",
        + "merchant_supplied_id": "string",
        + "description": "string",
        + "availability": "ACTIVE",
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
            * "merchant_supplied_item_id": "string",
            * "name": "string",
            * "availability": "ACTIVE",
            * "price_info": {
              + "base_price": 0},
            * "item_extra_option_special_hours": [
              + {
                - "day_index": "MON",
                - "start_time": "string",
                - "end_time": "string",
                - "start_date": "string",
                - "end_date": "string"}],
            * "description": "string",
            * "default": true,
            * "sort_id": 0,
            * "extras": [
              + { }]}]}]}]

}`

### Response samples

* 202
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{

* "operation_id": "string",
* "operation_status": "QUEUED",
* "message": "string"

}`

## Update inventory/pricing and other in-store attributes of item that is already sold in the store.

At this time, item with extras/options is supported only via job management endpoint. Request validation will fail if extras/options are present in POST/PATCH.

##### path Parameters

|  |  |
| --- | --- |
| store\_location\_id required | string <string>  ID of store where the item is physically sourced. |

##### Request Body schema: application/json

|  |  |
| --- | --- |
| meta | object  Only need this information when you use paginated pull workflow |
| items | Array of objects (StoreItem) |

### Responses

**202** 

operation successfully queued

**400** 

Request Validation Failed

**401** 

Request unauthorized

**403** 

Forbidden

**404** 

Not Found

**422** 

Request Entity Too Large

**429** 

Request is rate limited

**500** 

Internal service failure, please try again later

patch/api/v2/stores/{store\_location\_id}/items

https://openapi.doordash.com/marketplace/api/v2/stores/{store\_location\_id}/items

### Request samples

* Payload

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "meta": {
  + "current_page": 0,
  + "page_size": 0,
  + "total_page": 0},
* "items": [
  + {
    - "merchant_supplied_item_id": "string",
    - "item_availability": "ACTIVE",
    - "balance_on_hand": 0,
    - "last_sold_datetime": "string",
    - "price_info": {
      * "base_price": 0,
      * "sale_price": 0,
      * "tax_rate": 0,
      * "bottle_fee_deposit": 0,
      * "base_price_per_measurement_unit": 0,
      * "loyalty_price": 0,
      * "loyalty_price_per_measurement_unit": 0},
    - "location": {
      * "aisle": "string",
      * "zone": "string",
      * "shelf": "string",
      * "side": "string",
      * "additional_details": "string",
      * "coordinates": {
        + "x": 0,
        + "y": 0},
      * "raw_text": "string",
      * "section": "string"},
    - "item_special_hours": [
      * {
        + "day_index": "MON",
        + "start_time": "string",
        + "end_time": "string",
        + "start_date": "string",
        + "end_date": "string"}],
    - "extras": [
      * {
        + "name": "string",
        + "merchant_supplied_id": "string",
        + "description": "string",
        + "availability": "ACTIVE",
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
            * "merchant_supplied_item_id": "string",
            * "name": "string",
            * "availability": "ACTIVE",
            * "price_info": {
              + "base_price": 0},
            * "item_extra_option_special_hours": [
              + {
                - "day_index": "MON",
                - "start_time": "string",
                - "end_time": "string",
                - "start_date": "string",
                - "end_date": "string"}],
            * "description": "string",
            * "default": true,
            * "sort_id": 0,
            * "extras": [
              + { }]}]}]}]

}`

### Response samples

* 202
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{

* "operation_id": "string",
* "operation_status": "QUEUED",
* "message": "string"

}`

# Job Management endpoints

Endpoints to create jobs to support pull request flows.

## Create jobs to trigger various pull request flows. Job parameters should confirm to the schema defined for specific job.

##### Request Body schema: application/json

|  |  |
| --- | --- |
| job\_type | string  Enum: "PULL\_STORE\_ITEMS" "PULL\_STORE\_ITEMS\_WITH\_PAGINATION"  Use PULL\_STORE\_ITEMS if you can return all items in one pull call for one store, otherwise use PULL\_STORE\_ITEMS\_WITH\_PAGINATION which is paginated version pull. |
| job\_parameters | object |

### Responses

**200** 

Request to create job recevied.

**400** 

Request Validation Failed

**401** 

Request unauthorized

**403** 

Forbidden

**404** 

Not Found

**422** 

Request Entity Too Large

**429** 

Request is rate limited

**500** 

Internal service failure, please try again later

post/api/v2/jobs

https://openapi.doordash.com/marketplace/api/v2/jobs

### Request samples

* Payload

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "job_type": "PULL_STORE_ITEMS",
* "job_parameters": {
  + "property1": "string",
  + "property2": "string"}

}`

### Response samples

* 200
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{

* "operation_id": "string",
* "operation_status": "QUEUED",
* "message": "string",
* "max_page_size": 0

}`

# Promotion Management Endpoints

Endpoints for promotion management

## Create new promotion for store

##### path Parameters

|  |  |
| --- | --- |
| store\_location\_id required | string <string>  location ID of store |

##### Request Body schema: application/json

create new promotion

|  |  |
| --- | --- |
| promotion\_id | string  Promotion Id to identify a promotion uniquely with a Mx. Required. |
| promotion\_type | string  Enum: "BUY\_X\_FOR\_Y" "BUY\_X\_SAVE\_Y" "BUY\_X\_GET\_Y\_Z\_PERCENT\_OFF"  Promotion types |
| purchase\_criteria | object  Purchase criteria to redeem this promotion |
| redemption\_limit | object  Purchase criteria to redeem this promotion |
| discount\_options | object  Purchase criteria to redeem this promotion |
| start\_time | string <yyyy-MM-ddTHH:mm:ssXXX>  required, start time of the promotion with local timezone, example 2024-04-03T10:15:30Z <https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html#ISO_ZONED_DATE_TIME> |
| end\_time | string <yyyy-MM-ddTHH:mm:ssXXX>  required, end time of the promotion with local timezone <https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html#ISO_ZONED_DATE_TIME> |

### Responses

**202** 

Accepted

**400** 

Request Validation Failed

**401** 

Request unauthorized

**403** 

Forbidden

**404** 

Not Found

**422** 

Request Entity Too Large

**429** 

Request is rate limited

**500** 

Internal service failure, please try again later

post/api/v2/promotions/stores/{store\_location\_id}

https://openapi.doordash.com/marketplace/api/v2/promotions/stores/{store\_location\_id}

### Request samples

* Payload

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "promotion_id": "string",
* "promotion_type": "BUY_X_FOR_Y",
* "purchase_criteria": {
  + "purchase_items": [
    - "string"],
  + "purchase_quantity": 0},
* "redemption_limit": {
  + "limit_per_order": 0},
* "discount_options": {
  + "discount_total_price": 0,
  + "discount_price_off": 0,
  + "discount_percentage": 0,
  + "discount_quantity": 0},
* "start_time": "string",
* "end_time": "string"

}`

### Response samples

* 202
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{

* "operation_id": "string",
* "operation_status": "QUEUED",
* "message": "string"

}`

## Update promotions in store

##### path Parameters

|  |  |
| --- | --- |
| store\_location\_id required | string <string>  location ID of store to be updated |

##### Request Body schema: application/json

update promotions in store

|  |  |
| --- | --- |
| promotion\_id | string  Promotion Id to identify a promotion uniquely with a Mx. Required. |
| promotion\_type | string  Enum: "BUY\_X\_FOR\_Y" "BUY\_X\_SAVE\_Y" "BUY\_X\_GET\_Y\_Z\_PERCENT\_OFF"  Promotion types |
| purchase\_criteria | object  Purchase criteria to redeem this promotion |
| redemption\_limit | object  Purchase criteria to redeem this promotion |
| discount\_options | object  Purchase criteria to redeem this promotion |
| start\_time | string <yyyy-MM-ddTHH:mm:ssXXX>  required, start time of the promotion with local timezone, example 2024-04-03T10:15:30Z <https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html#ISO_ZONED_DATE_TIME> |
| end\_time | string <yyyy-MM-ddTHH:mm:ssXXX>  required, end time of the promotion with local timezone <https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html#ISO_ZONED_DATE_TIME> |

### Responses

**202** 

Accepted

**400** 

Request Validation Failed

**401** 

Request unauthorized

**403** 

Forbidden

**404** 

Not Found

**422** 

Request Entity Too Large

**429** 

Request is rate limited

**500** 

Internal service failure, please try again later

patch/api/v2/promotions/stores/{store\_location\_id}

https://openapi.doordash.com/marketplace/api/v2/promotions/stores/{store\_location\_id}

### Request samples

* Payload

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "promotion_id": "string",
* "promotion_type": "BUY_X_FOR_Y",
* "purchase_criteria": {
  + "purchase_items": [
    - "string"],
  + "purchase_quantity": 0},
* "redemption_limit": {
  + "limit_per_order": 0},
* "discount_options": {
  + "discount_total_price": 0,
  + "discount_price_off": 0,
  + "discount_percentage": 0,
  + "discount_quantity": 0},
* "start_time": "string",
* "end_time": "string"

}`

### Response samples

* 202
* 400
* 401
* 403
* 404
* 422
* 429
* 500

Content type

application/json

Copy

`{

* "operation_id": "string",
* "operation_status": "QUEUED",
* "message": "string"

}`

# Models

## Item

|  |  |
| --- | --- |
| merchant\_supplied\_item\_id | string  Merchant supplied Id to identify an item uniquely within business across all stores. Every item that is shopable by CX must be represented as an unique item |
| name | string  Name of the item |
| description | string  Description of the item |
| product\_traits | Array of strings (ProductTrait)  Items Enum: "ALCOHOL" "MEDICATION" "WEIGHTED"  Specifies type of product(s) represented by the item. These attributes will be used to validate product specific attributes in request and apply product specific business logic internally. For example, when WEIGHTED is specified as one of the product trait, presence of weighted\_item\_info will be validated in the request payload |
| other\_identifiers | Array of objects  Other identifiers associated with item. |
| images | Array of objects  Images of the item, atleast one image must be specified |
| size | object  size of the item |
| weighted\_item\_info | object  attributes related to items that are sold by weights |
| brand\_info | object  brand of the item if applicable |
| program\_eligibility | Array of strings (ProgramEligibility)  Items Enum: "SNAP" "HSA" "FSA"  Program eligibility of the item |
| item\_categorizations | Array of objects  One or more categories associated with the item |
| product\_attributes | Array of objects (ProductAttributes)  product\_attributes allow us to infer everything about an item necessary for customers to shop, dasher to fulfill, merchants to merchandise, and advertisers to advertise. See supported full attribute list: <https://developer.doordash.com/en-US/docs/marketplace/retail/catalog_management/supported_attribute> |

Copy

 Expand all  Collapse all

`{

* "merchant_supplied_item_id": "string",
* "name": "string",
* "description": "string",
* "product_traits": [
  + "ALCOHOL"],
* "other_identifiers": [
  + {
    - "identifier_type": "UPC",
    - "identifier_value": "string"}],
* "images": [
  + {
    - "url": "string",
    - "sort_id": 0}],
* "size": {
  + "details": {
    - "dimensions": {
      * "length": {
        + "value": 0,
        + "unit": "inch"},
      * "width": {
        + "value": 0,
        + "unit": "inch"},
      * "height": {
        + "value": 0,
        + "unit": "inch"}},
    - "weight": {
      * "value": 0,
      * "unit": "lbs"},
    - "volume": {
      * "value": 0,
      * "unit": "oz"},
    - "product_specific_size_definition": {
      * "value": "string",
      * "description": "string"}},
  + "pack_size_details": {
    - "count_per_pack": 0,
    - "per_item_size_details": {
      * "dimensions": {
        + "length": {
          - "value": 0,
          - "unit": "inch"},
        + "width": {
          - "value": 0,
          - "unit": "inch"},
        + "height": {
          - "value": 0,
          - "unit": "inch"}},
      * "weight": {
        + "value": 0,
        + "unit": "lbs"},
      * "volume": {
        + "value": 0,
        + "unit": "oz"},
      * "product_specific_size_definition": {
        + "value": "string",
        + "description": "string"}}}},
* "weighted_item_info": {
  + "average_weight_per_each": 0,
  + "average_weight_measurement_unit": "ea",
  + "shop_by_measurement_unit": "kg",
  + "price_by_measurement_unit": "kg"},
* "brand_info": {
  + "name": "string"},
* "program_eligibility": [
  + "SNAP"],
* "item_categorizations": [
  + {
    - "category": {
      * "name": "string",
      * "sub_category": { }}}],
* "product_attributes": [
  + {
    - "attribute_name": "string",
    - "attribute_value": {
      * "single_select_bool": true}}]

}`

## Store

|  |  |
| --- | --- |
| merchant\_supplied\_store\_id | string |
| open\_hours | Array of objects |
| special\_hours | Array of objects |

Copy

 Expand all  Collapse all

`{

* "merchant_supplied_store_id": "string",
* "open_hours": [
  + {
    - "day_index": "MON",
    - "start_time": "string",
    - "end_time": "string"}],
* "special_hours": [
  + {
    - "date": "string",
    - "start_time": "string",
    - "end_time": "string",
    - "closed": true}]

}`

## StoreItem

|  |  |
| --- | --- |
| merchant\_supplied\_item\_id | string |
| item\_availability | string  Enum: "ACTIVE" "INACTIVE" |
| balance\_on\_hand | integer |
| last\_sold\_datetime | string  DateTime in ISO8601 format of when the item was last sold at the store. |
| price\_info | object (PriceInfo) |
| location | object (ItemLocation)  Default location of an item in the store across business. Can be specified at store level for any store specific customizations. |
| item\_special\_hours | Array of objects (TimeBlock)  Special hours on when item will be available |
| extras | Array of objects (Extra) |

Copy

 Expand all  Collapse all

`{

* "merchant_supplied_item_id": "string",
* "item_availability": "ACTIVE",
* "balance_on_hand": 0,
* "last_sold_datetime": "string",
* "price_info": {
  + "base_price": 0,
  + "sale_price": 0,
  + "tax_rate": 0,
  + "bottle_fee_deposit": 0,
  + "base_price_per_measurement_unit": 0,
  + "loyalty_price": 0,
  + "loyalty_price_per_measurement_unit": 0},
* "location": {
  + "aisle": "string",
  + "zone": "string",
  + "shelf": "string",
  + "side": "string",
  + "additional_details": "string",
  + "coordinates": {
    - "x": 0,
    - "y": 0},
  + "raw_text": "string",
  + "section": "string"},
* "item_special_hours": [
  + {
    - "day_index": "MON",
    - "start_time": "string",
    - "end_time": "string",
    - "start_date": "string",
    - "end_date": "string"}],
* "extras": [
  + {
    - "name": "string",
    - "merchant_supplied_id": "string",
    - "description": "string",
    - "availability": "ACTIVE",
    - "sort_id": 0,
    - "min_num_options": 0,
    - "max_num_options": 0,
    - "num_free_options": 0,
    - "min_option_choice_quantity": 0,
    - "max_option_choice_quantity": 0,
    - "min_aggregate_options_quantity": 0,
    - "max_aggregate_options_quantity": 0,
    - "options": [
      * {
        + "merchant_supplied_item_id": "string",
        + "name": "string",
        + "availability": "ACTIVE",
        + "price_info": {
          - "base_price": 0},
        + "item_extra_option_special_hours": [
          - {
            * "day_index": "MON",
            * "start_time": "string",
            * "end_time": "string",
            * "start_date": "string",
            * "end_date": "string"}],
        + "description": "string",
        + "default": true,
        + "sort_id": 0,
        + "extras": [
          - { }]}]}]

}`

## Promotion

|  |  |
| --- | --- |
| promotion\_id | string  Promotion Id to identify a promotion uniquely with a Mx. Required. |
| promotion\_type | string  Enum: "BUY\_X\_FOR\_Y" "BUY\_X\_SAVE\_Y" "BUY\_X\_GET\_Y\_Z\_PERCENT\_OFF"  Promotion types |
| purchase\_criteria | object  Purchase criteria to redeem this promotion |
| redemption\_limit | object  Purchase criteria to redeem this promotion |
| discount\_options | object  Purchase criteria to redeem this promotion |
| start\_time | string <yyyy-MM-ddTHH:mm:ssXXX>  required, start time of the promotion with local timezone, example 2024-04-03T10:15:30Z <https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html#ISO_ZONED_DATE_TIME> |
| end\_time | string <yyyy-MM-ddTHH:mm:ssXXX>  required, end time of the promotion with local timezone <https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html#ISO_ZONED_DATE_TIME> |

Copy

 Expand all  Collapse all

`{

* "promotion_id": "string",
* "promotion_type": "BUY_X_FOR_Y",
* "purchase_criteria": {
  + "purchase_items": [
    - "string"],
  + "purchase_quantity": 0},
* "redemption_limit": {
  + "limit_per_order": 0},
* "discount_options": {
  + "discount_total_price": 0,
  + "discount_price_off": 0,
  + "discount_percentage": 0,
  + "discount_quantity": 0},
* "start_time": "string",
* "end_time": "string"

}`

## BatchAddOrUpdateItemRequest

|  |  |
| --- | --- |
| scope | object |
| items | Array of objects (Item) |

Copy

 Expand all  Collapse all

`{

* "scope": {
  + "business_ids": [
    - "string"]},
* "items": [
  + {
    - "merchant_supplied_item_id": "string",
    - "name": "string",
    - "description": "string",
    - "product_traits": [
      * "ALCOHOL"],
    - "other_identifiers": [
      * {
        + "identifier_type": "UPC",
        + "identifier_value": "string"}],
    - "images": [
      * {
        + "url": "string",
        + "sort_id": 0}],
    - "size": {
      * "details": {
        + "dimensions": {
          - "length": {
            * "value": 0,
            * "unit": "inch"},
          - "width": {
            * "value": 0,
            * "unit": "inch"},
          - "height": {
            * "value": 0,
            * "unit": "inch"}},
        + "weight": {
          - "value": 0,
          - "unit": "lbs"},
        + "volume": {
          - "value": 0,
          - "unit": "oz"},
        + "product_specific_size_definition": {
          - "value": "string",
          - "description": "string"}},
      * "pack_size_details": {
        + "count_per_pack": 0,
        + "per_item_size_details": {
          - "dimensions": {
            * "length": {
              + "value": 0,
              + "unit": "inch"},
            * "width": {
              + "value": 0,
              + "unit": "inch"},
            * "height": {
              + "value": 0,
              + "unit": "inch"}},
          - "weight": {
            * "value": 0,
            * "unit": "lbs"},
          - "volume": {
            * "value": 0,
            * "unit": "oz"},
          - "product_specific_size_definition": {
            * "value": "string",
            * "description": "string"}}}},
    - "weighted_item_info": {
      * "average_weight_per_each": 0,
      * "average_weight_measurement_unit": "ea",
      * "shop_by_measurement_unit": "kg",
      * "price_by_measurement_unit": "kg"},
    - "brand_info": {
      * "name": "string"},
    - "program_eligibility": [
      * "SNAP"],
    - "item_categorizations": [
      * {
        + "category": {
          - "name": "string",
          - "sub_category": { }}}],
    - "product_attributes": [
      * {
        + "attribute_name": "string",
        + "attribute_value": {
          - "single_select_bool": true}}]}]

}`

## BatchAddOrUpdateStoreItemRequest

|  |  |
| --- | --- |
| meta | object  Only need this information when you use paginated pull workflow |
| items | Array of objects (StoreItem) |

Copy

 Expand all  Collapse all

`{

* "meta": {
  + "current_page": 0,
  + "page_size": 0,
  + "total_page": 0},
* "items": [
  + {
    - "merchant_supplied_item_id": "string",
    - "item_availability": "ACTIVE",
    - "balance_on_hand": 0,
    - "last_sold_datetime": "string",
    - "price_info": {
      * "base_price": 0,
      * "sale_price": 0,
      * "tax_rate": 0,
      * "bottle_fee_deposit": 0,
      * "base_price_per_measurement_unit": 0,
      * "loyalty_price": 0,
      * "loyalty_price_per_measurement_unit": 0},
    - "location": {
      * "aisle": "string",
      * "zone": "string",
      * "shelf": "string",
      * "side": "string",
      * "additional_details": "string",
      * "coordinates": {
        + "x": 0,
        + "y": 0},
      * "raw_text": "string",
      * "section": "string"},
    - "item_special_hours": [
      * {
        + "day_index": "MON",
        + "start_time": "string",
        + "end_time": "string",
        + "start_date": "string",
        + "end_date": "string"}],
    - "extras": [
      * {
        + "name": "string",
        + "merchant_supplied_id": "string",
        + "description": "string",
        + "availability": "ACTIVE",
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
            * "merchant_supplied_item_id": "string",
            * "name": "string",
            * "availability": "ACTIVE",
            * "price_info": {
              + "base_price": 0},
            * "item_extra_option_special_hours": [
              + {
                - "day_index": "MON",
                - "start_time": "string",
                - "end_time": "string",
                - "start_date": "string",
                - "end_date": "string"}],
            * "description": "string",
            * "default": true,
            * "sort_id": 0,
            * "extras": [
              + { }]}]}]}]

}`

## CreateJobRequest

|  |  |
| --- | --- |
| job\_type | string  Enum: "PULL\_STORE\_ITEMS" "PULL\_STORE\_ITEMS\_WITH\_PAGINATION"  Use PULL\_STORE\_ITEMS if you can return all items in one pull call for one store, otherwise use PULL\_STORE\_ITEMS\_WITH\_PAGINATION which is paginated version pull. |
| job\_parameters | object |

Copy

 Expand all  Collapse all

`{

* "job_type": "PULL_STORE_ITEMS",
* "job_parameters": {
  + "property1": "string",
  + "property2": "string"}

}`

## CreatePullStoreItemsJobParameters

|  |  |
| --- | --- |
| store\_location\_id | string |
| pull\_mode | string  Value: "REPLACE" |
| merchant\_supplied\_page\_size | integer |

Copy

`{

* "store_location_id": "string",
* "pull_mode": "REPLACE",
* "merchant_supplied_page_size": 0

}`

## BatchAddOrUpdatePromotionRequest

|  |  |
| --- | --- |
| promotions | Array of objects (Promotion) |
| Array  |  |  | | --- | --- | | promotion\_id | string  Promotion Id to identify a promotion uniquely with a Mx. Required. | | promotion\_type | string  Enum: "BUY\_X\_FOR\_Y" "BUY\_X\_SAVE\_Y" "BUY\_X\_GET\_Y\_Z\_PERCENT\_OFF"  Promotion types | | purchase\_criteria | object  Purchase criteria to redeem this promotion | | redemption\_limit | object  Purchase criteria to redeem this promotion | | discount\_options | object  Purchase criteria to redeem this promotion | | start\_time | string <yyyy-MM-ddTHH:mm:ssXXX>  required, start time of the promotion with local timezone, example 2024-04-03T10:15:30Z <https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html#ISO_ZONED_DATE_TIME> | | end\_time | string <yyyy-MM-ddTHH:mm:ssXXX>  required, end time of the promotion with local timezone <https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html#ISO_ZONED_DATE_TIME> | | |

Copy

 Expand all  Collapse all

`{

* "promotions": [
  + {
    - "promotion_id": "string",
    - "promotion_type": "BUY_X_FOR_Y",
    - "purchase_criteria": {
      * "purchase_items": [
        + "string"],
      * "purchase_quantity": 0},
    - "redemption_limit": {
      * "limit_per_order": 0},
    - "discount_options": {
      * "discount_total_price": 0,
      * "discount_price_off": 0,
      * "discount_percentage": 0,
      * "discount_quantity": 0},
    - "start_time": "string",
    - "end_time": "string"}]

}`