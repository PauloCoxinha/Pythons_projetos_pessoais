import flet as ft 
from flet import Checkbox, FloatingActionButton, Icons, Page, TextField

def main(page: ft.Page):
    def add_clicked(e):
        task_view.controls.append(Checkbox(label=new_task.value))
        new_task.value = ''
        print(e)        
        page.update()

    new_task = TextField(hint_text="O que você quer fazer?", expand=True)
    task_view = ft.Column()
    view = ft.Column(
        width=350,  
        controls=[
                ft.Row(
                    controls=[
                        new_task,
                        ft.FloatingActionButton(icon=Icons.ADD, on_click=add_clicked),    
                    ],
                ),
                task_view,
        ],
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)

    page.add(ft.Text(value="Seja bem vindo a tela mais legal dos animes"))
    pass

ft.run(main)


