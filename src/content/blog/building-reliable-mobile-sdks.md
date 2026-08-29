---
title: "Architecting iOS & Android SDKs for Third-Party Consumption"
description: "Lessons learned from building high-performance native SDKs. From API surface design to binary footprint optimization."
pubDate: 2023-10-05
---

Building a mobile application is challenging, but building a mobile SDK meant to be consumed by other developers is an entirely different beast. When you ship an SDK (like a real-time video processing module), you are injecting your code into an unknown environment.

## API Surface Design

The most critical aspect of an SDK is its public API. Once released, it is extremely difficult to introduce breaking changes without angering your integrators. 
1. **Keep it minimal:** Expose only what is absolutely necessary. Hide implementation details behind strict access modifiers (`internal` in Swift, `internal` in Kotlin).
2. **Configuration objects:** Instead of passing ten arguments into an initialization function, use a strongly-typed `Configuration` object. It allows you to add non-breaking optional configurations later.

## Binary Footprint & Dependencies

App developers guard their binary size fiercely. If your SDK adds 50MB to their app, they will drop it.
- **Avoid heavy third-party dependencies:** Do not include a massive library like Alamofire or Retrofit just to make a few network calls. Use `URLSession` on iOS and `HttpURLConnection` (or lightweight alternatives) on Android.
- **Dynamic vs Static Linking:** Understand how your XCFrameworks or AARs are linked and provide clear integration guides to avoid symbol collisions.

Building SDKs forces you to become a better citizen of the mobile ecosystem.
