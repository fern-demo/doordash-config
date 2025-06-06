On this page

# [Explainer] Substitutions & Other Shopping Use Cases

Substitutions instructions can be specified in a few different ways for when the dasher is unable to find the requested item and marks it out of stock.

**An example flow:**
During ecommerce shopping, allow customers to select if they want an item to be substituted or not.

* If yes

  + Allow customers to pre-select items → pass these items through the delivery creation payload
  + If customers have not pre-selected items
    - Recommend most popular / probable substitutions to guide the dashers → pass these items through the delivery creation payload (merchant recommended subs)
    - [or] Choose the “contact” option as the substitution preference in the delivery creation payload so the dasher can contact the customer during shopping to align on a substitution preference
      * Allow dashers to add net new items to the cart upon customer request
  + Surface the white label subs link so customers can update their substitution instructions for any item even after the DoorDash order has been created.
* If not

  + Choose the Refund option as the substitution preference in the delivery creation payload so the dasher marks the item as out of stock and does not pick a substitute
  + Surface the white label subs link so customers can update their substitution instructions for any item even after the DoorDash order has been created.

Send through substitution instructions for an item in a few different ways:

### Item-specific option[​](#item-specific-option "Direct link to heading")

You can send item-specific substitution options for the Dasher to choose from as part of the Delivery Creation payload as well as the PATCH Update API endpoint (until dasher assignment).

**Customer-selected** if you allow your customers to pre-select items. This is highly recommended as the dasher has some options to choose from instead of having to call the customer.

![customer selected](/en-US/assets/images/dsx_cx_selected_option-d6f0ff40c134b29e8edf261572ee6283.png)

| Field Name (Drive API) | Field Value |
| --- | --- |
| items.item\_options.substitution\_preference | "substitute" |
| items.item\_options.substitute\_item\_ids | merchant item id(s) |
| items.item\_options.substitute\_item\_ids\_additional\_metadata.id | merchant item id(s) of substitute item |
| items.item\_options.substitute\_item\_ids\_additional\_metadata.quantity | quantity of substitution item |
| items.item\_options.substitute\_item\_ids\_additional\_metadata.weight | weight of substitution item |
| items.item\_options.substitute\_item\_ids\_additional\_metadata.weight\_unit | weight unit of substitution item (i.e. "lbs") |

**Merchant recommended subs** if you want to send through your own recommendations. This is especially helpful if your customers have not pre-selected their substitutions and you are able to provide some options for the dasher to choose from at the store. In this scenario, the dasher will still text the customer informing them of the item they are substituting with so the customer is able to confirm.

![merchant recommended](/en-US/assets/images/dsx_mx_recommended_option-9decbd79acc9a0cbe33ba886e2ca5ef9.png)

| Field Name (Drive API) | Field Value |
| --- | --- |
| items.item\_options.substitution\_preference | "substitute" |
| items.item\_options.merchant\_recommended\_substitute\_item\_ids | merchant item id(s) |
| items.item\_options.substitute\_item\_ids\_additional\_metadata.id | merchant item id(s) of substitute item |
| items.item\_options.substitute\_item\_ids\_additional\_metadata.quantity | quantity of substitution item |
| items.item\_options.substitute\_item\_ids\_additional\_metadata.weight | weight of substitution item |
| items.item\_options.substitute\_item\_ids\_additional\_metadata.weight\_unit | weight unit of substitution item (i.e. "lbs") |

The dasher\_completed\_shopping webhook will reflect this shopping via the following fields:
Substitution\_source = “dasher”

*Note: please reach out to the DoorDash Integrations team to enable this option via a configuration.*

### “Contact Me” option[​](#contact-me-option "Direct link to heading")

You can request that the Dasher contact the customer during the pick process to agree on a suitable substitution

![contact me](/en-US/assets/images/dsx_contact_me-7bf87d4be564be804439273350dc946b.png)

| Field Name (Drive API) | Field Value |
| --- | --- |
| items.item\_options.substitution\_preference | "contact" |

*Note: if you want to disable customer communications during dasher shop time, please reach out to DoorDash.*

### “Refund me” option[​](#refund-me-option "Direct link to heading")

You can ask the Dasher not to pick another option and mark the item out of stock, in the event that the requested item is unavailable.

| Field Name (Drive API) | Field Value |
| --- | --- |
| items.item\_options.substitution\_preference | "refund" |

