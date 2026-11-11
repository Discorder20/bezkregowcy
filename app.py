import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, 
    QPushButton, QLabel, QMessageBox
)
from PyQt6.QtCore import Qt

# ==============================================================================
# TUTAJ WKLEJ WARTOŚĆ STAŁEJ (NP. TOKEN, KLUCZ, ID SESJI) GDY GO UZYSKASZ:
SESSION_KEY = "TWOJA_STALA_WARTOŚĆ_TUTAJ"
# ==============================================================================

class FeatureModule(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Konfiguracja okna/modułu
        self.setWindowTitle("Panel Sesji")
        self.setFixedSize(450, 220)
        
        # Neutralna stylizacja w ciemnym motywie (CSS)
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e2e;
                color: #cdd6f4;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QLabel {
                font-size: 14px;
            }
            QPushButton {
                background-color: #89b4fa;
                color: #11111b;
                border: none;
                border-radius: 8px;
                padding: 12px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #b4befe;
            }
            QPushButton:pressed {
                background-color: #74c7ec;
            }
            #ValueDisplay {
                background-color: #181825;
                border: 1px solid #45475a;
                border-radius: 8px;
                padding: 12px;
                font-family: 'Consolas', 'Courier New', monospace;
                color: #a6e3a1;
                font-size: 15px;
            }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)

        # 1. Etykieta i wyświetlacz stałego klucza/tokena
        self.display_label_title = QLabel("Identyfikator / Kod:")
        layout.addWidget(self.display_label_title)

        self.key_display = QLabel(SESSION_KEY)
        self.key_display.setObjectName("ValueDisplay")
        self.key_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.key_display)

        # 2. Przycisk wykonania akcji
        self.start_btn = QPushButton("Rozpocznij sesję")
        self.start_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.start_btn.clicked.connect(self.run_action)
        layout.addWidget(self.start_btn)

        self.setLayout(layout)

    def run_action(self):
        """Wykonanie akcji po kliknięciu guzika"""
        if SESSION_KEY == "TWOJA_STALA_WARTOŚĆ_TUTAJ" or not SESSION_KEY.strip():
            QMessageBox.warning(
                self, 
                "Brak wartości", 
                "Nie ustawiono wartości klucza/tokena w kodzie programu."
            )
            return

        # Tutaj wywołujesz właściwą funkcję swojej aplikacji
        QMessageBox.information(
            self, 
            "Akcja wykonana", 
            f"Uruchomiono sesję z kluczem:\n\n{SESSION_KEY}"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = FeatureModule()
    ex.show()
    sys.exit(app.exec())