import sys
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

WORKSPACE_DIR = Path(__file__).parent
UI_PATH = WORKSPACE_DIR / "src" / "simple_interface.ui"


def main() -> int:
    """Entry point for pyqt_tp_chap4."""
    app = QApplication(sys.argv)

    window = uic.loadUi(UI_PATH)
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
