import reflex as rx
from web_cv.styles.styles import Size
from web_cv.styles.colors import Color
from web_cv.components.link_icon import link_icon

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
        rx.image(src="home.png",alt="HOME",
                 width=Size.BIG.value,
                 height=Size.BIG.value),
        rx.text("web portfolio"),
        rx.spacer(),
        link_icon("gmail","https://www.youtube.com/watch?v=h8Tn0ITRoQs&t=10657s"),
        width="100%"),
        position="sticky",
        bg= Color.PRIMARY.value,
        border_bottom = f"0.25em solid {Color.SECONDARY.value}",
        padding_x = Size.BIG.value,
        padding_y = Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"

        )
    