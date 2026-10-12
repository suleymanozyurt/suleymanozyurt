# Kullanım: python clone_tts.py   (venv içinde coqui-tts + torch CPU gerekir)
# Kullanıcının kendi ses kaydından (vo_clone/ref_voice.wav) XTTS v2 ile 6 sahne anlatımı üretir.
import os,sys,time
os.environ['COQUI_TOS_AGREED']='1'
import torch
from TTS.api import TTS
SCENES={
 's1':"Küstüm otu, dokunulunca yaprağını kapatır. Peki neden?",
 's2':"Dokunuş bir sinyale dönüşür, yaprak dibindeki eklem suyunu boşaltır. Yaprak katlanır. Ortada ne kas var, ne de sinir.",
 's3':"Hareket edemeyen yapraklar, çekirgeler tarafından yaklaşık iki kat fazla yendi.",
 's4':"Bunun bir bedeli de var. Gündüz kapanmaya zorlanan bitkide, dokunmanın etkisi ayrıldıktan sonra, üreme kütlesi yüzde kırk yedi azaldı.",
 's5':"Gece zaten kapanıyor. Yani zamanlama, her şeyi değiştiriyor.",
 's6':"Koruma mı, büyüme mi? Bitki bu dengeyi, hücrelerindeki suyla kuruyor."}
only=sys.argv[1:] or list(SCENES)
torch.set_num_threads(os.cpu_count())
tts=TTS('tts_models/multilingual/multi-dataset/xtts_v2').to('cpu')
for k in only:
    t=time.time()
    tts.tts_to_file(text=SCENES[k],speaker_wav='vo_clone/ref_voice.wav',language='tr',file_path=f'vo_clone/{k}.wav',split_sentences=True)
    print(k,'bitti',round(time.time()-t,1),'sn',flush=True)
