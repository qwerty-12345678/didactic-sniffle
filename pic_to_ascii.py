from PIL import Image

class AsciiConverter:
    ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZ0QLCJUYXzcvunxrjft/\\|1?-_+~<>i!lI;:,. "

    def __init__(self, source):
        if isinstance(source, str):
            self.image = Image.open(source)

        elif isinstance(source, Image.Image):
            self.image = source
        else:
            raise TypeError("source must be a file path or a PIL Image")

    def to_grayscale(self):
        self.image = self.image.convert('L')

    def resize(self, new_width=100):
        width, height = self.image.size
        aspect_ratio = height / width
        new_height = int(aspect_ratio * new_width * 0.55)
        self.image = self.image.resize((new_width, new_height))

    def pixels_to_ascii(self):
        pixels = self.image.getdata()
        ascii_str = ""
        width = self.image.width

        for i, pixel in enumerate(pixels):
            index = pixel * (len(self.ASCII_CHARS) - 1) // 255
            ascii_str += self.ASCII_CHARS[index]
            if (i+1) % width == 0:
                ascii_str += '\n'
        
        return ascii_str