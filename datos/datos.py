import json


def open_json():
    """
    Abre y lee el archivo JSON llamado 'leads.json' con codificación utf-8.

    Returns:
        list: Lista de diccionarios que contiene los datos de los leads.
    """
    with open("leads.json", "r", encoding="utf-8") as file:
        leads_data = json.load(file)
    return leads_data


def leads_filter():
    """
    Filtra los leads cuya ubicación es Medellín.

    Returns:
        list: Lista de diccionarios que contiene los leads que buscan vivienda en Medellín.
    """
    leads_data = open_json()
    leads_medellin = []
    for lead in leads_data:
        if lead["location"] == "Medellín":
            leads_medellin.append(lead)
    return leads_medellin


def calculate_total_budged():
    """
    Calcula el presupuesto total para los leads en Medellín.

    Returns:
        int: El presupuesto total de todos los leads en Medellín.
    """
    leads_medellin = leads_filter()
    total_budget: int = 0  # Inicializa el presupuesto total en 0

    for lead in leads_medellin:
        total_budget += lead["budget"]  # Suma el presupuesto de cada lead
    return total_budget


def leads_sort():
    """
    Ordena los leads de Medellín de mayor a menor presupuesto.

    Returns:
        list: Lista de diccionarios con los leads ordenados por presupuesto en orden descendente.
    """
    leads_medellin = leads_filter()
    leads_medellin.sort(key=lambda x: x["budget"], reverse=True)  # Ordena por presupuesto, de mayor a menor
    lead_sort = []
    for lead in leads_medellin:
        lead_sort.append(lead)
    return lead_sort


def print_message(message: str, range_print):
    """
    Imprime un mensaje con un encabezado y un rango de datos.

    Args:
        message (str): El mensaje o título a imprimir.
        range_print (list): La lista de leads que serán impresos.
    """
    print("\n" + "=" * 50)
    print(f"{message}")
    print("=" * 50)

    for lead in range_print:
        print(lead)

    print("=" * 50 + "\n")


def main():
    """
    Función principal que llama a las funciones para filtrar leads,
    calcular el presupuesto total y ordenar los leads.
    Luego imprime los resultados.
    """
    medellin_leads = leads_filter()  # Filtra los leads de Medellín
    medellin_leads_sort = leads_sort()  # Ordena los leads filtrados de Medellín por presupuesto
    total_budget = calculate_total_budged()  # Calcula el presupuesto total

    # Imprime los leads de Medellín
    print_message("Leads que buscan vivienda en Medellín:", medellin_leads)
    # Imprime el presupuesto total
    print("El presupuesto total en Medellín es:", total_budget)
    # Imprime los leads ordenados por presupuesto
    print_message("Leads filtrados y ordenados:", medellin_leads_sort)


if __name__ == "__main__":
    main()
