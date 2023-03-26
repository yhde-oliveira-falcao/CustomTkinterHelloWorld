import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x300")
app.title("Hello World example")


def button_callback():
    label_2.configure(text="Pythonista, Olá Mundo")


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text="Aperte o botão para ver a mensagem:", justify=customtkinter.LEFT)
label_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, text="Botão", command=button_callback)
button_1.pack(pady=10)

label_2 = customtkinter.CTkLabel(master=frame_1, text="", justify=customtkinter.LEFT)
label_2.pack(pady=10, padx=10)

app.mainloop()


#this code was inspired on the great work of TomSchimansky at https://github.com/TomSchimansky/CustomTkinter
#follow his examples to have a introduction to all the potential of customtkinter