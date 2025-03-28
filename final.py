import tkinter as tk
from PIL import Image, ImageTk
from IA import IA

reponse_ia = "bonjour"
font_size = 16
bot = IA()

def afficher_texte(event=None):
    texte = e1.get()
    if texte:
        champ_ia.config(state=tk.NORMAL)
        champ_ia.insert(tk.END, f"Vous: {texte}\n", 'user')

        reponse_ia = bot.send_message(texte)

        champ_ia.insert(tk.END, "IA: " + reponse_ia + "\n", 'ia')
        champ_ia.yview(tk.END)
        champ_ia.config(state=tk.DISABLED)
        e1.delete(0, tk.END)
        e1.focus()


def demarrer_chatbot():
    frame_bienvenue.pack_forget()
    frame_chat.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

master = tk.Tk()
master.state('zoomed')
master.title("Chatbot IA")
master.geometry("600x500")
master.config(bg="#2F2F2F")
master.option_add("*TButton*font", ('Arial', font_size))
master.option_add("*Label*font", ('Arial', font_size))

frame_bienvenue = tk.Frame(master, bg="#2F2F2F")
frame_bienvenue.pack(fill=tk.BOTH, expand=True)

image_bg = Image.open("IA/phototrobi1.webp")
photo_bg = ImageTk.PhotoImage(image_bg)
label_bg = tk.Label(frame_bienvenue, image=photo_bg)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)
label_bg.lower()

label_bienvenue = tk.Label(
    frame_bienvenue,
    text="Bienvenue à l'Hôtel California !\nCliquez sur le bouton ci-dessous pour accéder au Chatbot :3",
    fg="#D3D3D3", bg="#2F2F2F", font=("Arial", 16), justify="center"
)
label_bienvenue.pack(pady=30)

btn_acceder = tk.Button(
    frame_bienvenue,
    text="Accéder au Chatbot",
    command=demarrer_chatbot,
    bg="#4CAF50", fg="black", bd=2, relief="solid", font=("Arial", 14)
)
btn_acceder.pack()

frame_chat = tk.Frame(master, bg="#2F2F2F")

champ_ia = tk.Text(
    frame_chat,
    height=15, width=70,
    wrap="word",
    state=tk.DISABLED,
    bg="#1E1E1E", fg="#D3D3D3",
    font=("Arial", font_size), bd=2, relief="solid"
)
champ_ia.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
champ_ia.tag_config('user', foreground="#ADD8E6", justify='left')
champ_ia.tag_config('ia', foreground="#90EE90", justify='left')

e1 = tk.Entry(
    frame_chat,
    font=('Arial', font_size),
    bd=2, relief="solid",
    width=50,
    bg="#1E1E1E", fg="#D3D3D3"
)
e1.pack(padx=10, pady=10)

btn_envoyer = tk.Button(
    frame_chat,
    text="Envoyer",
    command=afficher_texte,
    bg="#4CAF50", fg="black", bd=2, relief="solid", width=15
)
btn_envoyer.pack(pady=10)

master.bind('<Return>', afficher_texte)
master.grid_rowconfigure(0, weight=1)
master.grid_rowconfigure(1, weight=0)
master.grid_rowconfigure(2, weight=0)
e1.focus()

master.mainloop()

