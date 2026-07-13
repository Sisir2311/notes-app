from nicegui import ui
from app.pages.home import create_home_page

create_home_page()

ui.run(
    title="Notes",
    reload=True
)