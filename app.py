import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QLineEdit, QPushButton, QLabel, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class StreamSessionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Konfiguracja okna głównego
        self.setWindowTitle("Manager Sesji Strumieniowania")
        self.setFixedSize(500, 320)
        
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
            QLineEdit {
                background-color: #313244;
                border: 2px solid #45475a;
                border-radius: 8px;
                padding: 10px;
                color: #f5e0dc;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #89b4fa;
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
                padding: 10px;
                font-family: 'Consolas', 'Courier New', monospace;
                color: #a6e3a1;
                font-size: 15px;
            }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)

        # 1. Etykieta i pole do wprowadzania klucza
        self.input_label = QLabel("Wprowadź klucz strumieniowania:")
        layout.addWidget(self.input_label)

        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("np. live_123456789_abcdef...")
        self.key_input.setEchoMode(QLineEdit.EchoMode.Password)  # Ukrywa wpisywany tekst (kropki)
        self.key_input.textChanged.connect(self.update_display)
        layout.addWidget(self.key_input)

        # 2. Wyświetlacz aktualnego klucza
        self.display_label_title = QLabel("Podgląd klucza:")
        layout.addWidget(self.display_label_title)

        self.key_display = QLabel("---")
        self.key_display.setObjectName("KeyDisplay")
        self.key_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.key_display)

        # 3. Przycisk rozpoczęcia sesji
        self.start_btn = QPushButton("Rozpocznij Sesję")
        self.start_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.start_btn.clicked.connect(self.start_session)
        layout.addWidget(self.start_btn)

        self.setLayout(layout)

    def update_display(self, text):
        """Aktualizuje podgląd klucza na ekranie na żywo"""
        if text.strip():
            self.key_display.setText(text)
        else:
            self.key_display.setText("---")

    def start_session(self):
        """Obsługa kliknięcia guzika Rozpocznij sesje"""
        stream_key = self.key_input.text().strip()
        
        if not stream_key:
            QMessageBox.warning(self, "Błąd", "Najpierw wprowadź klucz strumieniowania!")
            return

        # Tutaj dodaj własną logikę (np. uruchomienie OBS, wysłanie żądania API itp.)
        QMessageBox.information(
            self, 
            "Sesja Uruchomiona", 
            f"Sesja strumieniowania została pomyślnie rozpoczęta dla klucza:\n\n{stream_key}"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = StreamSessionApp()
    ex.show()
    sys.exit(app.exec())