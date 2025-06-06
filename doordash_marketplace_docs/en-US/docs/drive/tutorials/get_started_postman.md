On this page

# Get started (Postman)

Drive API Production Access is Limited

<Warning>
Production access to the Drive API is currently restricted, and we cannot provide a timeline for certification following development. If you have not completed development and submitted a production access request, we recommend pausing development. Contact us [here](https://docs.google.com/forms/d/e/1FAIpQLSfggU_NjGWCdi9vyWUicrnzJmtu9vC4zgbfSC3ROwSvW4eV2g/viewform) to record your interest.
</Warning>

This tutorial will introduce you to the Drive API, DoorDash's API for requesting deliveries fulfilled by our fleet of Dashers, using the [Postman API development tool](https://www.postman.com). It assumes you're familiar with the basics of Postman. If you'd like to learn the Drive APIs by writing code, you should use the [Get started (Node.js SDK) tutorial](/en-US/docs/drive/tutorials/get_started_sdk) or [Get started (API) tutorial](/en-US/docs/drive/tutorials/get_started) instead.

Want to jump right in?

If you're already familiar with how to use Postman, you can jump right in:

## Table of contents[​](#table-of-contents "Direct link to heading")

1. [Sign into the Developer Portal](#sign-into-the-developer-portal)
2. [Create an access key](#create-an-access-key)
3. [Set up Postman](#set-up-postman)
4. [Create a delivery](#create-a-delivery)
5. [Use the Delivery Simulator](#use-the-delivery-simulator)
6. [Get the status of your delivery](#get-the-status-of-your-delivery)
7. [Finish up](#finish-up)

## 1. Sign into the Developer Portal[​](#1-sign-into-the-developer-portal "Direct link to heading")

Go to the [Developer Portal](/en-US/portal) using the link in the top right corner of this page. If you already have a DoorDash account, enter your email and password and sign in; if not, or if you want to use a different account for development, click Sign Up and follow the process to create an account.

![A screenshot of the Developer Portal sign-in screen](/en-US/assets/images/sign-in-sign-up-a14648f233a279c0354fbaa1dda0b549.png)

## 2. Create an access key[​](#2-create-an-access-key "Direct link to heading")

In the left navigation, click Credentials.

![A screenshot of the Developer Portal left navigation menu with the Credentials navigation item highlighted](/en-US/assets/images/credentials-1e988ace8eaadb88fa371bef019e0cef.png)

On the Credentials page, click the plus (`+`) icon in the center of the page to create a new access key. You'll use this access key to create a JSON Web Token (JWT) that you can use to make requests to the Drive API.

![A screenshot of the Credentials page with the button for creating a new access key highlighted](/en-US/assets/images/create-access-key-101a83f323917717db3d49992fceb02b.png)

Name your key `test-app` and click Create Access Key.

![A screenshot of the modal for creating an access key](/en-US/assets/images/create-access-key-detail-0041520a3a79e66b9a54213124967a3f.png)

Click Copy to copy the access key to your clipboard and then paste it somewhere where you can access it later in the tutorial.

![A screenshot of an access key](/en-US/assets/images/access-key-dfdd7a9997f69864d42c51ef8d001d25.png)

## 3. Set up Postman[​](#3-set-up-postman "Direct link to heading")

First, click the button below to [fork the DoorDash Drive Postman collection](https://app.getpostman.com/run-collection/19023848-9a5768fb-9eb1-4a42-9f0a-78ff923dab4b?action=collection%2Ffork&collection-url=entityId%3D19023848-9a5768fb-9eb1-4a42-9f0a-78ff923dab4b%26entityType%3Dcollection%26workspaceId%3D6ae497bc-a028-444b-8dba-766b5ffb682e):

You may need to sign up for Postman if you don't have an account.

### 3.1. Set up a Postman environment[​](#31-set-up-a-postman-environment "Direct link to heading")

Once you have the fork of the collection, set up an Environment to store your access key.

1. In the left sidebar, click Environments, then click the ➕ symbol.
2. Name your environment "Drive sandbox".
3. Add two default variables called "developer\_id" and "key\_id", and two secret variables called "signing\_secret" and "JWT" (note the capitalization) and paste in each of the values from your Access Key. Leave "JWT" blank.

![A screenshot of the Postman environment screen](/en-US/assets/images/postman-environment-ca69d2c5ee7c58fa2ee881c732e76917.png)

In the upper right, next to the eyeball, click the dropdown and select the "Drive sandbox" environment you just created.

![A screenshot of the Postman environment picker](/en-US/assets/images/postman-environment-picker-509463eb44bdb8ad02542452e1790b58.png)

## 4. Create a delivery[​](#4-create-a-delivery "Direct link to heading")

Now you can create a delivery by making a request to the Drive API using Postman.

tip

When you created your access key, you created it for the Sandbox environment (until you [request production access](/en-US/docs/drive/how_to/get_production_access), you can only create access keys for the Sandbox environment). Because you're using an access key for the Sandbox environment, you can experiment with the API as much as you like without incurring real costs or hailing real Dashers.

In the left sidebar, click Collections, then expand the Drive collection that you forked and click the Create a Delivery request. Click the Body tab to see the request that will be sent.

![A screenshot of the Postman request screen](/en-US/assets/images/postman-request-a376a4b5404bed7c069e2fb4b28c37ed.png)

Click Send to create the delivery.

## 5. Use the Delivery Simulator[​](#5-use-the-delivery-simulator "Direct link to heading")

You can use the Delivery Simulator to advance your delivery through the stages of the delivery process, from creation to Dasher assignment to pickup to delivery.

In the Developer Portal left navigation, click Simulator.

![A screenshot of the Developer Portal left navigation menu with the Simulator navigation item highlighted](/en-US/assets/images/simulator-8d3aa4a138f97e72a940c3bdf93527e8.png)

Find the delivery you created by looking for the identifier `#D-12345`. Click Advance to Next Step to move your delivery to the Delivery Confirmed stage.

![A screenshot of the Delivery Simulator with a delivery in the Delivery Created stage](/en-US/assets/images/delivery-simulator-47665a33b8fa6b7c826b3d1a9a20bcc4.png)

## 6. Get the status of your delivery[​](#6-get-the-status-of-your-delivery "Direct link to heading")

You can always get the latest status of a delivery by making a request to the Drive API.

In the left sidebar, click the Get Delivery Status request. Ensure that the URL of the request contains the delivery ID you want to get then click Send.

![A screenshot of the Postman request screen](/en-US/assets/images/postman-request-get-5f9ac7146d0332e8f9d314efd9d07be7.png)

## Finish up[​](#finish-up "Direct link to heading")

If you'd like, continue to use the Delivery Simulator to advance your delivery through the stages of the delivery process and then re-run the Get Delivery Status request to see how the delivery details change.

## Next steps[​](#next-steps "Direct link to heading")

Now that you're familiar with the Drive API, you're ready to start adding delivery capabilities to your app! If you'd like to follow a tutorial that will teach you how to use the Drive APIs in code, use [Get started (Node.js SDK) tutorial](/en-US/docs/drive/tutorials/get_started_sdk) or [Get started (API) tutorial](/en-US/docs/drive/tutorials/get_started). Or, to learn more, use the "How-to guides" section in the navigation on the left side of this page and the [How to Build for Restaurants guide](https://developer.doordash.com/en-US/docs/drive/how_to/build_for_restaurants/#a-validation-checklist-prior-to-requesting-a-demo).

[Previous

Get started (Node.js SDK)](/en-US/docs/drive/tutorials/get_started_sdk)[Next

Get started (WooCommerce Plugin)](/en-US/docs/drive/tutorials/get_started_woocommerce)

* [Table of contents](#table-of-contents)
* [1. Sign into the Developer Portal](#1-sign-into-the-developer-portal)
* [2. Create an access key](#2-create-an-access-key)
* [3. Set up Postman](#3-set-up-postman)
  + [3.1. Set up a Postman environment](#31-set-up-a-postman-environment)
* [4. Create a delivery](#4-create-a-delivery)
* [5. Use the Delivery Simulator](#5-use-the-delivery-simulator)
* [6. Get the status of your delivery](#6-get-the-status-of-your-delivery)
* [Finish up](#finish-up)
* [Next steps](#next-steps)