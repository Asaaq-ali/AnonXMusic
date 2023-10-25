import asyncio

from pyrogram import Client, filters

import config
from AnonXMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

@app.on_message(filters.regex("^$"))
async def khalid(client: Client, message: Message):
    user = message.from_user.mention
    await message.reply_text(f"""✧ <b> اهلين </b> {user} !\n✧ <b> اضغط الزر عشان تشوف اوامر سهى</b>**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "الاوامر", callback_data=f"am"),
                ],
            ]
        ),
    )



@app.on_message(filters.regex("^سهى الاحصائيات$") & filters.user(2089102006))
async def ahtek(client: Client, message: Message):
    m_reply = await message.reply_text(f"✧ <b> اهلين مطوري ارحب</b>\n✧ <b> هذي احصائيات سهى يا روحي :</b>\n\n-› عدد المشتركين : 12478\n-› عدد المجموعات : 11346\n\n• تم زيادة 1204 مشترك ونقص 2103 مجموعة  في اخر 24 ساعة\n\n- عدد الطرد من بوتات اخرى : 843\n- طرد يدوي : 1302\n\n╼╾")
    await m_reply_text("")


@app.on_message(filters.command("","."))
def vgdg(client,message):
        message.reply_text(
            f"""✧ Welcome Baby,
ᴅᴇᴠᴇʟᴏᴘᴇʀ -› [『𝐖𝐇𝐈𝐒𝐊𝐄𝐘 𝐓𝐍𝐓 ⏎ 』♪](t.me/A_S_A_S_K)
ᴄʜᴀɴɴᴇʟ -› [𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂](t.me/Mlze1bot)""", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "تحديثات سهى 🍻", url=f"t.me/Mlze1bot")
                    ]
                ]
            ),
            disable_web_page_preview=True

        )




@app.on_message(filters.regex("^رابط الحذف$"))
async def delet(client: Client, message: Message):
    await message.reply_text(f"""✧ <b> اهلين ياحلو</b>\n✧ <b> هذي روابط حذف جميع مواقع التواصل بالتوفيق</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Telegram •", url=f"https://my.telegram.org/auth?to=delete"),
                    InlineKeyboardButton(
                        "• Instagram •", url=f"https://www.instagram.com/accounts/login/?next=/accounts/remove/request/permanent/"),
                ],[
                    InlineKeyboardButton(
                        "• Snapchat •", url=f"https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fdeleteaccount"),
                    InlineKeyboardButton(
                        "• Facebook •", url=f"https://www.faecbook.com/help/deleteaccount"),
                ],[
                    InlineKeyboardButton(
                        "• Twitter •", url=f"https://mobile.twitter.com/settings/deactivate"),

                ],
            ]
        ),
    )


@app.on_message(filters.command("سهى نادي المطور", [".", ""]) & filters.group)
async def kstr(client: Client, message: Message):
       chat = message.chat.id
       gti = message.chat.title
       link = await app.export_chat_invite_link(chat)
       usr = await client.get_users(message.from_user.id)
       chatusername = f"@{message.chat.username}"
       user_id = message.from_user.id
       user_ab = message.from_user.username
       user_name = message.from_user.first_name
       buttons = [[InlineKeyboardButton(gti, url=f"{link}")]]
       reply_markup = InlineKeyboardMarkup(buttons)
       
       await app.send_message(-1001936852140, f"- قام {message.from_user.mention}\n- بمناداتك عزيزي المطور\n- ايديه {user_id}\n- يوزره @{user_ab}\n- ايدي القروب {message.chat.id}\n- يوزر القروب {chatusername}",
       reply_markup=reply_markup,
       )
       await message.reply_text(
        f"""✧ <b> ابشر ياعيوني ارسلت للمطور بيخش القروب ويشوف مشكلتك بأقرب وقت </b>\n\n✧ <b> تابع قناة البوت عشات تشوف التحديثات</b> -› [• 𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂 •](t.me/Mlze1bot)""", disable_web_page_preview=True     
    )


REPLY_MESSAGE = "✧ <b> اهلين ياحلو تحكم من الازرار اسفل </b>"