### White-label post checkout option[​](#white-label-post-checkout-option "Direct link to heading")

![white label subs](/en-US/assets/images/dsx_white_label-4c2869190c3dc933a9bf9d193959bdb9.png)

Customers, via a link, can update their substitution preferences to “contact me” or “refund me” options, or choose a substitution from DoorDash’s list of item recommendations.

* The link to this white-label UI will come through via customer text messages or through the tracking link (found in webhooks or delivery creation response payload).
* Customer preferences from past selections will be saved.
* Steps to enable functionality:
  + Step 1: Reach out to the DoorDash Integrations team to turn on the white label UI configuration.
  + Step 2
    *[if DoorDash owns customer communications]*
    - Navigate to the “SMS” Settings in your Developer Portal, select the appropriate business from the dropdown and configure the variable {subs\_link} to your desired text message.
      * We recommend you add the {subs\_link} variable to the “Delivery created” SMS. Example: “Please make substitution selections via {subs\_link}”
      * Ensure the Drive API field “should\_send\_notifications” is set to true to allow customer text messages to go through.
      * Skip this step if you do not want text messages enabled.
        *[if Merchant owns customer communications]*
    - We recommend you send the subs link right after the ecommerce checkout so the customers have the ability to fill in substitution instructions well in advance.

### Force Overrides[​](#force-overrides "Direct link to heading")

Allow the dasher pick up an item by asserting the item they have picked up is correct, regardless of a failed barcode scan. This feature is useful when the barcode is damaged or there is a UPC mismatch with the catalog data previously sent. To override, the dasher will click the button “I have the correct item”, take a photo and proceed.

Configuration options: Reach out to DoorDash if you want to allow dasher to pick an override

* That is in the catalog data sent to DoorDash

![force override 1](/en-US/assets/images/dsx_force_override_in_catalog-e29c6f4450df2d54be0b262270281c0f.png)

* That is not in the catalog data sent to DoorDash

![force override 2](/en-US/assets/images/dsx_force_override_not_in_catalog-5ba47c28d4c4d03a72f421b52ae1b0ba.png)

* The dasher\_completed\_shopping webhook will reflect this shopping via the following fields:
  + Substitution\_source = “dasher”
  + Scanned\_barcode = overridden item’s barcode

### Dasher-addition of new items to cart[​](#dasher-addition-of-new-items-to-cart "Direct link to heading")

This is the ability for a dasher to add net new items to the cart upon customer request during shop time. Activating the dasher-addition flow requires a call or text between the customer and dasher during the shopping process. This feature can help customers add items they may have forgotten when they first created the order. The dasher can add up to 5 new items (configurable). Maximum weight for an item can also be configured. A consideration for the merchant would be to plan for the incremental charges.

![dasher addition](/en-US/assets/images/dsx_dx_addition-8f364ad3eea316ffe0d90d85cd3d9c95.png)

The dasher\_completed\_shopping webhook will reflect this shopping via the following fields:
addition\_source = “dasher”

*Note: Reach out to the DoorDash Integrations team to enable this feature.*

### Multiple instance of same item[​](#multiple-instance-of-same-item "Direct link to heading")

You can add multiple instances of the same item (same item id) to an order if there are item-level differences for each instance. For example: allowing your customers to add two types of bananas (yellow bananas, green bananas) or two cuts of meat with different weights.

![multi instance](/en-US/assets/images/dsx_multi_instance-318eff34844e428160c83a901a8232eb.png)

Use the following fields to indicate the differences:

| Field Name (Drive API) | Field Value |
| --- | --- |
| items.special\_instructions | item-level notes (i.e. "green bananas") |
| items.external\_instance\_id | id to differentiate same external id |

[Previous

Drive Dasher Shop & Deliver Playbook](/en-US/docs/drive/how_to/Drive_DSX/build_for_dsx)[Next

[Explainer] Checkout & Audit](/en-US/docs/drive/how_to/Drive_DSX/how_to_checkout_audit)

* [Item-specific option](#item-specific-option)
* [“Contact Me” option](#contact-me-option)
* [“Refund me” option](#refund-me-option)
* [White-label post checkout option](#white-label-post-checkout-option)
* [Force Overrides](#force-overrides)
* [Dasher-addition of new items to cart](#dasher-addition-of-new-items-to-cart)
* [Multiple instance of same item](#multiple-instance-of-same-item)