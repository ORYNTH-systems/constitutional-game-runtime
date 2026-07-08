\# 41 — RG23 Consumption-Driven Hunger



\## Purpose



This document defines the RG23-C update to CP-003 Population Hunger Pressure.



Hunger Pressure should respond to the constitutional food consumption ratio rather than only checking whether food is zero.



\## Current Behavior



CP-003 currently increases hunger pressure only when food reaches zero.



\## RG23 Objective



Hunger should become proportional to resource deprivation.



\## Inputs



CP-003 evaluates:



\- Population

\- Food supply

\- Latest food consumption ratio

\- Current hunger pressure



\## Outputs



CP-003 updates:



\- Hunger Pressure



\## Deterministic Rules



\- Consumption Ratio = 1.0 → reduce hunger pressure

\- Consumption Ratio ≥ 0.75 → preserve hunger pressure

\- Consumption Ratio ≥ 0.50 → increase hunger pressure by 1

\- Consumption Ratio ≥ 0.25 → increase hunger pressure by 2

\- Consumption Ratio < 0.25 → increase hunger pressure by 3



\## Summary



This transforms hunger from a binary consequence into a proportional constitutional state derived from food allocation.

