#!/bin/sh

SINK='@DEFAULT_AUDIO_SINK@'

case $BLOCK_BUTTON in
    2) wpctl set-mute "$SINK" toggle ;; 
    1) wpctl set-volume "$SINK" 5%+ ;;  
    3) wpctl set-volume "$SINK" 5%- ;; 
esac

vol=$(wpctl get-volume "$SINK" | awk '{print $2*100}' | cut -d. -f1)
mute=$(wpctl get-volume "$SINK" | grep -q MUTED && echo true || echo false)
if [ "$mute" = "true" ]; then
    echo "🔇 ${vol}% │"
else
    echo "🔊 ${vol}% │"
fi
