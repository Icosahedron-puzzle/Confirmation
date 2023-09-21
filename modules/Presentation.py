from prettytable import PrettyTable, ALL
import pandas as pd


class Presentation:
    def __init__(self, dataframe):
        self.df = self.process_df(dataframe)
        self.table = PrettyTable()
        # self.table_df = self.df.iloc[:, :3]

    @staticmethod
    def process_df(dataframe):
        return dataframe.iloc[:, :4]

    def get_question_by_number(self, question_number):
        df = self.df.copy()
        filtered_df = df[df["Question Number"] == question_number]
        return filtered_df

    def populate_table(self):
        num_of_get_question_requests = self.df["Question Number"].unique()
        question_dfs = []
        tables = []
        for x in num_of_get_question_requests:
            df = self.get_question_by_number(x)
            filtered_df = df.iloc[:, :2]

            prompt = df.Question.unique()[0]
            number = df["Question Number"].unique()[0]
            prompt_final = f"Question #{number}: {prompt}"
            students = list(filtered_df.Name.unique())
            num_of_students = len(students)
            student_counter = 0

            question_dfs.append(filtered_df)
            table = PrettyTable(list(filtered_df.columns), title=prompt_final, max_table_width=80)
            # table.align["Name"] = 25
            table.max_width["Name"] = 25
            table.hrules = ALL
            table.field_names = list(filtered_df.columns)

            for _ in students:
                table.add_row(filtered_df.iloc[student_counter, :])
                student_counter += 1

            tables.append(table)
        return tables
