Sur cette page

# Drive Dasher Shop & Deliver Playbook

A Dasher Shop & Deliver integration enables you to use DoorDash’s on-demand logistics platform and fleet of Dashers to shop for your customers at your store and deliver their orders, with high quality and at speed.

A typical dasher shop flow follows the below steps:

1. Your customer places an order on your own app/website
2. You request a Dasher to shop & deliver the order via the DoorDash Drive API
3. A Dasher is dispatched to shop the items on your customer’s shopping list
4. The Dasher delivers the order to your customer

This document covers how to integrate by:

* Sending through your items data to set up a catalog flow and an inventory flow
* Creating a shop & deliver order with the items set up and pickup / dropoff details
* Enabling the dasher shopping experience with substitutions and item-level instructions
* Allowing the dasher to checkout the shopped items successfully
* Reconciling the shopped items with your POS & inventory management systems
* Tracking the progress of your orders all the way through customer dropoff

You will build to our [Marketplace for Retailers APIs](https://developer.doordash.com/en-US/api/marketplace_v2) (to push through your catalog & inventory items data) and [DoorDash Drive APIs](https://developer.doordash.com/en-US/api/drive) (to book your deliveries).

## Getting Started[​](#getting-started "Lien direct vers le titre")

**Step 1 - Account Set Up:** Get started by [creating a Developer Portal account](https://developer.doordash.com/en-US/docs/drive/tutorials/get_started/#sign-into-the-developer-portal). The Developer Portal is the tool you’ll use to build and manage your integration. You can also [add other members](https://developer.doordash.com/en-US/docs/drive/how_to/add_members/) to your organization and assign permissions for each user based on your organization’s needs.

**Step 2 - Business & Store Set Up:** DoorDash will create your business and store (location, store id, phone number details needed from you).

**Step 3 - Credentials:** go ahead and create credentials to Marketplace and Drive to gain access to both sets of APIs. Check out our JSON Web Token (JWT) [resources] (<https://developer.doordash.com/en-US/blog/doordash-drive-jwt-resources>) to help you generate a JWT and communicate securely with DoorDash. Feel free to use one of our tutorials, which will walk you through getting the credentials you need to call the APIs and making some basic API calls.

* [Get started via API](https://developer.doordash.com/en-US/docs/drive/tutorials/get_started): This tutorial references different coding languages including Python, PHP, Java, Kotlin, and C#.
* If you're writing an app in Node.js (using JavaScript or TypeScript), [get started using our Node.js SDK](https://developer.doordash.com/en-US/docs/drive/tutorials/get_started_sdk)
* If you'd like to try our APIs interactively, [get started using our Postman collection](https://developer.doordash.com/en-US/docs/drive/tutorials/get_started_postman)

**Step 4 - Catalog Data:** Using the [Item Management](https://developer.doordash.com/en-US/api/marketplace_v2#tag/ItemManagementEndpoints) endpoint, start sending through catalog data. For the first time, wait for confirmation from the DoorDash team on successful processing of this data.

**Step 5 - Inventory Data:** Once the DoorDash team confirms successful processing of Catalog data, use [Inventory Management](https://developer.doordash.com/en-US/api/marketplace_v2#tag/InventoryManagementEndpoints) endpoint to send through inventory data at the store level.

**Step 6 - Delivery Creation:** Now, you are ready to start creating deliveries via the [Create Delivery](https://developer.doordash.com/en-US/api/drive#tag/Delivery/operation/CreateDelivery) endpoint using the items data you pushed through via the catalog / inventory endpoints.

* Use the [Create Quote](https://developer.doordash.com/en-US/api/drive#tag/Delivery/operation/DeliveryQuote) endpoint to validate the feasibility of the delivery (including confirming the pickup/delivery distance is within configured radius, any items not fulfillable, and other potential order failures).
* Subscribe to [webhooks](https://developer.doordash.com/en-US/docs/drive/reference/webhooks/) from the Drive APIs to receive updates about each delivery. If you need these events sent to multiple systems, reach out to the DoorDash Integrations team to get help with configuring the additional webhook urls.
* Use the [Delivery Simulator](https://developer.doordash.com/en-US/docs/drive/how_to/use_delivery_simulator/) within the Drive section of the Developer Portal to test your integration during and post development. This tool will not dispatch real dashers, but will be a way to progress through the different stages of an order receiving all the relevant webhooks / SMS notifications.

## Core Topics[​](#core-topics "Lien direct vers le titre")

* **Substitutions:** Instructions on how and what to substitute can be passed through in a few different ways. Refer to the Substitutions Explainer ([reference](https://developer.doordash.com/en-US/docs/drive/how_to/Drive_DSX/how_to_subs_other_shopping_use_cases)).
* **Checkout / Audit:** Instructions on how to use the checkout Barcode/QR code, utilizing the Audit API, Refer to the Checkout Explainer ([reference](https://developer.doordash.com/en-US/docs/drive/how_to/Drive_DSX/how_to_checkout_audit)).
* **Picked Items:** For guidance on how to interpret the Dasher Completed Shopping workbook, refer to the Shopping Completed Webhook Explainer ([reference](https://developer.doordash.com/en-US/docs/drive/how_to/Drive_DSX/how_to_shopping_complete_webhook)).
* **Delivery Tracking:** Instruction on how to set up SMS text messages to customers, and all webhooks expected to be sent during an order. Refer to the Delivery Tracking Explainer ([reference](https://developer.doordash.com/en-US/docs/drive/how_to/Drive_DSX/how_to_dsx_delivery_tracking)).

## Optional Functionality[​](#optional-functionality "Lien direct vers le titre")

You can choose to enable the following functionality for your integration via the APIs or by talking to the DoorDash Integrations Team

* **SMS notifications** - DoorDash can send text messages to customers. The content of these text messages can be configured directly via Developer Portal ([reference](https://developer.doordash.com/en-US/docs/drive/how_to/Drive_DSX/how_to_dsx_delivery_tracking))
* **Merchant Recommended Subs** - Use this if you want to send through your own recommendations and customers have not pre-selected substitutions. ([reference](https://developer.doordash.com/en-US/docs/drive/how_to/Drive_DSX/how_to_subs_other_shopping_use_cases))
* **Dasher-addition of new items to cart** - This is the ability for a dasher to add net new items to the cart upon customer request. ([reference](https://developer.doordash.com/en-US/docs/drive/how_to/Drive_DSX/how_to_subs_other_shopping_use_cases))
* **White Label Subs** - Customers, via a link, can update their substitution preferences to “contact me” or “refund me” options, or choose a substitution from DoorDash’s list of item recommendations ([reference](https://developer.doordash.com/en-US/docs/drive/how_to/Drive_DSX/how_to_subs_other_shopping_use_cases))
* **Partial Cart** - Recommended functionality to allow orders to get created with items available in inventory and without items unavailable in inventory. If this functionality is not enabled, a Drive delivery creation request will get rejected, thus failing the entire order, even if one item fails inventory checks.
* **PATCH Update** - Use this endpoint to update delivery details, item details, and other info after an order has been created until a dasher has been assigned (notified via the DASHER\_CONFIRMED webhook) [reference](https://developer.doordash.com/en-US/api/drive/#tag/Delivery/operation/UpdateDelivery)

## Important API Fields[​](#important-api-fields "Lien direct vers le titre")

### Catalog[​](#catalog "Lien direct vers le titre")

[Item Management Endpoint](https://developer.doordash.com/en-US/api/marketplace_v2#tag/ItemManagementEndpoints)

| Parameter | Field Name (API) | Required or Recommended | Field Description |
| --- | --- | --- | --- |
| MSID | merchant\_supplied\_item\_id | Required | Merchant's unique Item ID |
| UPC | other\_identifiers | Required | UPC (preferably GTIN-14 format) |
| secondary\_upc | other\_identifiers | Recommended | Required if any secondary UPCs associated with a product exist (preferably GTIN-14). If multiple UPCs are applicable, please separate with a delimiter. |
| Item Name | name | Required | The full product name the Dasher will see in their shopping list. This should stand alone to allow the Dasher to identify the product. It should not have acronyms or abbreviations. |
| Size | size.details.product\_specific\_size\_definition.value | Required | Size of product. Just metric value of weight (eg: 10oz) or purchase quantity (eg: 12ct) |
| Unit of Measurement | size.details.product\_specific\_size\_definition | Required | Unit of measure |
| L1 Category | item\_categorizations.category.name | Required | Highest level category / department of a product. |
| L2 Category | item\_categorizations.category.subcategory | Required (+ helpful for subs) | Subcategory below L1 category |
| L3 Category | item\_categorizations.category.subcategory | Required (+ helpful for subs) | Subcategory below L2 category (if applicable) |
| L4 Category | item\_categorizations.category.subcategory | Required (+ helpful for subs) | Subcategory below L3 category (if applicable) |
| L5 Category | item\_categorizations.category.subcategory | Required (+ helpful for subs) | Subcategory below L4 category (if applicable) |
| Image URL | images.url | Required | URL link to the primary product image. Provided as image url (at least 1400 x 800px - JPG File Format) |
| is\_alcohol | product\_traits | Required | Specify if this is an alcohol product. Required if alcohol is sold by business |
| is\_weighted\_item | product\_traits | Required | Specify if this is a weighted item. Required if weighted items are sold by business |
| average\_weight\_per\_each | weighted\_item\_info.average\_weight\_per\_each | Required | For weighted items, use this field to differentiate between count/weight vs weight/weight items. Example: A package of in-store prepared/cut chicken breast is sold as weight/weight - 2.5 lbs. A peach is picked by each, sold by weight - average weight UOM as the indicator for if it's a pick by each (see cell P3) |
| average\_weight\_uom | weighted\_item\_info.average\_weight\_measurement\_unit | Required | For weighted items, unit of measure for the average weight. This is where we differentiate between a count/weight vs weight/weight item. Example: weight/weight items - 'lb'; count/weight items - 'ea'; Sent in lowercase format 'lb' |
| price\_lookup\_codes | other\_identifiers | Required | Price Look-Up Code (for produce products). 4 or 5 digits (conventional vs organic) |
| secondary\_plu | other\_identifiers | Recommended | Required if any other PLUs that map to this item exist. If multiple exist, separate with a delimiter |
| Description | product.short\_description | Recommended | Short description of the product |
| brand\_name | brand\_info.name | Recommended | Brand name |
| Variant | product.variant | Recommended | Product variation - color, flavor, material etc |

### Inventory[​](#inventory "Lien direct vers le titre")

[Inventory Management Endpoint](https://developer.doordash.com/en-US/api/marketplace_v2#tag/InventoryManagementEndpoints)

| Field Name | Required or Recommended? | Description | Why is this field important? |
| --- | --- | --- | --- |
| base\_price\_per\_measurement\_unit | Required, if weighted item is sold | base price per measurement unit(kg, lb) in cents for weighted items | Provides pricing accuracy for weighted items, ensuring customers are charged correctly based on the weight of the product. |
| merchant\_supplied\_item\_id | Required | The MSID used for the item in the Item Management endpoint | Ensures each product is uniquely identifiable in the system, preventing confusion and errors in inventory processing. |
| item\_availability | Required | Item availability status | Allows for real-time inventory management, ensuring that Dashers are aware of which items are in stock and available for purchase. |
| base\_price | Required | Standard price for the item | Provides pricing accuracy for items, ensuring customers are charged correctly. |
| balance\_on\_hand | Recommended | Current stock level for the item | Helps in providing substitution recommendations to Dashers |
| last\_sold\_datetime | Recommended | DateTime in ISO8601 format of when the item was last sold at the store | Helps in providing substitution recommendations to Dashers |
| sale\_price | Recommended | Sale price for the item | Provides pricing accuracy for items, ensuring customers are charged correctly. |
| aisle | Recommended | Aisle where the item can be found | Assists Dashers in quickly locating items within the store, improving efficiency and reducing the time spent on order fulfillment. |
| zone | Recommended | Zone within the aisle or a general zone within the store where the item can be found | Provides additional location details, helping Dashers navigate the store more effectively and locate items with greater precision. |
| shelf | Recommended | Shelf within the aisle where the item can be found | Offers specific location information, aiding Dashers in finding items quickly and accurately, thus enhancing the shopping experience. |
| side | Recommended | Side of the aisle where the item is located | Clarifies the item's exact position within the aisle, reducing search time and improving order picking efficiency. |
| additional\_details | Recommended | Additional information about the location of the item | Provides any extra location-related information that may assist Dashers in locating items, ensuring a smoother and more efficient shopping process. |

### Delivery Creation[​](#delivery-creation "Lien direct vers le titre")

[Create Delivery Endpoint](https://developer.doordash.com/en-US/api/drive/#tag/Delivery/operation/CreateDelivery)

| Field Name | Required or Recommended | Field Description | Why is this field important? |
| --- | --- | --- | --- |
| external\_delivery\_id | Required | delivery identifier | Ensures each DoorDash order is uniquely identifiable. This id will also be used to cross reference webhook events and call the PATCH Update endpoint |
| pickup\_external\_business\_id | Required | The DD team will create a business and set an id for you to pass into this field (let us know if you need this to be a specific value) | Used to identify the right business instance |
| pickup\_external\_store\_id | Required | The DD team will create the stores and set up ids for you to pass into this field (let us know what you want the store ids to be) | Used to identify the right store instance |
| order\_fulfillment\_method | Required | specifies the type of delivery (shop\_deliver for DSD orders; shop\_stage for DSS orders) | used to trigger dasher shop specific functionality |
| pickup\_address | Optional | Address where order should be picked up. This address is overridden by store properties if pickup\_external\_store\_id and pickup\_external\_business\_id are used. | Ensures the dasher has the right pickup location to go to |
| pickup\_business\_name | Recommended | Name of pickup location. This name is overridden by store properties if pickup\_external\_store\_id and pickup\_external\_business\_id are used. | This field is surfaced to the dasher to easily identify where they are headed |
| pickup\_phone\_number | Recommended | Store phone number. Must include the country code that matches the country where the delivery is taking place. This number is overridden by store properties if pickup\_external\_store\_id and pickup\_external\_business\_id are used. | Used for dashers or DoorDash support to contact store |
| pickup\_instructions | Recommended | Basic instructions to help the Dasher during the pickup process, e.g. "enter through side door." | This helps the dasher navigate at the point of pickup |
| pickup\_reference\_tag | Recommended | Order reference displayed on the dasher app | This field is surfaced to the dasher to easily identify the package they are picking up. This is often the external\_delivery\_id, for ease of reconciliation at the store. |
| dropoff\_address | Required | Address where order should be delivered |  |
| dropoff\_phone\_number | Required | Customer phone number, including the country code | Ensures the dasher has the right dropoff address to go to |
| dropoff\_instructions | Recommended | Basic instructions to help the Dasher during the dropoff process, e.g. "buzz #1234." Do not include prompts for contactless deliveries in this field. | This helps the dasher navigate at the point of dropoff |
| dropoff\_contact\_given\_name | Required | Customer first name | used for dasher / store identification of package |
| dropoff\_contact\_family\_name | Required | Customer last name | used for dasher / store identification of package |
| dropoff\_contact\_send\_notifications | Recommended | Enable / disable customer text messages from DoorDash. This field is enabled by default. | Further edits to text messages can be made directly in the developer portal settings. |
| shopping\_options.payment\_method | Required | The payment method to be used by the Dasher while shopping at the store. Recommended: barcode / qr code | See [checkout explainer](http://localhost:3000/docs/drive/how_to/Drive_DSX/how_to_checkout_audit) for more information. |
| payment\_barcode | Recommended | The token that will be scanned as a barcode at checkout lane as payment for the order in store. | See [checkout explainer](http://localhost:3000/docs/drive/how_to/Drive_DSX/how_to_checkout_audit) for more information. |
| order\_value | Required | Order subtotal, excluding tax, tips, and fees | This field is used to assess the value of the order, especially in cases of refunds. |
| items.name | Recommended | name of item | describes the item being requested and shopped |
| items.description | Recommended | description of item | describes the item being requested and shopped |
| items.quantity | Required | desired quantity | indicates to the dasher the desired amount to shop |
| items.external\_id | Required | Merchant's unique Item ID | Used to identify the right item in the system that was processed via the catalog / inventory data feeds, preventing confusion and errors in inventory processing. |
| items.external\_instance\_id | Optional | additional identifier | used to distinguish between multiple items with the same external\_id, such as for 2 steaks in the same order with separate weights |
| items.special\_instructions | Recommended | item-level notes to help dasher with picking | Reference the [Substitutions & Other Shopping Use Cases explainer](http://localhost:3000/docs/drive/how_to/Drive_DSX/how_to_subs_other_shopping_use_cases) for more information. |
| items.item\_options.substitution\_preference | Required | options: refund, contact, substitute | Reference the [Substitutions & Other Shopping Use Cases explainer](http://localhost:3000/docs/drive/how_to/Drive_DSX/how_to_subs_other_shopping_use_cases) for more information. |
| items.item\_options.substitute\_item\_ids | Recommended | customer pre-selected item ids; substitution\_preference = substitute | reference the [Substitutions explainer](http://localhost:3000/docs/drive/how_to/Drive_DSX/how_to_subs_other_shopping_use_cases) |
| items.item\_options.merchant\_recommended\_substitute\_item\_ids | Recommended | merchant recommended item ids; ; substitution\_preference = substitute | reference the [Substitutions explainer](http://localhost:3000/docs/drive/how_to/Drive_DSX/how_to_subs_other_shopping_use_cases) |
| items.item\_options.substitute\_item\_ids\_additional\_metadata.item\_id | Recommended | merchant item id(s) of substitute item | Used to describe the substitute item |
| items.item\_options.substitute\_item\_ids\_additional\_metadata.quantity | Recommended | quantity of substitution item | Used to describe the substitute item |
| items.item\_options.substitute\_item\_ids\_additional\_metadata.weight | Recommended | weight of substitution item | Used to describe the substitute item |
| items.item\_options.substitute\_item\_ids\_additional\_metadata.weight\_unit | Recommended | weight unit of substitution item (i.e. "lbs") | Used to describe the substitute item |
| items.item\_options.weight\_unit | Required | The weight unit for the item being shopped. Not updatable. | describes the quantity of the item to be shopped |
| pickup\_time OR dropoff\_time | Recommended | [ASAP deliveries] The UTC date-time (in ISO-8601 format) when the order should be picked up or dropped off. Only one or the other should be included in the request, not both. | Used to determine dasher assignments on the DoorDash side |
| pickup\_window AND dropoff\_window | Recommended | [scheduled deliveries] The UTC date-time (in ISO-8601 format) when the order should be picked up or dropped off. Only one or the other should be included in the request, not both. For effective dasher assignments and sufficient shopping time, pickup window start time should ideally be the store opening time, while the dropoff window end time should be the customer requested delivery time | Used to determine dasher assignments on the DoorDash side |
| contactless\_dropoff | Recommended | Allows the Dasher to leave the order at the customer’s door, prompting them to take a photo upon dropoff. Cannot be true for restricted item deliveries like alcohol. | guides the dasher through the dropoff process" |
| dropoff\_requires\_signature | as needed | Obtain a signature from customer before dropping off; This is recommended for high value orders or orders containing restricted items | guides the dasher through the dropoff process |
| action\_if\_undeliverable | "return" selection required for all restricted item deliveries | choose to return order to store or dispose; if the return option is not chosen, dasher will fall back to a contactless dropoff (leave at door) option | guides the dasher through the dropoff process |
| tip | Recommended | dasher tip | improves dasher acceptance rates |
| order\_contains | Required for all restricted item deliveries per DoorDash Policy (note there is a return fee associated with returns) | Specifies the restricted item(s) contained in the order (i.e. alcohol, otc, etc) | triggers the restricted items flow so the dasher is able to scan ID and take the necessary steps at pickup & dropoff |

## Testing[​](#testing "Lien direct vers le titre")

| Topic | Test Case |
| --- | --- |
| Order Creation | Delivery creation - full cart |
| Order Creation | Delivery creation - partial cart |
| Order Creation | Delivery creation - fail (all items unavailable) |
| Order Creation | pickup instructions |
| Order Creation | dropoff instructions |
| Order Creation | item-level notes (special\_instructions field) |
| Shopping - Item Type | Weighted Item (Count/Weight Item) |
| Shopping - Item Type | Weighted Item (Weight/Weight Item) |
| Shopping - Item Type | Count Item |
| Shopping - Item Type | Flowers - skip\_scan |
| Shopping - Item Type | Count Item - single\_scan |
| Shopping - Item Type | Count Item - single\_scan (PLU + UPC or UPC only) |
| Shopping - Item Type | Count/Weight Item - single\_scan |
| Shopping - Item Type | Count/Weight Meat & Fish Item multi\_scan |
| Shopping - Item Type | Weight/Weight Item Meat & Fish Item single\_scan |
| Shopping - Item Type | Weight/Weight Item Not Meat & Fish Item skip\_scan |
| Shopping - Item Type | Variant Item - Same Name |
| Shopping - Item Type | Variant Item - Same Name |
| Shopping - Item Type | Variant Item - Same Name |
| Shopping - Item Type | Variant Item - Same Name |
| Shopping - Item Type | Multi-instance of the same item in an order |
| Shopping - Substitutions | Multi-instance substitutions |
| Shopping - Item Type | Multi-PLU item (same SKU, different PLUs, same store); By PLU OCR |
| Shopping - Item Type | Multi-PLU item (same SKU, different PLUs, same store); By PLU input |
| Shopping - Item Type | Multi-PLU item (same SKU, different PLUs, same store); By GS1 barcode |
| Shopping - Item Type | Alcohol item |
| Shopping - Item Type | 18+ OTC item |
| Shopping - Item Type | Prepackaged produce item (eg: boxed salad) |
| Shopping - Item Type | Deli-service counter item (packed on-demand) |
| Shopping - Item Type | Deli-service counter item (pre-packed) |
| Shopping - Substitutions | substitutions preference = refund |
| Shopping - Substitutions | substitutions preference = contact |
| Shopping - Substitutions | substitutions preference = No Regrets sub picked |
| Shopping - Substitutions | No Regrets sub picked, then changed |
| Shopping - Substitutions | Meat / Fish as sub |
| Shopping - Substitutions | Produce as sub |
| Shopping - Substitutions | Alcohol subs - orig order doesn't have alcohol enabled |
| Shopping - Substitutions | White-label subs |
| Shopping - Pickup Variation | Photo override item (in catalog) / Dx override |
| Shopping - Pickup Variation | Photo override item (not in catalog) / Dx addition |
| Shopping - Pickup Variation | No items picked (refunded) |
| Shopping - Pickup Variation | Item with secondary location(s) |
| Shopping - Pickup Variation | Granular aisle locations |
| Shopping - Pickup Variation | Optimal pick path |
| Shopping - Pickup Variation | Indoor maps |
| Shopping - Pickup Variation | Same UPC, different flavors |
| Shopping - Pickup Variation | Same PLU, different flavors |
| Checkout | Audit - Pass / Happy path |
| Checkout | Audit - Skip QR code scan (Dx shows order ID) |
| Checkout | Audit - Bypass |
| Checkout | Audit - Fail |
| Dropoff | HITM order - happy path |
| Dropoff | HITM order - unattended contactless fallback |
| Dropoff | HITM order w/ alcohol - happy path |
| Dropoff | HITM order w/ alcohol - return |
| Dropoff | General returns |
| Dropoff | Signature order |
| Dropoff | Cancellation |

## Get Production Access[​](#get-production-access "Lien direct vers le titre")

Once the DoorDash team sets up and approves your production environment, you can generate your credentials directly on your developer portal account.

[Précédent

How to Build for Restaurants](/fr-CA/docs/drive/how_to/build_for_restaurants)[Suivant

[Explainer] Substitutions & Other Shopping Use Cases](/fr-CA/docs/drive/how_to/Drive_DSX/how_to_subs_other_shopping_use_cases)

* [Getting Started](#getting-started)
* [Core Topics](#core-topics)
* [Optional Functionality](#optional-functionality)
* [Important API Fields](#important-api-fields)
  + [Catalog](#catalog)
  + [Inventory](#inventory)
  + [Delivery Creation](#delivery-creation)
* [Testing](#testing)
* [Get Production Access](#get-production-access)