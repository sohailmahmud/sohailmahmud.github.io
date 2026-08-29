---
title: "Mastering Payment SDKs: From PCI Compliance to Edge Cases"
description: "Integrating payment gateways into mobile apps requires more than just calling an API. A deep dive into robust payment architecture."
pubDate: 2022-09-12
---

Working on enterprise retail platforms like *VALT POS* and *ZatiqPOS* has given me extensive exposure to integrating modern Payment SDKs. While providers like Stripe, Square, and localized payment gateways have excellent documentation, real-world integration in a POS environment requires handling severe edge cases.

## The Golden Rule: Never Touch the PAN

To maintain PCI compliance and reduce your organization's security burden, the raw Primary Account Number (PAN) must never touch your application's memory or your backend servers. 
Always rely on the SDK's secure tokenization views. The SDK intercepts the card data directly, communicates with the payment processor, and returns a secure, single-use token to your app.

## Handling the Unknown State

The most dangerous scenario in mobile payments is the network dropping immediately after the user taps "Pay." Did the payment go through? 
1. **Idempotency Keys:** Every payment request from your mobile app must include a unique, client-generated UUID (Idempotency Key). If the app retries the same transaction, the processor knows to return the previous result rather than charging the user twice.
2. **Webhooks are the Source of Truth:** The mobile app's success callback is a UI convenience, not a guarantee. Your backend must listen to provider Webhooks and update the internal database to mark an order as truly "Paid."

Robust payment integration is about designing for failure at every step of the transaction lifecycle.
