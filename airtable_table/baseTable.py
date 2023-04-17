from airtable import Airtable


class AirtableTable:
    def __init__(self, base_key, table_name, api_key):
        self.airtable = Airtable(base_key, table_name, api_key)

    def get_all_records(self):
        return self.airtable.get_all()

    def get_record_by_formula(self, formula):
        return self.airtable.get_all(formula=formula)

    def get_record(self, record_id):
        return self.airtable.get(record_id)

    def create_record(self, fields):
        return self.airtable.insert(fields)

    def update_record(self, record_id, fields):
        return self.airtable.update(record_id, fields)
