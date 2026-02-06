
"""
Noetivis Bootstrap Merger

Usage:
  python tools/bootstrap_merge.py --dest ./noetivis_repo --zips phase1.zip phase2.zip ... phase12.zip

What it does:
- Extracts ZIPs in order into dest (overlay/merge)
- Finds any main_patch.txt/App_patch.txt and lists them
- Writes MERGE_REPORT.md into dest
"""

import argparse, os, zipfile, pathlib

def extract_zip(zip_path: str, dest: str):
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(dest)

def find_patches(dest: str):
    patches = []
    for root, _, files in os.walk(dest):
        for fn in files:
            if fn.endswith("main_patch.txt") or fn.endswith("App_patch.txt"):
                patches.append(os.path.join(root, fn))
    return patches

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dest", required=True)
    ap.add_argument("--zips", nargs="+", required=True)
    args = ap.parse_args()

    dest = args.dest
    pathlib.Path(dest).mkdir(parents=True, exist_ok=True)

    report_lines = ["# Merge Report", f"Destination: {dest}", "## Zips applied:"]
    for zp in args.zips:
        report_lines.append(f"- {zp}")
        extract_zip(zp, dest)

    patches = find_patches(dest)
    report_lines.append("## Patch files to apply manually")
    if not patches:
        report_lines.append("- None found")
    else:
        for p in patches:
            rel = os.path.relpath(p, dest)
            report_lines.append(f"- {rel}")

    report_path = os.path.join(dest, "MERGE_REPORT.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines) + "\n")

    print("Merge complete.")
    print("Patch files found:")
    for p in patches:
        print(" -", p)
    print("Wrote:", report_path)

if __name__ == "__main__":
    main()