REPLY_MESSAGE_BUTTONS = [

         [

             ("كيفية استخدام سهى"),                   

             ("اوامر سهى")




          ],

          [

             ("المطور"),

             ("السورس")

          ],

          [

             ("اخفاء الازرار")

          ]

]




  

@app.on_message(filters.regex("^ميوزك$"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        photo=config.DRTYU_VENUE,
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اخفاء الازرار") & filters.group)
async def down(client, message):
          m = await message.reply("✧ <u> ابشر تم اخفاء الازرار بنجاح</u>\n✧ <b> لو تبي تطلعها مرة ثانية اكتب سهى</b>", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.group & filters.command(["كيفية استخدام سهى"],""))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""✧ <b> هلا والله ياعيني عشان تفعل بوت سهى اتبع الخطوات الي بالاسفل </b>
1 • ارفعه مشرف بكل الصلاحيات 
2 • لو تبي تشوف الاوامر اكتب [ م الاوامر ] ولو تبي تشغل على طول اكتب سهى شغلي + اسم المقطع الصوتي
• مثال : سهى شغلي قالوا عليكي
- لو واجهت مشكله كلم مطور البوت ~ @A_S_A_S_K""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "𝗔𝗦𝗔𝗔𝗤", user_id=6218149232),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/smauabot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.group & filters.command(["سوررس"],""))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""✧ <b> اهلين فيك بسورس سهى ياحلو
• لو تبي تنصب مثل هالبوت تواصل مع مطور السورس
• عندك استفسار او اقتراح بخصوص البوت تواصل مع مطور البوت</b>
مطور السورس -› [𝗔𝗦𝗔𝗔𝗤](t.me/A_S_A_S_K)
قناة السورس -› [𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂](t.me/Mlze1bot)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "تحديثات سهى 🍻", url=f"https://t.me/Mlze1bot"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/smauabot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )




REPLY_MESSAGEE = "✧ <b> هلا فيك في قسم اوامر سهى</b>"

REPLY_MESSAGE_BUTTONSS = [
         [
             ("منصات الاغاني")
          ],
          [
             ("اوامر الجروبات"),
             ("اوامر القنوات")
          ],
          [
             ("طريقة البحث")
          ],
          [
             ("حفظ التشغيل")             
          ],
          [
             ("")
          ],
          [
            ("اخفاء الازرار")
          ]
]

  
@app.on_message(filters.group & filters.command(["اوامر سهى"],""))
async def com(_, message: Message):             
        text = REPLY_MESSAGEE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONSS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



@app.on_message(filters.group & filters.command(""))
async def bask(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )


