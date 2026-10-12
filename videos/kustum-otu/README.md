# Küstüm otu — 9:16 açıklayıcı film
Yeniden üretim: `python3 build.py` → `NODE_PATH=/opt/node22/lib/node_modules node render.js video 0` (4 paralel parça) ve `render.js audio`; ses ffmpeg ile −16 LUFS'a getirilip videoya eklenir.

## Test edilenler
- Aynı kare (t=20,5 sn) iki kez render edildi, `cmp` ile birebir aynı.
- 28 kare kontak sayfasında (out/contact.png) metin taşması ve çakışma gözle incelendi; iki düzeltme yapıldı (taşan satır, ≈2× çakışması).
- ffprobe: h264 1080×1920, 60 fps, 3200 kare, 53,33 sn, AAC ses.
- Ses: −16,0 LUFS entegre, tepe −3,0 dBFS (ebur128).
- Kontrast: ink/zemin 12,9; ikincil metin 6,8; vurgu/zemin 5,5; krem/pill 14,3 (en kötü 9,2).
- Azaltılmış hareket (`?reduced=1`) sürümü render edildi (hareketler anlık geçiş).

## Test edilmeyenler
- 16:9 ve 1:1 formatlar yok.
- Gerçek telefonda oynatma / platformların yeniden kodlaması.
- Ses cue'larının kulakla değerlendirmesi (yalnız ölçüldü).
