"""The examples in the README must work."""

import re
from pathlib import Path

import ubl_bindings

README = Path(__file__).parent.parent / "README.md"


def test_written_document_is_valid():
    namespace = {}
    exec(readme_code("Write a document"), namespace)

    assert ubl_bindings.validate(namespace["xml"]) == []


def test_links_are_absolute():
    # PyPI shows the README without the repository, so relative links break there.
    links = re.findall(r"\]\(([^)]+)\)", README.read_text())

    assert [link for link in links if not link.startswith(("https://", "#"))] == []


def readme_code(heading: str) -> str:
    section = README.read_text().split(f"### {heading}\n", 1)[1]
    return re.search(r"```python\n(.*?)```", section, re.DOTALL).group(1)
