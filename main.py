import sys

from PyQt6.QtWidgets import QApplication

from src.main_compiled import CompiledMainWindow


def main() -> int:
    """Entry point for pyqt_tp_chap4."""
    app = QApplication(sys.argv)

    window = CompiledMainWindow()
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
