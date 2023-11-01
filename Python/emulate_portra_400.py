import argparse
import cv2

def emulate_portra_400(input_image_path, output_image_path):
    try:
        # Load the input image
        image = cv2.imread(input_image_path)

        if image is None:
            print("Error: Could not open or read the image.")
            return

        # Apply Portra 400 emulation
        # Adjustments you can fine-tune further
        brightness = 10
        contrast = 10
        saturation = -10

        image = cv2.convertScaleAbs(image, alpha=1 + contrast / 100, beta=brightness)
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        s = hsv[:, :, 1] * (1 + saturation / 100)
        s = s.clip(0, 255)
        hsv[:, :, 1] = s
        image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        # Save the processed image
        cv2.imwrite(output_image_path, image)
        print(f"Portra 400 emulation applied to {output_image_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Emulate Portra 400 film look on an image.")
    parser.add_argument("input_image", help="Input image file (JPEG format)")
    parser.add_argument("output_image", help="Output image file (JPEG format)")
    args = parser.parse_args()

    emulate_portra_400(args.input_image, args.output_image)

