from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def generate_buttons(buttons_info: dict | list):
    buttons_list = []
    for row in buttons_info:
        if isinstance(row, list):
            temp = list()
            for item in row:
                if item.get('url'):
                    temp.append(InlineKeyboardButton(text=item['text'], url=item['url']))
                else:
                    temp.append(InlineKeyboardButton(text=item['text'], callback_data=item['callback_data']))
            buttons_list.append(temp)
        else:
            if row.get('url'):
                buttons_list.append([InlineKeyboardButton(text=row['text'], url=row['url'])])
            else:
                buttons_list.append([InlineKeyboardButton(text=row['text'], callback_data=row['callback_data'])])
    keyboard_inline_buttons = InlineKeyboardMarkup(inline_keyboard=buttons_list)
    return keyboard_inline_buttons