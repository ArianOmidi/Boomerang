from boomerang import Boomerang

if __name__ == '__main__':
    # Modifiers
    create_frames = True
    output_fps = 30
    loop = 4

    # Video Input
    path = "/Users/arianomidi/Dropbox/Personal/Code/Python/Projects/Boomerang/resources/videos/"
    filename = "santorini"
    extension = '.mp4'

    # Output
    out_path = "/Users/arianomidi/Dropbox/Personal/Code/Python/Projects/Boomerang/resources/boomerangs/"
    output_name = filename + "_boomerang"

    boomerang = Boomerang(path, filename, out_path, output_fps, output_name, extension, create_frames, loop)
    boomerang.run()