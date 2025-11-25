import customtkinter as ctk
from PIL import Image

# =========================
#   CONFIG
# =========================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

AFYA_PINK = "#E4006F"
AFYA_PINK_LIGHT = "#ff4fa3"
WHITE = "#ffffff"

app = ctk.CTk()
app.geometry("950x520")
app.title("Login - Ultra Premium Glass")
app.resizable(False, False)


# =========================
#  LEFT SIDE WITH LOGO
# =========================
left_frame = ctk.CTkFrame(app, width=480, fg_color="#111")
left_frame.pack(side="left", fill="both")


label_bg = ctk.CTkLabel(left_frame, text="")
label_bg.place(relx=0.5, rely=0.5, anchor="center")


# =========================
#  GLASSMORPHISM CARD
# =========================
glass_frame = ctk.CTkFrame(
    app,
    width=430,
    height=500,
    fg_color=("white", "#ffffff"),
    corner_radius=35
)
glass_frame.place(x=500, y=10)

# --- Glass Effect (blur REAL)
glass_effect = ctk.CTkFrame(
    glass_frame,
    fg_color="#ffffff",
    corner_radius=35,
)
glass_effect.pack(fill="both", expand=True, padx=3, pady=3)

glass_effect.configure(
    bg_color="#ffffff",
)

# To simulate blur: use semi-transparent layer
overlay = ctk.CTkFrame(
    glass_effect,
    fg_color="#ffffff",  # transparência verdadeira
    corner_radius=35
)
overlay.pack(fill="both", expand=True)


# =========================
#  CONTENT INSIDE GLASS
# =========================
content = ctk.CTkFrame(overlay, fg_color="transparent")
content.pack(fill="both", expand=True, padx=30, pady=25)


title = ctk.CTkLabel(
    content,
    text="Welcome Back!",
    font=("Segoe UI", 32, "bold"),
    text_color=AFYA_PINK
)
title.pack(pady=(10, 5))

subtitle = ctk.CTkLabel(
    content,
    text="Sign in to continue",
    font=("Segoe UI", 15),
    text_color="#555"
)
subtitle.pack(pady=(0, 25))


# =========================
#   NEW INPUT STYLE
# =========================

def input_field(placeholder):
    entry = ctk.CTkEntry(
        content,
        width=300,
        height=45,
        fg_color="#ffffff",
        text_color="black",
        border_color=AFYA_PINK,
        border_width=2,
        placeholder_text=placeholder,
        corner_radius=15
    )
    entry.pack(pady=10)
    return entry

email = input_field("Email")
password = input_field("Password")


# =========================
#  LOGIN BUTTON
# =========================
login_btn = ctk.CTkButton(
    content,
    text="Login",
    width=300,
    height=45,
    fg_color=AFYA_PINK,
    hover_color=AFYA_PINK_LIGHT,
    corner_radius=15,
    font=("Segoe UI", 17, "bold")
)
login_btn.pack(pady=(20, 12))


# =========================
#  GOOGLE
# =========================
google_btn = ctk.CTkButton(
    content,
    text="Continue with Google",
    width=300,
    height=45,
    fg_color="#ffffff",
    text_color="black",
    corner_radius=15,
    border_width=1,
    border_color="#bbb",
    hover_color="#f2f2f2"
)
google_btn.pack(pady=5)


# =========================
#  SIGN UP
# =========================
footer = ctk.CTkLabel(
    content,
    text="Don't have an account?  Sign up",
    font=("Segoe UI", 12),
    text_color="#444"
)
footer.pack(pady=5)


app.mainloop()
