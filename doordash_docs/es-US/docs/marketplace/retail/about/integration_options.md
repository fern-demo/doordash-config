En esta página

# Integration for DoorDash Retail UI

This document outlines the integration solution designed for non-restaurant merchants in verticals like Convenience, Alcohol, Grocery, and Retail where a retail-centric user experience on DoorDash marketplace is optional.

> **Note:** API integration is the preferred method for Partners to share item-specific and store-level data as it enables more real-time data sharing, allowing us to closely mirror the in-store shopping experience on DoorDash.

An integration involves four main aspects:

1. **Sharing Item-Specific Data at the Business Level:**
   Partners need to share item-specific data such as unique identifiers, brand, size information, and images.

   * **Catalog Management API:**

     + Documentation: [Catalog Management API Documentation](https://developer.doordash.com/en-US/docs/marketplace/retail/catalog_management/overview)
   * **Feed File Integration:**

     + Learn more about [Feed File integration.](https://developer.doordash.com/en-US/docs/marketplace/inventory_feed_integration/overview)
2. **Sharing Item-Specific Data at the Store Level:**
   Partners need to share store-level data, including availability, pricing, balance on hand, and in-store location. We recommend sharing this information in as near-real time as possible to ensure that Customers have an accurate view of what is available for purchase with accurate pricing.

   * **Inventory/Pricing API:**

     + Documentation: [Inventory/Pricing Management API Documentation](https://developer.doordash.com/en-US/docs/marketplace/retail/inventory_pricing/overview)
   * **Feed File Integration:**

     + Learn more about [Feed File integration.](https://developer.doordash.com/en-US/docs/marketplace/inventory_feed_integration/overview)
3. **Order Fulfillment:**
   Partners need a mechanism for orders to be fulfilled. Options include:

   * **Dasher Shop and Deliver:** DoorDash dispatches Dashers to the store to shop and checkout.
   * **Merchant Pick:**

     + **Order API Integration:** Integrate through the Order API, sending order data to the Merchant's Order Management System (OMS) or Point of Sale (POS). Store employees pick the order, and after picking, the Merchant can choose to:
       - Utilize standard Dasher Delivery: A Dasher picks up the order and delivers it to the customer.
       - Opt for Self-Delivery: The Merchant uses their own delivery drivers.
     + **DoorDash Tablet:** Utilize DoorDash provided tablets to receive the order data necessary for in-store employees to pick the order.
4. **Managing Store Hours:**
   In addition to the primary integration components, partners also need to manage store hours on the platform. This is achieved through the recently released **Store Management API**.

   * **Store Management API:**
     + Documentation: [Store Management API Documentation](https://developer.doordash.com/en-US/docs/marketplace/retail/store_management/overview)

## API Endpoint Call Patterns:[​](#api-endpoint-call-patterns "Enlace directo al encabezado")

| API Endpoint | Batch Size | Rate Limit |
| --- | --- | --- |
| Inventory/Pricing API POST | 10k | 5-10 QPS |
| Inventory/Pricing API PATCH | 10k | 5-10 QPS |
| Inventory PULL | 10k | 5-10 QPS |
| Catalog Management API POST | 1k | 5-10 QPS |
| Catalog Management API PATCH | 1k | 5-10 QPS |
| PROMOTION Management API POST | 1k | 5-10 QPS |
| STORE HOURS API PATCH | N/A | 5-10 QPS |

## Steps to Start API Integration:[​](#steps-to-start-api-integration "Enlace directo al encabezado")

**Note:** The following steps are only necessary for Partners looking to utilize the DoorDash APIs.

1. **Join the Developer Portal:**

   * Create a [Developer Portal](https://developer.doordash.com/portal?Marketplace=true) account to establish a Developer Portal organization.
     + **Note:** If you already have a DoorDash account with their associated email, you can just “Sign-In” using the existing account OR you can use a different email address to create a new account.
   * Follow [these steps](https://developer.doordash.com/en-US/docs/marketplace/how_to/add_members) to add additional members to the development team.
2. **Add a Marketplace Integration:**

   * Reach out to your DoorDash technical account manager to add a Marketplace integration.
3. **Create a Provider:**

   * Configure a sandbox provider using the guide [here](https://developer.doordash.com/en-US/docs/marketplace/how_to/create_a_provider).
4. **Create Credentials:**

   * Create sandbox credentials following these [instructions](https://developer.doordash.com/en-US/docs/drive/how_to/manage_credentials/).
5. **Configure JWT Authentication:**

   * Follow the DoorDash guide to configure the JWT authentication method required for API interaction. [Guide to Configure JWT Authentication](https://developer.doordash.com/en-US/docs/marketplace/how_to/JWTs)
6. **Test Store Setup:**

   * Reach out to your DoorDash technical account manager to have a test store added to the Developer Portal.

## Enablement Requirements[​](#enablement-requirements "Enlace directo al encabezado")

If you are a third-party integration partner, you are also required to share [merchant-facing enablement materials](https://docs.google.com/forms/d/e/1FAIpQLScISb9PitX6f_xJC14eFS93sjcCuSnY7osFo9WePoQ0d-vdaA/viewform) during certification to onboard additional locations post-pilot. This includes:

* A list of supported systems the integration supports and any version requirements that merchants should be aware of if applicable.
* A link to your Merchant facing portal i.e where a Merchant can log in to manage their integration.
* A URL for a help article where Merchants can find information on any steps they need to complete on their end to prepare for the integration process.
* A URL for a help article where Merchants can find information on inventory and store availability management to educate Merchants on how to manage their stores once they’ve integrated.

## API Documentation:[​](#api-documentation "Enlace directo al encabezado")

* [Catalog Management API Documentation](https://developer.doordash.com/en-US/api/marketplace_v2/#tag/ItemManagementEndpoints)
* [Inventory/Pricing Management API Documentation](https://developer.doordash.com/en-US/api/marketplace_v2/#tag/InventoryManagementEndpoints)
* [Store Management API Documentation](https://developer.doordash.com/en-US/api/marketplace_v2/#tag/StoreManagementEndpoints)
* [Order API Documentation](https://developer.doordash.com/en-US/api/marketplace#tag/Order-Endpoints)

[Anterior

Update your Legacy Marketplace Integration](/es-US/docs/marketplace/faq/legacy_partner_migration)[Siguiente

Integration for DoorDash Retail UI](/es-US/docs/marketplace/retail/about/integration_options)

* [API Endpoint Call Patterns:](#api-endpoint-call-patterns)
* [Steps to Start API Integration:](#steps-to-start-api-integration)
* [Enablement Requirements](#enablement-requirements)
* [API Documentation:](#api-documentation)