import time
import cv2
from picamera2 import Picamera2

class DummyPreview:
    def __init__(self):
        self.fullscreen = False
        self.window = (0, 0, 640, 480)
        self.annotate_text = ""


class Camera:
    """
    Wrapper for PiCamera2 to mimic PiCamera API
    Compatible with Raspberry Pi Camera Module 3
    """

    def __init__(self):
        self.picam2 = Picamera2()

        # Preview (fast, ISP processed, natural colours)
        self.preview_config = self.picam2.create_preview_configuration(
            main={"size": (1280, 720), "format": "RGB888"}
        )

        # Still (HQ photo capture)
        self.still_config = self.picam2.create_still_configuration(
            main={"size": (2304, 1296), "format": "RGB888"}
        )

        # Start with preview
        self.picam2.configure(self.preview_config)
        self.picam2.start()

        # Enable auto controls
        self.picam2.set_controls({
            "AwbEnable": True,
            "AeEnable": True,
        })

        self.preview = DummyPreview()
        self.previewing = True

    def start_preview(self):
        if not self.previewing:
            self.picam2.configure(self.preview_config)
            self.picam2.start()
            self.previewing = True

    def stop_preview(self):
        if self.previewing:
            self.picam2.stop()
            self.previewing = False

    def get_frame(self):
        """Return current preview frame (natural colours)."""
        return self.picam2.capture_array("main")

    def capture(self, filename, resize=None):
        """Capture HQ still image with ISP processing."""
        self.picam2.switch_mode_and_capture_file(self.still_config, filename)
        # Switch back to preview
        self.picam2.configure(self.preview_config)
        self.picam2.start()

    def close(self):
        self.picam2.stop()


# Alias for compatibility
PiCamera = Camera


# ---------------- STANDALONE TEST ----------------
if __name__ == "__main__":
    cam = Camera()
    print("? Live preview. Press 'c' to capture, 'q' to quit.")
    while True:
        frame = cam.get_frame()
        cv2.imshow("Test Preview", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("c"):
            cam.capture("snapshot.jpg")
            print("?? Saved snapshot.jpg")
        elif key == ord("q"):
            break
    cam.close()
    cv2.destroyAllWindows()
