Sur cette page

# [Explainer] Shopping Complete Webhooks

## DASHER\_COMPLETED\_SHOPPING[​](#dasher_completed_shopping "Lien direct vers le titre")

The DASHER\_COMPLETED\_SHOPPING webhook is sent when a Dasher completes in-store shopping for an order, before checking-out. No webhooks are sent while the Dasher is actively shopping. This webhook delivers detailed information about the shopping event, including Dasher details, pickup and dropoff information, and a comprehensive list of items that were shopped.

The shopped\_items section will indicate each item that was shopped, and the associated quantity. This section will also indicate if the item was a substitution.

| Field Name (Shopped Items Section) | Description | Always Expected or May be Null |
| --- | --- | --- |
| name | The name of the item | Always Expected |
| description | Description of the item | Always Expected |
| quantity | The number of units of the item shopped | Always Expected |
| weight | The weight of the item, if applicable (may be null). | May be Null |
| weight\_components | An array detailing the components of the weight, if applicable. | May be Null |
| weight\_unit | The unit of weight measurement, if applicable (may be null). | May be Null |
| external\_id | Merchant's unique item identifier. | Always Expected |
| requested\_item\_external\_id | Merchant's unique item identifier of the original item ordered. | May be Null (if originally requested item picked) |
| external\_instance\_id | An additional identifier for the item used to distinguish between multiple items with the same external\_id, such as for 2 steaks in the same order with separate weights or the "line number" of an itemized SKU in the order | May be Null (if additional identifier not used) |
| price | The price of the item in cents. | Always Expected |
| substitution\_source | Source of substitution, if applicable (may be null). "Dasher" when substitution was picked by the dasher (as an override or upon customer request when contacted by dasher); "Customer" when substitution was directly selected by the customer; "Merchant" when substitution was recommended by merchant (customer still gets notified by dasher in case they want something else). Reference the substitutions explainer for more details. | May be Null (if originally requested item picked) |
| scanned\_code | The barcode or PLU code of the item. | Always Expected |
| scanned\_data\_list | A list of ScannedData objects, each representing a possible deconstruction of the scanned barcode. Barcodes can conform to different formats (e.g., UPC-A, EAN-13), and this list captures the parsed components for each possible format. scanned\_data\_list[0] contains the components for the most likely barcode format (e.g., UPC-A). scanned\_data\_list[1], scanned\_data\_list[2], etc., represent the same barcode interpreted under other formats (e.g., EAN-13). The list is ordered by likelihood, with the most probable format appearing first | Always Expected |
| format | Format of barcode. Enum ["upc-a","upc-e","ean-13","ean-8","plu","gtin-14","unknown"] | Always Expected |
| is\_variable\_measure | Indicates whether the barcode represents a variable measure product with price or weight | May be null |
| indicator\_digit | Used in Gtin14 barcodes to classify the type of item | May be null |
| product\_code | Product code identifies an item within a given system, used in most barcode formats. | Always Expected |
| check\_digit | Check digit if applicable. Typically the last digit of scanned UPC and EAN | May be null |
| country\_code | Identify the country where the manufacturer is registered, used in EAN-13 and EAN-8 | May be null |
| manufacturer\_code | Identifies the company that produced the product, used in UPC-A, EAN-13, UPC-E | May be null |
| number\_system | The type of barcode and its categorization, used in UPC-A, UPC-E | May be null |
| plu\_check\_digit | Price check digit used in variable measure barcodes | May be null |
| company\_prefix | Part of Gtin14 barcode, identifying the brand owner or manufacturer | May be null |
| item\_reference | Identifies a product within a company’s, used in Gtin14 barcodes | May be null |
| scanned\_code\_sans\_check\_digit | Barcode without check digit | May be null |
| addition\_source | Source of a new item added to the order after shopping has started, if applicable (may be null). Enum ["dasher","customer","merchant"] | May be Null (if no new item was added) |
| requested\_item\_external\_instance\_id | The external instance ID of the requested item, if applicable (may be null). This is used to identify the additional uniqueness of an item in an order, such as the "line number" of an itemized SKU in the order. | May be Null (if additional identifier not used) |
| fulfilled\_substitution\_type | Type of substitution fulfilled, if applicable (may be null). Enum ["no\_substitution","pre\_selected","customer\_contacted","dasher\_override"] | May be null |
| is\_unknown | Boolean indicating if the item is unknown (may be null). Will be TRUE if the item is not found in the catalog | May be null |

### **Scenario 1:** Item shopped as ordered[​](#scenario-1-item-shopped-as-ordered "Lien direct vers le titre")

