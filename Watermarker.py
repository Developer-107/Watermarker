from PIL import Image

# This is project is made for method testing.
# This project can be enhanced in many ways.


# Background image example.
img = Image.open("../Watermarker/ImageForTheLearning.jpg")

# Watermark example.
watermark = Image.open("../Watermarker/PngForTestPic.png")

# Copy and resize watermark image.
watermark_image = watermark.copy()
watermark_image = watermark_image.convert("RGBA")
watermark_image = watermark_image.resize(size=(img.width // 7,img.height // 7))

# Copy of background image.
img_copy = img.copy()

# Put watermark on image.
img_copy.paste(watermark_image, (500, 200), watermark_image)

# Show result.
img_copy.show()