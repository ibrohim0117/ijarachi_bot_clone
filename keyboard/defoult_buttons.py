from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram_i18n import I18nContext


def language_button(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('choose_language_text_uz')),
                KeyboardButton(text=_('choose_language_text_ru')),
                KeyboardButton(text=_('choose_language_text_en'))
            ]
        ],
        resize_keyboard=True
    )



def head_menu(i18n: I18nContext) -> ReplyKeyboardMarkup:
    _ = i18n

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_('rent')),
                KeyboardButton(text=_('give_for_rent'))
            ],

            [
                KeyboardButton(text=i18n('about_me')),
                KeyboardButton(text=_('change_language'))
            ]
        ],
        resize_keyboard=True
    )