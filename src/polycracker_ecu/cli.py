import argparse
import hashlib
import json
import platform
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
import uuid
import zipfile
from pathlib import Path

from . import __version__

RELEASE_URL = (
    "https://github.com/parrot-software-bc/polycracker-ecu/"
    "releases/download/v1.0.0/polycracker-ecu-v1.0.0-win64.zip"
)
RELEASE_SHA256 = "C2806A5F8A2228D60095D76ACF97E9CA312D9A046A37413B92BB5818353AC325"
TRIAL_ENDPOINT = "https://portal.polycracker.dev/api/v1/trial-tune"
INSTALL_DIR = Path.home() / ".polycracker-ecu" / f"v{__version__}"
EXE_NAME = "Polycracker-ECU.exe"


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def _machine_hash() -> str:
    raw = "|".join([
        platform.system(),
        platform.machine(),
        platform.node(),
        str(uuid.getnode()),
    ])
    return hashlib.sha256(raw.encode("utf-8")).hexdigest().lower()


def cmd_tune(args: argparse.Namespace) -> int:
    exe_path = INSTALL_DIR / EXE_NAME
    if not exe_path.exists():
        print("Polycracker ECU is not installed yet. Run: polycracker-ecu install", file=sys.stderr)
        return 1

    tune_dest = INSTALL_DIR / "tune.jwt"

    if args.file:
        src = Path(args.file).expanduser().resolve()
        if not src.exists():
            print(f"Tune file not found: {src}", file=sys.stderr)
            return 1
        shutil.copy2(src, tune_dest)
        print(f"Flashed custom tune -> {tune_dest}")
        return 0

    payload = json.dumps({
        "machine_hash": _machine_hash(),
        "client_version": __version__,
    }).encode("utf-8")

    req = urllib.request.Request(
        TRIAL_ENDPOINT,
        data=payload,
        headers={"Content-Type": "application/json", "User-Agent": f"polycracker-ecu/{__version__}"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        if e.code == 409:
            print("Free 30-day Stage 2 trial has expired for this machine.", file=sys.stderr)
            print("Create a custom tune at: https://portal.polycracker.dev/dashboard/tuning-house", file=sys.stderr)
        elif e.code == 429:
            print("Trial rate limit reached for this network (max 3 machines per 30 days).", file=sys.stderr)
        else:
            print(f"Trial server returned HTTP {e.code}: {body}", file=sys.stderr)
        return 1
    except urllib.error.URLError as e:
        print(f"Could not reach {TRIAL_ENDPOINT}: {e.reason}", file=sys.stderr)
        return 1

    tune_jwt = data.get("tune_jwt")
    if not tune_jwt:
        print(f"Unexpected response from trial server: {data}", file=sys.stderr)
        return 1

    tune_dest.write_text(tune_jwt, encoding="utf-8")
    preset = data.get("preset_name", "Stage 2 - Track Spec")
    expires = data.get("expires_at", "30 days")
    print(f"Minted free trial tune: {preset}")
    print(f"Expires: {expires}")
    print(f"Saved to: {tune_dest}")
    return 0


def cmd_install(args: argparse.Namespace) -> int:
    if platform.system() != "Windows":
        print("Polycracker ECU v1.0.0 binaries are currently Windows x64 only.", file=sys.stderr)
        return 1

    INSTALL_DIR.mkdir(parents=True, exist_ok=True)
    zip_path = INSTALL_DIR / "polycracker-ecu-v1.0.0-win64.zip"

    print(f"Downloading Polycracker ECU v{__version__}...")
    try:
        urllib.request.urlretrieve(RELEASE_URL, zip_path)
    except Exception as e:
        print(f"Download failed: {e}", file=sys.stderr)
        return 1

    actual_hash = _sha256_file(zip_path)
    if actual_hash != RELEASE_SHA256:
        zip_path.unlink(missing_ok=True)
        print("SHA-256 verification failed!", file=sys.stderr)
        print(f"  Expected: {RELEASE_SHA256}", file=sys.stderr)
        print(f"  Actual:   {actual_hash}", file=sys.stderr)
        return 1

    print("SHA-256 verified. Extracting...")
    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(INSTALL_DIR)
    zip_path.unlink(missing_ok=True)

    print(f"Installed Polycracker ECU -> {INSTALL_DIR / EXE_NAME}")

    if not args.no_trial:
        print("Provisioning free 30-day Stage 2 Track Spec trial tune...")
        return cmd_tune(argparse.Namespace(file=None))
    return 0


def cmd_wrap(args: argparse.Namespace) -> int:
    exe_path = INSTALL_DIR / EXE_NAME
    if not exe_path.exists():
        print("Polycracker ECU is not installed. Run: polycracker-ecu install", file=sys.stderr)
        return 1

    proc = subprocess.run([str(exe_path), *args.ecu_args], cwd=str(INSTALL_DIR))
    return proc.returncode


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="polycracker-ecu",
        description="Local CLI wrapper and installer for Polycracker ECU.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    p_install = sub.add_parser("install", help="Download, verify, and install Polycracker ECU.")
    p_install.add_argument("--no-trial", action="store_true", help="Skip automatic 30-day Stage 2 trial tune minting.")
    p_install.set_defaults(func=cmd_install)

    p_tune = sub.add_parser("tune", help="Mint a free 30-day Stage 2 trial tune or flash a custom tune.jwt.")
    p_tune.add_argument("--file", help="Path to a custom tune.jwt downloaded from the Tuning House.")
    p_tune.set_defaults(func=cmd_tune)

    p_wrap = sub.add_parser("wrap", help="Launch Polycracker-ECU.exe (forwards stdio and arguments).")
    p_wrap.add_argument("ecu_args", nargs=argparse.REMAINDER, help="Arguments forwarded to Polycracker-ECU.exe.")
    p_wrap.set_defaults(func=cmd_wrap)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
