import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, 
    QPushButton, QLabel, QMessageBox
)
from PyQt6.QtCore import Qt

# ==============================================================================
# TUTAJ WKLEJ SWÓJ KLUCZ STRUMIENIOWANIA GDY GO UZYSKASZ:
STREAM_KEY = "TWÓJ_KLUCZ_STRUMIENIOWANIA_TUTAJ"
# ==============================================================================

class StreamSessionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Konfiguracja okna głównego
        self.setWindowTitle("Bezkręgowcy czy coś idk.")
        self.setFixedSize(450, 240)
        
        # Stylizacja w ciemnym motywie (CSS)
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
            #KeyDisplay {
                background-color: #181825;
                border: 1px dashed #45475a;
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

        # 1. Etykieta i wyświetlacz stałego klucza
        self.display_label_title = QLabel("Aktualny klucz strumieniowania:")
        layout.addWidget(self.display_label_title)

        self.key_display = QLabel(STREAM_KEY)
        self.key_display.setObjectName("KeyDisplay")
        self.key_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.key_display)

        # 2. Przycisk rozpoczęcia sesji
        self.start_btn = QPushButton("Rozpocznij Sesję")
        self.start_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.start_btn.clicked.connect(self.start_session)
        layout.addWidget(self.start_btn)

        self.setLayout(layout)

    def start_session(self):
        """Obsługa kliknięcia guzika Rozpocznij sesję"""
        # Sprawdzenie, czy klucz został zmieniony ze domyślnego tekstu
        if STREAM_KEY == "TWÓJ_KLUCZ_STRUMIENIOWANIA_TUTAJ" or not STREAM_KEY.strip():
            QMessageBox.warning(
                self, 
                "Brak klucza", 
                "Nie podano jeszcze poprawnego klucza strumieniowania w kodzie programu!"
            )
            return

        # Tutaj wykonuje się logika uruchomienia sesji z użyciem zmiennej STREAM_KEY
        QMessageBox.information(
            self, 
            "Sesja Uruchomiona", 
            f"Sesja strumieniowania została pomyślnie rozpoczęta dla klucza:\n\n{STREAM_KEY}"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = StreamSessionApp()
    ex.show()
    sys.exit(app.exec())