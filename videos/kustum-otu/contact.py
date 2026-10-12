import sys,glob
from PIL import Image,ImageDraw
d=sys.argv[1];out=sys.argv[2];cols=int(sys.argv[3]) if len(sys.argv)>3 else 7
fs=sorted(glob.glob(d+'/t*.png'));w,h=270,480
rows=(len(fs)+cols-1)//cols
sheet=Image.new('RGB',(cols*w,rows*(h+24)),'#222')
dr=ImageDraw.Draw(sheet)
for i,f in enumerate(fs):
    im=Image.open(f).convert('RGB').resize((w,h));x=(i%cols)*w;y=(i//cols)*(h+24)
    sheet.paste(im,(x,y+24));dr.text((x+6,y+6),f.split('/t')[-1][:-4]+'s',fill='white')
sheet.save(out);print(len(fs),sheet.size)
