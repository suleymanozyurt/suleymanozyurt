// Kullanım: NODE_PATH=/opt/node22/lib/node_modules node render.js <mod> ...
//  frame <t> <out> [reduced] | stills [reduced] | audio | shard <i> <n> <reduced> | video <reduced>
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const {spawn,spawnSync}=require('child_process');
const EXE='/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell';
const FPS=60,URL='file://'+path.resolve(__dirname,'index.html');
const OUT=path.resolve(__dirname,'out');fs.mkdirSync(OUT,{recursive:true});
async function open(reduced){
  const br=await chromium.launch({executablePath:EXE,args:['--no-sandbox','--force-color-profile=srgb']});
  const pg=await br.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
  await pg.goto(URL+'?f=9x16'+(reduced?'&reduced=1':''));
  await pg.evaluate(()=>document.fonts.ready);
  const dur=await pg.evaluate(()=>TIMELINE.duration);
  return{br,pg,dur};
}
const shot=async(pg,t)=>{await pg.evaluate(t=>seek(t),t);return pg.screenshot({type:'png'});};
(async()=>{
  const [m,a,b2,c]=process.argv.slice(2);
  if(m==='frame'){const{br,pg}=await open(c==='reduced');fs.writeFileSync(b2,await shot(pg,+a));await br.close();}
  else if(m==='stills'){const{br,pg,dur}=await open(a==='reduced');const B=60/90;
    const ts=[];for(let i=0;i<=80;i+=4)ts.push(Math.min(i*B,dur-0.01));
    // her sahne için ek: metin görünür olduğunda
    ts.push(8*B+6*B,10.9,14.5*B+1.5,29*B,34*B,44*B,50*B,62*B+1.5,72*B);
    ts.sort((x,y)=>x-y);
    fs.mkdirSync(OUT+'/stills',{recursive:true});
    for(const t of ts)fs.writeFileSync(`${OUT}/stills/t${t.toFixed(2).padStart(6,'0')}.png`,await shot(pg,t));
    await br.close();}
  else if(m==='audio'){const{br,pg}=await open(false);const b64=await pg.evaluate(()=>window.renderAudio());
    fs.writeFileSync(OUT+'/bed.raw',Buffer.from(b64,'base64'));await br.close();}
  else if(m==='shard'){const i=+a,n=+b2,red=c==='1';const{br,pg,dur}=await open(red);
    const total=Math.round(dur*FPS),per=Math.ceil(total/n),s=i*per,e=Math.min(total,s+per);
    const f=`${OUT}/seg_${red?'r':'n'}${i}.mp4`;
    const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',String(FPS),'-c:v','png','-i','-','-c:v','libx264','-crf','16','-pix_fmt','yuv420p','-r',String(FPS),'-g','60',f],{stdio:['pipe','inherit','inherit']});
    for(let k=s;k<e;k++){const buf=await shot(pg,k/FPS);if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));}
    ff.stdin.end();await new Promise(r=>ff.on('close',r));await br.close();}
  else if(m==='video'){const red=a==='1'||a==='reduced',n=4;
    await Promise.all([...Array(n)].map((_,i)=>new Promise(r=>spawn('node',[__filename,'shard',i,n,red?'1':'0'],{stdio:'inherit'}).on('close',r))));
    const tag=red?'r':'n';
    fs.writeFileSync(`${OUT}/list_${tag}.txt`,[...Array(n)].map((_,i)=>`file 'seg_${tag}${i}.mp4'`).join('\n'));
    spawnSync('ffmpeg',['-y','-loglevel','error','-f','concat','-safe','0','-i',`${OUT}/list_${tag}.txt`,'-c','copy',`${OUT}/silent_${tag}.mp4`],{stdio:'inherit'});}
})();
