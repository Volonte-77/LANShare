import flet as ft

# --- CONSTANTES DE DESIGN ---
# Couleurs futuristes
BG_COLOR = "#050508"
CYAN_NEON = "#00ffff"
MAGENTA_NEON = "#ff00ff"
GLASS_WHITE = "rgba(255, 255, 255, 0.05)"
GLASS_BORDER = "rgba(0, 255, 255, 0.2)"

class GlassCard(ft.Container):
    """Un conteneur stylisé effet 'verre' avec bordure néon."""
    def __init__(self, content, title=None, border_color=CYAN_NEON, expand=False):
        super().__init__()
        self.content = ft.Column([
            ft.Text(title, size=18, weight="bold", color=border_color) if title else ft.Container(),
            ft.Divider(color=ft.colors.with_opacity(0.1, border_color), height=1) if title else ft.Container(),
            content
        ], spacing=15)
        
        self.bgcolor = GLASS_WHITE
        self.padding = 20
        self.border_radius = 15
        self.expand = expand
        self.blur = ft.Blur(15, 15, ft.BlurTileMode.CLAMP)
        self.border = ft.border.all(1, ft.colors.with_opacity(0.3, border_color))
        # Ombre pour l'effet de lueur (Glow)
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors.with_opacity(0.15, border_color),
            offset=ft.Offset(0, 0),
        )

def main(page: ft.Page):
    # Configuration de la page
    page.title = "LANShare - Futuriste"
    page.bgcolor = BG_COLOR
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1100
    page.window_height = 800
    page.window_resizable = True
    # page.window_title_bar_hidden = True  # Décommenter pour un look sans bordure (nécessite gestion manuelle du bouton fermer)
    
    # --- SECTION 1 : DASHBOARD RÉSEAU (GAUCHE) ---
    peers_list = ft.Column([
        ft.ListTile(
            leading=ft.Icon(ft.icons.COMPUTER, color=CYAN_NEON),
            title=ft.Text("User_Alpha", color="white"),
            subtitle=ft.Text("192.168.1.15 • 12ms", color="gray"),
            trailing=ft.Text("ONLINE", color=CYAN_NEON, size=10)
        ),
        ft.ListTile(
            leading=ft.Icon(ft.icons.SMARTPHONE, color=MAGENTA_NEON),
            title=ft.Text("Device_Beta", color="white"),
            subtitle=ft.Text("192.168.1.28 • 25ms", color="gray"),
        ),
    ], scroll=ft.ScrollMode.AUTO)

    left_panel = GlassCard(
        title="Network Dashboard",
        content=peers_list,
        border_color=CYAN_NEON,
        expand=True
    )

    # --- SECTION 2 : RADAR CENTRAL (MILIEU) ---
    # Ici nous placerons plus tard le Radar animé en Canvas
    radar_placeholder = ft.Column([
        ft.Stack([
            # Simuler les cercles du radar
            ft.Container(width=200, height=200, border=ft.border.all(1, "rgba(0, 255, 255, 0.2)"), border_radius=100),
            ft.Container(width=150, height=150, border=ft.border.all(1, "rgba(0, 255, 255, 0.4)"), border_radius=75, margin=25),
            ft.Container(
                content=ft.Icon(ft.icons.WIFI, color=CYAN_NEON, size=40),
                width=100, height=100, border=ft.border.all(2, CYAN_NEON),
                border_radius=50, margin=50, alignment=ft.alignment.center
            ),
        ], alignment=ft.alignment.center),
        ft.Text("LANShare Radar", size=24, weight="bold", color="white"),
        ft.Text("Scanning for peers...", italic=True, color="gray"),
        ft.Row([
            ft.ElevatedButton("Remote Clipboard", icon=ft.icons.COPY, color=CYAN_NEON),
            ft.Switch(label="Auto-Zip", value=True, active_color=MAGENTA_NEON),
        ], alignment=ft.MainAxisAlignment.CENTER)
    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    center_panel = GlassCard(
        content=radar_placeholder,
        border_color=CYAN_NEON,
        expand=True
    )

    # --- SECTION 3 : VISUALISEUR DE TRANSFERT (DROITE) ---
    transfer_queue = ft.Column([
        ft.Container(
            content=ft.Row([
                ft.Icon(ft.icons.INSERT_DRIVE_FILE, color=MAGENTA_NEON),
                ft.Column([
                    ft.Text("Project_Video.mp4", size=12, color="white"),
                    ft.ProgressBar(value=0.6, width=150, color=MAGENTA_NEON, bgcolor="rgba(255,0,255,0.1)"),
                ], spacing=2)
            ]),
            padding=10, bgcolor="rgba(255,255,255,0.03)", border_radius=10
        )
    ], scroll=ft.ScrollMode.AUTO)

    right_panel = GlassCard(
        title="Transfer Visualizer",
        content=ft.Column([
            ft.Text("Speed Graph (Placeholder)"),
            ft.Container(height=100, bgcolor="rgba(0,0,0,0.2)", border_radius=10), # Zone pour le graphique
            ft.Text("Task Queue", size=14, color=MAGENTA_NEON),
            transfer_queue
        ]),
        border_color=MAGENTA_NEON,
        expand=True
    )

    # --- LAYOUT PRINCIPAL ---
    layout = ft.Container(
        content=ft.Row([
            left_panel,
            center_panel,
            right_panel
        ], spacing=20, alignment=ft.MainAxisAlignment.CENTER),
        padding=20,
        expand=True
    )

    page.add(layout)

# Lancement de l'application
if __name__ == "__main__":
    ft.app(target=main)