# 🐍 Python Builder by Danx

Python Builder is a PySide6-based GUI application designed to simplify the process of compiling .py files into .exe executables using PyInstaller.

It is designed with a focus on automation, portability, and Windows version metadata integration, as well as support for automatic ZIP deployment.

---

## 🚀 Key Features

- ✅ Intuitive GUI interface for building Python executables.
- ⚙️ Full support for PyInstaller options such as:
- One-File Mode (--onefile)
- Disable Console (--windowed)
- Custom Icon (--icon)
- 🏷️ Automatic Windows version metadata generator (Company, Product, File Version, etc.).

- 📦 **Automatic ZIP Deployment** using LZMA compression.
- 💾 **Profile (.mpb)** system for saving and loading build configurations.
- 🧩 Support for including:
- Additional files
- Additional folders
- Hidden modules (hidden imports)
- 🧠 Real-time log and build time indicator.
- 🧰 *Preview Command* button to see the PyInstaller command that will be executed.

---

## 🖼️ Interface Appearance
The application uses a **QGroupBox**-based layout with a modular setup:
- **Input / Output Section**
Select the Python file and output directory.
- **Compilation Options & Version Info**
Specify the build mode, number of cores, and Windows version metadata.
- **Additional Files & Modules**
Add additional files, folders, or modules to the build.
- **Compilation Log**
Displays the compilation results and progress in real-time.

---
📝 Changelog v3.4.0
## Fixed
- Profile Save Logic: Resolved an issue where saving an existing profile would trigger a "Save As" dialog. The application now correctly overwrites the currently active profile while preserving the file path.
- UI Reset State: Fixed a bug where the active file path was not cleared after a "New/Reset" action, ensuring subsequent saves correctly prompt for a new filename.

## Added
- Active Profile Tracking: Implemented a state management system to track the currently loaded .mpb file. The file name is now dynamically displayed in the window title for better user context.
- Persistent Directory Memory: Integrated QSettings to remember the "Last Known Location." File dialogs for scripts, icons, and profiles will now automatically open in the last used directory, significantly improving workflow efficiency.
- Explicit "Save As" Command: Added a "Save Profile As..." option to the File menu and assigned the standard Ctrl+Shift+S shortcut for greater flexibility.
- Enhanced Menu Navigation: Updated the MenuHandler to support the new saving workflow and improved integration with the Recent Files list.
- 
## Improved
- File I/O Modularization: Refactored the internal saving mechanism into a dedicated private method to ensure consistency between "Save" and "Save As" operations.
- User Feedback: Enhanced status log messages to provide clearer confirmation when a profile is successfully updated or loaded.

---

📸 Screenshot
<img width="1365" height="767" alt="Screenshot 2025-12-14 222110" src="https://github.com/user-attachments/assets/0bf3be08-92fe-43e7-b72a-3906c895fe16" />




---

## 🧩 Dependencies

Ensure the following dependencies are installed:

```bash
pip install PySide6 pyinstaller

## 🧠 Internal Architecture
This application utilizes:
QThread to run the PyInstaller process to prevent UI freezes.
QTimer to calculate build times.
zipfile.ZipFile with ZIP_LZMA mode for automated deployment.
QFileDialog, QInputDialog, and QListWidget for dynamic build configuration.
JSON serialization (.mbp) for storing configuration profiles.

## 🧾 License
Developed by Danx
Part of the Macan Angkasa Engineering ecosystem.
License: MIT License

## 💡 Note
“Understanding the structure before transforming it is a key principle in any responsible build process.”
— Danx, Macan Angkasa Engineering Manifesto

## 🔗 Contact & Contributions
Contributions are open for further development.
Report bugs, submit pull requests, or contact the Macan Angkasa team for collaboration.
