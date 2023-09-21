import sys
import pandas as pd
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QApplication


class OpenFile(QMainWindow):
    def __init__(self):
        super().__init__()

        self.file_loc = None
        self.showFileDialog()

    def showFileDialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select a file', '', '*.csv')
        if file_path:
            self.file_loc = file_path
        else:
            print("No file selected.")


class OrganizeData:
    def __init__(self, filename):
        self.df = self.process_dataframe(filename)
        self.filtered_df = self.filtering()
        self.multiple_choice_df = None
        self.open_ended_df = None
        self.filtered_multiple_df = None
        self.filtered_open_df = None
        self.get_question_type()

    def get_question_type(self):
        df = self.filtered_df.copy()
        self.multiple_choice_df = df[df["Question Type"] == "Multiple"]
        self.filtered_multiple_df = df[df["Question Type"] == "Multiple"]
        self.open_ended_df = df[df["Question Type"] == "Open"]
        self.filtered_open_df = df[df["Question Type"] == "Open"]
        # return df[df["Question Type"] == question_type]

    def filtering(self):
        df = self.df.copy()
        filtered = df[["Name", "Answer", "Question", "Question Number", "Question Type"]]
        return filtered

    @staticmethod
    def process_dataframe(filename):
        df = pd.read_csv(filename)
        df["Question Number"] = pd.factorize(df["Question"])[0]
        return df


def get_data_file() -> str:
    app = QApplication(sys.argv)
    of = OpenFile()
    of.show()
    of.close()
    app.exit()
    return of.file_loc
