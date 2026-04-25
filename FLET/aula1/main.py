import flet as ft 
from flet import Checkbox, FloatingActionButton, Icons, Page, TextField

def main(page: ft.Page):
    def add_clicked(e):

        page.add(Checkbox(label=new_task.value))
        new_task.value = ''
        print(e)
        page.update()

    new_task = TextField(hint_text="O que você quer fazer?")
    page.add(new_task, FloatingActionButton(icon=Icons.ADD, on_click=add_clicked))

    page.add(ft.Text(value="Seja bem vindo a tela mais legal dos animes"))
    pass

ft.run(main)


