#!/bin/sh
# Kullanım: sh mix.sh <silent.mp4> <çıktı.mp4>   (vo/s1,s2,s3,s5,s6.mp3 + out/bed_n.wav gerekir; s4 yoksa o sahne seslendirilmez)
set -e
V=${VO:-vo}; BED=out/bed_n.wav
IN=""; F=""; N=0; MIX=""
add(){ f="$1"; t="$2"; [ -f "$V/$f.mp3" ] || return 0; IN="$IN -i $V/$f.mp3"; ms=$(python3 -c "print(int($t*1000))"); F="$F[$((N+2))]adelay=${ms}|${ms},volume=1.0[v$N];"; MIX="$MIX[v$N]"; N=$((N+1)); }
add s1 1.0; add s2 6.0; add s3 17.3; add s4 27.4; add s5 39.6; add s6 46.1
F="$F${MIX}amix=inputs=$N:normalize=0:dropout_transition=0[voice];[1]volume=-9dB[bed];[bed][voice]amix=inputs=2:normalize=0:duration=first[m];[m]loudnorm=I=-16:TP=-1.5:LRA=7[out]"
ffmpeg -y -loglevel error -i "$1" -i $BED $IN -filter_complex "$F" -map 0:v -map "[out]" -c:v copy -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart "$2"
