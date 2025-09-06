"""
BadUSB Advanced Demo – Raspberry Pi Pico (CircuitPython)
--------------------------------------------------------
Ushbu dastur Pico’ni USB klaviatura sifatida ishlatadi.
Yangi qo‘shilgan funksiyalar:
    1. run_command()   → Windows Run orqali buyruq bajarish
    2. open_url()      → Brauzer orqali URL ochish
    3. open_cmd()      → CMD terminalini ochish
    4. open_powershell() → PowerShell oynasini ochish
    5. type_text()     → Istalgan matnni yozish
    6. press_keys()    → Klaviatura kombinatsiyalarini bosish
"""

import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# === Boshlang‘ich sozlamalar ===
time.sleep(5)  # Kompyuter HID qurilmani tanishi uchun
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)


# === Funksiyalar ===

def run_command(command: str, delay: float = 0.5):
    """Windows Run oynasini ochib, buyrug‘ni bajaradi."""
    kbd.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.7)
    layout.write(command)
    time.sleep(delay)
    kbd.send(Keycode.ENTER)


def open_url(url: str):
    """Brauzer orqali URL ochish."""
    run_command(url, delay=0.4)


def open_cmd():
    """CMD terminalini ochish."""
    run_command("cmd", delay=0.7)


def open_powershell():
    """PowerShell terminalini ochish."""
    run_command("powershell", delay=0.7)


def type_text(text: str):
    """Istalgan matnni yozish."""
    layout.write(text)


def press_keys(*keys):
    """Bir nechta tugmalarni birga bosish (masalan CTRL+C)."""
    kbd.send(*keys)


# === Asosiy dastur oqimi (DEMO) ===

# 1. YouTube kanalini ochamiz
open_url("https://www.youtube.com/@Kiber_Pro")
time.sleep(5)

# 2. CMD terminalini ochib, ipconfig va whoami bajarish
open_cmd()
time.sleep(1)
type_text("ipconfig")
kbd.send(Keycode.ENTER)
time.sleep(1)
type_text("whoami")
kbd.send(Keycode.ENTER)

# 3. PowerShell ochib, salom yozish
time.sleep(3)
open_powershell()
time.sleep(1)
type_text("Write-Output 'Salom, bu BadUSB demo!'")
kbd.send(Keycode.ENTER)

# 4. Notepad ochib matn yozish
time.sleep(3)
run_command("notepad", delay=1.0)
time.sleep(1)
type_text("Bu yozuv Raspberry Pi Pico orqali avtomatik yozildi!")
kbd.send(Keycode.ENTER)
