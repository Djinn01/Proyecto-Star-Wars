from statistics import mean, mode
from collections import defaultdict
class ShipsStats:
    def mostrar_estadísticas_de_naves(lista_de_naves):
        # Crear diccionarios para almacenar estadísticas para cada clase de nave
        estadísticas_hiperimpulsor = defaultdict(list)
        estadísticas_mglt = defaultdict(list)
        estadísticas_velocidad_atmósfera = defaultdict(list)
        estadísticas_costo = defaultdict(list)

        # Iterar sobre la lista de naves y poblar los diccionarios
        for nave in lista_de_naves:
            estadísticas_hiperimpulsor[nave.starship_class].append(nave.hyperdrive_rating)
            estadísticas_mglt[nave.starship_class].append(nave.MGLT)
            estadísticas_velocidad_atmósfera[nave.starship_class].append(nave.max_atmorphering_speed)
            estadísticas_costo[nave.starship_class].append(nave.cost_in_credits)

        # Imprimir la tabla de estadísticas
        print("Estadísticas de clases de naves:")
        print("----------------------------")
        for starship_class in estadísticas_hiperimpulsor:
            print(f"Clase: {starship_class}")
            print(f"  Calificación de hiperimpulsor: Media={mean(estadísticas_hiperimpulsor[starship_class]):.2f}, Moda={mode(estadísticas_hiperimpulsor[starship_class])}, Máximo={max(estadísticas_hiperimpulsor[starship_class])}, Mínimo={min(estadísticas_hiperimpulsor[starship_class])}")
            print(f"  MGLT: Media={mean(estadísticas_mglt[starship_class]):.2f}, Moda={mode(estadísticas_mglt[starship_class])}, Máximo={max(estadísticas_mglt[starship_class])}, Mínimo={min(estadísticas_mglt[starship_class])}")
            print(f"  Velocidad máxima en atmósfera: Media={mean(estadísticas_velocidad_atmósfera[starship_class]):.2f}, Moda={mode(estadísticas_velocidad_atmósfera[starship_class])}, Máximo={max(estadísticas_velocidad_atmósfera[starship_class])}, Mínimo={min(estadísticas_velocidad_atmósfera[starship_class])}")
            print(f"  Costo en créditos: Media={mean(estadísticas_costo[starship_class]):.2f}, Moda={mode(estadísticas_costo[starship_class])}, Máximo={max(estadísticas_costo[starship_class])}, Mínimo={min(estadísticas_costo[starship_class])}")
            print()
