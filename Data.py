from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
**❄️ مـرحـبـاً بـڪ ** {},
━━━━━━━━━━━━━━━━━━━
** ⌯ ¦ في بــوت استـخـراج جلـسـات تࢪيمكس

** ⌯ ¦ وبــايــروجـرام للـمـيــوزك🎧**
━━━━━━━━━━━━━━━━━━━
** ⌯ ¦ هـذا البـوت بواسطـة : سـورس سـيـمـو **
━━━━━━━━━━━━━━━━━━━
** ⌯ ¦ يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـهہ

   ⌯ ¦ و للحصـول على كـود تيرمكـس لتشغيل تلـيثون**

** ⌯ ¦ لا تقم بطـرد جلسـة البـوت بعـد استخـراج الكـود**

━━━━━━━━━━━━━━━━━━━
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("بـدء انشـاء جلسـة البـوت", callback_data="generate")],
        [InlineKeyboardButton(text=" رجــوع ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("بـدء انشـاء جلسـة البـوت", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("بـدء انشـاء جلسـة البـوت", callback_data="generate")],
        
        [
            InlineKeyboardButton("مسـاعدة", callback_data="help"),
            InlineKeyboardButton("حول البوت", callback_data="about")
        ],
        
    ]

    # Help Message
    HELP = """
**- اوامـر البـوت الاخـرى ⌨:**

/about - حـول البـوت
/help - اوامـر المسـاعده
/start - بـدء تشغيـل البـوت
/generate - بـدء انشـاء جلسـه
/cancel - الغـاء
/restart - اعـادة تشغيـل
"""

    # About Message
    ABOUT = """
**- حــول البـــوت :**

**» بـوت انشـاء جلسـة البـوت واستخـراج كـود تيرمكـس التابـع لســورس سيمو .. مبني ع آخـر اصـدار لـ لغـة بايثـون 3.9.7** 🌐🦾
    
**» لغة البوت 🅿️:** [Python³](https://www.python.org/)

**» مطور البـوت 🧑🏻‍💻:** [✗ 『 𝐃𝐄𝐕↝𝐒𝐀𝐌𝐈𝐑 』 ✗](https://t.me/DEV_SAMIR)

**» قناة السورس 🌐:** [𝐒 𝐄 𝐌 𝐎](t.me/FTTUTY)

**» الشـروحـات 🛂:** 
- [شروحات تنصيب 𝐒 𝐄 𝐌 𝐎](t.me/FTTUTY)
- [شروحات تنصيب](t.me/FTTUTY)

    """
