import os
import sys
import random
from pdf2image import convert_from_path
from PIL import Image, ImageEnhance, ImageFilter


def generate_color_scanned_pdf(input_path, output_path, dpi=150):

    if not os.path.exists(input_path):
        print(f"Error: could not find {input_path}")
        return

    print(f"[+] Opening PDF document {input_path} (DPI: {dpi})...")
    pages = convert_from_path(input_path, dpi=dpi)

    scanned_pages = []

    for i, page in enumerate(pages):
        print(f"[>] Page {i+1}/{len(pages)} in progress...")

        # color mode
        img = page.convert('RGB')

        # slight curvature (optional)
        angle = random.uniform(-0.4, 0.4)
        img = img.rotate(angle, resample=Image.BICUBIC,
                         expand=False, fillcolor=(255, 255, 255))

        # contrast & brightness optimization
        # a value between 1.2 and 1.4 is OK for color enhancement
        img = ImageEnhance.Contrast(img).enhance(1.3)
        img = ImageEnhance.Brightness(img).enhance(1.02)

        # saturation optimization for ink-based annotations
        img = ImageEnhance.Color(img).enhance(1.15)

        # scanning blur effect (optional but recommended)
        img = img.filter(ImageFilter.GaussianBlur(radius=0.3))
        img = ImageEnhance.Contrast(img).enhance(1.1)

        scanned_pages.append(img)

    print("[+] Merging processed pages...")
    if scanned_pages:
        scanned_pages[0].save(
            output_path,
            save_all=True,
            append_images=scanned_pages[1:])
        print(f"[✓] Completed: {output_path}")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage:")
        print("python scan.py [input_filename].pdf")
        print("python scan.py [input_filename].pdf -o [output_filename].pdf")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = "output.pdf"

    if len(sys.argv) >= 4 and sys.argv[2] == '-o':
        output_pdf = sys.argv[3]

    generate_color_scanned_pdf(input_pdf, output_pdf)
