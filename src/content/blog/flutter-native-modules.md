---
title: "When Flutter Isn't Enough: Bridging to Native Modules"
description: "Cross-platform frameworks are incredible, but true senior engineering means knowing when and how to drop down to native code."
pubDate: 2023-01-15
---

Flutter and Kotlin Multiplatform have revolutionized mobile development, allowing us to build features at unprecedented speeds. However, cross-platform tools are abstractions, and all abstractions eventually leak.

## The Limits of Cross-Platform

While Flutter handles UI rendering beautifully via Impeller/Skia, there are times when you need bare-metal access. For example, during the development of *YakiyaPOS*, we needed seamless, low-latency NFC reading. Relying purely on third-party plugins was not yielding the reliability required for a high-traffic point-of-sale system.

## Dropping Down to Native

The solution was to write our own native modules. 

Using **MethodChannels** in Flutter, we bridged our Dart code to custom Android (Kotlin) and iOS (Swift) implementations. 
- On Android, we utilized the low-level Android NFC API.
- On iOS, we hooked into CoreNFC.

By isolating the heavy hardware interactions in native code and only passing the serialized results back over the bridge, we achieved enterprise-grade reliability while still keeping 95% of our codebase in Dart. 

Understanding how to orchestrate these hybrid architectures is what separates a good mobile developer from a great one.
