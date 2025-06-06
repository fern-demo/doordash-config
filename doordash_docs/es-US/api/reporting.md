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

* [🇺🇸 English](/en-US/api/reporting)
* [🇫🇷 français](/fr-CA/api/reporting)
* [🇪🇸 español](/es-US/api/reporting)

[Portal para desarrolladores](https://developer.doordash.com/portal)

* postRequest Report
* getGet Report Link

[API docs by Redocly](https://redocly.com/redoc/)

# Reporting APIs (1.0.0)

## Request Report

##### Request Body schema: application/json

|  |  |
| --- | --- |
| business\_ids | Array of integers |
| store\_ids | Array of integers |
| report\_type required | string  Enum: "CONSUMER\_FEEDBACK" "MENU\_ITEM\_ERROR" "MENU\_OPEN\_HOURS" "MENU\_SPECIAL\_HOURS" "ORDER\_DETAIL" "PAYOUT\_SUMMARY" "TRANSACTION\_DETAIL" "TEMPORARY\_DEACTIVATION" "AVOIDABLE\_WAIT" "CANCELLED\_ORDERS" "NV\_PAYMENTS" "NV\_TRANSACTIONS" "NV\_ORDER\_ITEMS" |
| start\_date required | string([0-9]{4})-(?:[0-9]{2})-([0-9]{2}) |
| end\_date required | string([0-9]{4})-(?:[0-9]{2})-([0-9]{2}) |
| webhook\_url | string(https:\/\/.)[-a-zA-Z0-9@:%.\_\+~#=]{2,256}\.[...Show pattern |

### Responses

**200** 

OK

**400** 

Bad Request

**401** 

Unauthenticated

**403** 

Forbidden - Invalid Business or Store ID

**404** 

Data not found

**429** 

Rate Limit Exceeded

**500** 

Internal Server Error

postdataexchange/v1/reports

https://openapi.doordash.comdataexchange/v1/reports

### Request samples

* Payload

Content type

application/json

Copy

 Expand all  Collapse all

`{

* "business_ids": [
  + 123,
  + 456],
* "store_ids": [
  + 123,
  + 456],
* "report_type": "CONSUMER_FEEDBACK",
* "start_date": "2021-12-10",
* "end_date": "2021-12-11",
* "webhook_url": "https://yourdomain.com/callback"

}`

### Response samples

* 200

Content type

application/json

Copy

`{

* "report_id": "3aae518c-0772-4842-9de8-14e0921c5c7d"

}`

## Get Report Link

##### path Parameters

|  |  |
| --- | --- |
| report\_id required | string <uuid>  Example:  3aae518c-0772-4842-9de8-14e0921c5c7d  ID of report to return |

### Responses

**200** 

OK

**400** 

Bad Request

**401** 

Unauthenticated

**403** 

Forbidden

**404** 

Data not found

**429** 

Rate Limit Exceeded

**500** 

Internal Server Error

getdataexchange/v1/reports/{report\_id}/reportlink

https://openapi.doordash.comdataexchange/v1/reports/{report\_id}/reportlink

### Response samples

* 200

Content type

application/json

Copy

`{

* "report_id": "3aae518c-0772-4842-9de8-14e0921c5c7d",
* "report_link": "https://link.to.report",
* "report_status": "SUCCEEDED"

}`