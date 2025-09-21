import sys
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

WORKSPACE_DIR = Path(__file__).parent
UI_PATH = WORKSPACE_DIR / "src" / "simple_interface.ui"


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        uic.loadUi(UI_PATH, self)
        self.my_button.clicked.connect(self.my_button_clicked)

    def my_button_clicked(self) -> None:
        self.my_label.setText("Hello, World!")


def main() -> int:
    """Entry point for pyqt_tp_chap4."""
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
