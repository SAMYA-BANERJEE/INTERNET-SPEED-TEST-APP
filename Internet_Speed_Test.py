import tkinter as tk
import speedtest

class Speed_Test:
    def download_speed(self):
        self.st = speedtest.Speedtest()
        # Get a list of available servers
        servers = self.st.get_servers()
        # Select the best server manually (optional)
        self.st.get_best_server()
        
        self.download_speed = round(self.st.download() / (1024 * 1024), 2)
        return self.download_speed

    def upload_speed(self):
        # Get upload speed (in bits per second, divide by 1024 * 1024 to convert to Mbps)
        self.upload_speed = round(self.st.upload() / (1024 * 1024), 2)
        return self.upload_speed

    def ping(self):
        # Get the best server based on ping
        self.st.get_best_server()
        # Get ping (in milliseconds)
        self.ping_result = round(self.st.results.ping, 2)
        return self.ping_result


class TASK_BAR_IMAGE(Speed_Test):
    def __init__(self, parent,box_image_instance):
        super().__init__()
        self.boximg = tk.PhotoImage(file="taskbar_1_.png")
        self.boxlabel = tk.Label(parent, image=self.boximg, background="gray5")
        self.boxlabel.place(x=0, y=0)
        # ping:
        self.ping_ = tk.Label(parent, text="00.00", font="arial 14 bold", background="#384056", fg="white", bd=0)
        self.ping_.place(x=47, y=77)
        # download:
        self.download = tk.Label(parent, text="00.00", font="arial 14 bold", background="#384056", fg="white", bd=0)
        self.download.place(x=156, y=77)
        # upload:
        self.upload = tk.Label(parent, text="00.00", font="arial 14 bold", background="#384056", fg="white", bd=0)
        self.upload.place(x=266, y=77)

        self.box_image = box_image_instance
    def speed_check(self):
        # Store the download speed result in a variable
        download_result = self.download_speed()
        # Update the labels with the speed result
        self.download.configure(text=download_result)
        self.box_image.speed_show.configure(text=f"{download_result}\nMBPS")

        # After 2 seconds, calculate and display the upload speed and ping
        self.download.after(10, self.get_upload_and_ping)

    def get_upload_and_ping(self):
        # Get upload speed and ping
        self.upload.configure(text=self.upload_speed())
        self.box_image.speed_show.configure(text=f"{self.upload_speed}\nMBPS")
        self.box_image.download_label.configure(text="    Upload   ")        
        self.ping_.configure(text=self.ping())


class BOX_IMAGE():
    def __init__(self, parent):
        super().__init__()

        self.task_img = tk.PhotoImage(file="blue_box.png")
        self.task_image_label = tk.Label(parent, image=self.task_img, background="gray5")
        self.task_image_label.place(x=0, y=170)

        self.speed_show=tk.Label(parent,text="00.00",font="arial 26 bold", background="#384056",fg="black")
        self.speed_show.place(x=135,y=330)

        self.download_label=tk.Label(parent,text=" Download ",font="arial 18 bold", background="#384056",fg="white")
        self.download_label.place(x=116,y=450)


class BLUE_BUTTON:
    def __init__(self, parent, task_bar_instance):
        super().__init__()

        self.button_img = tk.PhotoImage(file="blue_button.png")
        self.button = tk.Button(parent, image=self.button_img, background="gray5", activebackground="gray5", bd=0, cursor="hand2", command= task_bar_instance.speed_check)
        self.button.place(x=80, y=535)


class APP(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("365x630")
        self.resizable(False, False)
        self.wm_iconbitmap("net_speed_icon.ico")
        self.title("Internet Speed Test")
        self.config(background="gray5")
        self.app_photo = BOX_IMAGE(self)
        self.task_image = TASK_BAR_IMAGE(self, self.app_photo )
        self.button = BLUE_BUTTON(self, self.task_image)
        self.mainloop()

a = APP()