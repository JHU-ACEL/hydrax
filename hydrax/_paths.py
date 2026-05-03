"""Bundled asset root (``models/``, …) without depending on ``hydrax`` package init order."""

from pathlib import Path

# Same value as historical ``hydrax.ROOT``: inner package dir ``…/hydrax/hydrax``.
ROOT = str(Path(__file__).resolve().parent)
