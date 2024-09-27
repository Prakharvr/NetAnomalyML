import platform
import socket
import uuid
import re
import logging
import wmi

import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import psutil
import scikitplot as skplt
import xlsxwriter


def display_library_versions():
    """Prints the versions of the imported libraries."""
    print(f'scikit-learn v{sklearn.__version__},')
    print(f'NumPy v{np.__version__},')
    print(f'Pandas v{pd.__version__},')
    print(f'Matplotlib v{plt.__version__},')
    print(f'Seaborn v{sns.__version__},')
    print(f'Psutil v{psutil.__version__},')
    print(f'Scikitplot v{skplt.__version__}')


def display_system_info():
    system_info = {
        'Platform': platform.system(),
        'Platform Release': platform.release(),
        'Platform Version': platform.version(),
        'Architecture': platform.machine(),
        'Hostname': socket.gethostname(),
        'IP Address': socket.gethostbyname(socket.gethostname()),
        'MAC Address': ':'.join(re.findall('..', '%012x' % uuid.getnode())),
        'Processor': platform.processor(),
        'RAM': f"{round(psutil.virtual_memory().total / (1024.0 ** 3))} GB"
    }

    computer = wmi.WMI()
    os_info = computer.Win32_OperatingSystem()[0]
    os_name = f"{platform.system()} {platform.release()}"
    os_version = f"{os_info.Version} {os_info.BuildNumber}"
    proc_info = computer.Win32_Processor()[0]
    gpu_info = computer.Win32_VideoController()[0]
    total_ram_gb = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

    print(f'OS Name: {os_name}')
    print(f'OS Version: {os_version}')
    print(f'Architecture: {platform.machine()}')
    print(f'CPU: {proc_info.Name}')
    print(f'RAM: {round(total_ram_gb)} GB')
    print(f'Graphics Card: {gpu_info.Name}')

    for key, value in system_info.items():
        print(f'{key}: {value}')

display_library_versions()
display_system_info()
current_process = psutil.Process()
memory_usage = current_process.memory_percent()
print(memory_usage)

print('The end.')
quit()

