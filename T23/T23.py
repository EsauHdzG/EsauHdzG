import pyautogui
import subprocess
import datetime
#Fecha y hora actuales
now = datetime.datetime.now()
time = now.strftime("%Y-%m-%d_%H-%M-%S")
filename_captura = f'screenshot_{time}.png'
#Toma de captura
try:
    captura = pyautogui.screenshot()
    captura.save(filename_captura)
except Exception as e:
    print("Ocurrio un erro en la captura: {e}")
#Subprocess
result = subprocess.run('tasklist', shell=True, capture_output=True, text=True)
filename = f'subprocess_{time}.txt'
if result.returncode==0:
    with open(filename, 'w') as file:
        file.write(result.stdout)
else:
    print("No se ejecuto el comando: ",result.stderr)
    
    

 
