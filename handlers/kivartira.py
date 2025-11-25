# from aiogram import Router, F
# from aiogram import types
# from aiogram.fsm.context import FSMContext

# dp = Router()


# @dp.message(F.text == "Kivartira")
# async def k(message: types.Message, state: FSMContext):
#     await message.answer("Qancha muddatga ijaraga berasiz?")
#     await state.set_state(Register.holati)


# @dp.message(Register.holati)
# async def amsgdj(message: types.Message, state: FSMContext):
#     if message.text in ["jasjk", 'jakbkja']:
#         await state.update_data(bskja=message.text)
#         await message.answer("Tuman")
#         await state.set_state(Register.nimadur)
#     else:
#         await message.answer("Buttoni bos")
#         await state.set_state(Register.holati) 