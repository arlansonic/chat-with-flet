import flet as ft


def main(pagina):
    text = ft.Text(
        "Hero Zap",
        color=ft.colors.PURPLE_500,
        italic=True,
        size=50,
    )

    img = ft.Image(
        src=f"src/assets/hero.png",
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
    )

    chat = ft.Column()

    def sendMessageTunel(mensagem):
        type = mensagem["type"]
        if type == "message":
            textMessage = mensagem["text"]
            userMessage = mensagem["user"]
            chat.controls.append(ft.Text(f"{textMessage}: {userMessage} "))
        else:
            userMessage = mensagem["user"]
            chat.controls.append(
                ft.Text(
                    f"{userMessage} entrou no chat!",
                    size=12,
                    italic=True,
                    color=ft.colors.PURPLE_500,
                )
            )
        pagina.update()

    pagina.pubsub.subscribe(sendMessageTunel)

    def sendMessage(event):
        pagina.pubsub.send_all(
            {"user": nameUser.value, "text": bodyMessage.value, "type": "message"}
        )
        bodyMessage.value = ""
        pagina.update()

    nameUser = ft.TextField(label="Nome do usuário")
    bodyMessage = ft.TextField(label="Digite sua mensagem", on_submit=sendMessage)
    buttonSendMessage = ft.ElevatedButton("Enviar", on_click=sendMessage)

    def startPopup(event):
        pagina.pubsub.send_all({"user": nameUser.value, "type": "Prohibited"})
        pagina.add(chat)
        popup.open = False
        pagina.remove(button_start)
        pagina.remove(text)

        pagina.add(ft.Row([bodyMessage, buttonSendMessage]))
        pagina.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Welcome to SonicZap"),
        content=nameUser,
        actions=[ft.ElevatedButton("Entrar", on_click=startPopup)],
    )

    def startChat(event):
        pagina.add(popup)
        popup.open = True
        pagina.update()

    button_start = ft.ElevatedButton("Iniciar chat", on_click=startChat)

    pagina.add(text)
    pagina.add(button_start)
    pagina.add(img)


# ft.app(target=main)

ft.app(target=main, view=ft.WEB_BROWSER, port=8000)
