import os
import cv2
import pywt
import numpy as np

def apply_symlet_transform(image):
    coeffs2 = pywt.dwt2(image, 'sym2')
    LL, (LH, HL, HH) = coeffs2
    return LH

def apply_daubechies_transform(image):
    coeffs2 = pywt.dwt2(image, 'db2')
    LL, (LH, HL, HH) = coeffs2
    return LH

def apply_haar_transform(image):
    coeffs2 = pywt.dwt2(image, 'haar')
    LL, (LH, HL, HH) = coeffs2
    return LH

def enhance_contrast(image):
    normalized_image = ((image - np.min(image)) / (np.max(image) - np.min(image))) * 255
    return normalized_image.astype(np.uint8)

def process_images_in_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        original = cv2.imread(input_path)
        horizontal_detail = apply_haar_transform(original)
        horizontal_detail = enhance_contrast(horizontal_detail)
        horizontal_detail = cv2.resize(horizontal_detail, (640, 640))

        output_path = os.path.join(output_folder, f'{image_file}')
        cv2.imwrite(output_path, original, [int(cv2.IMWRITE_JPEG_QUALITY), 20])
        print(f"Detalhe horizontal da transformada wavelet salvo em {output_path}")

#input_folder = "./assets/Tes"
input_folder = "./imgs/Normal/Test/images"
output_folder = "./imgs/Haar_Compressed/Test/images"
process_images_in_folder(input_folder, output_folder)
