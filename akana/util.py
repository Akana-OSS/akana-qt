"""Shared helpers for Akana Qt widgets (repolish, a11y, geometry)."""

from __future__ import annotations

from typing import Any

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget


def repolish(widget: QWidget) -> None:
    """Force QSS re-evaluation after dynamic property changes."""
    style = widget.style()
    if style is not None:
        style.unpolish(widget)
        style.polish(widget)
    widget.update()


def set_dyn(widget: QWidget, name: str, value: Any) -> None:
    """Set a dynamic property and repolish."""
    widget.setProperty(name, value)
    repolish(widget)


def clear_layout(layout) -> None:
    """Remove and delete all items from a layout."""
    while layout.count():
        item = layout.takeAt(0)
        w = item.widget()
        if w is not None:
            w.setParent(None)
            w.deleteLater()
        child = item.layout()
        if child is not None:
            clear_layout(child)


def hand_cursor(widget: QWidget) -> None:
    widget.setCursor(Qt.CursorShape.PointingHandCursor)
