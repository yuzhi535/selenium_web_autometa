import os
import shutil
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QFileDialog,
    QShortcut,
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QKeySequence


class ImagePreviewThread(QThread):
    image_loaded = pyqtSignal(QPixmap)

    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path

    def run(self):
        pixmap = QPixmap(self.image_path)
        self.image_loaded.emit(pixmap)


class Imagecopyer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.image_folder = None
        self.image_files = []
        self.current_image_index = 0
        self.scale_factor = 1.0

    def initUI(self):
        self.setWindowTitle("图片预览和复制")
        
        self.last_pic_path=[]
        self.parent_folder=None

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.folder_button = QPushButton("选择文件夹", self)
        self.folder_button.clicked.connect(self.select_folder)

        self.prev_button = QPushButton("上一张", self)
        self.prev_button.clicked.connect(self.show_previous_image)
        self.prev_button.setShortcut("j")

        self.next_button = QPushButton("下一张", self)
        self.next_button.clicked.connect(self.show_next_image)
        self.next_button.setShortcut("k")
        
        self.delete_button = QPushButton("删除", self)
        self.delete_button.clicked.connect(self.delete_image)
        self.delete_button.setShortcut("d")

        self.zoom_in_button = QPushButton("放大", self)
        self.zoom_in_button.clicked.connect(self.zoom_in)

        self.zoom_out_button = QPushButton("缩小", self)
        self.zoom_out_button.clicked.connect(self.zoom_out)

        self.parent_path = QLineEdit(self)
        self.parent_path.setPlaceholderText("目标文件夹的父文件夹")
        self.parent_path.setReadOnly(True)

        self.copy_button = QPushButton("选择目标文件夹的父文件夹", self)
        self.copy_button.clicked.connect(self.make_parent)
        self.copy_button.setShortcut('Enter')
        
        self.undo_button = QPushButton("撤销", self)
        self.undo_button.clicked.connect(self.undo)
        self.undo_button.setShortcut('3')

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.folder_button)
        hbox1.addWidget(self.prev_button)
        hbox1.addWidget(self.next_button)
        hbox1.addWidget(self.zoom_in_button)
        hbox1.addWidget(self.zoom_out_button)
        hbox1.addWidget(self.delete_button)
        hbox1.addWidget(self.undo_button)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.parent_path)
        hbox2.addWidget(self.copy_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)
        
         # 设置快捷键
        self.shortcut_1 = QShortcut(QKeySequence("1"), self)
        self.shortcut_1.activated.connect(lambda: self.move_image("1"))
        self.shortcut_2 = QShortcut(QKeySequence("2"), self)
        self.shortcut_2.activated.connect(lambda: self.move_image("2"))
    
    def make_parent(self):
        folder_path = QFileDialog.getExistingDirectory(self, "选择目标父文件夹")
        self.parent_folder = folder_path
        self.parent_path.setText(self.parent_folder)


    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "选择图片文件夹")
        if folder_path:
            self.image_folder = folder_path
            self.image_files = [
                f
                for f in os.listdir(folder_path)
                if os.path.isfile(os.path.join(folder_path, f))
                and f.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp"))
            ]
            self.current_image_index = 0
            self.load_current_image()
            
    def undo(self):
        self.current_image_index-=1
        os.remove(self.last_pic_path[-1])
        self.last_pic_path.pop()
        print(f'undo！ {self.current_image_index+1}/{len(self.image_files)}')
        self.load_current_image()

    def load_current_image(self):
        if self.image_files:
            image_path = os.path.join(
                self.image_folder, self.image_files[self.current_image_index]
            )
            self.preview_thread = ImagePreviewThread(image_path)
            self.preview_thread.image_loaded.connect(self.update_image)
            self.preview_thread.start()

    def delete_image(self, ):
        current_image_path = os.path.join(
            self.image_folder, self.image_files[self.current_image_index]
        )
        if self.current_image_index < len(os.listdir(self.image_folder)):
            self.image_files.pop(self.current_image_index)
            os.remove(current_image_path)
            # self.current_image_index+=1
            self.load_current_image()
            print(f'delete! {self.current_image_index+1}/{len(self.image_files)}')
        else:
            print('最后一张图片已被删除')  # 只过一轮得了
    
    def update_image(self, pixmap):
        self.original_pixmap = pixmap  # 保存原始大小的pixmap
        self.scaled_pixmap = self.original_pixmap.scaled(
            self.original_pixmap.size() * self.scale_factor,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation,
        )
        self.image_label.setPixmap(self.scaled_pixmap)

    def show_previous_image(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.load_current_image()
        print(f'previous! {self.current_image_index+1}/{len(self.image_files)}')

    def show_next_image(self):
        if self.current_image_index < len(self.image_files) - 1:
            self.current_image_index += 1
            self.load_current_image()
        print(f'next! {self.current_image_index+1}/{len(self.image_files)}')

    def move_image(self, target_folder_num='none'):
        if not self.image_folder or not self.image_files:
            return

        # 获取要处理图片文件夹的父目录
        if self.parent_folder == '':
            parent_folder = os.path.dirname(self.image_folder)
        else:
            parent_folder = self.parent_folder
        target_folder = os.path.join(parent_folder, target_folder_num)

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        current_image_path = os.path.join(
            self.image_folder, self.image_files[self.current_image_index]
        )
        try:
            shutil.copy(current_image_path, target_folder)
            self.last_pic_path.append(os.path.join(target_folder, current_image_path.split('\\')[-1]))
            print(f"{self.current_image_index+1}/{len(self.image_files)}: 已将图片{current_image_path}复制到: {target_folder}")
            if self.current_image_index >= len(self.image_files):
                self.current_image_index -= 1
            self.current_image_index += 1
            self.parent_path.clear()
            self.load_current_image()
        except IndexError:
            print('最后一张图片了！')
            
        except Exception as e:
            print(f"复制图片失败: {e}")

    def zoom_in(self):
        self.scale_factor *= 1.2
        self.update_image(self.original_pixmap)

    def zoom_out(self):
        self.scale_factor /= 1.2
        self.update_image(self.original_pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Imagecopyer()
    ex.resize(800, 600)
    ex.show()
    sys.exit(app.exec_())
