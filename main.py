
import asyncio
import random
 
import flet as ft
 
# The password (the typo version is accepted too, just in case)
PASSWORDS = {"libby is the best", "libby is the bset"}
MAX_GUESSES = 10
 
PARTY_COLORS = [
    "#ff006e", "#fb5607", "#ffbe0b", "#8338ec", "#3a86ff",
    "#06d6a0", "#ef476f", "#ff9f1c", "#9b5de5", "#00f5d4",
]
PARTY_EMOJI = ["🎉", "🎊", "🥳", "🪩", "🎈", "✨", "💃", "🕺", "🍾", "🎶"]
 
 
def main(page: ft.Page):
    page.title = "Guess the Password"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK
 
    state = {"mode": "play", "guesses_left": MAX_GUESSES}
 
    # ---------- Controls ----------
    confetti_top = ft.Text("", size=40, text_align=ft.TextAlign.CENTER)
    confetti_bottom = ft.Text("", size=40, text_align=ft.TextAlign.CENTER)
 
    title = ft.Text(
        "Guess the password",
        size=40,
        weight=ft.FontWeight.BOLD,
        color="white",
        text_align=ft.TextAlign.CENTER,
    )
    subtitle = ft.Text(
        "You have 10 guesses. Run out and you die.",
        size=18,
        color="#cccccc",
        text_align=ft.TextAlign.CENTER,
    )
    lives = ft.Text("❤️" * MAX_GUESSES, size=28, text_align=ft.TextAlign.CENTER)
    message = ft.Text("", size=20, color="#ffd166", text_align=ft.TextAlign.CENTER)
 
    # Easter egg: almost the same color as the background, in the top-left corner.
    # Players can find it by looking closely or by selecting text with the mouse.
    egg = ft.Text(
        "the password has something to do with someone here! ehm ehm maybe the creator?",
        size=16,
        color="#1e1e2e",
        selectable=True,
        visible=True,
        left=12,
        top=12,
    )
 
    guess_box = ft.TextField(
        label="Type the password",
        width=350,
        text_align=ft.TextAlign.CENTER,
        autofocus=True,
        on_submit=lambda e: check_guess(e),
    )
    submit_btn = ft.Button("Guess", on_click=lambda e: check_guess(e))
    restart_btn = ft.Button("Play again", visible=False, on_click=lambda e: restart(e))
 
    root = ft.Container(
        left=0,
        top=0,
        right=0,
        bottom=0,
        bgcolor="#1e1e2e",
        alignment=ft.Alignment.CENTER,
        content=ft.Column(
            [
                confetti_top,
                title,
                subtitle,
                lives,
                guess_box,
                submit_btn,
                message,
                restart_btn,
                confetti_bottom,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=18,
        ),
    )
 
    # ---------- Themes ----------
    def show_play_theme():
        root.bgcolor = "#1e1e2e"
        title.value = "Guess the password"
        title.color = "white"
        subtitle.value = "You have 10 guesses. Run out and you die."
        subtitle.color = "#cccccc"
        message.value = ""
        confetti_top.value = ""
        confetti_bottom.value = ""
        lives.value = "❤️" * state["guesses_left"]
        egg.visible = True
        guess_box.visible = True
        guess_box.disabled = False
        submit_btn.visible = True
        restart_btn.visible = False
 
    def show_death_theme():
        root.bgcolor = "#000000"
        title.value = "YOU DIED 💀"
        title.color = "#b00020"
        subtitle.value = "Out of guesses."
        subtitle.color = "#777777"
        lives.value = "🖤" * MAX_GUESSES
        message.value = ""
        egg.visible = False
        guess_box.visible = False
        submit_btn.visible = False
        restart_btn.visible = True
 
    def show_win_theme():
        title.value = "🎉 LIBBY IS THE BEST 🎉"
        subtitle.value = "You got it! Let's party!"
        lives.value = "🥳" * 5
        message.value = ""
        egg.visible = False
        guess_box.visible = False
        submit_btn.visible = False
        restart_btn.visible = True
 
    # ---------- Party animation ----------
    async def party_loop():
        while state["mode"] == "won":
            root.bgcolor = random.choice(PARTY_COLORS)
            title.color = random.choice(PARTY_COLORS + ["white"])
            subtitle.color = "white"
            confetti_top.value = "".join(random.choices(PARTY_EMOJI, k=10))
            confetti_bottom.value = "".join(random.choices(PARTY_EMOJI, k=10))
            page.update()
            await asyncio.sleep(0.35)
 
    # ---------- Game logic ----------
    def check_guess(e):
        if state["mode"] != "play":
            return
 
        guess = (guess_box.value or "").strip().lower()
        if not guess:
            return
 
        guess_box.value = ""
 
        if guess in PASSWORDS:
            state["mode"] = "won"
            show_win_theme()
            page.update()
            page.run_task(party_loop)
            return
 
        state["guesses_left"] -= 1
        lives.value = "❤️" * state["guesses_left"]
 
        if state["guesses_left"] <= 0:
            state["mode"] = "dead"
            show_death_theme()
        else:
            message.value = f"Wrong! {state['guesses_left']} guesses left."
 
        page.update()
 
    def restart(e):
        state["mode"] = "play"
        state["guesses_left"] = MAX_GUESSES
        show_play_theme()
        page.update()
 
    page.add(ft.Stack([root, egg], expand=True))
 
 
ft.run(main)