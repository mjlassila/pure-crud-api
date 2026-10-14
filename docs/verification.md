# Verification performed

Completed in the managed workspace on 2026-10-14 using Python 3.12 and the versions recorded in `requirements-dev.lock`.

| Check | Actual result |
| --- | --- |
| Inspect original API contract | Pure 5.36.3; server `/ws/api`; `api-key` header; 970 operations |
| Generate with openapi-python-client 0.27.1 | Completed; original warnings captured in `generation-original.log`; final warnings in `generation.log` |
| Import generated modules | All 1,551 generated submodules imported |
| Operation accounting | 970 inventoried: 928 generated, 21 partial binary downloads, 21 unsupported wildcard uploads |
| `pytest -q` | **92 passed**; two upstream Typer/Click deprecation warnings |
| Original YAML preservation | Byte-for-byte match to uploaded file |
| Repeat `python -m scripts.generate` | Successful; all 1,570 tracked source, test, script, configuration, lock, and specification files retained identical SHA-256 digests |
| `python -m build --no-isolation` | Wheel and source distribution built successfully |
| Install wheel in a fresh venv | Installed successfully, independently of checkout source paths |
| Installed Python imports | `PureClient`, `Settings`, generated `PersonsQuery`, and `person_list` imported successfully |
| Installed mocked workflow | Configured client performed a list operation through MockTransport successfully |
| Installed CLI help | `pure --help` and `pure persons search --help` exited successfully |
| Installed `pip check` | No broken requirements |

The regeneration comparison excludes Python and formatter caches. Formatter caches were excluded from the generated source copy and do not appear in the wheel.

Original specification SHA-256:

```text
f0a592a907105f2151d1dfe9fcacb3096a13ba63c29d010ff55908e3c6f2b517
```

All behavioral HTTP verification was mocked. No live Pure instance was called; there was no credential requirement for routine tests. Generated operations outside the representative client/CLI workflows were import-checked and inventoried, not individually behavior-tested. Wildcard binary upload support remains blocked by the pinned generator's unsupported request content type; download modules have no success parser but expose raw response bytes. These limitations are explicitly listed in `coverage.md` and `coverage.json`.
