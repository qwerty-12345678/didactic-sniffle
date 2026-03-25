from pic_to_ascii import AsciiConverter
from vid_to_ascii import VideoAsciiConverter

def pic_ascii(new_width=100):
    image = input("Enter image path: ")
    converter = AsciiConverter(image)
    converter.to_grayscale() # Convert image to grayscale
    converter.resize(new_width) # Resize image, with new_width as the paramete
    ascii_art = converter.pixels_to_ascii() # Conversion of image to ascii art

    # Output art using text file 
    with open('output.txt', 'w') as f:
        f.write(ascii_art)

    print("Image converted to ascii art!")


def vid_ascii(): 
    source = input("Enter video path: ")
    converter = VideoAsciiConverter(source) 
    converter.read_frames() # Reads and converts frames to grayscale for ascii conversion
    converter.play_ascii() # Plays the converted ascii frames in the terminal
    
    print("Video has been succesfully played!")


pic_ascii()
vid_ascii()