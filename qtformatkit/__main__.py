import os
import sys
from PySide6 import QtCore
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QPushButton,
    QLabel,
    QApplication,
    QListWidget,
    QPlainTextEdit,
    QHBoxLayout,
)

pkg_dir = os.path.split(os.path.realpath(__file__))[0]


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("qtformatkit")

        self.setWindowIcon(QIcon(os.path.join(pkg_dir, "icons", "update.png")))

        self.original = [
            "Элемент 0",
            "Элемент 1",
            "Элемент 2",
            "Элемент 3",
            "Элемент 4",
            "Элемент 5",
            "Элемент 6",
            "Элемент 7",
            "Элемент 8",
        ]

        self.final = [
            "Элемент 0",
            "Элемент 1",
            "Элемент 2",
            "Элемент 3",
            "Элемент 4",
            "Элемент 5",
            "Элемент 6",
            "Элемент 7",
            "Элемент 8",
        ]

        # Создаем список элементов
        self.list_widget_original = QListWidget()
        self.list_widget_original.addItems(self.original)

        self.list_widget_final = QListWidget()
        self.list_widget_final.addItems(self.final)

        self.label_original = QLabel(f"Исходный: {self.get_text_original()}")
        self.label_final = QLabel(f"Результирующий: {self.get_text_final()}")
        # self.label.setFont(QFont("Arial", 12))

        # Создаем и размещаем кнопки
        self.up_button_original = QPushButton("Вверх")
        self.up_button_original.clicked.connect(self.up_item_original)

        self.up_button_final = QPushButton("Вверх")
        self.up_button_final.clicked.connect(self.up_item_final)

        self.down_button_original = QPushButton("Вниз")
        self.down_button_original.clicked.connect(self.down_item_original)

        self.down_button_final = QPushButton("Вниз")
        self.down_button_final.clicked.connect(self.down_item_final)

        self.result_button = QPushButton("Выполнить")
        self.result_button.clicked.connect(self.get_result)

        # palette = self.result_button.palette()
        # palette.setColor(QPalette.ColorRole.Button, QColor(255, 255, 255))
        # self.result_button.setPalette(palette)
        self.result_button.setStyleSheet("background-color: green;")
        self.result_button.setFont(QFont("Arial", 12, QFont.Weight.Bold))

        # Создаем вертикальный бок
        layoutV = QVBoxLayout()

        layoutV.addWidget(self.label_original)
        layoutV.addWidget(self.label_final)

        # Создаем горизонтальный бок
        layoutH = QHBoxLayout()

        # Создаем вертикальный бок
        layoutV1 = QVBoxLayout()
        layoutV1.addWidget(self.list_widget_original)
        layoutV1.addWidget(self.up_button_original)
        layoutV1.addWidget(self.down_button_original)
        # layoutV1.addWidget(self.result_button)
        layoutH.addLayout(layoutV1)

        layoutV2 = QVBoxLayout()
        layoutV2.addWidget(self.list_widget_final)
        layoutV2.addWidget(self.up_button_final)
        layoutV2.addWidget(self.down_button_final)
        # layoutV2.addWidget(self.result_button)
        layoutH.addLayout(layoutV2)

        # Создаем вертикальный бок
        layoutV3 = QVBoxLayout()
        self.text_before = QPlainTextEdit()
        self.text_after = QPlainTextEdit()
        layoutV3.addWidget(self.text_before)
        layoutV3.addWidget(self.text_after)

        layoutH.addLayout(layoutV3)

        layoutV.addLayout(layoutH)

        layoutV.addWidget(self.result_button)

        self.setLayout(layoutV)

    def get_text_list_widget(self, list_widget: QListWidget):
        my_list = []
        for i in range(list_widget.count()):
            item = list_widget.item(i)
            my_list.append(item.text())
        return my_list

    @QtCore.Slot()
    def up_item_original(self):
        selected_item = self.list_widget_original.currentItem()
        current_index = self.list_widget_original.currentRow()
        if selected_item is not None and current_index > 0:
            new_index = current_index - 1
            self.list_widget_original.takeItem(current_index)
            self.list_widget_original.insertItem(new_index, selected_item)
            self.list_widget_original.setCurrentRow(new_index)

            self.label_original.setText(f"Исходный: {self.get_text_original()}")

    @QtCore.Slot()
    def down_item_original(self):
        selected_item = self.list_widget_original.currentItem()
        current_index = self.list_widget_original.currentRow()
        if (
            selected_item is not None
            and current_index < self.list_widget_original.count() - 1
        ):
            new_index = current_index + 1
            self.list_widget_original.takeItem(current_index)
            self.list_widget_original.insertItem(new_index, selected_item)
            self.list_widget_original.setCurrentRow(new_index)

            self.label_original.setText(f"Исходный: {self.get_text_original()}")

    def get_text_original(self):
        my_list = self.get_text_list_widget(self.list_widget_original)
        return "|".join(value for value in my_list)

    @QtCore.Slot()
    def up_item_final(self):
        selected_item = self.list_widget_final.currentItem()
        current_index = self.list_widget_final.currentRow()
        if selected_item is not None and current_index > 0:
            new_index = current_index - 1
            self.list_widget_final.takeItem(current_index)
            self.list_widget_final.insertItem(new_index, selected_item)
            self.list_widget_final.setCurrentRow(new_index)

            self.label_final.setText(f"Результирующий: {self.get_text_final()}")

    @QtCore.Slot()
    def down_item_final(self):
        selected_item = self.list_widget_final.currentItem()
        current_index = self.list_widget_final.currentRow()
        if (
            selected_item is not None
            and current_index < self.list_widget_final.count() - 1
        ):
            new_index = current_index + 1
            self.list_widget_final.takeItem(current_index)
            self.list_widget_final.insertItem(new_index, selected_item)
            self.list_widget_final.setCurrentRow(new_index)

            self.label_final.setText(f"Результирующий: {self.get_text_final()}")

    def get_text_final(self):
        my_list = self.get_text_list_widget(self.list_widget_final)
        return "|".join(value for value in my_list)

    @QtCore.Slot()
    def get_result(self):
        original = self.get_text_list_widget(self.list_widget_original)
        final = self.get_text_list_widget(self.list_widget_final)

        list_line = self.text_before.toPlainText().split("\n")

        list_line_result = []
        reordered_list = []

        for line in list_line:
            list_elements = line.split("|")
            reordered_list = [""] * len(list_elements)
            for index, elem in enumerate(list_elements):
                try:
                    value_original = original[index]
                except KeyError:
                    break
                index_final = final.index(value_original)
                reordered_list[index_final] = elem

            list_line_result.append("|".join(reordered_list))

        self.text_after.setPlainText("\n".join(list_line_result))


if __name__ == "__main__":
    app = QApplication([])

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
