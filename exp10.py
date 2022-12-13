import win32com.client
import time
excel = win32com.client.Dispatch("Excel.Application")

excel.Visible = True
excel.DisplayAlerts = False
time.sleep(5)
# excel.Quit()