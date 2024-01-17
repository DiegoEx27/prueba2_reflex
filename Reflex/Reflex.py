import reflex as rx

class Personas(rx.Model, table=True):
    #id: int = rx.Field(primary_key=True)
    nombre: str
    apellido: str
    edad: int
    
    def obtener_datos():
        with rx.session() as s:
            personas = s.exec(Personas.select).all()
            nombres = [persona.nombre for persona in personas]
            apellidos = [persona.apellido for persona in personas]
            edades = [persona.edad for persona in personas]
            return nombres, apellidos, edades

class Estado(rx.State):
    nombres: str = None
    apellidos: str = None
    edades: str = None
    
    def refrescar(self):
        self.nombres = Personas.obtener_datos()[0]
        self.apellidos = Personas.obtener_datos()[1]
        self.edades = Personas.obtener_datos()[2]
    @rx.var
    def datos(self) -> str:
        return self.nombres, self.apellidos, self.edades

def index() -> rx.Component:
    return rx.vstack(
        
        rx.heading(Estado.datos[0],font_size="2em"),
        rx.heading(Estado.datos[1],font_size="2em"),
        rx.heading(Estado.datos[2],font_size="2em"),
        rx.button(
        "Click Me!",
        on_click=Estado.refrescar
        )
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()

'''def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", font_size="2em"),
            rx.box("Get started by editing ", rx.code(filename, font_size="1em")),
            rx.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )
    def obtener_nombres():
        with rx.session() as s:
            personas = s.exec(Personas.select).all()
            nombres = [persona.nombre for persona in personas]
            return nombres

    def obtener_apellidos():
        with rx.session() as s:
            personas = s.exec(Personas.select).all()
            apellidos = [persona.apellido for persona in personas]
            return apellidos

    def obtener_edades():
        with rx.session() as s:
            personas = s.exec(Personas.select).all()
            edades = [persona.edad for persona in personas]
            return edades
    '''