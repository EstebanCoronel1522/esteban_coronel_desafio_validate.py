import a_input

resultado_int = a_input.get_int("Solicitud:", "Error: número inválido.", 1, 10, 3)
print(f"El número entero ingresado es: {resultado_int}")

resultado_float = a_input.get_float("Solicitud:", "Error: número inválido.", 1.0, 10.0, 3)
print(f"El número decimal ingresado es: {resultado_float}")

resultado_string = a_input.get_string(5)
print(f"Es valido. Ingreso: {resultado_string}")