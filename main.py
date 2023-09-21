import sys
from PyQt6.QtWidgets import QApplication
from modules.Configuration import OpenFile, OrganizeData
from modules.Presentation import Presentation


def get_data_file() -> str:
    app = QApplication(sys.argv)
    of = OpenFile()
    of.show()
    of.close()
    app.exit()
    return of.file_loc


def main():
    file_name = get_data_file()
    get_data = OrganizeData(file_name)
    present_data = Presentation(get_data.filtered_open_df)
    tables = present_data.populate_table()
    for table in tables:
        print(table)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
