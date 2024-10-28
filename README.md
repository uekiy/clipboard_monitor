# clipboard_monitor
Clipboard MonitorはPythonのミニアプリです。
クリップボードを監視し、スクリーンショットが格納されると、自動でファイル名を付け選択したフォルダに保存します。
Tkinterを使用したシンプルなGUI。Windows10で動作確認済み。

## Overview
Clipboard Monitor is a Python mini-app that automates the tedious task of saving screenshots. Whenever an image is copied to the clipboard, this app automatically saves it to a selected folder with a unique filename based on the image dimensions and timestamp.

This project is confirmed to work on Windows 10.

## Features
- **Automated Clipboard Monitoring**: Detects images copied to the clipboard and saves them automatically.
- **Custom Save Directory**: Allows users to select their preferred folder for saving images.
- **Unique Filenames**: Filenames are generated based on image dimensions and timestamp (e.g., `1920x1080_20241028_153000.png`).
- **User-Friendly GUI**: Built with Tkinter, the GUI allows easy ON/OFF monitoring control and save directory selection.

## Installation
1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd clipboard_monitor
   ```

2. **Install Dependencies**
   - Ensure you have Python 3 installed.
   - Install the required libraries by running:
     ```bash
     pip install -r requirements.txt
     ```

## Usage
1. **Run the App**
   ```bash
   python clipboard_monitor.py
   ```
2. **Select Save Directory**: Choose where to save the screenshots using the provided GUI button.
3. **Start Monitoring**: Click "Start Monitoring" to begin saving images from the clipboard automatically.

## Dependencies
- **Python 3**
- **Tkinter**: For GUI development
- **Pillow (PIL)**: For handling images

## How It Works
1. **Clipboard Monitoring**: The app continually monitors the clipboard for new images.
2. **Save Directory Selection**: Users can freely select a folder to save images.
3. **Image Saving**: When a new image is detected, it is saved with a unique filename that includes the dimensions and timestamp.

## Example
- Copy a screenshot or image to your clipboard.
- The app will detect the new image and automatically save it as, for example, `1920x1080_20241028_153000.png` in your chosen directory.

## Customization
Feel free to modify the code to suit your specific needs. The code is designed to be easy to understand and modify for Python beginners.

## License
This project is open-source and available under the MIT License.

## Contributions
Contributions are welcome! Feel free to submit a pull request or open an issue for any feature requests or bugs.

## Contact
For questions or support, please open an issue in the repository or contact me directly.

---
This README provides a comprehensive guide to understand and use the Clipboard Monitor app. If you have any suggestions or improvements, feel free to contribute!

