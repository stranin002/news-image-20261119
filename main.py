"""News image entry for 19 Nov 2026: copy the built entry.png to /output/entry.png.
Standard library only, deterministic, no network.
"""
import os
import shutil

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
shutil.copyfile(os.path.join(os.path.dirname(__file__), "entry.png"), os.path.join(out, "entry.png"))
