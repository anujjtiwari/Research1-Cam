Photobooth Setup Guide (Raspberry Pi)

This guide explains how to set up the photobooth app with Raspberry Pi Camera Module 3 using Picamera2, Tkinter, and OpenCV.

1. Update System
sudo apt update && sudo apt upgrade -y

2. Install System Packages (needed for camera + numpy + simplejpeg)
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

3. Create Virtual Environment (with access to system packages)
cd ~/pbooth_updated
python3 -m venv --system-site-packages venv
source venv/bin/activate

4. Upgrade pip inside venv
pip install --upgrade pip

5. Install Extra Python Packages (in venv only)

⚠️ Don’t install numpy or simplejpeg here (they come from system packages).

pip install pillow opencv-python tk
