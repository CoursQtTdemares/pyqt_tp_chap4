from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow

from src.simple_interface import Ui_MainWindow


class CompiledMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setupUi(self)
        self.nb_clicks = 0

        self.setup_ui_customisation()
        self.setup_ui_signals()

    def my_button_clicked(self) -> None:
        self.nb_clicks += 1
        self.my_label.setText(f"Nb de clicks: {self.nb_clicks}")

    def setup_ui_customisation(self) -> None:
        font = self.my_label.font()
        font.setPointSize(16)
        self.my_label.setFont(font)
        self.my_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def setup_ui_signals(self) -> None:
        self.my_button.clicked.connect(self.my_button_clicked)
