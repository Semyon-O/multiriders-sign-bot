import pprint

import cachetools
from cachetools import cached
import airtable_table

from airtable_table import tables
from airtable_table import config as acf

# settings
cache_strategy = cachetools.TTLCache(maxsize=100, ttl=120)


@cached(cache=cache_strategy)
def show_program_cache(id: str):
    program_id = id
    programs = tables.ProgramsTable(airtable_table.config.base_token, airtable_table.config.api_token)
    program = programs.get_program(program_id)
    return program


@cached(cache=cache_strategy)
def get_all_programs():
    programs = tables.ProgramsTable(acf.base_token, acf.api_token)
    # TODO: Костыль. Нужно сделать инкапсуляция класса Airtable.
    all_programs = programs.table.airtable.get_all(sort=[('Даты_начала_программы', 'asc')])
    program_list = {}
    for program in all_programs:
        program_list[program["id"]] = program["fields"]["Название_программы"]

    return program_list