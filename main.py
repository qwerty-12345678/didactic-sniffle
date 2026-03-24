from vid_to_ascii import VideoAsciiConverter

source = input("Enter video path: ")
converter = VideoAsciiConverter(source)
converter.read_frames()
converter.play_ascii()

