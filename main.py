from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from main_window import Ui_MainWindow
import sys
import os

from pydub import AudioSegment
from mutagen.mp3 import MP3

def getduration(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No such file: '{file_path}'")
    audio = MP3(file_path)
    return audio.info.length

def createmp3(duration, output_path):
    silent_audio = AudioSegment.silent(duration=duration * 1000)
    silent_audio.export(output_path, format="mp3")

def convert(ui):
    file_dialog = QFileDialog()
    file_path, _ = file_dialog.getOpenFileName(None, "Open MP3 File", "", "MP3 Files (*.mp3)")
    if file_path:
        print(f"Selected MP3 file: {file_path}")

    duration = getduration(file_path)

    output_path, _ = file_dialog.getSaveFileName(None, "Save Audio File", "", "MP3 Files (*.mp3)")
    if output_path:
        print(f"Saving silent MP3 file at: {output_path}")
        createmp3(duration, output_path)
        print(f"Silent MP3 file created at: {output_path}")

        ui.progressBar.setValue(100)

def abouttext(main_window):
    QMessageBox.about(main_window, "About This Program", "Link Voice Maker v1.0 by Elliot\nReleased under MIT License\nRelease "
                                            "date: 2024/05/25")


def quit_application():
    QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    ui.browse_button.clicked.connect(lambda: convert(ui))
    ui.actionOpen.triggered.connect(lambda: convert(ui))
    ui.actionQuit.triggered.connect(quit_application)
    ui.actionAbout.triggered.connect(lambda: abouttext(mainWindow))

    mainWindow.show()
    sys.exit(app.exec_())
