"""Akana Qt — monochrome empty state (web `.ak-empty`)."""

from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout, QWidget

from akana.icons import glyph
from akana.tokens import SPACE


class AkEmptyState(QFrame):
    def __init__(
        self,
        title: str = "Nothing here",
        body: str = "",
        *,
        icon: str | None = None,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.setObjectName("AkEmptyState")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setMaximumWidth(420)

        root = QVBoxLayout(self)
        root.setContentsMargins(SPACE[12], SPACE[12], SPACE[12], SPACE[12])
        root.setSpacing(SPACE[2])
        root.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._icon = QLabel(icon if icon is not None else glyph("empty"))
        self._icon.setObjectName("akEmptyIcon")
        self._icon.setFixedSize(48, 48)
        self._icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._icon.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        root.addWidget(self._icon, 0, Qt.AlignmentFlag.AlignHCenter)
        root.addSpacing(SPACE[3])

        self._title = QLabel(title)
        self._title.setObjectName("akEmptyTitle")
        self._title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._title.setWordWrap(True)
        root.addWidget(self._title)

        self._body = QLabel(body)
        self._body.setObjectName("akEmptyBody")
        self._body.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._body.setWordWrap(True)
        self._body.setMaximumWidth(280)
        self._body.setVisible(bool(body))
        root.addWidget(self._body, 0, Qt.AlignmentFlag.AlignHCenter)

        self._actions = QHBoxLayout()
        self._actions.setSpacing(SPACE[3])
        self._actions.setAlignment(Qt.AlignmentFlag.AlignCenter)
        root.addSpacing(SPACE[4])
        root.addLayout(self._actions)

    def add_action(self, widget: QWidget) -> None:
        self._actions.addWidget(widget)

    def set_title(self, title: str) -> None:
        self._title.setText(title)

    def set_body(self, body: str) -> None:
        self._body.setText(body)
        self._body.setVisible(bool(body))

    def set_icon(self, glyph_text: str) -> None:
        self._icon.setText(glyph_text)
