
"""
Noetivis Repo Validator
Usage:
  python tools/validate_repo.py --repo ./noetivis_repo
"""

import argparse, os, sys

EXPECTED = [
  "backend",
  "backend/app",
  "backend/app/main.py",
  "docs",
  "README.md"
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    args = ap.parse_args()

    missing = []
    for p in EXPECTED:
        if not os.path.exists(os.path.join(args.repo, p)):
            missing.append(p)

    if missing:
        print("Missing expected paths:")
        for m in missing:
            print(" -", m)
        sys.exit(1)

    print("Repo looks OK ✅")
    sys.exit(0)

if __name__ == "__main__":
    main()
