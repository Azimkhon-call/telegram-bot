from aiogram import F, Router
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram import Bot
from keyboard import inline, keyboard,inline_rt,inline_uz


router = Router()

uz = FSInputFile('uzbek10mp10.mp3')
uz2 = FSInputFile('uzbekm4.m4a')
uz3 =FSInputFile('uzbek1uz1.mp3')
uz4 =FSInputFile('uzbek4mp4.m4a')
uz5 =FSInputFile('uzbek5m5.mp3')
uz6 =FSInputFile('uzbek6mp6.mp3')
uz7 =FSInputFile('uzbek7mp7.mp3')
uz8 =FSInputFile('uzbek8mp8.mp3')
uz9 =FSInputFile('uzbek9mp9.mp3')
uz10 =FSInputFile('uzbek10mp10.mp3')
########
jazz =FSInputFile('Helen Merrill - Just Imagine.mp3')
jazz2 =FSInputFile('jazz2mp2.mp3')
jazz3 =FSInputFile('jazz3mp3.mp3')
jazz4 =FSInputFile('jazz4mp4.mp3')
jazz5 =FSInputFile('jazz5mp5.mp3')
jazz6 =FSInputFile('jazz6mp6.mp3')
jazz7 =FSInputFile('jazz7mp7.mp3')
#########
jaxon =FSInputFile('4 MY- Jaxon (Official Music Video) - fSPBYHk_jns.m4a')
jaxon2 =FSInputFile('JAXON2MP2.mp3')
jaxon3 =FSInputFile('jaxon3mp3.m4a')
jaxon4 =FSInputFile('jaxon4mp4.mp3')
jaxon5 =FSInputFile('newyork jaz.m4a')
jaxon6 =FSInputFile('jaxon6mp6.m4a')
jaxon7 =FSInputFile('JAXON2MP2.mp3')
jaxon8 =FSInputFile('newyork jaz.m4a')
jaxon9 =FSInputFile('jaxon4mp4.mp3')
jaxon10 =FSInputFile('jazz3mp3.mp3')
############################################################################################
@router.message(F.text == '/start')
async def start(message: Message):
    await message.answer('😊salom qanday yordam bera olaman☺️', reply_markup=keyboard)

######################################JAXON#########################################
@router.message(F.text == 'Jaxon')
async def python(message: Message):
    await message.answer('Natijalar 1-10 gacha\n\n1.4 MY-jaxon\n2.JAXON\n3.jaxon -mp3\n4.Maverick Phonex-jaxon\n5.newyork\n6.jaxon\n7.Jaxon6\n8.jaxon\n9.jaxon music10.MAVERICK -JAXON', reply_markup=inline)



@router.callback_query(lambda c: c.data == 'jahon1')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jaxon)



@router.callback_query(lambda c: c.data == 'jahon2')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jaxon2)

@router.callback_query(lambda c: c.data == 'jahon3')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jaxon3)

@router.callback_query(lambda c: c.data == 'jahon4')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jaxon4)

@router.callback_query(lambda c: c.data == 'jahon5')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jaxon5)

@router.callback_query(lambda c: c.data == 'jahon6')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jaxon6)

@router.callback_query(lambda c: c.data == 'jahon7')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jaxon7)

@router.callback_query(lambda c: c.data == 'jahon8')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jaxon8)

@router.callback_query(lambda c: c.data == 'jahon9')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jaxon9)

@router.callback_query(lambda c: c.data == 'jahon10')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jaxon10)
#####################################CONTACT+Lication##########################################

@router.message(F.text == 'Contact')
async def contact(massage: Message):
    await massage.answer('share you Contact')


@router.message(F.text == 'Location')
async def location(massage: Message):
    await massage.answer('share you Location')

