
# Consolidation Guide

1) Put all Noetivis phase ZIPs in one folder.
2) Run:
   python tools/bootstrap_merge.py --dest ./noetivis_repo --zips <phase zips in order>
3) Open MERGE_REPORT.md and apply each main_patch.txt instruction.
4) Validate:
   python tools/validate_repo.py --repo ./noetivis_repo
5) Initialize git + push to GitHub.
