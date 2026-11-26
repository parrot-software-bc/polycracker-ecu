# Polycracker ECU

Local CLI wrapper and release installer for **Polycracker ECU** - deterministic, surgical Python AST token compression on your workstation via local stdio MCP.

- **Zero cloud code upload:** Compression runs locally on your machine.
- **Free 30-day Stage 2 Track Spec trial:** Provisioned automatically during `polycracker-ecu install`.
- **Tuning House:** Customize 8 macro sliders and 36 micro-dials into offline Ed25519-signed `tune.jwt` calibration maps at [portal.polycracker.dev/dashboard/tuning-house](https://portal.polycracker.dev/dashboard/tuning-house).

## Quick Start (Windows x64)

    pip install polycracker-ecu
    polycracker-ecu install
    polycracker-ecu wrap

### Flash a Custom Tune

    polycracker-ecu tune --file path/to/tune.jwt
