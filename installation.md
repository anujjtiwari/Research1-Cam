# 📸 Photobooth Setup Guide (Raspberry Pi)

This guide explains how to set up the Photobooth app with **Raspberry Pi Camera Module 3** using **Picamera2**, **Tkinter**, and **OpenCV**.

---

## 1. Update System

Keep your Raspberry Pi up to date before installing packages.

```bash
sudo apt update && sudo apt upgrade -y
2. Install System Packages
These packages provide camera support, image processing, GUI tools, and dependencies.

bash
Copy code
sudo apt install -y \
  python3-opencv \
  python3-pil \
  python3-numpy \
  python3-pyqt5 \
  python3-simplejpeg \
  python3-tk \
  python3-pip \
  libatlas-base-dev \
  libjpeg-dev \
  libcamera-dev \
  libopenjp2-7-dev \
  v4l-utils
3. Create Virtual Environment
We’ll use a virtual environment with access to system packages.

bash
Copy code
cd ~/pbooth_updated
python3 -m venv --system-site-packages venv
source venv/bin/activate
4. Upgrade pip Inside Venv
Always update pip inside the venv to avoid compatibility issues.

bash
Copy code
pip install --upgrade pip
5. Install Extra Python Packages (Venv Only)
⚠️ Do not install numpy or simplejpeg here – they are already provided by system packages.

Install only the missing extras:

bash
Copy code
pip install pillow opencv-python