| Field Name (Shopped Items Section) | Value | Description |
| --- | --- | --- |
| name | Cereal | Name of ordered item |
| description | 25oz cereal box | Description of the ordered item |
| quantity | 2 | Quantity ordered |
| weight | 2.5 | Total weight of the item |
| weight\_components |  |  |
| weight\_unit | oz | Weight unit of measure |
| external\_id | 258147369 | Merchant's item identifier |
| requested\_item\_external\_id |  |  |
| external\_instance\_id | 861555aa-6875-4b02-b5f2-58ee14f323a9 | Additional identifier as passed in the original payload |
| price | 499 | Price provided by merchant in inventory feed |
| substitution\_source |  |  |
| scanned\_code | 41303002001 | Barcode scanned by Dasher |
| addition\_source |  |  |
| requested\_item\_external\_instance\_id |  |  |
| scanned\_data\_list | see json below | see explanation below |
| fulfilled\_substitution\_type | no\_substitution | Original item picked |
| is\_unknown | false | This item exists in catalog |

scanned\_data\_list:

```
[  
  {  
    "format": "upc-a",  
    "is_variable_measure": false,  
    "product_code": "00200",  
    "check_digit": "1",  
    "manufacturer_code": "41303",  
    "number_system": "0",  
    "scanned_code_sans_check_digit": "04130300200"  
  },  
  {  
    "format": "ean-13",  
    "is_variable_measure": false,  
    "product_code": "00200",  
    "check_digit": "1",  
    "country_code": "004",  
    "manufacturer_code": "1303",  
    "scanned_code_sans_check_digit": "004130300200"  
  }  
]  
  

```

The barcode scanned by the mobile device is a UPC-A barcode. However, for 13-digit barcodes that start with a leading zero, mobile devices may automatically omit the first zero during scanning. As a result, the scanned\_data\_list contains two items: scanned\_data\_list

* [0] represents the components of the barcode interpreted as a UPC-A code, which is the most likely format; scanned\_data\_list
* [1] represents the components of the same barcode interpreted as an EAN-13 code, which is also a valid possibility

### **Scenario 2:** Weighted Item shopped as ordered[​](#scenario-2-weighted-item-shopped-as-ordered "Lien direct vers le titre")

| Field Name (Shopped Items Section) | Value | Description |
| --- | --- | --- |
| name | Banana | Name of ordered item |
| description | Chiquita Bananas | Description of the ordered item |
| quantity | 8 | Quantity ordered |
| weight | 3.25 | Total weight of the item |
| weight\_components | 3.25 | Array of individually weighted items (if applicable) |
| weight\_unit | oz | Weight unit of measure |
| external\_id | 4011 | Merchant's item identifier |
| requested\_item\_external\_id |  |  |
| external\_instance\_id | 861555aa-6875-4b02-b5f2-58ee14f323a9 | Additional identifier as passed in the original payload |
| price | 191 | Price provided by merchant in inventory feed. If the item is a weighted item, this value will be total weight multiplied by the weighted price |
| substitution\_source |  |  |
| scanned\_code | 4011 | Barcode scanned by Dasher |
| addition\_source |  |  |
| requested\_item\_external\_instance\_id |  |  |
| scanned\_data\_list | see json below | Components of the barcode interpreted as a PLU code |
| fulfilled\_substitution\_type | no\_substitution | Original item picked |
| is\_unknown | false | This item exists in catalog |

scanned\_data\_list:

```
[  
    {  
    "format": "plu",  
    "is_variable_measure": false,  
    "product_code": "4011"  
    }  
]  
  

```

### **Scenario 3:** Item substituted when the preference is set to contact customer[​](#scenario-3-item-substituted-when-the-preference-is-set-to-contact-customer "Lien direct vers le titre")

