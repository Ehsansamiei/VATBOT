from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
import sys

def start_bot():
    file_name, _ = QFileDialog.getOpenFileName(None, "انتخاب فایل اکسل", "", "Excel Files (*.xlsx)")
    print("فایل:", file_name)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("ربات ثبت VAT169")
window.setGeometry(200, 200, 300, 150)

btn = QPushButton("انتخاب فایل اکسل و شروع", window)
btn.clicked.connect(start_bot)
btn.move(70, 50)

window.show()
sys.exit(app.exec_())
