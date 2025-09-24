# stitch.py
import cv2, glob

imgs = [cv2.imread(f) for f in sorted(glob.glob("map_*.jpg"))]
stitcher = cv2.Stitcher_create()
status, pano = stitcher.stitch(imgs)

if status == cv2.Stitcher_OK:
    cv2.imwrite("panorama.jpg", pano)
    print("✅ Panorama saved as panorama.jpg")
else:
    print("❌ Stitch failed, status:", status)
