from nicegui import ui
from app.pages.home import create_home_page

create_home_page()

ui.run(
    title="Notes",
    host="127.0.0.1",
    port=8080,
    reload=False,
    show=True,
)