# IBM-SKILLSBUILD---AICTE

**Image Steganography using LSB (Least Significant Bit) Method**

**📌 Project Description**

This project implements image steganography using the Least Significant Bit (LSB) technique to securely hide and extract messages within images. It allows users to embed secret messages inside images without visible changes and retrieve them when needed. The tool is simple, efficient, and ensures covert communication.

**🚀 Features**

>>**Hide Secret Messages:** Encode text within an image using LSB manipulation.
>>**Extract Hidden Messages:** Retrieve hidden data from the encoded image.
>>**User-Friendly:** Takes user inputs dynamically for easy encoding and decoding.
>>**Supports PNG Format:** Works best with PNG images to avoid data loss due to compression.

**🛠️ Technologies Used**

>>**Python** – Main programming language.
>>**Pillow (PIL)** – For image processing.
>>**NumPy** – For efficient pixel manipulation.

**📥 Installation**

Ensure you have Python installed, then install the required dependencies:
<<pip install pillow numpy>>

**📌 Usage**

Run the script and follow the prompts to encode or decode a message.

>python stegno.py
_____________________________________________________________________
**Encoding a Message**
>Provide the input image filename (e.g., scenery.png).
>Enter the secret message to be hidden.
>Provide the output image filename (e.g., img.png).
>The message will be embedded, and the encoded image will be saved.
_____________________________________________________________________
**Decoding a Message**
>Enter the encoded image filename (e.g., encoded.png).
>The hidden message will be extracted and displayed.

**⚠️ Notes**

>>PNG images are recommended to prevent data loss.
>>If using a JPEG image, convert it to PNG before encoding.
>>Ensure the image has enough pixels to store the message.

**📌 Future Enhancements**

>>Encryption Integration for added security.
>>Steganalysis Resistance to evade detection.
>>GUI Implementation for better user experience.


**🤝 Contributing**

Feel free to fork the repository, improve the code, and submit a pull request!


🔥 Developed for secure data hiding and covert communication! 🔥
