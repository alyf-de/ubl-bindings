"""Generate the bindings for one UBL release.

Usage: uv run scripts/generate.py 2.5

Reads  src/ubl_bindings/schemas/<release>/xsd/maindoc/
Writes src/ubl_bindings/v<major>_<minor>/
"""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKAGE_DIR = ROOT / "src" / "ubl_bindings"

# xsdata re-exports all classes of the UBL namespaces in this package.
# We re-export them again, so that users can write `from ubl_bindings.v2_5 import Invoice`.
INIT_TEMPLATE = '''"""Generated bindings for UBL {release}. Do not edit. See scripts/generate.py."""

from ubl_bindings.{module}.oasis.names.specification.ubl.schema.xsd import *  # noqa: F403
'''


def main(release: str) -> None:
    module = "v" + release.replace(".", "_")
    maindoc_dir = PACKAGE_DIR / "schemas" / release / "xsd" / "maindoc"
    target_dir = PACKAGE_DIR / module

    with tempfile.TemporaryDirectory() as tmp:
        # Generate into a temporary directory, because xsdata also writes
        # ubl_bindings/__init__.py, which is hand-written.
        run_xsdata(maindoc_dir, f"ubl_bindings.{module}", cwd=tmp)
        shutil.rmtree(target_dir, ignore_errors=True)
        shutil.copytree(
            Path(tmp) / "ubl_bindings" / module,
            target_dir,
            ignore=shutil.ignore_patterns("__pycache__"),
        )

    init_code = INIT_TEMPLATE.format(release=release, module=module)
    (target_dir / "__init__.py").write_text(init_code)
    print(f"Generated {target_dir.relative_to(ROOT)}")


def run_xsdata(source_dir: Path, package: str, cwd: str) -> None:
    command = [
        "xsdata",
        "generate",
        "--config",
        str(ROOT / ".xsdata.xml"),
        "--package",
        package,
        "--recursive",
        str(source_dir),
    ]
    subprocess.run(command, cwd=cwd, check=True)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
