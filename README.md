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
📝 Changelog v3.2.0
* Added features

1. Full Menu Bar

File Menu:

New / Reset (Ctrl+N)
Save Profile (Ctrl+S)
Load Profile (Ctrl+O)
Recent Files (submenu)
Clear Recent Files
Exit (Alt+F4)

Help Menu:

Help Content
Register .mpb Format
About

2. Recent Files

Saves up to the last 10 profile files
Keyboard shortcuts Ctrl+1 to Ctrl+9
Auto-update when saving/loading a profile
Double-click a .mpb file to load it immediately

3. System Monitor (Status Bar)

Displays CPU usage with a bar indicator
Displays RAM usage with a bar indicator
System information (OS, version, architecture)
Real-time updates every 1 second
Red color for CPU > 85%

4. Registry Integration

Register the .mpb file extension in Windows
Double-clicking an .mpb file opens the application directly
Icon association for .mpb files

5. Improved Layout

Menu bar at the top
Main content in the center
Status bar at the bottom
Splitter still works properly

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
