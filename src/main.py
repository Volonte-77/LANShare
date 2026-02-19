import flet as ft

def main(page: ft.Page):
    page.title = "LANShare - Partage de fichiers"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Label pour afficher le fichier choisi
    file_label = ft.Text("Aucun fichier sélectionné")

    # Fonction appelée quand on choisit un fichier
    def pick_file_result(e: ft.FilePickerResultEvent):
        if e.files:
            file_label.value = f"Fichier choisi: {e.files[0].name}"
        else:
            file_label.value = "Aucun fichier sélectionné"
        page.update()

    # FilePicker
    file_picker = ft.FilePicker(on_result=pick_file_result)
    page.overlay.append(file_picker)

    # Bouton pour ouvrir le FilePicker
    pick_button = ft.ElevatedButton("Choisir un fichier", on_click=lambda _: file_picker.pick_files())

    # Bouton pour envoyer (pour l'instant juste un print)
    send_button = ft.ElevatedButton("Envoyer", on_click=lambda _: print("Envoi du fichier..."))

    page.add(file_label, pick_button, send_button)

ft.app(target=main)