# BadUSB Demo – Raspberry Pi Pico  

🚀 Ushbu loyiha Raspberry Pi Pico/Pico W yordamida **BadUSB** texnologiyasini ko‘rsatadi.  
Qurilma kompyuterga USB orqali ulanganida, u **klaviatura emulyatsiyasi** qilib, avtomatik buyruqlarni bajaradi  
(masalan, brauzerda sahifa ochish, CMD/PowerShell komandalarini bajarish).  

⚠️ **Ogohlantirish:** Ushbu loyiha faqat **ta’limiy va laboratoriya sharoitida** foydalanish uchun mo‘ljallangan.  
Amaliyotdan tashqarida ishlatish **qonunbuzarlik** hisoblanadi!  

---

## ✨ Xususiyatlar
- Windows Run (`Win+R`) oynasida buyruqlar bajarish  
- Brauzer orqali URL ochish  
- CMD yoki PowerShell terminalini avtomatik ishga tushirish  
- Notepad yoki boshqa dasturlarda matn yozish  
- Klaviatura tugmalarini kombinatsiya orqali bosish (CTRL+C, ALT+TAB va h.k.)  

---

## 🛠️ Talablar
- Raspberry Pi Pico yoki Pico W  
- CircuitPython 9.x+ (Adafruit versiyasi)  
- `adafruit_hid` kutubxonasi (`lib` papkasida bo‘lishi kerak)  

Kutubxonani yuklab olish:  
👉 [Adafruit HID Library](https://github.com/adafruit/Adafruit_CircuitPython_HID)  

CircuitPython firmware:  
👉 [CircuitPython for Raspberry Pi Pico](https://circuitpython.org/board/raspberry_pi_pico/)  

---

## 📂 O‘rnatish
1. Raspberry Pi Pico’ni CircuitPython bilan flesh qiling.  
2. `lib/` papkasiga `adafruit_hid` kutubxonasini joylashtiring.  
3. `code.py` faylini to‘g‘ridan-to‘g‘ri Pico qurilmasiga nusxa qiling.  
4. Pico’ni kompyuterga ulang va avtomatik ishga tushishini kuzating.  

---

## 💻 Qo‘llanish
### Asosiy funksiyalar
- `open_url("https://...")` → Brauzer orqali sayt ochish  
- `open_cmd()` → CMD terminalini ochish  
- `open_powershell()` → PowerShell terminalini ochish  
- `run_command("notepad")` → Notepad ochish  
- `type_text("Hello World")` → Matn yozish  
- `press_keys(Keycode.CTRL, Keycode.C)` → Tugmalar kombinatsiyasi  

---

## 📖 Namuna
```python
# YouTube kanalini ochish
open_url("https://www.youtube.com/@Kiber_Pro")

# CMD orqali buyruqlar bajarish
open_cmd()
time.sleep(1)
type_text("ipconfig")
kbd.send(Keycode.ENTER)
