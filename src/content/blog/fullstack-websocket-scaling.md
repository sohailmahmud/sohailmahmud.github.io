---
title: "Scaling WebSockets in a Fullstack Environment"
description: "Handling real-time state across millions of connections requires more than just opening a socket. How to scale real-time infrastructure."
pubDate: 2023-11-20
---

In modern applications like the *Hurraayy Marketplace* or the *VALT POS* ecosystem, REST APIs are often not fast enough. Users expect real-time pricing, instant booking confirmations, and live chat. We achieve this through WebSockets.

## The Scaling Challenge

Opening a WebSocket connection is easy. Keeping 100,000 WebSocket connections open across a distributed backend is hard.

Unlike stateless HTTP requests which can be easily round-robined by a standard load balancer, WebSockets are stateful. If Client A is connected to Server Node 1, and Client B sends a chat message that hits Server Node 2, how does Node 1 know to push the message to Client A?

## The Pub/Sub Backplane

The architectural solution is a Publish/Subscribe (Pub/Sub) backplane.
Whenever a node receives an event (e.g., "Price Dropped"), it does not just broadcast to its own connected clients. It publishes the event to a central message broker—typically Redis Pub/Sub or Apache Kafka. 

Every backend node subscribes to this broker. When the broker emits the "Price Dropped" event, all nodes receive it simultaneously and push the update down to their respective connected WebSockets. 

Mastering this pattern was critical to reducing API polling by 40% on our mobile clients while maintaining sub-200ms latency across our cloud infrastructure.
