#!/bin/bash

# Opciones del menú
options="Apagar\nReiniciar\nSuspender\nCerrar sesión"

# Mostrar menú con Rofi
chosen=$(echo -e "$options" | rofi -dmenu -i -p "¿Qué quieres hacer?")

case "$chosen" in
    Apagar)
        systemctl poweroff
        ;;
    Reiniciar)
        systemctl reboot
        ;;
    Suspender)
        systemctl suspend
        ;;
    "Cerrar sesión")
        # Detecta si estás usando Openbox, i3, etc.
        if [ "$XDG_CURRENT_DESKTOP" = "openbox" ] || [ "$DESKTOP_SESSION" = "openbox" ]; then
            openbox --exit
        else
            pkill -KILL -u "$USER"
        fi
        ;;
    *)
        # Cancelado o cerrado
        exit 0
        ;;
esac
