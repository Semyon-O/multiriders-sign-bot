from typing import List, Dict
from .baseTable import AirtableTable


class ProgramsTable:

    def __init__(self, base_key, api_key):
        self.table = AirtableTable(base_key, 'Программы', api_key)

    def get_all_programs(self):
        return self.table.get_all_records()

    def get_program_by_name(self, name):
        formula = f"{{Номер_программы}} = {name}"
        return self.table.get_record_by_formula(formula)

    def get_program(self, id_program):
        return self.table.get_record(id_program)

    def get_program_by_formula(self, formula):
        return self.table.get_record_by_formula(formula)


class RequestTable:
    def __init__(self, base_key, api_key):
        self.table = AirtableTable(base_key, 'Заявки_на_программу', api_key)

    def create_request(self, fields):
        return self.table.create_record(fields)

    def get_all_request(self):
        ...

    def update_request(self):
        ...

    def delete_request(self):
        ...
