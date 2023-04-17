from typing import List, Dict
from .baseTable import AirtableTable


class ProgramsTable:

    last_query: List[Dict] = None

    def __init__(self, base_key, api_key):
        self.table = AirtableTable(base_key, 'Программы', api_key)

    def get_all_programs(self):
        self.last_query = self.table.get_all_records()
        return self.table.get_all_records()

    def get_program_by_name(self, name):
        formula = f"{{Номер_программы}} = {name}"
        self.last_query = self.table.get_record_by_formula(formula)
        return self.table.get_record_by_formula(formula)

    def get_program(self, id_program):
        return self.table.get_record(id_program)


class RequestTable:
    def __init__(self, base_key, api_key):
        self.table = AirtableTable(base_key, 'Заявки', api_key)

    def create_request(self):
        ...

    def get_all_request(self):
        ...

    def update_request(self):
        ...

    def delete_request(self):
        ...
