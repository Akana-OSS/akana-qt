"""Akana Qt — monochrome, text-first, offline Qt design system.

Port of web Akana (https://github.com/alptekinege/Akana) v0.5:
3-layer tokens, no accent color, bundled IBM Plex TTF.
"""

from akana import fonts, styles, theme, tokens, winchrome

__version__ = "0.5.0"

__all__ = [
    "tokens",
    "theme",
    "styles",
    "fonts",
    "winchrome",
    "__version__",
]
