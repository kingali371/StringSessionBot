import os
from threading import Thread
from flask import Flask

# تهيئة Flask لربط المنفذ المطلوب من Render
app_flask = Flask('')

@app_flask.route('/')
def main():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))  # استخدم المنفذ من Render
    app_flask.run(host="0.0.0.0", port=port)

# ---------- دالة بدء البوت الخاصة بك ----------
# هنا ضع الدالة التي تشغل بوت التليجرام (polling)
def run_bot():
    # مثال: updater.start_polling() أو bot.infinity_polling()
    # ضع كود البوت الخاص بك هنا
    pass
# -----------------------------------------

if __name__ == "__main__":
    # تشغيل Flask في خيط منفصل لفتح المنفذ
    t = Thread(target=run_flask)
    t.start()
    
    # تشغيل البوت في الخيط الرئيسي
    run_bot()
