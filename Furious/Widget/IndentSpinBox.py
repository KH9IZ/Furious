# Copyright (C) 2023  Loren Eteval <loren.eteval@proton.me>
#
# This file is part of Furious.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from Furious.Utility.Utility import (
    StateContext,
    SupportConnectedCallback,
    bootstrapIcon,
)
from Furious.Utility.Translator import Translatable, gettext as _

from PySide6 import QtCore
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLabel,
    QSpinBox,
)


class IndentSpinBox(Translatable, SupportConnectedCallback, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle(_('Set Indent'))
        self.setWindowIcon(bootstrapIcon('rocket-takeoff-window.svg'))

        self.indentText = QLabel(_('Indent:'))

        self.indentSpin = QSpinBox()
        self.indentSpin.setRange(0, 8)
        self.indentSpin.setValue(2)

        self.dialogBtns = QDialogButtonBox(QtCore.Qt.Orientation.Horizontal)

        self.dialogBtns.addButton(_('OK'), QDialogButtonBox.ButtonRole.AcceptRole)
        self.dialogBtns.addButton(_('Cancel'), QDialogButtonBox.ButtonRole.RejectRole)
        self.dialogBtns.accepted.connect(self.accept)
        self.dialogBtns.rejected.connect(self.reject)

        layout = QFormLayout()

        layout.addRow(self.indentText, self.indentSpin)
        layout.addRow(self.dialogBtns)
        layout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def value(self):
        return self.indentSpin.value()

    def connectedCallback(self):
        self.setWindowIcon(bootstrapIcon('rocket-takeoff-connected-dark.svg'))

    def disconnectedCallback(self):
        self.setWindowIcon(bootstrapIcon('rocket-takeoff-window.svg'))

    def retranslate(self):
        with StateContext(self):
            self.setWindowTitle(_(self.windowTitle()))

            self.indentText.setText(_(self.indentText.text()))

            for button in self.dialogBtns.buttons():
                button.setText(_(button.text()))
