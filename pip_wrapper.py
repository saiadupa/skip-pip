#!/usr/bin/env python3
import sys
import subprocess
import argparse
import os

def skip_install_requirements(requirements_files, extra_args):
    failed_packages = []  # list to collect packages that failed installation
    for req in requirements_files:
        if not os.path.exists(req):
            print(f"Error: Requirements file '{req}' does not exist.", file=sys.stderr)
            continue
        with open(req, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                print(f"\nInstalling package: {line}")
                cmd = [sys.executable, "-m", "pip", "install"] + extra_args + [line]
                try:
                    result = subprocess.run(
                        cmd,
                        check=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,
                    )
                    print(result.stdout)
                except subprocess.CalledProcessError as error:
                    print(f"Error installing {line}. Skipping.", file=sys.stderr)
                    print(f"Details: {error.stderr.strip()}", file=sys.stderr)
                    failed_packages.append(line)
    if failed_packages:
        print("\nThe following packages failed to install:")
        for pkg in failed_packages:
            print(f" - {pkg}")
    return failed_packages

def forward_to_pip(args):
    """Forwards all arguments to the actual pip command."""
    cmd = [sys.executable, "-m", "pip"] + args
    subprocess.run(cmd)

def main():
    if len(sys.argv) < 2:
        print("Usage: pip <command> [options]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "install":
        parser = argparse.ArgumentParser(prog="pip install", add_help=False)
        parser.add_argument("-r", "--requirement", action="append", dest="requirements")
        parser.add_argument("packages", nargs="*", help="Packages to install")
        # Allow extra pip options to be passed along
        parser.add_argument("--", dest="extra", nargs=argparse.REMAINDER,
                            help="Extra arguments for pip install")
        parsed, unknown = parser.parse_known_args(sys.argv[2:])
        extra_args = unknown  # pass along any unrecognized arguments

        if parsed.requirements:
            skip_install_requirements(parsed.requirements, extra_args)
            # Also install packages provided directly on the command line (if any)
            for pkg in parsed.packages:
                print(f"\nInstalling package: {pkg}")
                cmd = [sys.executable, "-m", "pip", "install"] + extra_args + [pkg]
                try:
                    result = subprocess.run(
                        cmd,
                        check=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,
                    )
                    print(result.stdout)
                except subprocess.CalledProcessError as error:
                    print(f"Error installing {pkg}. Skipping.", file=sys.stderr)
                    print(f"Details: {error.stderr.strip()}", file=sys.stderr)
        else:
            forward_to_pip(sys.argv[1:])
    else:
        # For commands other than "install", just forward them to pip.
        forward_to_pip(sys.argv[1:])

if __name__ == "__main__":
    main()
