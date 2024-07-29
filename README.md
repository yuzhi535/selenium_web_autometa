## Image preview and classification tool

This is a graphical interface tool based on PyQt5, which is used to quickly preview and classify images.

### Design intention

My original intention of writing this tool was to **quickly** annotate and classify images, so **keyboard** operation is essential, and the mouse will only slow down the speed. Furthermore, only one key is needed to perform the corresponding operation. So, how should I display the results of the operation? I output it to the terminal, because other forms of display on the GUI will either interfere with the annotation speed or interfere with concentration. Generally, it is enough to go through the image once. If you think of a previous mistake, you can use the undo key to return to the previous step. I also designed a shortcut key for it (3).

### Function

- **Image preview**: Browse the images in the folder, support previous, next, zoom in, zoom out and other operations.
- **Shortcut keys**: Use the `j` and `k` keys to quickly switch images, and use the `Enter` key to confirm the copy operation.
- **Image Classification**: Copy the current image to the specified destination folder by entering the number keys (1, 2...). The destination folder is located in the parent directory of the image source folder and is named with a number.

### How to use

1. **Select Folder**: Click the "Select Folder" button to select the folder containing the images to be processed.
2. **Preview Image**: Use the "Previous", "Next", "Zoom In", "Zoom Out" buttons or the `j`, `k` shortcut keys to browse the images.
3. **Copy Image**:
- Enter the number of the destination folder in the input box (for example, enter "1" to copy to the folder named "1").
- Press the `Enter` key or click the "Copy" button to copy the current image to the destination folder and automatically switch to the next image.
- You can also directly press the number keys (1, 2...) to quickly copy the image to the corresponding folder.

### Example

Assume that you have a folder named "Photos" which contains the pictures you want to classify. The folder is located in the "D:\MyPictures" directory.

1. Run the program, click the "Select Folder" button, and select the "D:\MyPictures\Photos" folder.
2. The program will display the first picture in the "Photos" folder.
3. Preview the picture and zoom in or out as needed.
4. If you want to copy the current picture to the "D:\MyPictures\1" folder, you can directly press the number key `1`, or enter "1" in the input box and press the `Enter` key.
5. The program will copy the current picture to the "D:\MyPictures\1" folder and automatically load the next picture.


### Install dependencies

```bash
pip install -e .
```

### Run the program

```bash
python src/selenium_web_autometa/main.py
```

### Notes

- The target folder will be created automatically, no need to create it manually.
- The program will **copy** the image to the target folder, and will not delete the original image.


## License

[MIT](https://choosealicense.com/licenses/mit/)