@app.on_message(filters.group & filters.command(["منصات الاغاني"],""))
async def mnsat(client: Client, message: Message):
    await message.reply_text(f"""✧ <b> اهلين فيك في قسم تشغيل المنصات
- المنصات المدعومة هي ↓
• Telegram
• Youtube
• SoundCloud
• AppleMusic
• Spotify
- لو واجهت مشكلة تواصل مع مطور السورس @A_S_A_S_K</b>
- [𝑺𝒐𝒖𝒓𝒄𝒆 𝒔𝒐𝒉𝒂](t.me/Mlze1bot)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/smauabot?startgroup=true"),

                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.group & filters.command(["اوامر الجروبات"],""))
async def laksk(client: Client, message: Message):
    await message.reply_text(f"""\n\n\n╭── • [𝘀𝗼𝗵𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/Mlze1bot) • ──╮\n\n ✧ <b><u> اوامر التشغيل بالجروبات </u></b>\n\n✧ <b>سهى شغلي + اسم الاغنية او بالرد</b> \n-› لتشغيل الاغاني فالمجموعة\n\n✧ <b>سهى طفيها او ايقاف</b>\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n✧ <b>سهى الي بعده او تخطي</b>\n-› لتشغيل التالي بالانتظار\n\n ✧ <b>سهى اص  او اسكتي</b>\n-› لكتم صوت الحساب المساعد بالمكالمة\n\n✧ <b>سهى تكلمي</b>\n-› لالغاء الكتم واكمال التشغيل\n\n✧ <b> سهى اسكت او ايقاف مؤقت</b>\n -› لايقاف التشغيل بشكل مؤقت\n\n✧ <b> سهى كملي او كمل </b>\n -› لاكمال التشغيل بعد الايقاف المؤقت\n\n╰── • [𝘀𝗼𝗵𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/Mlze1bot) • ──╯""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/Mlze1bot"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/smauabot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )


@app.on_message(filters.group & filters.command(["اوامر القنوات"],""))
async def channvom(client: Client, message: Message):
    await message.reply_text(f"""\n\n╭── • [𝘀𝗼𝗵𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/Mlze1bot) • ──╮\n\n ✧ <b>اوامر التشغيل بالقنوات </b> \n\n✧ <b> ق تشغيل + اسم الاغنية او بالرد </b> \n-› لتشغيل الاغاني بالقناة\n\n ✧ <b> ق ايقاف </b>\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n  ✧ <b>ق تخطي </b>\n-› لتشغيل التالي بالانتظار\n\n ✧ <b>ق اص</b>\n-› لكتم صوت الحساب المساعد بالمكالمة\n\n✧ <b> ق كملي </b>\n-› لالغاء الكتم واكمال التشغيل\n\n✧ <b> اسكت او اسكتي </b>\n -› لايقاف التشغيل بشكل مؤقت\n\n✧ <b> كمل او سهى كملي </b>\n -› لاكمال التشغيل بعد الايقاف المؤقت\n\n╰── • [𝘀𝗼𝗵𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/Mlze1bot) • ──╯""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/Mlze1bot"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/smauabot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.group & filters.command(["طريقة البحث"],""))
async def dowmmr(client: Client, message: Message):
    await message.reply_text(f"""اهلين فيك في قسم التحميل ♪
للبحث عن اغنية او فيديو استخدم الامر التالي ↓
[ بحث + اسم المطلوب ..]
مثال -› بحث بحبك وحشتني
- الامر يشتغل بخاص البوت والمجموعة ايضا .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/Mlze1bot"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/smauabot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.group & filters.command(["حفظ التشغيل"],""))
async def dowhmr(client: Client, message: Message):
    await message.reply_text(f"""✧ <b> اهلين فيك في قسم حفظ التشغيل</b>\n\n✧ <b>حفظ التشغيل هو حفظ الاغاني الي اشتغلت بالمجموعة وحفظها يعني انك تقدر تشغلها بدون ما ترجع تبحث عنها مرة ثانية وتبقى محفوظة لك فقط</b>\n\n- عشان تحفظ الاغنية او المُشغل الحالي بالمكالمة لازم تضغط على زر -› ( </b>حفظ التشغيل <b> )\n\n✧ <b> عشان تشوف الاغاني او الصوتيات الي حفظتها اكتب امر -›</b> (قائمة تشغيلي )\n\n- وطريقة تشغيل قائمتك تكتب فقط امر -› ( تشغيل قائمتي )\n\n- طريقة حذف اغنية او مقطع من محفوظاتك تكتب امر -› ( حذف تشغيلي ) وتكمل الخطوات بخاص البوت ..\n\n✧ <b>ملاحظة : اذا حفظت اغنية بتكون محفوظة عندك فقط يعني كل شخص عنده قائمة تشغيل خاصة فيه ومحد يقدر يحفظ اغنية عندك والعكس ايضا\n✶ لو ما فهمت تابع الفيديو الي فوق عشان تفهم اكثر ❤️</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/Mlze1bot"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/smauabot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.group & filters.command(["طريقة ربط القنوات"],""))
async def dowhmo(client: Client, message: Message):
    await message.reply_text("""- هلا والله\n◌**عشان تشغل بالقنوات لازم تسوي بعض الخطوات وهي◌** :\n\n1 -› تدخل البوت قناتك وترفعه مشرف\n2 -› ترجع للقروب وتكتب { **ربط + يوزر القناة** }\n3 -› **اضغط على زر اوامر التشغيل عشان تعرف كيف تشغل**..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/Mlze1bot"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/smauabot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
  )
