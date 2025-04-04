def imprimirRondas(ronda, num, jugadores):
    print()
    print("RANKING RONDA",num,": ")
    print("Jugador   Kills   Asistencias   Muertes     MVP     Puntos")
    print("------------------------------------------------------------")
    mvp = {
            "nombre": "",
            "puntos": 0
        }
    for jugador, stats in ronda.items():
        puntos = ((stats["kills"]*3)+stats["assists"]) - stats["deaths"]
        if puntos > mvp["puntos"]:
            mvp["nombre"] = jugador
            mvp["puntos"] = puntos
    
    for jugador, stats in ronda.items():
        best = False
        if jugador == mvp["nombre"]:
            best = True
            jugadores[jugador]["MVPs"] += 1
        puntos = ((stats["kills"]*3)+stats["assists"]) - stats["deaths"]
        jugadores[jugador]["Puntos"] += puntos
        jugadores[jugador]["Deaths"] += stats["deaths"]
        jugadores[jugador]["Assists"] += stats["assists"]
        jugadores[jugador]["Kills"] += stats["kills"]
        print(f" {jugador} :   {stats["kills"]}          {stats["assists"]}         {stats["deaths"]}    ",best,"    ",puntos)  
    print("------------------------------------------------------------")
    print()
    print()

def imprimirTodos(jugadores):
    print()
    print("RANKING FINAL: ")
    print("Jugador   Kills   Asistencias   Muertes     MVP     Puntos")
    print("------------------------------------------------------------")
    for jugador, stats in jugadores.items():
        print(f" {jugador} :   {stats["Kills"]}          {stats["Assists"]}           {stats["Deaths"]}         {stats["MVPs"]}        {stats["Puntos"]}")
    print("------------------------------------------------------------")
    print()
    print()    