# -*- coding: utf-8 -*-


# Python Builder
# Author: Danx
# Description: A GUI for compiling Python files (.py) into executables (.exe)
#              using PyInstaller. Created to provide more detailed control
#              over the compilation process and to avoid large file size issues
#              sometimes caused by automatic hooks.


import sys
import os
import subprocess
import base64
import time
import json
from PySide6.QtCore import (
    Qt, QThread, Signal, QSize, QTimer
)
from PySide6.QtGui import (
    QIcon, QFont, QTextCursor
)
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QGroupBox, QLabel, QLineEdit, QPushButton,
    QCheckBox, QComboBox, QFileDialog, QListWidget, QListWidgetItem,
    QTextEdit, QMessageBox, QInputDialog
)


# Base64 data for the default icon. This will create icon.ico if it doesn't exist.
ICON_B64 = b'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-A+g8S9Wl2r5sW+5gAAAABJRU5ErkJggg=='


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def create_default_icon():
    """ Creates the default icon.ico file if it doesn't exist """
    if not os.path.exists('icon.ico'):
        try:
            with open('icon.ico', 'wb') as f:
                f.write(base64.b64decode(ICON_B64))
        except Exception as e:
            print(f"Failed to create default icon file: {e}")


class BuildThread(QThread):
    """
    Worker thread to run the PyInstaller process so the UI doesn't freeze.
    """
    progress = Signal(str)
    finished = Signal(int)

    def __init__(self, command):
        super().__init__()
        self.command = command
        self.process = None

    def run(self):
        """ Run the command in a subprocess """
        try:
            # Using Popen to read output in real-time
            self.process = subprocess.Popen(
                self.command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding='utf-8',
                creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0
            )

            # Read output line by line
            for line in iter(self.process.stdout.readline, ''):
                self.progress.emit(line.strip())
            
            self.process.stdout.close()
            return_code = self.process.wait()
            self.finished.emit(return_code)

        except FileNotFoundError:
            self.progress.emit("Error: 'pyinstaller' not found.")
            self.progress.emit("Please make sure PyInstaller is installed and in your system's PATH.")
            self.progress.emit("You can install it with: pip install pyinstaller")
            self.finished.emit(1)
        except Exception as e:
            self.progress.emit(f"An error occurred: {e}")
            self.finished.emit(1)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Builder by Danx")
        self.setWindowIcon(QIcon(resource_path('icon.ico')))
        self.setGeometry(100, 100, 400, 650)
        #self.setMinimumSize(800, 700)

        # Timer for elapsed time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_elapsed_time)
        self.start_time = 0

        self.setup_ui()
        self.build_thread = None

    def setup_ui(self):
        """ Set up all UI elements """
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # --- Input Section ---
        input_group = QGroupBox("Input / Output")
        input_layout = QGridLayout(input_group)
        
        self.script_input = QLineEdit()
        self.script_input.setPlaceholderText("Select Python file (.py)")
        browse_script_btn = QPushButton("Browse...")
        browse_script_btn.clicked.connect(self.select_script)
        
        self.output_dir_input = QLineEdit()
        self.output_dir_input.setPlaceholderText("Select output folder")
        browse_output_btn = QPushButton("Browse...")
        browse_output_btn.clicked.connect(self.select_output_dir)

        input_layout.addWidget(QLabel("Select Python Script (.py)"), 0, 0)
        input_layout.addWidget(self.script_input, 0, 1)
        input_layout.addWidget(browse_script_btn, 0, 2)
        input_layout.addWidget(QLabel("Output Directory"), 1, 0)
        input_layout.addWidget(self.output_dir_input, 1, 1)
        input_layout.addWidget(browse_output_btn, 1, 2)

        # --- Compilation Options and Version Info Section ---
        options_version_layout = QHBoxLayout()
        
        # Compilation Options
        comp_opts_group = QGroupBox("Compilation Options")
        comp_opts_layout = QGridLayout(comp_opts_group)

        self.onefile_check = QCheckBox("One-File Mode (single .exe)")
        self.noconsole_check = QCheckBox("Disable Console Window")
        self.shutdown_check = QCheckBox("Shutdown when done")
        
        self.cores_combo = QComboBox()
        self.cores_combo.addItems([str(i) for i in range(1, os.cpu_count() + 1)])
        self.cores_combo.setCurrentText(str(os.cpu_count()))
        
        self.icon_input = QLineEdit()
        self.icon_input.setPlaceholderText("Select icon file (.ico)")
        browse_icon_btn = QPushButton("Browse...")
        browse_icon_btn.clicked.connect(self.select_icon)
        
        comp_opts_layout.addWidget(self.onefile_check, 0, 0, 1, 2)
        comp_opts_layout.addWidget(self.noconsole_check, 1, 0, 1, 2)
        comp_opts_layout.addWidget(self.shutdown_check, 2, 0, 1, 2)
        comp_opts_layout.addWidget(QLabel("Compilation Cores:"), 3, 0)
        comp_opts_layout.addWidget(self.cores_combo, 3, 1)
        comp_opts_layout.addWidget(QLabel("Select Icon (.ico)"), 4, 0)
        comp_opts_layout.addWidget(self.icon_input, 5, 0, 1, 2)
        comp_opts_layout.addWidget(browse_icon_btn, 6, 1)
        
        options_version_layout.addWidget(comp_opts_group)

        # Windows Version Info
        version_info_group = QGroupBox("Windows Version Information")
        version_info_layout = QGridLayout(version_info_group)
        
        self.product_name_input = QLineEdit()
        self.product_version_input = QLineEdit()
        self.file_version_input = QLineEdit()
        self.file_description_input = QLineEdit()
        self.copyright_input = QLineEdit()

        version_info_layout.addWidget(QLabel("Product Name:"), 0, 0)
        version_info_layout.addWidget(self.product_name_input, 0, 1)
        version_info_layout.addWidget(QLabel("Product Version:"), 1, 0)
        version_info_layout.addWidget(self.product_version_input, 1, 1)
        version_info_layout.addWidget(QLabel("File Version:"), 2, 0)
        version_info_layout.addWidget(self.file_version_input, 2, 1)
        version_info_layout.addWidget(QLabel("File Description:"), 3, 0)
        version_info_layout.addWidget(self.file_description_input, 3, 1)
        version_info_layout.addWidget(QLabel("Copyright:"), 4, 0)
        version_info_layout.addWidget(self.copyright_input, 4, 1)
        
        options_version_layout.addWidget(version_info_group)
        options_version_layout.setStretch(0, 1)
        options_version_layout.setStretch(1, 1)

        # --- Additional Files, Folders, and Modules Section ---
        additional_group = QGroupBox("Include Additional Files, Folders, Modules")
        additional_layout = QGridLayout(additional_group)
        
        self.files_list = QListWidget()
        self.folders_list = QListWidget()
        self.modules_list = QListWidget()

        add_file_btn = QPushButton("Add Files...")
        add_file_btn.clicked.connect(self.add_files)
        remove_file_btn = QPushButton("Remove Selected")
        remove_file_btn.clicked.connect(lambda: self.remove_selected(self.files_list))
        
        add_folder_btn = QPushButton("Add Folder...")
        add_folder_btn.clicked.connect(self.add_folder)
        remove_folder_btn = QPushButton("Remove Selected")
        remove_folder_btn.clicked.connect(lambda: self.remove_selected(self.folders_list))
        
        add_module_btn = QPushButton("Add Module...")
        add_module_btn.clicked.connect(self.add_module)
        remove_module_btn = QPushButton("Remove Selected")
        remove_module_btn.clicked.connect(lambda: self.remove_selected(self.modules_list))

        additional_layout.addWidget(QLabel("Include Files:"), 0, 0)
        additional_layout.addWidget(self.files_list, 1, 0)
        additional_layout.addWidget(add_file_btn, 2, 0)
        additional_layout.addWidget(remove_file_btn, 3, 0)
        
        additional_layout.addWidget(QLabel("Include Folders:"), 0, 1)
        additional_layout.addWidget(self.folders_list, 1, 1)
        additional_layout.addWidget(add_folder_btn, 2, 1)
        additional_layout.addWidget(remove_folder_btn, 3, 1)

        additional_layout.addWidget(QLabel("Include Modules:"), 0, 2)
        additional_layout.addWidget(self.modules_list, 1, 2)
        additional_layout.addWidget(add_module_btn, 2, 2)
        additional_layout.addWidget(remove_module_btn, 3, 2)

        # --- Compilation Log Section ---
        log_group = QGroupBox("Compilation Log")
        log_layout = QVBoxLayout(log_group)

        log_header_layout = QHBoxLayout()
        self.elapsed_time_label = QLabel("Elapsed Time: 00:00:00")
        log_header_layout.addStretch()
        log_header_layout.addWidget(self.elapsed_time_label)

        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setFont(QFont("Courier", 9))
        self.log_output.setLineWrapMode(QTextEdit.NoWrap)

        log_layout.addLayout(log_header_layout)
        log_layout.addWidget(self.log_output)
        
        # --- Bottom Buttons Section ---
        bottom_buttons_layout = QHBoxLayout()
        self.load_profile_btn = QPushButton("Load Profile")
        self.load_profile_btn.clicked.connect(self.load_profile)
        self.save_profile_btn = QPushButton("Save Profile")
        self.save_profile_btn.clicked.connect(self.save_profile)
        self.reload_ui_btn = QPushButton("Reload UI")
        self.reload_ui_btn.clicked.connect(self.reset_ui)
        self.preview_cmd_btn = QPushButton("Preview Command")
        self.preview_cmd_btn.clicked.connect(self.preview_command)
        clear_log_btn = QPushButton("Clear Log")
        clear_log_btn.clicked.connect(self.log_output.clear)
        self.start_btn = QPushButton("Start Compilation")
        self.start_btn.setStyleSheet("background-color: #4CAF50; color: white; padding: 8px;")
        self.start_btn.clicked.connect(self.start_build)
        
        bottom_buttons_layout.addWidget(self.load_profile_btn)
        bottom_buttons_layout.addWidget(self.save_profile_btn)
        bottom_buttons_layout.addStretch(1)
        bottom_buttons_layout.addWidget(self.reload_ui_btn)
        bottom_buttons_layout.addWidget(self.preview_cmd_btn)
        bottom_buttons_layout.addWidget(clear_log_btn)
        bottom_buttons_layout.addStretch(1)
        bottom_buttons_layout.addWidget(self.start_btn)

        # --- Add all groups to the main layout ---
        main_layout.addWidget(input_group)
        main_layout.addLayout(options_version_layout)
        main_layout.addWidget(additional_group)
        main_layout.addWidget(log_group)
        main_layout.addLayout(bottom_buttons_layout)

    # --- FUNCTIONS FOR FILE & FOLDER SELECTION ---

    def select_script(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Python Script", "", "Python Files (*.py *.pyw)")
        if file_path:
            self.script_input.setText(file_path)
            # Auto-fill output directory if empty
            if not self.output_dir_input.text():
                 self.output_dir_input.setText(os.path.dirname(file_path))

    def select_output_dir(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if dir_path:
            self.output_dir_input.setText(dir_path)

    def select_icon(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Icon", "", "Icon Files (*.ico)")
        if file_path:
            self.icon_input.setText(file_path)
    
    def add_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Add Additional Files", "", "All Files (*)")
        if files:
            for file in files:
                self.files_list.addItem(file)
    
    def add_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Add Additional Folder")
        if folder:
            self.folders_list.addItem(folder)

    def add_module(self):
        module_name, ok = QInputDialog.getText(self, "Add Hidden Module", "Enter module name (e.g., 'PySide6.QtXml'):")
        if ok and module_name:
            self.modules_list.addItem(module_name)
    
    def remove_selected(self, list_widget):
        for item in list_widget.selectedItems():
            list_widget.takeItem(list_widget.row(item))
            
    # --- FUNCTIONS FOR BUILD PROCESS ---
    def get_pyinstaller_command(self):
        """ Build the PyInstaller command list based on UI inputs """
        script_path = self.script_input.text()
        if not script_path:
            self.show_error("Python script not selected!", "Please select a Python script file to compile.")
            return None

        command = ['pyinstaller', '--noconfirm']
        
        # Basic options
        if self.onefile_check.isChecked():
            command.append('--onefile')
        if self.noconsole_check.isChecked():
            command.append('--windowed') # or --noconsole
        
        # Cores
        command.extend(['--nproc', self.cores_combo.currentText()])

        # Icon
        if self.icon_input.text():
            command.extend(['--icon', self.icon_input.text()])
            
        # Output directory
        output_dir = self.output_dir_input.text() or os.path.dirname(script_path)
        command.extend(['--distpath', os.path.join(output_dir, 'dist')])
        command.extend(['--workpath', os.path.join(output_dir, 'build')])
        command.extend(['--specpath', output_dir])

        # Files, Folders, Modules
        for i in range(self.files_list.count()):
            file_path = self.files_list.item(i).text()
            # Format: 'source;destination_folder'
            # We place it in the root (.)
            command.extend(['--add-data', f'{file_path}{os.pathsep}.'])

        for i in range(self.folders_list.count()):
            folder_path = self.folders_list.item(i).text()
            folder_name = os.path.basename(folder_path)
            command.extend(['--add-data', f'{folder_path}{os.pathsep}{folder_name}'])
        
        for i in range(self.modules_list.count()):
            command.extend(['--hidden-import', self.modules_list.item(i).text()])

        # Add the main script at the end
        command.append(script_path)
        
        return command

    def preview_command(self):
        command = self.get_pyinstaller_command()
        if command:
            # Use subprocess.list2cmdline to show an 'executable' command string
            cmd_string = subprocess.list2cmdline(command)
            self.log_output.append("--- PREVIEW COMMAND ---\n" + cmd_string + "\n-----------------------\n")
            self.log_output.moveCursor(QTextCursor.End)

    def start_build(self):
        command = self.get_pyinstaller_command()
        if not command:
            return

        if self.build_thread and self.build_thread.isRunning():
            self.show_error("Build in Progress", "A build is already running. Please wait.")
            return

        self.log_output.clear()
        self.log_output.append("Starting compilation...\n")

        self.build_thread = BuildThread(command)
        self.build_thread.progress.connect(self.update_log)
        self.build_thread.finished.connect(self.build_finished)
        
        self.start_time = time.time()
        self.timer.start(1000) # Update every 1 second
        
        self.build_thread.start()
        self.set_ui_state(enabled=False)

    def update_log(self, text):
        self.log_output.append(text)
        self.log_output.moveCursor(QTextCursor.End)

    def update_elapsed_time(self):
        elapsed = int(time.time() - self.start_time)
        hours, remainder = divmod(elapsed, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.elapsed_time_label.setText(f"Elapsed Time: {hours:02}:{minutes:02}:{seconds:02}")

    def build_finished(self, return_code):
        self.timer.stop()
        self.update_elapsed_time() # Final update
        
        if return_code == 0:
            self.log_output.append("\n--- COMPILATION SUCCESSFUL! ---")
            if self.shutdown_check.isChecked():
                self.close()
        else:
            self.log_output.append("\n--- COMPILATION FAILED! ---")
        
        self.log_output.moveCursor(QTextCursor.End)
        self.set_ui_state(enabled=True)

    def set_ui_state(self, enabled):
        """ Enable/Disable UI controls during the build process """
        self.start_btn.setEnabled(enabled)
        self.preview_cmd_btn.setEnabled(enabled)
        self.load_profile_btn.setEnabled(enabled)
        self.save_profile_btn.setEnabled(enabled)
        self.reload_ui_btn.setEnabled(enabled)

        if enabled:
            self.start_btn.setText("Start Compilation")
            self.start_btn.setStyleSheet("background-color: #4CAF50; color: white; padding: 8px;")
        else:
            self.start_btn.setText("Compiling...")
            self.start_btn.setStyleSheet("background-color: #f44336; color: white; padding: 8px;")

    # --- PROFILE SAVE/LOAD AND UI RESET ---

    def save_profile(self):
        """Saves the current UI configuration to a .mpb file."""
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Profile", "", "Macan Profile Builder (*.mpb)")
        if not file_path:
            return

        profile_data = {
            'script_path': self.script_input.text(),
            'output_dir': self.output_dir_input.text(),
            'icon_path': self.icon_input.text(),
            'one_file': self.onefile_check.isChecked(),
            'no_console': self.noconsole_check.isChecked(),
            'shutdown': self.shutdown_check.isChecked(),
            'cores': self.cores_combo.currentText(),
            'product_name': self.product_name_input.text(),
            'product_version': self.product_version_input.text(),
            'file_version': self.file_version_input.text(),
            'file_description': self.file_description_input.text(),
            'copyright': self.copyright_input.text(),
            'included_files': [self.files_list.item(i).text() for i in range(self.files_list.count())],
            'included_folders': [self.folders_list.item(i).text() for i in range(self.folders_list.count())],
            'included_modules': [self.modules_list.item(i).text() for i in range(self.modules_list.count())],
        }

        try:
            with open(file_path, 'w') as f:
                json.dump(profile_data, f, indent=4)
            self.update_log(f"Profile saved to: {file_path}")
        except Exception as e:
            self.show_error("Save Error", f"Failed to save profile: {e}")

    def load_profile(self):
        """Loads a UI configuration from a .mpb file."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Load Profile", "", "Macan Profile Builder (*.mpb)")
        if not file_path:
            return

        try:
            with open(file_path, 'r') as f:
                profile_data = json.load(f)
        except Exception as e:
            self.show_error("Load Error", f"Failed to load or parse profile file: {e}")
            return

        # Apply the loaded data to the UI
        self.reset_ui() # Clear existing settings first
        self.script_input.setText(profile_data.get('script_path', ''))
        self.output_dir_input.setText(profile_data.get('output_dir', ''))
        self.icon_input.setText(profile_data.get('icon_path', ''))
        self.onefile_check.setChecked(profile_data.get('one_file', False))
        self.noconsole_check.setChecked(profile_data.get('no_console', False))
        self.shutdown_check.setChecked(profile_data.get('shutdown', False))
        self.cores_combo.setCurrentText(profile_data.get('cores', str(os.cpu_count())))
        self.product_name_input.setText(profile_data.get('product_name', ''))
        self.product_version_input.setText(profile_data.get('product_version', ''))
        self.file_version_input.setText(profile_data.get('file_version', ''))
        self.file_description_input.setText(profile_data.get('file_description', ''))
        self.copyright_input.setText(profile_data.get('copyright', ''))
        
        for file in profile_data.get('included_files', []): self.files_list.addItem(file)
        for folder in profile_data.get('included_folders', []): self.folders_list.addItem(folder)
        for module in profile_data.get('included_modules', []): self.modules_list.addItem(module)
        
        self.update_log(f"Profile loaded from: {file_path}")

    def reset_ui(self):
        """Resets all UI fields to their default state."""
        self.script_input.clear()
        self.output_dir_input.clear()
        self.icon_input.clear()
        
        self.onefile_check.setChecked(False)
        self.noconsole_check.setChecked(False)
        self.shutdown_check.setChecked(False)
        
        self.cores_combo.setCurrentText(str(os.cpu_count()))
        
        self.product_name_input.clear()
        self.product_version_input.clear()
        self.file_version_input.clear()
        self.file_description_input.clear()
        self.copyright_input.clear()
        
        self.files_list.clear()
        self.folders_list.clear()
        self.modules_list.clear()
        
        self.update_log("UI has been reset to default values.")

    # --- DIALOG HELPER ---
    def show_error(self, title, message):
        QMessageBox.critical(self, title, message)

    def closeEvent(self, event):
        if self.build_thread and self.build_thread.isRunning():
            reply = QMessageBox.question(self, 'Confirm Exit', 
                                         "A build is currently in progress. Are you sure you want to exit?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                if self.build_thread.process:
                    self.build_thread.process.terminate() # Forcefully stop the subprocess
                self.build_thread.terminate() # Terminate the thread
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()


if __name__ == '__main__':
    # Ensure the icon file exists when the app starts
    create_default_icon()
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())