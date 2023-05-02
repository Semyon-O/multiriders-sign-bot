from aiogram.filters.callback_data import CallbackData


class RequestClientCallbackData(CallbackData, prefix="request"):
    action: str
    program_id: str


class ShortFormCallbackData(CallbackData, prefix="child"):
    program_id: str
    wasChild: bool
