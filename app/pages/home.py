import json
from pathlib import Path
from nicegui import ui

# -----------------------------
# Storage
# -----------------------------

FILE_NAME = Path("tasks.json")
tasks = []


def load_tasks():
    """Load tasks from JSON file if it exists."""
    global tasks

    if FILE_NAME.exists():
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)


def save_tasks():
    """Save current tasks to JSON."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# -----------------------------
# UI Refresh
# -----------------------------

def refresh_tasks(container, sort_order):

    container.clear()

    if sort_order.value == "High → Low":
        display_tasks = sorted(
            tasks,
            key=lambda x: x["effort"],
            reverse=True,
        )
    else:
        display_tasks = sorted(
            tasks,
            key=lambda x: x["effort"],
        )

    with container:

        if not display_tasks:
            ui.label("No tasks yet.").classes("text-gray-500")
            return

        for task in display_tasks:

            with ui.row().classes("items-center w-full gap-4"):

                checkbox = ui.checkbox().bind_value(
                    task,
                    "completed",
                )

                checkbox.on(
                    "update:model-value",
                    lambda _: save_tasks(),
                )

                ui.label(task["text"]).classes("w-80")

                ui.label("⭐" * task["effort"])

                def delete_task(t=task):
                    tasks.remove(t)
                    save_tasks()
                    refresh_tasks(container, sort_order)

                ui.button(
                    "Delete",
                    on_click=delete_task,
                ).props("flat color=red")


# -----------------------------
# Main Page
# -----------------------------

def create_home_page():

    load_tasks()

    ui.label("Notes").classes("text-3xl font-bold")

    ui.separator()

    task_input = ui.input(
        placeholder="Enter Task..."
    ).classes("w-96")

    effort = ui.select(
        {
            1: "Very Low",
            2: "Low",
            3: "Medium",
            4: "High",
            5: "Very High",
        },
        value=3,
        label="Effort",
    )

    sort_order = ui.select(
        [
            "High → Low",
            "Low → High",
        ],
        value="High → Low",
        label="Sort",
    )

    task_container = ui.column().classes("w-full")

    def add_task():

        if not task_input.value:
            return

        tasks.append(
            {
                "text": task_input.value,
                "effort": effort.value,
                "completed": False,
            }
        )

        save_tasks()

        task_input.value = ""

        refresh_tasks(
            task_container,
            sort_order,
        )

    ui.button(
        "Add Task",
        on_click=add_task,
    )

    sort_order.on(
        "update:model-value",
        lambda _: refresh_tasks(
            task_container,
            sort_order,
        ),
    )

    ui.separator()

    refresh_tasks(
        task_container,
        sort_order,
    )