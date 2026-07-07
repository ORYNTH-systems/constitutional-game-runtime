# Architecture

The Constitutional Game Runtime treats a game world as a governed execution environment.

A game action is not executable merely because it was requested. It must remain admissible at the moment of execution under the current world state.

## Architectural Thesis

Traditional game engines execute scripted behavior.

The Constitutional Game Runtime evaluates execution eligibility through current-state governance.

## Execution Flow

Intent
-> Current World State
-> State Reconstruction
-> Constraint Evaluation
-> Governance Decision
-> Execution Eligibility
-> Execution or Denial
-> Replay Evidence

## Core Components

- World State: current condition of the simulated environment.
- Entity Identity: players, NPCs, agents, factions, objects, or governed actors.
- Action Requests: intended operations submitted for execution.
- Simulation Clock: temporal structure for ticks, events, and evolving processes.
- Resource Constraints: bounded conditions that may permit or deny execution.
- Governance Rules: admissibility logic applied at runtime.
- Execution Results: approved or denied outcomes.
- Replay Evidence: recorded execution history for verification.

## Runtime Layers

- engine/: core runtime primitives.
- governance/: admissibility decisions.
- simulation/: world evolution.
- validation/: proof and benchmark surface.
- examples/: demonstration flows.
- documentation/: architecture documentation.

## Execution Principle

An action is not valid merely because it was requested.

It must remain admissible at execution time under the current world state.

## Novelty

The runtime does not only simulate objects inside a world.

It simulates whether activity inside that world remains constitutionally admissible as the world changes.

This makes it suitable for persistent worlds, autonomous agents, strategic simulations, economic systems, faction systems, sports simulations, and open-world environments where state changes continuously.
