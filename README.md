# 🏎️ Polycracker ECU

[![PyPI version](https://img.shields.io/pypi/v/polycracker-ecu?style=for-the-badge&color=FF4500&logo=pypi&logoColor=white)](https://pypi.org/project/polycracker-ecu/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20x64-0078D6?style=for-the-badge&logo=windows&logoColor=white)](#quick-start-windows-x64)
[![Execution](https://img.shields.io/badge/Execution-100%25%20Local-2EA043?style=for-the-badge)](#universal-local-hookup)
[![Interface](https://img.shields.io/badge/Interface-Proxy%20%2B%20MCP-6E40C9?style=for-the-badge)](#universal-local-hookup)
[![License](https://img.shields.io/badge/CLI-MIT%20%7C%20Core-Proprietary-555555?style=for-the-badge)](#license)

**Stop letting blind, one-size-fits-all pruners chop up your context and bill you for the wreckage.**

Most context harnesses hand you a bloated middleware suite with a static trimmer—or worse, an opaque auto-router that uses a second AI model to *guess* which lines of your code and JSON don't matter. When lossy trimming drops a critical detail, their fallback is hoping the LLM notices and pays for a retrieval tool call. Instead, the model hallucinates, fails checks, and falls into **retry loops and extra agent turns**. Every extra turn re-sends conversation history, busts your KV-cache, and generates expensive output tokens—quietly **ballooning your monthly bill** even while a dashboard brags about 90% token savings.

**Polycracker ECU is a precision instrument that puts you in the driver's seat.** Drop it in front of *anything* via the **universal local proxy** or plug it straight into your coding agent over **stdio MCP**. No platform sprawl, no cloud relays, no extra tokens burned—just a surgical, zero-bloat local binary delivering strictly deterministic Python AST-to-IR compression and real **knock detection** *(measuring context drift upfront so you catch when aggressive compression is about to strip critical meaning and make the LLM misfire)*—running **100% on your machine**.

We don't sell dashboard vanity metrics or ask you to take 95% claims on faith. Run it against your own repo, your own prompts, and your own provider invoice. Every byte in and every byte out is verifiable.

It ships ready to rip out of the box with a balanced **30-day Stage 2 Track Spec base tune**. When you want full manual control instead of auto-magic guessing, open the **[Tuning House](https://portal.polycracker.dev/dashboard/tuning-house)**, dial in **8 macro sliders and 36 micro-dials** (right down to raw JSON trimming), and flash an offline **Ed25519-signed `tune.jwt`** straight to your machine.

---

## 🔌 Universal Local Hookup

Polycracker ECU isn't locked to one IDE or one agent framework. Route any API client, script, or agent through the **local proxy**, or connect directly over **stdio MCP**—your code never leaves your machine.

```text
┌──────────────────────────────────────────────────────────┐
│   ANY IDE / Coding Agent / Script / API Client           │
└───────────────────┬──────────────────────┬───────────────┘
                    │ Universal Local Proxy│ stdio MCP
                    ▼                      ▼
┌──────────────────────────────────────────────────────────┐
│  Polycracker-ECU.exe  (100% Local on Your Machine)       │
│  • Deterministic AST-to-IR Compression                   │
│  • Offline Ed25519-Signed tune.jwt Calibration Map       │
│  • Knock Detection (Upfront Context-Drift Telemetry)     │
└──────────────────────────────┬───────────────────────────┘
                               │ Compressed IR (Zero Extra LLM Burn)
                               ▼
                   Your LLM Provider / Local Model
```

---

## ⚡ Why Polycracker ECU?

| Dimension | Typical Context Harnesses & Proxies | Polycracker ECU |
| :--- | :--- | :--- |
| **Architecture & Footprint** | Sprawling middleware suites (content routers, shared memory layers, heavy proxies) | **Precision instrument**—a surgical, zero-bloat local binary (`Polycracker-ECU.exe`) that stays out of your way |
| **Compression Engine** | Opaque auto-magic routers mixing heuristics with secondary ML models to guess what to drop | **Deterministic Python AST-to-IR compression**—zero secondary ML guessing, zero extra LLM token burn |
| **Handling Broken Context** | Cuts blind and relies on a retrieval tool—*hoping* the LLM notices missing context and pays for a recovery round-trip | **Prevent the misfire upfront**—real **knock detection** *(context-drift telemetry that flags breakage risk before the model hallucinates or loops)* |
| **Real Invoice Impact** | Loud headline claims ("60–95% fewer tokens") that often backfire via retry loops, extra turns, and higher bills | **Anti-hype, invoice-first**—verify exact token deltas and real provider billing on your own codebase |
| **KV-Cache Protection** | Passive—warns about volatile prefixes without addressing prefix churn | **Prefix-aware**—treats per-turn tax and KV-cache prefix stability as core invoice drivers |
| **Execution & Privacy** | Heavy middleware, cloud relays, or remote APIs | **100% local on your machine** via Universal Proxy + stdio MCP—zero cloud code upload |
| **Calibration & Control** | Static, one-size-fits-all defaults or black-box auto-routing | **Explicit control**—you are the tuner with 8 macro sliders + 36 micro-dials exported as offline `tune.jwt` maps |

---

## 🛠️ Why One-Size-Fits-All Breaks

Nobody puts a locked, factory-stock fuel map on a built engine—so why let an opaque auto-router apply the same static trimmer across completely different workloads?

* **Fragile Legacy Refactors:** Aggressive blind pruning strips comments, type hints, or structural cues, triggering context knock and expensive **retry loops** that erase any input-token savings. Flash a conservative **Street Tune** to keep maximum structural fidelity.
* **Noisy Agent & Tool Dumps:** Agents dumping massive raw JSON payloads and repetitive logs burn through context windows in minutes. Dial up **raw JSON trimming** and aggressive AST stripping to crush per-turn bloat.
* **High-Frequency Multi-Turn Loops:** Unstable prompt prefixes destroy KV-cache hit rates and quietly inflate your bill. Tune your map to protect prefix stability while compressing the payload that actually changes.

---

## 📊 The Dyno Sheet (Verify It Yourself)

Don't trust dashboard vanity metrics—run your own files through `Polycracker-ECU.exe` and check the numbers against your actual provider invoice.

> **Tip:** Drop your own real before/after readout right here once you run your benchmark, or test the included **Stage 2 Track Spec** trial map directly on your active repo.

```text
# Example Verification Readout (Replace with your live capture)
Input Payload:    [Your Python / JSON workload]
Raw Tokens:       100% baseline
Polycracker IR:   Deterministic compressed output (0 secondary LLM tokens spent)
Knock Status:     Monitored upfront via context-drift telemetry (zero blind cuts)
```

---

## 🚀 Quick Start (Windows x64)

1. **Install the open-source CLI wrapper:**

```powershell
pip install polycracker-ecu
```

2. **Download, SHA-256 verify, and extract `Polycracker-ECU.exe` + provision your 30-day Stage 2 Track Spec trial tune:**

```powershell
polycracker-ecu install
```

3. **Start the local ECU (System Tray / Universal Proxy / stdio MCP):**

```powershell
polycracker-ecu run
```

*(Testing from a local clone? Run `pip install -e .` in step 1.)*

---

## 🎛️ The Tuning House & `tune.jwt`

Out of the box, `polycracker-ecu install` provisions a balanced **30-day Stage 2 Track Spec** base tune so you can start testing immediately without touching a single dial.

When you want explicit control instead of black-box auto-magic, head to the **[Tuning House](https://portal.polycracker.dev/dashboard/tuning-house)**:

* **8 Macro Sliders & 36 Micro-Dials:** Dial in everything from broad compression aggressiveness down to granular AST stripping rules and **raw JSON trimming**.
* **🔐 Offline Ed25519-Signed `tune.jwt`:** The Tuning House compiles your exact configuration into a lightweight, cryptographically signed `tune.jwt` calibration file. Drop it on your machine and it runs **100% offline**—no phone-home required.
* **Flash a Custom Map in Seconds:** Once you download your `tune.jwt`, flash it to your local ECU:

```powershell
polycracker-ecu tune --file .\Downloads\tune.jwt
```

---

## 🔄 Reopen & Uninstall

Exiting from the system tray stops the active process without deleting your installation or your `tune.jwt`.

* **Reopen after closing the tray:**

```powershell
polycracker-ecu run
```

* **Delete `Polycracker-ECU.exe` and its installed files** *(close from the tray first)*:

```powershell
Remove-Item "$env:USERPROFILE\.polycracker-ecu\v1.0.0" -Recurse -Force
```

* **Remove the Python CLI wrapper as well:**

```powershell
pip uninstall polycracker-ecu
```

---

## ⚖️ License

* **CLI wrapper (`src/polycracker_ecu/`):** MIT License.
* **Compiled binary & release assets (`Polycracker-ECU.exe`, `EULA.txt`, `PRIVACY.txt`):** Proprietary — Parrot Integrated Software Development.