import flet as ft

# --- CONFIGURATION DU DESIGN ---
BG_COLOR = "#050508"
CYAN_NEON = "#00ffff"
MAGENTA_NEON = "#ff00ff"
GLASS_WHITE = "rgba(255, 255, 255, 0.05)"

class GlassCard(ft.Container):
    """Composant de carte à effet de verre avec bordure lumineuse."""
    def __init__(self, content, title=None, border_color=CYAN_NEON, expand=False):
        # Construction du contenu interne
        inner_content = ft.Column([
            ft.Text(title, size=18, weight=ft.FontWeight.BOLD, color=border_color) if title else ft.Container(),
            ft.Divider(color=ft.Colors.with_opacity(0.1, border_color), height=1) if title else ft.Container(),
            content
        ], spacing=15)
        
        super().__init__(
            content=inner_content,
            bgcolor=GLASS_WHITE,
            padding=20,
            border_radius=15,
            expand=expand,
            blur=ft.Blur(15, 15, ft.BlurTileMode.CLAMP),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.3, border_color)),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.with_opacity(0.15, border_color),
            )
        )

async def main(page: ft.Page):
    # Configuration de la fenêtre et de la page
    page.title = "LANShare - Partage de fichiers local"
    page.bgcolor = BG_COLOR
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    
    # Paramètres de la fenêtre (Compatibilité Flet 0.25.0+)
    page.window.width = 1150
    page.window.height = 850
    page.window.min_width = 800
    page.window.min_height = 600

    # Sélecteur de fichiers
    async def on_pick_files(e):
        try:
            # pick_files est une coroutine qui retourne les fichiers sélectionnés dans Flet 0.80+
            files = await file_picker.pick_files()
            if files:
                print(f"Fichier prêt à l'envoi : {files[0].name}")
        except Exception as ex:
            print(f"Erreur lors de la sélection : {ex}")

    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)

    # --- PANNEAU DE GAUCHE : DASHBOARD RÉSEAU ---
    peers_list = ft.Column([
        ft.ListTile(
            leading=ft.Icon(ft.Icons.COMPUTER, color=CYAN_NEON),
            title=ft.Text("Poste-De-Travail-01", color="white"),
            subtitle=ft.Text("192.168.1.45 • Latence: 5ms", color="gray", size=12),
            trailing=ft.Text("EN LIGNE", color=CYAN_NEON, size=10, weight=ft.FontWeight.BOLD)
        ),
        ft.ListTile(
            leading=ft.Icon(ft.Icons.SMARTPHONE, color=MAGENTA_NEON),
            title=ft.Text("iPhone-De-Jean", color="white"),
            subtitle=ft.Text("192.168.1.12 • Latence: 18ms", color="gray", size=12),
        ),
    ], scroll=ft.ScrollMode.AUTO, spacing=5)

    left_panel = GlassCard(
        title="Appareils à proximité",
        content=peers_list,
        border_color=CYAN_NEON,
        expand=1
    )

    # --- PANNEAU CENTRAL : RADAR DE DÉCOUVERTE ---
    radar_visual = ft.Stack([
        ft.Container(width=220, height=220, border=ft.Border.all(1, "rgba(0, 255, 255, 0.1)"), border_radius=110),
        ft.Container(width=160, height=160, border=ft.Border.all(1, "rgba(0, 255, 255, 0.2)"), border_radius=80),
        ft.Container(
            content=ft.Icon(ft.Icons.WIFI, color=CYAN_NEON, size=40),
            width=100, height=100, 
            border=ft.Border.all(2, CYAN_NEON),
            border_radius=50, 
            alignment=ft.Alignment.CENTER,
            shadow=ft.BoxShadow(blur_radius=20, color=ft.Colors.with_opacity(0.3, CYAN_NEON))
        ),
    ], alignment=ft.Alignment.CENTER)

    radar_content = ft.Column([
        radar_visual,
        ft.Container(height=20),
        ft.Text("LANShare Radar", size=26, weight=ft.FontWeight.BOLD, color="white"),
        ft.Text("Recherche de pairs sur le réseau...", italic=True, color="cyan", size=14),
        ft.Container(height=30),
        ft.Row([
            ft.OutlinedButton(
                content=ft.Text("Choisir Fichier"), 
                icon=ft.Icons.UPLOAD_FILE, 
                on_click=on_pick_files,
                style=ft.ButtonStyle(color=CYAN_NEON)
            ),
            ft.Switch(label="Auto-Zip", value=True, active_color=MAGENTA_NEON),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)
    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    center_panel = GlassCard(
        content=radar_content,
        border_color=CYAN_NEON,
        expand=2
    )

    # --- PANNEAU DE DROITE : VISUALISEUR DE TRANSFERTS ---
    queue_items = ft.Column([
        ft.Container(
            content=ft.Row([
                ft.Icon(ft.Icons.VIDEO_FILE, color=MAGENTA_NEON),
                ft.Column([
                    ft.Text("Presentation_Finale.mp4", size=12, color="white", weight=ft.FontWeight.W_500),
                    ft.ProgressBar(value=0.75, width=180, color=MAGENTA_NEON, bgcolor="rgba(255,0,255,0.1)"),
                    ft.Row([
                        ft.Text("75%", size=10, color="gray"),
                        ft.Text("12 MB/s", size=10, color="gray"),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                ], spacing=5, expand=True)
            ]),
            padding=15, bgcolor="rgba(255,255,255,0.03)", border_radius=10, border=ft.Border.all(1, "rgba(255,255,255,0.05)")
        )
    ], scroll=ft.ScrollMode.AUTO, spacing=10)

    right_panel = GlassCard(
        title="Transferts en cours",
        content=ft.Column([
            ft.Text("Statistiques de vitesse", size=14, color="white"),
            ft.Container(
                height=100, 
                border=ft.Border.all(1, "rgba(255,0,255,0.2)"), 
                border_radius=10,
                bgcolor="rgba(0,0,0,0.2)",
                content=ft.Icon(ft.Icons.TIMELINE, color="rgba(255,0,255,0.3)", size=40),
                alignment=ft.Alignment.CENTER
            ),
            ft.Divider(height=20, color="transparent"),
            ft.Text("File d'attente", size=14, color=MAGENTA_NEON, weight=ft.FontWeight.BOLD),
            queue_items
        ]),
        border_color=MAGENTA_NEON,
        expand=1
    )

    # --- ASSEMBLAGE DU LAYOUT ---
    main_layout = ft.Row([
        left_panel,
        center_panel,
        right_panel
    ], spacing=20, alignment=ft.MainAxisAlignment.CENTER, expand=True)

    page.add(main_layout)

if __name__ == "__main__":
    ft.run(main)