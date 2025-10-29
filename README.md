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
📝 Changelog v2.7.0
Fixed
- UI Freezing During ZIP Deployment: Resolved a major bug where the application UI would freeze or become unresponsive ("Not Responding") when the "Deploy (.zip) using LZMA" option was enabled.
- The ZIP compression process, which is CPU-intensive, was previously running on the main UI thread. This process has now been moved to a dedicated background worker thread (ZipThread).
- The application now remains fully responsive during the zipping phase, similar to how it handles the PyInstaller build process.
- The "Start Compilation" button state is now updated correctly to "Zipping..." during this phase.
- The closeEvent handler has been improved to also prevent the application from closing while a ZIP process is active, ensuring data integrity.

---

📸 Screenshot
<img width="1016" height="684" alt="Screenshot 2025-10-29 235239" src="https://github.com/user-attachments/assets/66489d6d-9b94-4097-8778-b37ab64213f5" />
<img width="1017" height="683" alt="Screenshot 2025-10-29 235941" src="https://github.com/user-attachments/assets/85a3c02d-1e9c-465f-99db-dcf43fc18b80" />



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
