# Polycracker ECU

Local CLI wrapper and release installer for **Polycracker ECU** - deterministic, surgical Python AST token compression on your workstation via local stdio MCP.

- **Local-first compression:** Runs on your machine with zero cloud code upload.
- **30-day Stage 2 Track Spec trial:** Provisioned automatically during polycracker-ecu install (or via polycracker-ecu tune).
- **Tuning House:** Customize 8 macro sliders and 36 micro-dials into offline Ed25519-signed 	une.jwt calibration maps in the [Tuning House](https://portal.polycracker.dev/dashboard/tuning-house), then flash them locally.

## Quick Start (Windows x64)

1. Install the open-source CLI wrapper:

    pip install polycracker-ecu

2. Download, verify, and extract Polycracker-ECU.exe + provision your 30-day Stage 2 trial tune:

    polycracker-ecu install

3. Start the local ECU / MCP server:

    polycracker-ecu run

*(Testing from a local clone before PyPI release? Run pip install -e . in step 1.)*

## Custom Tunes

Flash a signed calibration map exported from the [Tuning House](https://portal.polycracker.dev/dashboard/tuning-house):

    polycracker-ecu tune --file path/to/tune.jwt

## Reopen & Uninstall

Exiting from the system tray stops the active process without deleting your installation or 	une.jwt.

- **Reopen after closing the tray:**

    polycracker-ecu run

- **Delete Polycracker-ECU.exe and its installed files** (close from the tray first):

    Remove-Item "C:\Users\npare\.polycracker-ecu\v1.0.0" -Recurse -Force

- **Remove the Python CLI wrapper as well:**

    pip uninstall polycracker-ecu

## License

- **CLI wrapper (src/polycracker_ecu/):** MIT License.
- **Compiled binary & release assets (Polycracker-ECU.exe, EULA.txt, PRIVACY.txt):** Proprietary - Parrot Integrated Software Development.