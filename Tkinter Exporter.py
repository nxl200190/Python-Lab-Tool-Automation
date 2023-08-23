from tkinter import *
from PIL import Image, ImageTk
import pyautogui as py
import subprocess
import os
import glob
import threading
import time



def get_folders_in_directory(directory):
    folder_directories = []

    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_dir():
                folder_directories.append(entry.path)
    return folder_directories


def open_file_by_directory(directory):
    # Specify the directory where the files are located

    if os.path.exists(directory) and os.path.isdir(directory):
        # Find files with the specified extension in the directory
        files = glob.glob(os.path.join(directory, f"*.eds"))
        print(files)
        if len(files) == 0:
            print("No files found with the specified extension.")
        elif len(files) == 1:
            file_path = files[0]
            subprocess.run(f'"{file_path}"', shell=True)
        else:
            print("Multiple files found with the specified extension.")
    else:
        print("Directory does not exist.")


def png_match_task(snippet_path, x):
    while True:
        screen = py.screenshot()
        snippet_image = Image.open(snippet_path)
        snippet_location = py.locate(snippet_image, screen)

        if snippet_location:
            center_x = snippet_location.left + snippet_location.width // x
            center_y = snippet_location.top + snippet_location.height // 2

            py.moveTo(center_x, center_y, )
            py.click()
            break

    time.sleep(2)


def png_match_task2(snippet_path, x, y):
    while True:
        screen = py.screenshot()
        snippet_image = Image.open(snippet_path)
        snippet_location = py.locate(snippet_image, screen)

        if snippet_location:
            center_x = snippet_location.left + snippet_location.width // x
            center_y = snippet_location.top + snippet_location.height // y

            py.moveTo(center_x, center_y, )
            py.click()
            break

    time.sleep(2)


def check_state(snippet_path):
    while True:
        screen = py.screenshot()
        snippet_image = Image.open(snippet_path)
        snippet_location = py.locate(snippet_image, screen)
        if not snippet_location:
            break
        time.sleep(2)


def advance_with_tab(num):
    for _ in range(num):
        py.press('tab', interval=0.1)


def advance_with_down(num):
    for _ in range(num):
        py.press('down', interval=0.1)


def gene_expression_export():
    location = "temp"
    folder_path = r'C:\Users\openarray\Desktop\Images' + '\\' + location
    woList = get_folders_in_directory(folder_path)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    for WOs in woList:
        folders = get_folders_in_directory(WOs)
        for export_path in folders:
            open_file_by_directory(export_path)
            png_match_task(os.path.join(script_dir, 'Export Button.PNG'), 2)
            png_match_task(os.path.join(script_dir, 'Load Export Set.png'), 2)
            advance_with_tab(1)
            py.press('enter', interval=0.5)
            py.press('enter', interval=0.5)
            advance_with_tab(19)
            py.typewrite(export_path, interval=0)
            advance_with_tab(2)
            py.typewrite(export_path[-12:-7], interval=0)
            png_match_task(os.path.join(script_dir, 'Results Tab.PNG'), 1.08)
            png_match_task(os.path.join(script_dir, 'Selected Result.PNG'), 1.08)
            advance_with_tab(1)
            py.press('space', interval=0.5)
            advance_with_tab(1)
            py.press('space', interval=0.5)
            png_match_task(os.path.join(script_dir, 'Load Export Set.png'), 10)
            py.move(-100, 0)
            png_match_task(os.path.join(script_dir, 'Load Export Set.png'), 1.1)
            py.press('enter', interval=0.5)
            png_match_task(os.path.join(script_dir, 'Close.PNG'), 1.9)
            py.press('enter', interval=0.5)
            png_match_task(os.path.join(script_dir, 'Blank Screen.PNG'), 1)


def start_gene_expression():
    threading.Thread(target=gene_expression_export).start()
    window.destroy()


def ceph_genotyping():
    location = "temp"
    folder_path = r'C:\Users\openarray\Desktop\Images' + '\\' + location
    woList = get_folders_in_directory(folder_path)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    for WOs in woList:
        folders = get_folders_in_directory(WOs)
        for export_path in folders:
            open_file_by_directory(export_path)
            png_match_task(os.path.join(script_dir, 'Export Button.PNG'), 2)
            advance_with_tab(11)
            py.typewrite(export_path, interval=0)
            png_match_task(os.path.join(script_dir, 'Load Export Set.png'), 1.1)
            py.press('enter', interval=0.5)
            py.move(200, 0)
            png_match_task(os.path.join(script_dir, 'Load Export Set.png'), 1.1)
            py.press('enter', interval=0.5)
            png_match_task(os.path.join(script_dir, 'Setup.PNG'), 2)
            py.move(0, 150)
            py.click()
            png_match_task(os.path.join(script_dir, 'Import.PNG'), 2)
            advance_with_tab(13)
            advance_with_down(11)
            py.press('enter', interval=1)
            py.press('enter', interval=1)
            py.move(-130, 350)
            py.click()
            png_match_task(os.path.join(script_dir, 'Analyze.PNG'), 1.9)
            check_state(os.path.join(script_dir, 'AnalysisProg.PNG'))
            png_match_task(os.path.join(script_dir, 'Close.PNG'), 1.9)
            py.press('enter', interval=1)
            png_match_task(os.path.join(script_dir, 'Blank Screen.PNG'), 1)