#########################################JAZZ#################################
@router.message(F.text == 'jazz music')
async def python(message: Message):
    await message.answer('Natijalar 1 - 10 gacha\n\n1.Helen Merrill\n2.jazz musik 3.jazz mp3\n4.jazz\n5.JAZZ\n6.music jazz\n7.jazz\n8.Jaz\n9.jazz\n10.music ', reply_markup=inline_rt)


@router.callback_query(lambda c: c.data == 'jazz1')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jazz)

@router.callback_query(lambda c: c.data == 'jazz2')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jazz2)


@router.callback_query(lambda c: c.data == 'jazz3')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jazz3)

@router.callback_query(lambda c: c.data == 'jazz4')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jazz4)

@router.callback_query(lambda c: c.data == 'jazz5')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jazz5)

@router.callback_query(lambda c: c.data == 'jazz6')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jazz6)

@router.callback_query(lambda c: c.data == 'jazz7')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jazz7)

@router.callback_query(lambda c: c.data == 'jazz8')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jazz2)

@router.callback_query(lambda c: c.data == 'jazz9')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jazz3)

@router.callback_query(lambda c: c.data == 'jazz10')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=jazz5)
####################################################UZBEK########################################

@router.message(F.text == 'uzbek')
async def python(message: Message):
    await message.answer('Natijalar 1 - 10 gacha\n\n1. TREND YULDUZLAR – Хамдам Собиров - Дайдиб (Аудио) Мp3 Xamdam Sobirov - Daydib (Official… 3:27 3.2M 129k\n2. Хамдам Собиров /Жанзе [Премьера клипа 2023] Xamdam Sobirov /Janze… 0:56 0.9M 134k\n3. Humo Music – Yomg‘irlarda kel - Xamdam Sobirov | Ёмгирларда кел - Хамдам Собиров… 0:45 0.7M 129k\n4. Xamdam Sobirov & Mirjalol Nematov – Menga o\'xshagani tug\'ilmaydi 4:18 4.3M 139k\n5. Muzikalar 2023 – Xamdam Sobirov Va Gulinur ♡ Yuragimni Yaraladi | Гулинур Ва Хамдам… 2:06 2.5M 169k6. Xamdam_Sobirov_Rayhon_Qizil_koylagim_sen_uchun_emas_rayhon_xam 3:20 3.2M 134k7. COSMOS YouTube – Xamdam Sobirov va Rayhon - Qizil Koʻylak #PREMYERA Хамдам Собиров… 3:20 3.2M 133k8. Xamdam Sobirov – Janze 4:04 3.8M 131k9. Toybop musiqalar – Xamdam Sobirov-Qishloqqa qayt Хамдам Собиров-Кишлокка кайт 4:02 3.7M 129k10. Ziyoda & Xamdam Sobirov – Qora Atirgul (soundtrack) | 3:22 3.1M 128', reply_markup=inline_uz)



@router.callback_query(lambda c: c.data == 'uzbek1')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=uz)

###########
@router.callback_query(lambda c: c.data == 'uzbek2')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=uz2)
###############
@router.callback_query(lambda c: c.data == 'uzbek3')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=uz3)
###############
@router.callback_query(lambda c: c.data == 'uzbek4')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=uz4)
##################
@router.callback_query(lambda c: c.data == 'uzbek5')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=uz5)
##################
@router.callback_query(lambda c: c.data == 'uzbek6')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=uz6)

@router.callback_query(lambda c: c.data == 'uzbek7')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=uz7)

@router.callback_query(lambda c: c.data == 'uzbek8')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=uz8)

@router.callback_query(lambda c: c.data == 'uzbek9')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=uz9)

@router.callback_query(lambda c: c.data == 'uzbek10')
async def uzbek(call: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(call.id)
    await bot.send_audio(chat_id=call.from_user.id, audio=uz10)


##############################################################################################
@router.callback_query(F.data == 'exit')
async def python(call.CallbackQuery):
    await call.message.delete()
    await message.answer('Qayta qanday yordam bera olaman',reply_markup=keyboard)










