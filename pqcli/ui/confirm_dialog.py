import typing as T

import urwid

from pqcli.ui.button import MenuButton


class ConfirmDialog(urwid.Overlay):
    signals = ["confirm", "cancel"]

    def __init__(self, label: str, parent: urwid.Widget) -> None:
        question = urwid.Text(("bold", label), "center")
        yes_btn = MenuButton(
            "Yes", hint="Y", on_press=lambda _user_data: self.confirm()
        )
        no_btn = MenuButton(
            "No", hint="N", on_press=lambda _user_data: self.cancel()
        )

        line_box = urwid.LineBox(
            urwid.ListBox(
                urwid.SimpleFocusListWalker([question, no_btn, yes_btn])
            )
        )

        super().__init__(
            line_box, parent, "center", len(label) + 6, "middle", 5
        )

    def keypress(self, size: T.Any, key: str) -> T.Optional[str]:
        if key in {"y", "Y"}:
            self.confirm()
            return None
        if key in {"n", "N"}:
            self.cancel()
            return None
        return T.cast(T.Optional[str], super().keypress(size, key))

    def confirm(self) -> None:
        self._emit("confirm")

    def cancel(self) -> None:
        self._emit("cancel")