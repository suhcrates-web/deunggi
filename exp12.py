import wmi
from wmi import connect
from win32com.client import GetObject, Dispatch

# Initializing the wmi constructor
f = wmi.WMI()
print(f)

# Printing the header for the later columns
print("pid   Process name")

# Iterating through all the running processes
for process in f.Win32_Process():
    # Displaying the P_ID and P_Name of the process
    print(f"{process.ProcessId:<10} {process.Name} {process.CommandLine}")
print(connect().Win32_Process())
# for process in connect().Win32_Process():
#     print(process.Hash)
# print(GetObject('').Win32_Process())