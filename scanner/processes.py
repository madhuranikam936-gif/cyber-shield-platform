import psutil

def get_running_processes():
    processes = []
    for process in psutil.process_iter(['pid', 'name']):
        try:
            processes.append(process.info['name'])
        except:
            pass
    print(processes[:10])
    
    return processes[:10]