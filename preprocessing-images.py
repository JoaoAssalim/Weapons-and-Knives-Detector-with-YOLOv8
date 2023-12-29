import os
import cv2
import pywt

def apply_wavelet_transform(image):
    coeffs2 = pywt.dwt2(image, 'bior1.3')
    LL, (LH, HL, HH) = coeffs2
    return LH

def process_images_in_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        original = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
        horizontal_detail = apply_wavelet_transform(original)
        output_path = os.path.join(output_folder, image_file)
        cv2.imwrite(output_path, horizontal_detail)
        print(f"Detalhe horizontal da transformada wavelet salvo em {output_path}")


input_folder = "./model/train/images"
output_folder = "./model/train/images"
process_images_in_folder(input_folder, output_folder)
