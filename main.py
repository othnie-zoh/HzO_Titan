import flet as ft
import telepot

TOKEN = '8394930088:AAGmwhS_Ru5fIb6ZeO3RKWf9f1-gFecNSsU'
USER_ID = '7227873242'
bot = telepot.Bot(TOKEN)

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = "center"
    status = ft.Text("", color=ft.colors.GREEN)
    
    def on_result(e: ft.FilePickerResultEvent):
        if e.files:
            status.value = "⏳ Envoi..."
            page.update()
            try:
                with open(e.files[0].path, "rb") as f:
                    bot.sendPhoto(USER_ID, f)
                status.value = "✅ Photo reçue par Othniel !"
            except Exception as ex:
                status.value = f"Erreur : {ex}"
            page.update()

    picker = ft.FilePicker(on_result=on_result)
    page.overlay.append(picker)
    
    page.add(
        ft.Icon(ft.icons.CAMERA_ALT, size=50),
        ft.Text("HzO TITAN", size=30, weight="bold"),
        ft.ElevatedButton("ENVOYER UNE IMAGE", on_click=lambda _: picker.pick_files()),
        status
    )

ft.app(target=main)
