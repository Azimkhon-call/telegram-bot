from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

keyboard = ReplyKeyboardMarkup(keyboard=[

    [
        KeyboardButton(text='Jaxon'),
        KeyboardButton(text='jazz music'),
        KeyboardButton(text='uzbek'),
    ],

    [
        KeyboardButton(
            text='Contact', request_contact=True
        ),
        KeyboardButton(
            text='Location', request_location=True
        )
    ],
]
)
#####################################################################
inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data='jahon1'),
            InlineKeyboardButton(text='2', callback_data='jahon2'),
            InlineKeyboardButton(text='3', callback_data='jahon3'),
            InlineKeyboardButton(text='4', callback_data='jahon4'),
            InlineKeyboardButton(text='5', callback_data='jahon5'),
        ],
        [
            InlineKeyboardButton(text='6', callback_data='jahon6'),
            InlineKeyboardButton(text='7', callback_data='jahon7'),
            InlineKeyboardButton(text='8', callback_data='jahon8'),
            InlineKeyboardButton(text='9', callback_data='jahon9'),
            InlineKeyboardButton(text='10', callback_data='jahon10'),
            InlineKeyboardButton(text='❌', callback_data='exit'),
        ],

    ], resize_keyboard=True)



########################################################################################################
inline_rt = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data='jazz1'),
            InlineKeyboardButton(text='2', callback_data='jazz2'),
            InlineKeyboardButton(text='3', callback_data='jazz3'),
            InlineKeyboardButton(text='4', callback_data='jazz4'),
            InlineKeyboardButton(text='5', callback_data='jazz5'),
        ],
        [
            InlineKeyboardButton(text='6', callback_data='jazz6'),
            InlineKeyboardButton(text='7', callback_data='jazz7'),
            InlineKeyboardButton(text='8', callback_data='jazz8'),
            InlineKeyboardButton(text='9', callback_data='jazz9'),
            InlineKeyboardButton(text='10', callback_data='jazz10'),
            InlineKeyboardButton(text='❌', callback_data='exit'),
        ],

    ], resize_keyboard=True)

############################################################################################
inline_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data='uzbek1'),
            InlineKeyboardButton(text='2', callback_data='uzbek2'),
            InlineKeyboardButton(text='3', callback_data='uzbek3'),
            InlineKeyboardButton(text='4', callback_data='uzbek4'),
            InlineKeyboardButton(text='5', callback_data='uzbek5'),
        ],
        [
            InlineKeyboardButton(text='6', callback_data='uzbek6'),
            InlineKeyboardButton(text='7', callback_data='uzbek7'),
            InlineKeyboardButton(text='8', callback_data='uzbek8'),
            InlineKeyboardButton(text='9', callback_data='uzbek9'),
            InlineKeyboardButton(text='10', callback_data='uzbek10'),
            InlineKeyboardButton(text='❌',callback_data='exit')
        ],

    ], resize_keyboard=True)

