from aiogram import types
from loader import dp,bot,Database

@dp.my_chat_member_handler()
async def some_handler(my_chat_member: types.ChatMemberUpdated):
    if my_chat_member.chat.type =='private':
        status = my_chat_member.new_chat_member.status
        user_id = my_chat_member.from_user.id
        if status == 'member':
            sql = "UPDATE users SET `status` = 'active' WHERE user_id =%s"
            await Database.apply(sql,(user_id))
        elif status == 'kicked':
            sql = "UPDATE users SET `status` = 'passive' WHERE user_id =%s"
            await Database.apply(sql,(user_id))
        else:
            sql = "UPDATE users SET `status` = 'active' WHERE user_id =%s"
            await Database.apply(sql,(user_id))

