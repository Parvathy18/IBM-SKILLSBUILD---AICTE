from PIL import Image
import numpy as np

def encode_message(image_path, message, output_path):
    img = Image.open("scenery.png")
    img_array = np.array(img)
    message += "###"
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    flat_pixels = img_array.flatten()
    if len(binary_message) > len(flat_pixels):
        raise ValueError("Message too large to hide in image")
    for i in range(len(binary_message)):
        flat_pixels[i] = (flat_pixels[i] & ~1) | int(binary_message[i])
    new_img_array = flat_pixels.reshape(img_array.shape)
    encoded_img = Image.fromarray(new_img_array.astype(np.uint8))
    encoded_img.save(output_path)
    print(f"Message successfully hidden in {output_path}")

def decode_message(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    flat_pixels = img_array.flatten()
    binary_message = "".join(str(flat_pixels[i] & 1) for i in range(len(flat_pixels)))
    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        if message.endswith("###"):
            return message[:-3]
        message += char
    return "Message not found"


choice = input("Do you want to (1) Encode a message or (2) Decode a message? Enter 1 or 2: ")
if choice == "1":
    image_path = input("Enter the input image filename (with extension): ")
    message = input("Enter the secret message: ")
    output_path = input("Enter the output image filename (with extension): ")
    encode_message(image_path, message, output_path)
elif choice == "2":
    image_path = input("Enter the encoded image filename (with extension): ")
    print("Hidden Message:", decode_message(image_path))
else:
    print("Invalid choice. Please enter 1 or 2.")
