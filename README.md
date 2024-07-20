## Image Preview and Sorting Tool

This is a PyQt5-based graphical tool for quickly previewing and sorting images into different folders.

### Features

- **Image preview**: Browse through images in a folder, with support for next/previous image, zoom in/out, etc.
- **Keyboard shortcuts**: Use `j` and `k` keys to quickly switch between images, and `Enter` to confirm the copying operation.
- **Image sorting**:  Copy the currently viewed image to a specific target folder by pressing the corresponding number key (1, 2...). Target folders are named with numbers and located in the parent directory of the source image folder.

### How to Use

1. **Select Folder**: Click the "Choose Folder" button and select the folder containing the images you want to process.
2. **Enter Target Parent Folder**: edit the bottem text line and enter the desired target parent folder. __if you don't edit this, the parent folder is the chosed folder's parent folder__. 
3. **Preview Images**: Use the "Previous", "Next", "Zoom In", and "Zoom Out" buttons or the `j` and `k` keys to navigate through the images.
4. **Copy Images**:
    - Enter the number of the target folder in the input field (e.g., enter "1" to copy to a folder named "1").
    - Press the `Enter` key or click the "Copy" button to copy the current image to the target folder and automatically load the next image.
    - You can also directly press the number keys (1, 2...) to quickly copy the image to the corresponding folders.

### Example

Suppose you have a folder named "Photos" containing the images you want to sort, and this folder is located in the directory "D:\MyPictures".

1. Run the program and click the "Choose Folder" button. Select the "D:\MyPictures\Photos" folder.
2. The program will display the first image in the "Photos" folder.
3. Preview the image and zoom in or out as needed.
4. If you want to copy the current image to the "D:\MyPictures\1" folder, you can directly press the number key `1`, or enter "1" in the input field and press `Enter`.
5. The program will copy the current image to the "D:\MyPictures\1" folder and automatically load the next image.

### Requirements

- Python 3.x
- PyQt5
- os
- shutil

### Installation

```bash
pip install PyQt5
```

### Running the Program

```bash
python main.py
```

### Notes

- The target folders will be created automatically if they do not exist.
- The program will **copy** the images to the target folders, the original images will not be deleted.

## License

[MIT](https://choosealicense.com/licenses/mit/)
