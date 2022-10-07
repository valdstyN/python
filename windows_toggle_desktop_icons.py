# pip install pywin32
import win32gui, win32con
hWnd = win32gui.GetWindow(win32gui.FindWindow("Progman", "Program Manager"), 5);
win32gui.SendMessage(hWnd, 0x111, 0x7402, 0);
