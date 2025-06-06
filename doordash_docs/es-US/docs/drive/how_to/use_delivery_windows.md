En esta página

# Schedule deliveries using windows

By default, deliveries you create are picked up and delivered as soon as possible (ASAP). If you want to enable your customers to order ahead for a later delivery time, you can use delivery windows.

tip

Delivery windows are generally best for when you're delivering non-perishable goods that don't need to be picked up or delivered at a specific time. If you're delivering perishable goods like food and drinks that you want to schedule for a specific time in the future, use [scheduled deliveries](/es-US/docs/drive/how_to/schedule_deliveries).

## 1. Prerequisites[​](#1-prerequisites "Enlace directo al encabezado")

If you're new to Drive and haven't yet created your first delivery, you should start with one of our tutorials. The tutorials will walk you through getting the credentials you need to call the APIs and making some basic API calls.

* [Get started by making API calls](/es-US/docs/drive/tutorials/get_started)
* If you're writing an app in Node.js (using JavaScript or TypeScript), [get started using our Node.js SDK](/es-US/docs/drive/tutorials/get_started_sdk)
* If you'd like to try our APIs interactively, [get started using our Postman collection](/es-US/docs/drive/tutorials/get_started_postman)

## 2. Set up delivery quotes[​](#2-set-up-delivery-quotes "Enlace directo al encabezado")

For delivery windows, we recommend using delivery quotes; if you're not already using quotes, you should follow the [quotes how-to guide](/es-US/docs/drive/how_to/quote_deliveries) before this one.

When you create a quote for a windowed delivery, DoorDash's fulfillment systems will evaluate if we can meet the requested windows and provide our estimated pickup and dropoff times in the response to your quote request. You can then validate whether these estimated times meet your requirements, either using logic built into your app or by showing the estimated times to the end customer.

## 3. Schedule a delivery[​](#3-schedule-a-delivery "Enlace directo al encabezado")

TO create a windowed delivery, include **both** the `pickup_window` and `dropoff_window` fields. You may also want to enable SMS notifications for the dropoff contact.

* `pickup_window`: A Dasher will show up within this window to collect your order
* `dropoff_window`: The Dasher will deliver the order within this window
* `dropoff_contact_send_notifications`: When this is set to `true`, DoorDash will send SMS notifications to the `dropoff_phone_number` with updates on the status of the order and a link to the tracking page

The windows are validated according to the following rules:

* Each time must be formatted in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) using the "complete date plus hours, minutes, and seconds" format that looks like this: "2023-05-02T17:00:00Z"
* Each window must be at least 60 minutes long
* Each window's `start_time` must be before its `end_time`
* The dropoff window's `start_time` must be the same or later than the pickup window's `end_time` (`dropoff_window.start_time >= pickup_window.end_time`)

```
{  
    ... // other fields  
    "pickup_window": {  
        "start_time": "2023-05-02T17:00:00Z",  
        "end_time": "2023-05-02T18:00:00Z"  
    },  
    "dropoff_window": {  
        "start_time": "2023-05-02T18:00:00Z",  
        "end_time": "2023-05-02T20:00:00Z"  
    },  
}  

```

The response to your quote request will include a few estimated time fields that you can reference to see when DoorDash can fulfill the delivery.

* `estimated_pickup_time`: When we expect the Dasher will arrive at the pickup location
* `estimated_dropoff_time`: When we expect the Dasher will arrive the dropoff location

## 4. Set up webhooks[​](#4-set-up-webhooks "Enlace directo al encabezado")

When using delivery windows, it's important to have [set up webhooks](/es-US/docs/drive/how_to/webhooks) so that you receive real-time notifications when a Dasher is assigned and on the way to pick up your delivery.

## Next steps[​](#next-steps "Enlace directo al encabezado")

* [Customize the SMS messages](/es-US/docs/drive/how_to/configure_sms) that are sent to the `dropoff_phone_number`

[Anterior

Schedule deliveries for later](/es-US/docs/drive/how_to/schedule_deliveries)[Siguiente

Settings & inheritance](/es-US/docs/drive/explain/settings_inheritance)

* [1. Prerequisites](#1-prerequisites)
* [2. Set up delivery quotes](#2-set-up-delivery-quotes)
* [3. Schedule a delivery](#3-schedule-a-delivery)
* [4. Set up webhooks](#4-set-up-webhooks)
* [Next steps](#next-steps)