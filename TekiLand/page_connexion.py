#Code pas terminé, on a fait de notre mieux. On a essayé d'utiliser seulement des tutos youtube et évité chatGPT.
#Pour se connecter login = admind et mdp = 1234


from tkinter import *
from tkinter import messagebox
import ast
# ----------------------------------------------------------------------------
screen = Tk()
screen.title("TekIland")
screen.geometry("900x500")
screen.configure(bg="#000000")
screen.resizable(False, False)
# ----------------------------------------------------------------------------
def signup_command():
    fenetre=Toplevel(screen)
    fenetre.title("Inscription")
    fenetre.geometry("900x500")
    fenetre.configure(bg="black")
    fenetre.resizable(False, False)
    #--------------------------------------------------------------------------------------------
    def inscrip():
        username=user.get()
        password=mdp.get()
        conform_password=conf_mdp.get()

        if password==conform_password:
            messagebox.showinfo("OK")

        else:
            messagebox.showerror("Invalide", "Les mots de passes doivent correspondre")
    #--------------------------------------------------------------------------------------------
    def sign():
        fenetre.destroy()
    #--------------------------------------------------------------------------------------------
    img = PhotoImage(file="TekiLand.png")
    Label(fenetre, image=img, bg="#000000").place(x=5, y=-55)
    #--------------------------------------------------------------------------------------------
    zone = Frame(fenetre, width=350, height=350, bg="black")
    zone.place(x=460, y=80)

    entt = Label(fenetre, text="Inscription", fg="#FF5757", bg="black", font=("Verdana", 25, "bold"))
    entt.place(x=580, y=90)
    #--------------------------------------------------------------------------------------------
    def on_enter(e):
        user.delete(0, "end")
    def on_leave(e):
        if user.get()=="":
            user.insert(0, "Pseudo")

    user = Entry(fenetre, width=25, fg="#68696E", border=0, bg="black", font=("Verdana", 15,))
    user.place(x=580, y=170)
    user.insert(0, "Pseudo")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(fenetre, width=295, height=2, bg="#FF5757").place(x=580, y=200)
    #--------------------------------------------------------------------------------------------
    def on_enter(e):
        mdp.delete(0, "end")

    def on_leave(e):
        if mdp.get()=="":
            mdp.insert(0, "Mot de passe")

    mdp = Entry(fenetre, width=25, fg="#68696E", border=0, bg="black", font=("Verdana", 15,))
    mdp.place(x=580, y=240)
    mdp.insert(0, "Mot de passe")
    mdp.bind("<FocusIn>", on_enter)
    mdp.bind("<FocusOut>", on_leave)

    Frame(fenetre, width=295, height=2, bg="#FF5757").place(x=580, y=270)
    #--------------------------------------------------------------------------------------------
    def on_enter(e):
        conf_mdp.delete(0, "end")

    def on_leave(e):
        if conf_mdp.get()=="":
            conf_mdp.insert(0, "Confirmer mot de passe")

    conf_mdp = Entry(fenetre, width=25, fg="#68696E", border=0, bg="black", font=("Verdana", 15,))
    conf_mdp.place(x=580, y=310)
    conf_mdp.insert(0, "Confirmer mot de passe")
    conf_mdp.bind("<FocusIn>", on_enter)
    conf_mdp.bind("<FocusOut>", on_leave)

    Frame(fenetre, width=295, height=2, bg="#FF5757").place(x=580, y=340)
    #--------------------------------------------------------------------------------------------
    Button(fenetre, width=15, pady=5, text="S'inscrire", bg="#FF5757", fg="#68696E", border=0, command=inscrip,  font=("Verdana", 15,)).place(x=580, y=370)
    label=Label(fenetre, text="J'ai déjà un compte : ", fg="#FF5757", bg="black", font=("Verdana", 10))
    label.place(x=580, y=430)

    se_connecter = Button(fenetre, width=15, text="Se connecter", border=0, bg="black", cursor="hand2", fg="#68696E", command=sign)
    se_connecter.place(x=720, y=430)
    #--------------------------------------------------------------------------------------------


    fenetre.mainloop()
# ----------------------------------------------------------------------------
def inscrip():
    psseudo = user.get()
    mddp = mdp.get()

    if psseudo == "admin" and mddp == "1234":
        ecran = Toplevel(screen)
        ecran.title("App")
        ecran.geometry("700x250")
        screen.config(bg="black")

        Label(ecran, text="Loading...", bg="black", fg="#FF5757", font=("Verdana", 50, "bold")).pack(expand=True)

    elif psseudo != "admin" and mddp != "1234":
        messagebox.showerror("Échec", "Pseudo et mot de passe invalide")

    elif mddp != "1234":
        messagebox.showerror("Échec", "Mot de passe invalide")

    elif psseudo != "admin":
        messagebox.showerror("Échec", "Pseudo invalide")
# ----------------------------------------------------------------------------
img = PhotoImage(file="TekiLand.png")
Label(screen, image=img, bg="#000000").place(x=5, y=-55)

zone = Frame(screen, width=350, height=350, bg="black")
zone.place(x=460, y=80)

txt_principal = Label(screen, text="TekiLand, la plateforme de chat tech !", bg="black", fg="#68696E",font=("Verdana, 11"))
txt_principal.place(x=130, y=280)

entt = Label(screen, text="Connexion", fg="#FF5757", bg="black", font=("Verdana", 25, "bold"))
entt.place(x=580, y=90)
# ----------------------------------------------------------------------------
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Pseudo')

user = Entry(screen, width=25, fg="#68696E", border=0, bg="black", font=("Verdana", 15,))
user.place(x=580, y=170)
user.insert(0, "Pseudo")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(screen, width=295, height=2, bg="#FF5757").place(x=580, y=200)
# ----------------------------------------------------------------------------
def on_enter(e):
    mdp.delete(0, 'end')

def on_leave(e):
    name = mdp.get()
    if name == '':
        mdp.insert(0, 'Mot de passe')

mdp = Entry(screen, width=25, fg="#68696E", border=0, bg="black", font=("Verdana", 15,))
mdp.place(x=580, y=270)
mdp.insert(0, "Mot de passe")
mdp.bind('<FocusIn>', on_enter)
mdp.bind('<FocusOut>', on_leave)

Frame(screen, width=295, height=2, bg="#FF5757").place(x=580, y=300)
# ----------------------------------------------------------------------------
Button(screen, width=15, pady=5, text="Se connecter", bg="#FF5757", fg="#68696E", border=0, font=("Verdana", 15,),
       command=inscrip).place(x=580, y=330)
label = Label(screen, text="Pas de compte ?", fg="#FF5757", bg="black", font=("Verdana", 10))
label.place(x=580, y=400)

inscirption = Button(screen, width=15, text="Créer un compte", border=0, bg="black", cursor="hand2", fg="#68696E", command=signup_command)
inscirption.place(x=700, y=401)
# ----------------------------------------------------------------------------
screen.mainloop()
