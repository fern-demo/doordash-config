## [New testing and monitoring tools](/es-US/blog/new-testing-monitoring-tools)

24 de mayo de 2023 · 4 min de lectura

[![Alex Mullans](https://avatars.githubusercontent.com/u/99431555?v=4)](https://github.com/infin8x-dd)

[Alex Mullans](https://github.com/infin8x-dd)

Product Manager

Whether you're using our white-label delivery product and need food to be picked up just as it's hot and ready to go, or you're bringing orders from DoorDash Marketplace into your point-of-sale and kitchen systems in the height of the dinner rush, you customers expect that everything "just works". To meet those expectations, we strive to ensure that every integration between DoorDash and our partners—merchants, online ordering systems, point-of-sale systems, etc.—is highly reliable.

To help integration providers create highly reliable integrations, we're introducing new tools that make it easier to monitor and troubleshoot an integration: integration health dashboards and event logs. We're also introducing tools and guides that enable every partner to build a more fully-featured integration right from the start, including an upgraded delivery simulator for DoorDash Drive and feature usage tracking built into the Developer Portal.

## Monitor the health of your integration with new dashboards[​](#monitor-the-health-of-your-integration-with-new-dashboards "Enlace directo al encabezado")

We've introduced new dashboards in the Developer Portal that show you up-to-the-minute status, and a historical view, of API requests (from you to DoorDash) and webhooks (from DoorDash to you). You can use these dashboards to see, in ~real-time, if something is wrong between DoorDash and your systems. Soon, we'll also proactively notify you if we detect an issue with the integration, so that it's even faster to remediate and get back to accepting orders and requesting deliveries.

You can check out your dashboard in the [Developer Portal](https://developer.doordash.com/portal) - look for the new **Overview** tab!

![A screenshot of the Developer Portal dashboard](/es-US/assets/images/overview-dashboard-c532794c7bf3502c4420ba9377ef71a3.png)

## Investigate issues using the event log[​](#investigate-issues-using-the-event-log "Enlace directo al encabezado")

The Developer Portal now keeps a log of every API request & response we exchange with your integration, in addition to the [webhook logs](https://developer.doordash.com/blog/2022-11-22-webhook-logs) we introduced late last year. This can help if you're trying to troubleshoot issues with a particular delivery or order, because you can see the full request that DoorDash received from your integration and what we sent back as a result.

To get started with Event Logs, head into the [Developer Portal](https://developer.doordash.com/portal) and look for the **Event Log** tab.

![A screenshot of the Developer Portal event log](/es-US/assets/images/event-log-fd60c71e886e862bb0110ab15272cc7b.png)

tip

[Personally identifiable information](https://csrc.nist.gov/glossary/term/personally_identifiable_information) (or "PII") is redacted before it's stored in the Event Log. It's normal to see `REDACTED` in the Event Log when looking at a field that has PII, like `dropoff_contact_given_name`.

## Track and discover new features[​](#track-and-discover-new-features "Enlace directo al encabezado")

The new Features page in the Developer Portal will have a full list of all Marketplace and Drive features. Each feature will be linked to DoorDash’s developer documentation with detailed guides to help you implement and enable these features. As new features are built,they will be checked off helping you keep track of your integration.

![A screenshot of the Developer Portal features](/es-US/assets/images/features-089c4bf5ca60b924a104e9355028777a.png)

# Get Started with Doordash APIs

The Getting Started Page will help guide you through the steps to successfully integrate with Doordash APIs. The page has step by step directions to help you to set up your test environment, generate access keys, and configure test stores. It also walks you through building required features for a Doordash integration and the steps to get your production environment approved.

![A screenshot of the Developer Portal Get Started Page](/es-US/assets/images/get_started-1167e29a8db3d70475d92659101928e1.png)

## Drive integrations: test "enroute" webhooks and more with an upgraded simulator[​](#drive-integrations-test-enroute-webhooks-and-more-with-an-upgraded-simulator "Enlace directo al encabezado")

When you build an integration for Drive, our API for on-demand local delivery, you can [use the Delivery Simulator](https://developer.doordash.com/docs/drive/how_to/use_delivery_simulator) to fully test out your integration and make sure you're prepared for anything that can happen during a live delivery. Based on feedback from our integration partners, we've added some frequently-requested capabilities to the simulator. You can now simulate:

* The "enroute" [webhooks](/es-US/docs/drive/how_to/webhooks) that your app can use to show the Dasher's location in real time on a map
* A [returnable delivery](/es-US/docs/drive/how_to/return_to_pickup)
* A [high-value or signature-required delivery](/es-US/docs/drive/how_to/deliver_high_value_items)
* A Dasher reassignment
* A DoorDash Support-initiated cancellation

To get started, [go to the simulator](https://developer.doordash.com/portal/integration/drive/delivery_simulator), create a delivery, and look out for new options like the ones shown here:

![A screenshot of the delivery simulator showing actions like sending an enroute webhook](/es-US/assets/images/delivery-simulator-enroute-2349811785a8848796d9ca4ade717f78.png)

## Share your thoughts[​](#share-your-thoughts "Enlace directo al encabezado")

Whether you're building an integration with DoorDash for the first time or you've been a partner for a long time, we look forward to your feedback on these new tools. Join us in the [DoorDash Developer Discord](https://discord.gg/8Z5vgFw8Qf) and tell us your thoughts!

**Etiquetas:**

* [drive-api](/es-US/blog/tags/drive-api)
* [marketplace-api](/es-US/blog/tags/marketplace-api)
* [developer-portal](/es-US/blog/tags/developer-portal)
* [dev-tools](/es-US/blog/tags/dev-tools)

## [Customized SMS messages and other Drive API updates](/es-US/blog/customized-sms-messages-and-other-drive-updates)

8 de marzo de 2023 · 3 min de lectura

[![Bethany Christy](https://avatars.githubusercontent.com/u/91620868?v=4)](https://github.com/bethanychristy)

[Bethany Christy](https://github.com/bethanychristy)

Senior Manager, Product Operations

We’ve been busy making improvements to the Drive API and Developer Portal so you can create and manage deliveries more easily. Here’s what’s new:

* [Customize the SMS messages](https://developer.doordash.com/portal/integration/drive/configuration/sms)sent to customers about their deliveries.
* Leverage new [Drive API](https://developer.doordash.com/en-US/api/drive/) capabilities: update tip when accepting a quote, provide item-level details, specify what vehicle types are allowed for your deliveries, and require signature upon delivery.
* Authenticate with the Drive APIs more easily with our new [JWT utilities](https://developer.doordash.com/en-US/blog/doordash-drive-jwt-resources).

## Configure SMS delivery updates[​](#configure-sms-delivery-updates "Enlace directo al encabezado")

During the course of a delivery, customers receive automated SMS notifications about the Dasher’s progress. These texts include the tracking link returned in our response to delivery creation requests, as well as status updates as the Dasher picks up the items and arrives at the dropoff location.

Depending on your business needs, you may wish to customize these SMS messages. The new [Settings view](https://developer.doordash.com/portal/integration/drive/configuration/sms) in the Developer Portal allows you to do just that by controlling which SMS customers receive and the text for each message. In the case that you’re managing multiple businesses and/or stores, you’re also able to control SMS notifications at the business level, for both sandbox and production environments.

SMS message customization is just the first feature we’re introducing as part of the Settings view. Stay tuned as we roll out new features to give you greater control over your DoorDash integration and the delivery experience!

[Learn more in our docs](https://developer.doordash.com/docs/drive/how_to/configure_sms)

## JWT utilities[​](#jwt-utilities "Enlace directo al encabezado")

In order to communicate securely with DoorDash, your application must pass a JSON Web Token (JWT) to authenticate with our API. We've compiled a list of [tools and resources](https://developer.doordash.com/en-US/blog/doordash-drive-jwt-resources/) to help your development team get started with JWTs.

## Sample Applications on GitHub[​](#sample-applications-on-github "Enlace directo al encabezado")

You can download and clone sample applications that communicate with the DoorDash API from GitHub. Sample applications include [Node.js](https://github.com/JoshAtDoorDash/DoorDashAPI-Nodejs-Sample), [Python](https://github.com/JoshAtDoorDash/DoorDashAPI-Python-Sample), [PHP](https://github.com/JoshAtDoorDash/DoorDashAPI-PHP-Sample), [Java](https://github.com/JoshAtDoorDash/DoorDashAPI-Java-Sample), [Kotlin](https://github.com/JoshAtDoorDash/DoorDashAPI-Kotlin-Sample), and [C#/.NET](https://github.com/JoshAtDoorDash/DoorDashAPI-CSharp-Dotnet-Sample).

## Update tip when accepting a quote[​](#update-tip-when-accepting-a-quote "Enlace directo al encabezado")

By popular demand, we’ve updated the Drive API to allow `tip` to be updated when accepting a delivery quote. This is particularly useful in an e-commerce checkout experience where the customer may wish to get a delivery quote when they start their order, and then add a tip just before completing checkout.

## Allowed vehicles[​](#allowed-vehicles "Enlace directo al encabezado")

With the new `dasher_allowed_vehicles` field on the Drive API, you can now control the vehicle type(s) that a Dasher can use to complete your delivery. For example, as a laundry service moving large bags of clothes, you can specify that your deliveries should be handled by a Dasher in a car.

## Item-level details[​](#item-level-details "Enlace directo al encabezado")

Provide added details about the items being delivered, such as price, for more accurate deliveries and refunds.

**Etiquetas:**

* [jwt](/es-US/blog/tags/jwt)
* [drive-api](/es-US/blog/tags/drive-api)
* [settings](/es-US/blog/tags/settings)

## [Helpful JWT resources](/es-US/blog/doordash-drive-jwt-resources)

15 de febrero de 2023 · 2 min de lectura

[![Josh Hurley](https://avatars.githubusercontent.com/u/109998658?v=4)](https://github.com/JoshAtDoorDash)

[Josh Hurley](https://github.com/JoshAtDoorDash)

Developer Advocate

After creating a new DoorDash Developer account, your next step is to explore the [DoorDash Drive API](https://developer.doordash.com/en-US/api/drive/). In order to communicate securely with DoorDash, your application must pass a JSON Web Token (JWT) to authenticate with our API. You’ll first want to create sandbox [DoorDash Drive API credentials](https://developer.doordash.com/en-US/docs/drive/how_to/manage_credentials) that will be used in generating a JWT. Many languages and frameworks provide libraries to create JWT for you. You can find examples for popular language in the [step-by-step guide for creating a DoorDash JWT](https://developer.doordash.com/en-US/docs/drive/how_to/JWTs/).

As you develop against the DoorDash Drive API, you can use the [make-doordash-jwt CLI](https://github.com/infin8x/make-doordash-jwt) to generate a DoorDash JWT on Windows and Mac. When using Postman you use the [DoorDash Postman Collection](https://developer.doordash.com/en-US/docs/drive/tutorials/get_started_postman/) to create and send the JWT for each call.

You can learn more about the [DoorDash JWT Format](https://developer.doordash.com/en-US/docs/drive/reference/JWTs/) if your stack doesn’t support JWT creation, or if you’re looking to validate the output of your solution. Additionally, tools are available to you that illustrate the three parts of the DoorDash JWT in the [JSFiddle JWT Sample](https://bit.ly/doordashapi) and [WinForms Sample App](https://github.com/JoshAtDoorDash/DoorDashAPIWinFormsApp) (for Windows users). A popular utility developers use to validate a JWT is the [Auth0 JWT Debugger](https://jwt.io/) (check off the “secret base64 encoded” option when using the credentials provided by DoorDash. *Please keep in mind that providing secrets on public websites carries a risk, and you should never expose your production credential secrets.*

The [DoorDash SDK Sample Application](https://github.com/doordash-oss/doordash_sdk_example_application) provides a prototype full stack solution with React and Node Express server that uses the [Doordash SDK](https://www.npmjs.com/package/@doordash/sdk) to communicate with the DoorDash Drive API. For developers that use WooCommerce, the JWT creation is provided in the plugin, the [Get Started (WooCommerce Plugin)](https://developer.doordash.com/en-US/docs/drive/tutorials/get_started_woocommerce/) provides details on adding your credentials and configuring the plugin.

Please join our [Discord community](https://discord.com/channels/951208871828013066/951208872478113875) to share feedback and questions about the DoorDash JWT and getting started with DoorDash Drive!

**Etiquetas:**

* [jwt](/es-US/blog/tags/jwt)
* [drive-api](/es-US/blog/tags/drive-api)
* [dev-tools](/es-US/blog/tags/dev-tools)

## [Event Logs and other Drive updates](/es-US/blog/webhook-logs)

22 de noviembre de 2022 · 2 min de lectura

[![Brian Quach](https://avatars.githubusercontent.com/u/83295664?v=4)](https://github.com/brianquachdd)

[Brian Quach](https://github.com/brianquachdd)

Software Engineer

Webhooks are a critical part of a successful on-demand delivery integration. They enable DoorDash to inform your integration about delivery updates, like when the Dasher has arrived at the pickup location or where they are along their route in real time. This real-time information lets you keep both the sender and receiver of the delivery up-to-date with precisely what’s happening.

It can be challenging to develop and test the part of your integration that receives and handles webhooks. How can you confirm that DoorDash sent a webhook that you were expecting to receive? How can you confirm that your application parsed the webhook details correctly?

We’re introducing Event Logs to answer exactly those kinds of questions. Event Logs is a [new view in the Developer Portal](https://developer.doordash.com/portal/integration/drive/event_log) that shows a history of all the webhooks sent to your integration. Each log includes the endpoint to which the webhook was sent, the HTTP response code DoorDash received from that endpoint, and the full body of the webhook that DoorDash sent. You can search for all the webhooks for a particular delivery ID or inspect all of the webhooks that were sent in a specific date range.

![A screenshot of the Event Logs view in the Developer Portal](/img/blog/webhook-logs.png)

## Enroute webhooks & other Drive API updates[​](#enroute-webhooks--other-drive-api-updates "Enlace directo al encabezado")

Alongside the new Event Logs, we’ve also brought some new features to the Drive API:

* `enroute` webhooks can now be enabled for your integration, so you can receive frequent updates on the Dasher’s location
* The new `dasher_allowed_vehicles` field enables you to specify the transportation methods that a driverDasher can use to make the delivery: `"car"`, `"bicycle"` and/or `"walking"`
* You can use the `items` field to provide more detail about what’s in the delivery; this detail can be seen by Dashers as they’re making the deliveries and by the receiver of the delivery on the tracking page

Event Logs and all of these new features are ready to use today! Check out the [Event Logs view in the Developer Portal](https://developer.doordash.com/portal/integration/drive/event_log), and see the [Drive API docs](https://developer.doordash.com/en-US/api/drive/#tag/Delivery/operation/CreateDelivery) for more details on the new Drive API features.

**Etiquetas:**

* [new-feature](/es-US/blog/tags/new-feature)
* [drive-api](/es-US/blog/tags/drive-api)
* [dev-tools](/es-US/blog/tags/dev-tools)

## [Add same-day delivery to your business using DoorDash Drive API](/es-US/blog/same-day-delivery-using-doordash-drive-api)

26 de septiembre de 2022 · 4 min de lectura

[![Eva Zhang](/img/blog/eva-postman-profile.jpeg)](https://blog.postman.com/author/eva-zhang/)

[Eva Zhang](https://blog.postman.com/author/eva-zhang/)

Partner Marketing Manager at Postman

*This post originally appeared on the Postman blog. Check it out [here](https://blog.postman.com/add-same-day-delivery-to-your-business-doordash-drive-api/).*

With unpredictable shipping delays and wait times, today’s consumer is looking for everything from same-day solutions for last-minute needs. From dry clean pickup during business trips to dog food purchases for furry friends, the various use cases for same-day delivery are growing. In this blog post, we’ll look into Drive, the best-kept secret at DoorDash.

![An illustration showing a DoorDash driver on a scooter driving through a portal](/es-US/assets/images/doordash-postman-art-7a173122d6e48651cb6e98f1a0c20d61.jpeg)

Drive is a white label delivery API that allows businesses of all sizes to easily enable local fulfillment without the hassle of staffing their own delivery fleet. With a single API call, DoorDash Drive integration partners can request a delivery, which gets fulfilled by the DoorDash Dasher network.

## Making Developers Productive[​](#making-developers-productive "Enlace directo al encabezado")

Bobby Abraham manages Developer Strategy & Operations at DoorDash and is primarily focused on working with partner development teams to onboard developers onto Drive. In an effort to make the developer experience immersive and seamless, Bobby decided to leverage the power of the Postman API Network. He created a [DoorDash Public Workspace](https://www.postman.com/doordash/workspace/doordash/documentation/19023848-9a5768fb-9eb1-4a42-9f0a-78ff923dab4b) that would allow DoorDash to tap into Postman’s 20 million registered users in a central place. Here, Drive could get easy access to and be discovered by API consumers and API producers, providing merchants a cost-effective way to deliver products directly to customers on demand.

> I thought the Postman [Public API Network](https://www.postman.com/explore) would be a great way to spread awareness of DoorDash Drive and provide a delightful experience for our developers. The Postman team was great in helping us understand how to optimize our documentation to serve our developer partners better.
> *Bobby Abraham, Developer Strategy & Operations at DoorDash*

## After Joining Postman API Network[​](#after-joining-postman-api-network "Enlace directo al encabezado")

Since landing their Public Workspace on Postman API Network, the DoorDash team observed a significant decrease in development time for its partners. Developers can now make their first API call the same day they signup for Drive, and many partners have **finished development in less than a week**. This significantly decreases the time to first call (TTFC) partly due to the API-first design approach and in-depth documentation provided by the Postman API platform.

## How to Get Started[​](#how-to-get-started "Enlace directo al encabezado")

Let’s look at how you can get started using the [Drive API Postman Collection](https://www.postman.com/doordash/workspace/doordash/collection/19023848-9a5768fb-9eb1-4a42-9f0a-78ff923dab4b?ctx=documentation).

### Setting Up[​](#setting-up "Enlace directo al encabezado")

1. Go to [DoorDash Public Workspace](https://www.postman.com/doordash/workspace/doordash/overview?utm_source=Web&utm_medium=Referral&utm_campaign=https://www.postman.com/doordash) to select a collection that matches the API you’d like to use. Then, fork the collection into your Postman workspace by **clicking the button below**.

![A screenshot of the Postman fork collection dialog](/es-US/assets/images/postman-fork-dbbf0b7162f9479a3767b73393f96d18.png)

2. Once you have the fork of the collection, you’ll need to add a DoorDash Developer Access Key to your Environment. Go to [DoorDash Developer Portal](https://developer.doordash.com/en-US/) to create an account and an access key [on the portal](https://developer.doordash.com/en-US/docs/drive/tutorials/get_started_postman); make sure to leave the pop-up with the essential details open.
3. Navigate to the [left sidebar](https://www.postman.com/doordash/workspace/infin8x-dd-s-public-workspace/documentation/19023848-d95c7227-99bc-4999-b8b0-089016f838c1), click Environment, then click the + symbol. And name your environment “Drive sandbox.”
4. Paste in the “**developer\_id**,” “**key\_id**,” and “**signing\_secret**” values that you generated in step 2. Leave “**JWT**” blank.

![A screenshot of the Postman environment screen](/es-US/assets/images/postman-environment-ca69d2c5ee7c58fa2ee881c732e76917.png)

5. In the upper right, next to the little **Eyeball**, click the dropdown and select the “**Drive sandbox**” environment you just created.

![A screenshot of the Postman environment picker](/es-US/assets/images/postman-environment-picker-509463eb44bdb8ad02542452e1790b58.png)

### Create a delivery (without hailing real Dashers)[​](#create-a-delivery-without-hailing-real-dashers "Enlace directo al encabezado")

Now you can create a delivery by making a request to Drive API using Postman. On the left sidebar, click **Collections**, then expand the Door Dash Drive collection that you forked and click **Create a Delivery** request. Click the **Body** tab to see the request that will be sent. Then click **Send** to create the delivery in the **Drive sandbox** environment.

![A screenshot of the Postman request screen](/es-US/assets/images/postman-request-a376a4b5404bed7c069e2fb4b28c37ed.png)

### Get the latest status of your delivery[​](#get-the-latest-status-of-your-delivery "Enlace directo al encabezado")

In the left sidebar, click the **Get Delivery Status** request. Ensure that the URL of the request contains the external delivery ID “**D-12345**” you want to get, then click **Send**.

![A screenshot of the Postman request screen](/es-US/assets/images/postman-request-get-5f9ac7146d0332e8f9d314efd9d07be7.png)

### Wrapping up[​](#wrapping-up "Enlace directo al encabezado")

If you’ve made it this far, you are ready to start adding delivery capabilities to your app and help your business reach an entirely new market!

Join the [Postman API Network](https://www.postman.com/api-network/) and share your APIs to 20M+ users in the world’s largest public API hub or [book a call](https://calendly.com/d/d3s-8p8-kxw/introduction-to-the-postman-api-network?month=2022-08) with one of Postman API Network Evangelists to learn more.

**Etiquetas:**

* [partner](/es-US/blog/tags/partner)
* [drive-api](/es-US/blog/tags/drive-api)
* [postman](/es-US/blog/tags/postman)

## [Add alcohol to your next delivery](/es-US/blog/add-alcohol-to-your-next-delivery)

12 de septiembre de 2022 · 2 min de lectura

[![Ruirui Yang](https://avatars.githubusercontent.com/u/107019904?v=4)](https://github.com/ruiruiyang-dd)

[Ruirui Yang](https://github.com/ruiruiyang-dd)

Software Engineer

Beer, wine, and even to-go cocktails are becoming an incredibly common addition to delivery menus for both restaurants and other verticals like grocery and convenience. Adding alcoholic drinks is a great way to boost your average order size and grow your delivery business. DoorDash Developer and the Drive API make it easy to start your own alcohol delivery business or [add alcohol to your existing deliveries](/es-US/docs/drive/how_to/deliver_alcohol).

## Get started with alcohol delivery[​](#get-started-with-alcohol-delivery "Enlace directo al encabezado")

If you already have an active Drive API integration, [submit a support ticket](https://developer.doordash.com/portal/support) and ask for alcohol delivery to be enabled. One of our operators will reach out within a few business days with a brief legal addendum for you to sign. Once that’s signed, you can create an alcohol delivery just like you’d create a standard delivery. Just add/update a few fields in the body of your request to the [create delivery API](/es-US/api/drive/#tag/Delivery/operation/CreateDelivery):

```
"order_contains": {  
    "alcohol": true  
},  
"action_if_undeliverable": "return_to_pickup",  
"contactless_dropoff": false  

```

If you’re new to Drive, get started using our tutorials for [Postman](/es-US/docs/drive/tutorials/get_started_postman), [Node.js](/es-US/docs/drive/tutorials/get_started_sdk), or [direct API calls](/es-US/docs/drive/tutorials/get_started). Then, follow the [alcohol delivery how-to guide](/es-US/docs/drive/how_to/deliver_alcohol).

## Compliance is key[​](#compliance-is-key "Enlace directo al encabezado")

For all of the deliveries done through DoorDash’s network of Dashers, and especially for deliveries of regulated items like alcohol, we work hard to comply with local laws. Our product prompts Dashers to scan the customer’s ID and, in some jurisdictions, to collect the customer’s signature before delivery. Our Drive product only allows alcohol deliveries in jurisdictions where alcohol delivery is legally permissible, but it is your responsibility to ensure that you (or the merchants using your services) have the required retail alcohol licenses, and that you are only requesting delivery of the types of alcohol that are allowed under your license and local laws.

## Next steps[​](#next-steps "Enlace directo al encabezado")

Jump into alcohol delivery using our [alcohol delivery how-to guide](/es-US/docs/drive/how_to/deliver_alcohol). We can’t wait to see the businesses you build and grow using Drive and alcohol deliveries.

**Etiquetas:**

* [new-feature](/es-US/blog/tags/new-feature)
* [drive-api](/es-US/blog/tags/drive-api)

## [Introducing the Business & Store APIs](/es-US/blog/business-and-store-apis)

11 de agosto de 2022 · 2 min de lectura

[![Kavya Vishwanath](https://avatars.githubusercontent.com/u/99763950?v=4)](https://github.com/KavyaVishwanath)

[Kavya Vishwanath](https://github.com/KavyaVishwanath)

Software Engineer

Goods are commonly delivered by a *business*–a merchant that owns a collection of stores–and from a *store*: a physical location that prepares the goods for delivery. Accordingly, DoorDash maintains a data model of businesses and stores. This model helps us make faster and more accurate deliveries by ensuring that we have the right store location before a delivery is requested and allowing us to store additional information about how a Dasher can correctly locate a store. Now, in both the Drive and Drive (classic) APIs, you can create businesses and stores and then create deliveries for those stores.

## Using businesses & stores[​](#using-businesses--stores "Enlace directo al encabezado")

Using businesses and stores in your Drive API integration is straightforward: just create a business and create a store(s) underneath it using calls to the [business & store APIs](/es-US/docs/drive/how_to/use_businesses_and_stores_api). Then, when creating a delivery or requesting a delivery quote, provide the `pickup_external_business_id` and `pickup_external_store_id` that you used when creating the business and store.

> POST `/drive/v2/deliveries`

```
{  
   "external_delivery_id": "D-1763",  
   // other fields  
   
   "pickup_external_business_id": "b-234-dzs",  
   "pickup_external_store_id": "s-475-fnr",  
}  

```

When you create a delivery that provides business and store IDs, the store's address and contact details are used, so you don't have to provide them in every delivery request. Additionally, by creating stores in advance, you can verify that DoorDash's address resolution system saved the correct address for your store, which helps Dashers get to the right pickup location every time. Creating businesses and stores for your deliveries also lays the groundwork for getting access to future delivery capabilities that require additional, business-level configuration, like delivery for alcohol and prescriptions.

When you're ready to start using businesses and stores:

* Jump right in with the [Drive businesses and stores how-to guide](/es-US/docs/drive/how_to/use_businesses_and_stores_api)
* Learn more about the concepts in the [businesses and stores reference guide](/es-US/docs/drive/reference/businesses_and_stores)

## Drive (classic) user?[​](#drive-classic-user "Enlace directo al encabezado")

For Drive (classic) users who've previously managed stores using external forms or [auto-onboarding](/es-US/docs/drive_classic/how_to/use_businesses_and_stores_auto_onboard), we're making it easier to manage the businesses and stores that you need in order to make deliveries. Your account manager or point of contact at DoorDash will be in touch with more details soon, but if you want to get a head start, use the upgrade guide that's right for your scenario:

* [Upgrade from Formstack/Nintex to the Business & Store APIs](/es-US/docs/drive_classic/how_to/upgrade_from_formstack)
* [Upgrade from auto-onboarding to the Business & Store APIs](/es-US/docs/drive_classic/how_to/upgrade_from_auto_onboarding)

**Etiquetas:**

* [new-feature](/es-US/blog/tags/new-feature)
* [drive-api](/es-US/blog/tags/drive-api)
* [drive-classic-api](/es-US/blog/tags/drive-classic-api)

## [Collaborate with your team: announcing Organizations](/es-US/blog/collaborate-with-team-organizations)

11 de julio de 2022 · 2 min de lectura

[![Jon Collette](https://avatars.githubusercontent.com/u/89093785?v=4)](https://github.com/collettej)

[Jon Collette](https://github.com/collettej)

Software Engineer

Software development is more fun with teammates! Since launching DoorDash Developer, many of our early adopters have told us that they want to be able to share important information about their integration with DoorDash–things like simulated deliveries and access keys–with members of their team. I'm excited to announce that you can now do just that, with Organizations.

## Organizations contain your members[​](#organizations-contain-your-members "Enlace directo al encabezado")

You can see and add members on the [Organization page in the Developer Portal](https://developer.doordash.com/portal/organization). At launch, you can add up to 49 other people to collaborate with you. All you need to add a new member is their email address.

![A screenshot of the organization members page in the Developer Portal](/img/blog/organization-members-screen.png)

## Organizations contain your billing and business details[​](#organizations-contain-your-billing-and-business-details "Enlace directo al encabezado")

Previously, DoorDash Developer combined your personal details with the details about your business: your business name, how you pay for deliveries, etc. Now, Organization Settings holds all these details, so everyone on your team can manage them.

## Get started[​](#get-started "Enlace directo al encabezado")

If you're already using DoorDash Developer, head to the [Organization page in the Developer Portal](https://developer.doordash.com/portal/organization) to add your first member!

If you're new to DoorDash Developer, [sign up in just a few steps](https://developer.doordash.com/signup).

**Etiquetas:**

* [new-feature](/es-US/blog/tags/new-feature)
* [developer-portal](/es-US/blog/tags/developer-portal)

## [May Drive updates: return-to-pickup, OAuth webhooks, and invoiced billing](/es-US/blog/return-to-pickup-oauth-invoicing)

20 de mayo de 2022 · 2 min de lectura

[![Alex Mullans](https://avatars.githubusercontent.com/u/99431555?v=4)](https://github.com/infin8x-dd)

[Alex Mullans](https://github.com/infin8x-dd)

Product Manager

Over the past few months, we've been hard at work unlocking new scenarios and adding new features to the DoorDash Drive API. With return-to-pickup, you can now deliver non-perishable and high-value goods that need to be returned to you if the customer is unavailable. If you use OAuth to protect your internet-facing endpoints, Drive and Drive (classic) can now send webhooks authenticated with OAuth. And, with invoiced billing support, you can choose to receive a monthly invoice for your deliveries, rather than paying upfront with a credit card.

## Return to pickup[​](#return-to-pickup "Enlace directo al encabezado")

In the event a customer is unavailable to receive a food delivery, DoorDash first tries all available methods to reach the customer but, if we're not successful, the Dasher will dispose of the delivery. For higher-value goods and non-perishable goods, it's often preferable to have the delivery returned to its pickup location if the customer is unavailable. Now, you can, by creating "return-to-pickup" delivery using the Drive API!

Read the [return to pickup how-to guide](/es-US/docs/drive/how_to/return_to_pickup) for more details, or just use the `action_if_undeliverable=return_to_pickup` field when you call the [delivery creation API](/es-US/api/drive#operation/CreateDelivery)

## OAuth webhooks[​](#oauth-webhooks "Enlace directo al encabezado")

Previously, DoorDash could only send webhooks to unauthenticated endpoints and endpoints protected by HTTP Basic authentication. We heard from many of you that your IT and Security teams preferred to protect all internet-facing endpoints with OAuth instead. So, we've added OAuth as a new option for webhook authentication. Learn more in the [webhooks how-to guide](/es-US/docs/drive/how_to/webhooks).

![A screenshot of the modal for creating a new webhook endpoint](/img/docs/drive/how_to/webhook-add.png)

## Invoiced billing[​](#invoiced-billing "Enlace directo al encabezado")

If you're a platform business that serves a variety of merchants, each with their own customers, you might like the ability to pass on charges, like DoorDash's delivery fees, to those merchants. Previously, the Drive API charged you (the developer) for each delivery as you created them. Now, you can request to receive a monthly invoice that can be paid by credit card or ACH transfer. Submit a [support request](/es-US/docs/drive/support) to get started.

**Etiquetas:**

* [new-feature](/es-US/blog/tags/new-feature)
* [drive-api](/es-US/blog/tags/drive-api)

## [Use Drive APIs via the new DoorDash Node.js SDK](/es-US/blog/nodejs-sdk)

24 de febrero de 2022 · 3 min de lectura

[![Alex Mullans](https://avatars.githubusercontent.com/u/99431555?v=4)](https://github.com/infin8x-dd)

[Alex Mullans](https://github.com/infin8x-dd)

Product Manager

The Drive APIs bring the power of DoorDash’s same-day local delivery to your application. You can build an app, using any programming language and runtime you want, to deliver goods from you to your customers–or from your customers back to you! Your application calls the APIs, and Dashers deliver your goods. Now, to make it even faster to add delivery to your application, we’re introducing SDKs for common languages, starting with JavaScript.

The new [DoorDash Node.js SDK](https://www.npmjs.com/package/@doordash/sdk) takes care of the boilerplate work of using our API, like [setting up the authentication token](/es-US/docs/drive/how_to/JWTs) and making HTTP requests. SDKs generally make it faster to use an API because they take care of this boilerplate work so you can get right to the task you’re trying to achieve–say, creating a delivery and requesting a Dasher. They can also help you write code more quickly because your code editor can provide inline documentation and autocomplete suggestions.

In the screenshot below, the code on the left creates a delivery using the Create Delivery API directly; the code on the right, using the DoorDash Node.js SDK.

![A screenshot comparing JavaScript code calling the APIs directly vs. using the DoorDash Node.js SDK](/es-US/assets/images/nodejs-sdk-comparison-6064c7863668ee1dad1e7ec68bf96962.png)

## Install the SDK to get started[​](#install-the-sdk-to-get-started "Enlace directo al encabezado")

Getting started with our Node.js SDK is easy: just run `npm i --save @doordash/sdk` to install it from npm and then reference it in your application.

The [SDK's readme](https://www.npmjs.com/package/@doordash/sdk) contains snippets showing you how to use the SDK in both JavaScript and TypeScript. If you don’t have the access key details needed to create the client, you can create them in the [Developer Portal](https://developer.doordash.com/portal/integration/drive/credentials).

*Note: You must be using the new Drive APIs, not the Drive (Classic) APIs, to use the DoorDash Node.js SDK.*

## Examples of using the SDK[​](#examples-of-using-the-sdk "Enlace directo al encabezado")

Here’s a simple example of creating a delivery in JavaScript:

```
import { DoorDashClient } from '@doordash/sdk'  
import { v4 as uuidv4 } from 'uuid'  
  
const client = new DoorDashClient({  
  developer_id: '{your developer_id}',  
  key_id: '{your key_id}',  
  signing_secret: '{your signing_secret}',  
})  
  
const response = await client.createDelivery({  
  external_delivery_id: uuidv4(),  
  pickup_address: '1000 4th Ave, Seattle, WA, 98104',  
  pickup_phone_number: '+1(650)5555555',  
  dropoff_address: '1201 3rd Ave, Seattle, WA, 98101',  
  dropoff_phone_number: '+1(650)5555555',  
})  

```

And here’s one in TypeScript:

```
import {  
  DeliveryResponse,  
  DoorDashAuthorizationError,  
  DoorDashClient,  
  DoorDashResponse,  
} from '@doordash/sdk'  
  
import { v4 as uuidv4 } from 'uuid'  
  
const client = new DoorDashClient({  
  developer_id: '{your developer_id}',  
  key_id: '{your key_id}',  
  signing_secret: '{your signing_secret}',  
})  
  
client  
  .createDelivery({  
    external_delivery_id: uuidv4(),  
    pickup_address: '1000 4th Ave, Seattle, WA, 98104',  
    pickup_phone_number: '+1(650)5555555',  
    dropoff_address: '1201 3rd Ave, Seattle, WA, 98101',  
    dropoff_phone_number: '+1(650)5555555',  
  })  
  .then((response: DoorDashResponse<DeliveryResponse>) => {  
    // do something  
  })  
  .catch((err: any) => {  
    // handle error  
  })  

```

As the DoorDash Developer community grows, we expect to create more SDKs in additional languages. Bookmark our blog to stay updated.

**Etiquetas:**

* [new-feature](/es-US/blog/tags/new-feature)
* [drive-api](/es-US/blog/tags/drive-api)
* [sdk](/es-US/blog/tags/sdk)
* [javascript](/es-US/blog/tags/javascript)

[Entradas más antiguas](/es-US/blog/page/2)