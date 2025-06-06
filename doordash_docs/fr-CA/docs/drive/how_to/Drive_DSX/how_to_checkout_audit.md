Sur cette page

# [Explainer] Checkout & Audit

### Checkout Barcode / QR Code Enablement[​](#checkout-barcode--qr-code-enablement "Lien direct vers le titre")

At checkout, the Dasher will present a QR code or barcode of your choosing to identify the order. You have the ability to send through a value that will be rendered on the Dasher’s phone as a barcode or QR code for the cashier to scan to facilitate payment. Optionally, DoorDash can configure a default value of available attributes (for example: order ID + store ID).

To set your own checkout barcode or QR code, populate the following fields in the order creations payload.

| Field Name (Drive API) | Field Value |
| --- | --- |
| shopping\_options.payment\_method | "barcode" |
| shopping\_options.payment\_barcode | barcode vaue (i.e. "123456789") |

### Audit API[​](#audit-api "Lien direct vers le titre")

Once the Dasher has finished shopping, you can temporarily pause the checkout process in the Dasher App until an audit is conducted at the point of sale. After the store associate completes the audit, your POS system can send a signal via the Audit API to notify us. This signal will enable the Dasher to proceed with the delivery flow in the Dasher App.

**Request Body Schema**
<https://developer.doordash.com/en-US/api/drive#tag/Audit/operation/CheckoutAuditSignal>

Request Header:

| Key | Value |
| --- | --- |
| Authorization | Same JWT token as other API |
| Is\_test (only needed for Staging environment) | TRUE |

**Bypass**

In the event of an outage or other technical issues, Dashers can bypass the Audit step in the Dasher App by entering a bypass code. This code should be provided by the store associate to the Dasher. By default, the bypass code is the last four digits of the support\_reference value found in the response body of the order creation API call.

Note: the Dasher will be able to proceed past checkout and to the delivery steps once this signal is received (even if "audit\_status" = "FAILED").

[Précédent

[Explainer] Substitutions & Other Shopping Use Cases](/fr-CA/docs/drive/how_to/Drive_DSX/how_to_subs_other_shopping_use_cases)[Suivant

[Explainer] Dasher Shop Delivery Tracking](/fr-CA/docs/drive/how_to/Drive_DSX/how_to_dsx_delivery_tracking)

* [Checkout Barcode / QR Code Enablement](#checkout-barcode--qr-code-enablement)
* [Audit API](#audit-api)