def start_ceph_genotyping():
    threading.Thread(target=ceph_genotyping).start()
    window.destroy()


def cf1_genotyping():
    location = "temp"
    folder_path = r'C:\Users\openarray\Desktop\Images' + '\\' + location
    woList = get_folders_in_directory(folder_path)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    for WOs in woList:
        folders = get_folders_in_directory(WOs)
        for export_path in folders:
            open_file_by_directory(export_path)
            png_match_task(os.path.join(script_dir, 'Export Button.PNG'), 2)
            advance_with_tab(11)
            py.typewrite(export_path, interval=0)
            png_match_task(os.path.join(script_dir, 'Load Export Set.png'), 1.1)
            py.press('enter', interval=0.5)
            py.move(200, 0)
            png_match_task(os.path.join(script_dir, 'Load Export Set.png'), 1.1)
            py.press('enter', interval=0.5)
            png_match_task(os.path.join(script_dir, 'Setup.PNG'), 2)
            py.move(0, 150)
            py.click()
            png_match_task(os.path.join(script_dir, 'Import.PNG'), 2)
            advance_with_tab(13)
            advance_with_down(10)
            py.press('enter', interval=1)
            py.press('enter', interval=1)
            py.move(-130, 350)
            py.click()
            png_match_task(os.path.join(script_dir, 'Analyze.PNG'), 1.9)
            check_state(os.path.join(script_dir, 'AnalysisProg.PNG'))
            png_match_task(os.path.join(script_dir, 'Close.PNG'), 1.9)
            py.press('enter', interval=1)
            png_match_task(os.path.join(script_dir, 'Blank Screen.PNG'), 1)


def start_cf1_genotyping():
    threading.Thread(target=cf1_genotyping).start()
    window.destroy()


def cf2_genotyping():
    location = "temp"
    folder_path = r'C:\Users\openarray\Desktop\Images' + '\\' + location
    woList = get_folders_in_directory(folder_path)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    for WOs in woList:
        folders = get_folders_in_directory(WOs)
        for export_path in folders:
            open_file_by_directory(export_path)
            png_match_task(os.path.join(script_dir, 'Export Button.PNG'), 2)
            advance_with_tab(11)
            py.typewrite(export_path, interval=0)
            png_match_task(os.path.join(script_dir, 'Load Export Set.png'), 1.1)
            py.press('enter', interval=0.5)
            py.move(200, 0)
            png_match_task(os.path.join(script_dir, 'Load Export Set.png'), 1.1)
            py.press('enter', interval=0.5)
            png_match_task(os.path.join(script_dir, 'Setup.PNG'), 2)
            py.move(0, 150)
            py.click()
            png_match_task(os.path.join(script_dir, 'Import.PNG'), 2)
            advance_with_tab(13)
            advance_with_down(9)
            py.press('enter', interval=1)
            py.press('enter', interval=1)
            py.move(-130, 350)
            py.click()
            png_match_task(os.path.join(script_dir, 'Analyze.PNG'), 1.9)
            check_state(os.path.join(script_dir, 'AnalysisProg.PNG'))
            png_match_task(os.path.join(script_dir, 'Close.PNG'), 1.9)
            py.press('enter', interval=1)
            png_match_task(os.path.join(script_dir, 'Blank Screen.PNG'), 1)


def start_cf2_genotyping():
    threading.Thread(target=cf2_genotyping).start()
    window.destroy()


window = Tk()
window.title("Export Tool")
window.configure(bg="black")

window.geometry("1000x800")

image = Image.open("//Ple01file01/Open_Array/Quality_Control/01_QC Personnel/Nathan/My Projects/Export Imager/Data.gif")

new_size = (1050, 850)
image_resized = image.resize(new_size)

photo_resized = ImageTk.PhotoImage(image_resized)

label = Label(window, image=photo_resized, bg="white")  # Change background color to white
label.grid(row=0, column=0)

button_style = {"font": ("Helvetica", 14, "bold"), "bg": "lightblue", "fg": "black", "padx": 5, "pady": 5, "width": 20,
                "height": 5}
button1 = Button(window, text="Gene Expression", command=start_gene_expression, **button_style)
button1.place(x=100, y=200)

button2 = Button(window, text="CEPH", command=start_ceph_genotyping, **button_style)
button2.place(x=650, y=200)

button3 = Button(window, text="CF1 (non-192 Format)", command=start_cf1_genotyping, **button_style)
button3.place(x=100, y=600)

button3 = Button(window, text="CF2 (192 Format)", command=start_cf2_genotyping, **button_style)
button3.place(x=650, y=600)

window.mainloop()
