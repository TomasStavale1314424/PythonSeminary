from funcions import imprimirRondas
from funcions import imprimirTodos

rounds = [
{
'Shadow': {'kills':  2, 'assists': 1, 'deaths': True},
' Blaze' : {'kills': 1, 'assists': 0, 'deaths': False},
' Viper' : {'kills': 1, 'assists': 2, 'deaths': True},
' Frost' : {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills':  1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills':  0, 'assists': 2, 'deaths': False},
' Blaze' : {'kills': 2, 'assists': 0, 'deaths': True},
' Viper' : {'kills': 1, 'assists': 1, 'deaths': False},
' Frost' : {'kills': 2, 'assists': 1, 'deaths': True},
'Reaper': {'kills':  0, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills':  1, 'assists': 0, 'deaths': False},
' Blaze' : {'kills': 2, 'assists': 2, 'deaths': True},
' Viper' : {'kills': 1, 'assists': 1, 'deaths': True},
' Frost' : {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills':  1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills':  2, 'assists': 1, 'deaths': False},
' Blaze' : {'kills': 1, 'assists': 0, 'deaths': True},
' Viper' : {'kills': 0, 'assists': 2, 'deaths': False},
' Frost' : {'kills': 1, 'assists': 1, 'deaths': True},
'Reaper': {'kills':  1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills':  1, 'assists': 2, 'deaths': True},
' Blaze' : {'kills': 0, 'assists': 1, 'deaths': False},
' Viper' : {'kills': 2, 'assists': 0, 'deaths': True},
' Frost' : {'kills': 1, 'assists': 1, 'deaths': False},
'Reaper': {'kills':  1, 'assists': 1, 'deaths': True} 
}
]

jugadores = {
    "Shadow": {'Kills': 0, 'Assists': 0, 'Deaths': 0,"MVPs": 0,"Puntos": 0}, 
    " Blaze": {'Kills': 0, 'Assists': 0, 'Deaths': 0,"MVPs": 0,"Puntos": 0}, 
    " Viper": {'Kills': 0, 'Assists': 0, 'Deaths': 0,"MVPs": 0,"Puntos": 0},  
    "Reaper": {'Kills': 0, 'Assists': 0, 'Deaths': 0,"MVPs": 0,"Puntos": 0}, 
    " Frost": {'Kills': 0, 'Assists': 0, 'Deaths': 0,"MVPs": 0,"Puntos": 0}
}

num_ronda = 1
for ronda in rounds:
    imprimirRondas(ronda, num_ronda, jugadores)
    num_ronda +=1
print(imprimirTodos(jugadores))