[(reference)](https://developer.doordash.com/en-US/docs/drive/how_to/Drive_DSX/how_to_subs_other_shopping_use_cases#contact-me-option)

| Field Name (Shopped Items Section) | Value | Description |
| --- | --- | --- |
| name | Cereal | Name of ordered item |
| description | 25oz cereal box | Description of the ordered item |
| quantity | 2 | Quantity ordered |
| weight | 2.5 | Total weight of the item |
| weight\_components |  |  |
| weight\_unit | oz | Weight unit of measure |
| external\_id | 987456321 | Merchant's item identifier of the substitute item |
| requested\_item\_external\_id | 258147369 | Merchant's item identifier of the original ordered item |
| external\_instance\_id | 861555aa-6875-4b02-b5f2-58ee14f323a9 | Additional identifier of the substitute item |
| price | 499 | Price provided by merchant in inventory feed |
| substitution\_source | DASHER | Item substituted by dasher |
| scanned\_code | 04904403 | Barcode scanned by Dasher |
| addition\_source |  |  |
| requested\_item\_external\_instance\_id | d4621a56-208b-4d03-b6dd-6dc5c1eea47f | Additional identifier as passed in the original payload |
| scanned\_data\_list | see json below | see explanation below |
| fulfilled\_substitution\_type | contact | The item is picked as substitution after contacting consumer |
| is\_unknown | false | This item exists in catalog |

scanned\_data\_list:

```
[  
  {  
    "format": "ean-8",  
    "is_variable_measure": false,  
    "product_code": "90440",  
    "check_digit": "3",  
    "country_code": "04",  
"scanned_code_sans_check_digit": "0490440"  
  }  
]  
  

```

### **Scenario 4:** Item substituted using a customer pre-selected substitute[​](#scenario-4-item-substituted-using-a-customer-pre-selected-substitute "Lien direct vers le titre")

[(reference)](https://developer.doordash.com/en-US/docs/drive/how_to/Drive_DSX/how_to_subs_other_shopping_use_cases#item-specific-option)

| Field Name (Shopped Items Section) | Value | Description |
| --- | --- | --- |
| name | Cereal | Name of ordered item |
| description | 25oz cereal box | Description of the ordered item |
| quantity | 2 | Quantity ordered |
| weight | 2.5 | Total weight of the item |
| weight\_components |  |  |
| weight\_unit | oz | Weight unit of measure |
| external\_id | 987456321 | Merchant's item identifier of the substitute item |
| requested\_item\_external\_id | 258147369 | Merchant's item identifier of the original ordered item |
| external\_instance\_id | 861555aa-6875-4b02-b5f2-58ee14f323a9 | Additional identifier of the substitute item |
| price | 499 | Price provided by merchant in inventory feed |
| substitution\_source | CUSTOMER | Item substitution pre-selected by customer |
| scanned\_code | 06541238 | Barcode scanned by Dasher |
| addition\_source |  |  |
| requested\_item\_external\_instance\_id | d4621a56-208b-4d03-b6dd-6dc5c1eea47f | Additional identifier as passed in the original payload |
| scanned\_data\_list | see json below | Components of the barcode interpreted as a UPC-E code |
| fulfilled\_substitution\_type | pre-selected | The item is pre-selected by customer as substitution |
| is\_unknown | false | This item exists in catalog |

scanned\_data\_list:

```
[  
  {  
    "format": "upc-e",  
    "is_variable_measure": false,  
    "product_code": "12",  
    "check_digit": "8",  
    "manufacturer_code": "654",  
    "number_system": "0",  
    "scanned_code_sans_check_digit": "0654123"  
  }  
]  
  

```

### **Scenario 5:** Item substituted using a merchant recommended substitute[​](#scenario-5-item-substituted-using-a-merchant-recommended-substitute "Lien direct vers le titre")

[(reference)](https://developer.doordash.com/en-US/docs/drive/how_to/Drive_DSX/how_to_subs_other_shopping_use_cases#item-specific-option)

| Field Name (Shopped Items Section) | Value | Description |
| --- | --- | --- |
| name | Cereal | Name of ordered item |
| description | 25oz cereal box | Description of the ordered item |
| quantity | 2 | Quantity ordered |
| weight | 2.5 | Total weight of the item |
| weight\_components |  |  |
| weight\_unit | oz | Weight unit of measure |
| external\_id | 987456321 | Merchant's item identifier of the substitute item |
| requested\_item\_external\_id | 258147369 | Merchant's item identifier of the original ordered item |
| external\_instance\_id | 861555aa-6875-4b02-b5f2-58ee14f323a9 | Additional identifier of the substitute item |
| price | 499 | Price provided by merchant in inventory feed |
| substitution\_source | MERCHANT | item substitution recommended by merchant |
| scanned\_code | 219408516284 | Barcode scanned by Dasher |
| addition\_source |  |  |
| requested\_item\_external\_instance\_id | d4621a56-208b-4d03-b6dd-6dc5c1eea47f | Additional identifier as passed in the original payload |
| scanned\_data\_list | see json below | see explanation below |
| fulfilled\_substitution\_type | pre-selected | The item is pre-selected by merchant as substitution |
| is\_unknown | false | This item exists in catalog |

scanned\_data\_list:

```
[  
  {  
    "format": "upc-a",  
    "is_variable_measure": true,  
    "product_code": "19408",  
    "check_digit": "4",  
    "number_system": "2",  
    "plu_check_digit": "5",  
    "scanned_code_sans_check_digit": "21940851628"  
  },  
  {  
    "format": "ean-13",  
    "is_variable_measure": true,  
    "product_code": "9408",  
    "check_digit": "4",  
    "country_code": "021",  
    "plu_check_digit": "5",  
    "scanned_code_sans_check_digit": "021940851628"  
  }  
]  

```

The barcode scanned by the mobile device is a UPC-A barcode starting with 2, which indicate it’s a weighted item:

* scanned\_data\_list[0] represents the components of the barcode interpreted as a UPC-A code, which is the most likely format.
* scanned\_data\_list[1] represents the components of the same barcode interpreted as an EAN-13 code, which is also a valid possibility"

### **Scenario 6:** Dasher Item Override *(When Overrides As Subs is not enabled)*[​](#scenario-6-dasher-item-override-when-overrides-as-subs-is-not-enabled "Lien direct vers le titre")

[(reference)](https://developer.doordash.com/en-US/docs/drive/how_to/Drive_DSX/how_to_subs_other_shopping_use_cases#force-overrides)

| Field Name (Shopped Items Section) | Value | Description |
| --- | --- | --- |
| name | Cereal | Name of ordered item |
| description | 25oz cereal box | Description of the ordered item |
| quantity | 2 | Quantity ordered |
| weight | 2.5 | Total weight of the item |
| weight\_components |  |  |
| weight\_unit | oz | Weight unit of measure |
| external\_id | 258147369 | Merchant's item identifier of the orginal ordered item |
| requested\_item\_external\_id |  |  |
| external\_instance\_id | 861555aa-6875-4b02-b5f2-58ee14f323a9 | Additional identifier as passed in the original payload |
| price | 499 | Price provided by merchant in inventory feed |
| substitution\_source | DASHER | Item substituted by dasher |
| scanned\_code | 10019320008266 | Barcode or PLU of the override item inputted by Dasher |
| addition\_source |  |  |
| requested\_item\_external\_instance\_id |  |  |
| scanned\_data\_list | see json below | Components of the barcode interpreted as a GTIN-14 code |
| fulfilled\_substitution\_type | override | Dasher assert they picked the correct item |
| is\_unknown | true | This item missing in catalog |

scanned\_data\_list:

```
[  
  {  
    "format": "gtin-14",  
    "indicator_digit": "1",  
    "product_code": "001932001351",  
    "check_digit": "2",  
    "scanned_code_sans_check_digit": "1001932001351"  
  }  
]  

```

### **Scenario 7:** Dasher Item Override when item is found in the catalog *(When Overrides As Subs is enabled)*[​](#scenario-7-dasher-item-override-when-item-is-found-in-the-catalog-when-overrides-as-subs-is-enabled "Lien direct vers le titre")

[(reference)](https://developer.doordash.com/en-US/docs/drive/how_to/Drive_DSX/how_to_subs_other_shopping_use_cases#force-overrides)

| Field Name (Shopped Items Section) | Value | Description |
| --- | --- | --- |
| name | Cereal | Name of ordered item |
| description | 25oz cereal box | Description of the ordered item |
| quantity | 2 | Quantity ordered |
| weight | 2.5 | Total weight of the item |
| weight\_components |  |  |
| weight\_unit | oz | Weight unit of measure |
| external\_id | 987456321 | Merchant's item identifier of the override item |
| requested\_item\_external\_id | 258147369 | Merchant's item identifier of the original ordered item |
| external\_instance\_id | 861555aa-6875-4b02-b5f2-58ee14f323a9 | Additional identifier as passed in the original payload |
| price | 499 | Price provided by merchant in inventory feed |
| substitution\_source | DASHER | Substituted by dasher |
| scanned\_code | 8901042957517 | Barcode or PLU of the override item inputted by Dasher |
| addition\_source |  |  |
| requested\_item\_external\_instance\_id |  |  |
| scanned\_data\_list | see json below | Components of the barcode interpreted as a EAN-13 code |
| fulfilled\_substitution\_type | override | Dasher assert they picked the correct item |
| is\_unknown | true | This item exists in catalog |

scanned\_data\_list:

```
[  
    {  
    "format": "ean-13",  
    "is_variable_measure": false,  
    "product_code": "95751",  
    "check_digit": "7",  
    "country_code": "890",  
    "manufacturer_code": "1042",  
    "scanned_code_sans_check_digit": "890104295751"  
    }  
]  

```

### **Scenario 8:** Dasher Item Override when item is not found in the catalog *(When Overrides As Subs is enabled)*[​](#scenario-8-dasher-item-override-when-item-is-not-found-in-the-catalog-when-overrides-as-subs-is-enabled "Lien direct vers le titre")

[(reference)](https://developer.doordash.com/en-US/docs/drive/how_to/Drive_DSX/how_to_subs_other_shopping_use_cases#force-overrides)

| Field Name (Shopped Items Section) | Value | Description |
| --- | --- | --- |
| name | Cereal | Name of ordered item |
| description | 25oz cereal box | Description of the ordered item |
| quantity | 2 | Quantity ordered |
| weight | 2.5 | Total weight of the item |
| weight\_components |  |  |
| weight\_unit | oz | Weight unit of measure |
| external\_id | 987456321 | Merchant's item identifier of the original ordered item even though there was an override item. This is because item info is unknown as it is not found in the catalog, this scenario is treated similar to overrides being disabled. Note: is\_unknown = true |
| requested\_item\_external\_id |  |  |
| external\_instance\_id | 861555aa-6875-4b02-b5f2-58ee14f323a9 | Additional identifier as passed in the original payload |
| price | 499 | Price provided by merchant in inventory feed |
| substitution\_source | DASHER | Substituted by dasher |
| scanned\_code | 10019320013512 | Barcode or PLU of the override item inputted by Dasher |
| addition\_source |  |  |
| requested\_item\_external\_instance\_id |  |  |
| scanned\_data\_list | see json below | Components of the barcode interpreted as a GTIN-14 code |
| fulfilled\_substitution\_type | override | Dasher assert they picked the correct item |
| is\_unknown | true | This item exists in catalog |

scanned\_data\_list:

```
[  
    {  
    "format": "gtin-14",  
    "indicator_digit": "1",  
    "product_code": "001932001351",  
    "check_digit": "2",  
    "scanned_code_sans_check_digit": "1001932001351"  
    }  
]  

```

## DASHER\_COMPLETED\_STAGING[​](#dasher_completed_staging "Lien direct vers le titre")

In Dasher Shop and Stage Orders, following the DASHER\_COMPLETED\_SHOPPING, a DASHER\_COMPLETED\_STAGING webhook will be sent to confirm the location where the Dasher has staged the order.

```
"staged_containers" : [  
  {  
    "external_id": "id1",  
    "external_location_id": "A1",  
    "external_zone_id": "Ambient"  
  },  
  {  
    "external_id": "id2",  
    "external_location_id": "A1",  
    "external_zone_id": "Ambient"  
  },  
  {  
    "external_id": "id3",  
    "external_location_id": "A1",  
    "external_zone_id": "Ambient"  
  }  
]  

```

[Précédent

[Explainer] Dasher Shop Delivery Tracking](/fr-CA/docs/drive/how_to/Drive_DSX/how_to_dsx_delivery_tracking)[Suivant

Notes de mise à jour](/fr-CA/docs/drive/overview/release_notes)

* [DASHER\_COMPLETED\_SHOPPING](#dasher_completed_shopping)
  + [**Scenario 1:** Item shopped as ordered](#scenario-1-item-shopped-as-ordered)
  + [**Scenario 2:** Weighted Item shopped as ordered](#scenario-2-weighted-item-shopped-as-ordered)
  + [**Scenario 3:** Item substituted when the preference is set to contact customer](#scenario-3-item-substituted-when-the-preference-is-set-to-contact-customer)
  + [**Scenario 4:** Item substituted using a customer pre-selected substitute](#scenario-4-item-substituted-using-a-customer-pre-selected-substitute)
  + [**Scenario 5:** Item substituted using a merchant recommended substitute](#scenario-5-item-substituted-using-a-merchant-recommended-substitute)
  + [**Scenario 6:** Dasher Item Override *(When Overrides As Subs is not enabled)*](#scenario-6-dasher-item-override-when-overrides-as-subs-is-not-enabled)
  + [**Scenario 7:** Dasher Item Override when item is found in the catalog *(When Overrides As Subs is enabled)*](#scenario-7-dasher-item-override-when-item-is-found-in-the-catalog-when-overrides-as-subs-is-enabled)
  + [**Scenario 8:** Dasher Item Override when item is not found in the catalog *(When Overrides As Subs is enabled)*](#scenario-8-dasher-item-override-when-item-is-not-found-in-the-catalog-when-overrides-as-subs-is-enabled)
* [DASHER\_COMPLETED\_STAGING](#dasher_completed_staging)