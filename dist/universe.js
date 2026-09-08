const canvas = document.getElementById('universe');
const ctx = canvas.getContext('2d');
const button = document.getElementById('motion');
const reduced = matchMedia('(prefers-reduced-motion: reduce)');
let paused = reduced.matches, width = 0, height = 0, time = 0, last = 0;
const pointer = {x: -2000, y: -2000};
let seed = 71;
function random() { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }
const stars = Array.from({length: 160}, () => ({x: random(), y: random(), s: random(), phase: random()*6.28}));
const dust = Array.from({length: 1850}, () => ({u: random(), arm: Math.floor(random()*4), spread: (random()-.5)*.12, size: random(), phase: random()*6.28}));
const colors = ['190,228,255','242,248,255','129,193,230','236,176,126','116,255,185','196,151,255'];
const baseColors={A:'#7fffc3',T:'#ffc482',G:'#ceacff',C:'#83dfff'};
function letters(text,x,y,alpha=1,size=16){ctx.font=`500 ${size}px ui-monospace, monospace`;ctx.globalAlpha=Math.min(1,alpha*1.3);for(const c of text){ctx.fillStyle=baseColors[c]||'#c5d9e6';ctx.shadowColor=ctx.fillStyle;ctx.shadowBlur=9;ctx.fillText(c,x,y);x+=size*.64;}ctx.shadowBlur=0;ctx.globalAlpha=1;}
const sprites = colors.map(color => {const c=document.createElement('canvas');c.width=c.height=64;const x=c.getContext('2d');const g=x.createRadialGradient(32,32,0,32,32,32);g.addColorStop(0,`rgba(${color},1)`);g.addColorStop(.08,`rgba(${color},.95)`);g.addColorStop(.2,`rgba(${color},.35)`);g.addColorStop(1,`rgba(${color},0)`);x.fillStyle=g;x.fillRect(0,0,64,64);return c;});
function glow(x,y,r,color,alpha=1) {r*=Math.max(1,Math.min(width/1100,1.45));ctx.globalAlpha=Math.min(1,alpha*1.18);ctx.drawImage(sprites[color],x-r,y-r,r*2,r*2);ctx.globalAlpha=1;}
function deflect(p) {if(paused)return p;const dx=p.x-pointer.x,dy=p.y-pointer.y,d=Math.hypot(dx,dy);if(d<250&&d>0){const f=(1-d/250)*48;p.x+=dx/d*f-dy/d*f*.32;p.y+=dy/d*f+dx/d*f*.32;p.light=1-d/250;}return p;}
function helixPoint(u, strand, offset) {const scale=Math.min(width*.19,250);const angle=u*17+time*.15+strand*Math.PI+offset;const z=Math.cos(angle);const center=width*.77+Math.sin(u*3+offset)*width*.09;return deflect({x:center+Math.sin(angle)*scale*.36,y:height*(u*1.12-.06)+Math.sin(time*.1+offset)*12,z,light:0});}
// Scroll-revealed conceptual genomics and ecological interaction diagrams.
function lowerSystems(){
 const reveal=Math.min(1,Math.max(0,(scrollY-height*.35)/(height*.5)));
 if(!reveal)return;
 ctx.save();
 const unit=Math.min(width,height), cx=width*.76, cy=height*.43;
 function dot(x,y,r,c,alpha=.8){const p=deflect({x,y,light:0});glow(p.x,p.y,r+p.light*9,c,alpha*reveal);return p;}
 function link(a,b,color=0){ctx.strokeStyle=`rgba(${colors[color]},${.32*reveal})`;ctx.lineWidth=.8;ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke();const f=(time*.16+color*.17)%1;dot(a.x+(b.x-a.x)*f,a.y+(b.y-a.y)*f,10,color);}
 function label(text,x,y,c=0){ctx.font='12px ui-monospace, monospace';ctx.fillStyle=`rgba(${colors[c]},${.85*reveal})`;ctx.shadowColor=ctx.fillStyle;ctx.shadowBlur=7;ctx.fillText(text,x,y);ctx.shadowBlur=0;}
 // Folded polypeptide schematic: connected residues, animated in projection.
 let prev=null;
 for(let i=0;i<85;i++){const u=i/84, a=u*19+time*.16;const p=dot(cx+Math.sin(a)*unit*.095+Math.sin(u*7)*unit*.045,cy+Math.cos(a*1.37)*unit*.065+u*unit*.12,6,i%3===0?5:0,.78);if(prev)linkResidue(prev,p);prev=p;}
 function linkResidue(a,b){ctx.strokeStyle=`rgba(173,212,249,${.24*reveal})`;ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke();}
 label('PROTEIN → FUNCTION',cx-unit*.11,cy-unit*.10,5);
 // Circular DNA / engineering motif with a highlighted insert segment.
 const px=width*.38,py=height*.68,pr=unit*.095;
 for(let i=0;i<100;i++){const a=i/100*Math.PI*2+time*.11;dot(px+Math.cos(a)*pr,py+Math.sin(a)*pr*.56, i%8===0?8:3,i>73&&i<88?4:0,.75);}
 label('DNA / GENE INSERT',px-pr,py+pr*.78,4);
 letters('AUG · GCU · UAC',cx-unit*.09,cy+unit*.19,.7*reveal,15);
 // Three coupled ecological systems, with moving signals along their links.
 const nodes=[{x:width*.62,y:height*.80,c:4,name:'PLANT'},{x:width*.85,y:height*.73,c:0,name:'MICROBES'},{x:width*.78,y:height*.93,c:3,name:'SOIL'}];
 for(let i=0;i<3;i++){const n=nodes[i];link(n,nodes[(i+1)%3],n.c);dot(n.x,n.y,23,n.c);label(n.name,n.x+15,n.y-12,n.c);for(let j=0;j<26;j++){const a=j*.24+time*.10*(i+1),r=unit*(.023+(j%4)*.007);dot(n.x+Math.cos(a)*r,n.y+Math.sin(a)*r*.65,3+(j%5===0?4:0),n.c,.7);}}
 ctx.restore();
}
function draw() {
 ctx.clearRect(0,0,width,height);ctx.fillStyle='#03070b';ctx.fillRect(0,0,width,height);
 for(const s of stars){glow(s.x*width,s.y*height,3+s.s*4,2,.28+s.s*.4+Math.sin(time*.3+s.phase)*.08);}
 // Sparse, curved particle filaments, inspired by the supplied reference.
 for(const d of dust){const a=d.u*7.9+d.arm*1.57+time*.025;const r=(.04+d.u*.51+d.spread)*Math.min(width,height);const p=deflect({x:width*.67+Math.cos(a)*r,y:height*.55+Math.sin(a)*r*.9,light:0});const alpha=(.36+d.size*.6)*(0.85+Math.sin(time*.45+d.phase)*.15);const size=d.size>.96?17:2.2+d.size*3.2;glow(p.x,p.y,size,Math.floor(d.phase)%4,Math.min(1,alpha+p.light*.4));}
 // Rotating paired strands and complementary bases form a floating DNA helix.
 const sequence='ATGCGTACGATCGGATCAGT';const complement={A:'T',T:'A',G:'C',C:'G'};
 for(let i=0;i<70;i++){const u=i/69;const a=helixPoint(u,0,0),b=helixPoint(u,1,0);if(i%2===0){ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.strokeStyle='rgba(145,204,225,.24)';ctx.lineWidth=.7;ctx.stroke();}for(const [j,p] of [a,b].entries()){const near=(p.z+1)/2;glow(p.x,p.y,7+near*8+p.light*8,j?0:1,.5+near*.5);if(i%4===0){const base=sequence[(i/4)%sequence.length];letters(j?complement[base]:base,p.x+12,p.y+5,.65+near*.35,17);}}}
 // Colored sequence fragments follow the current, brightening near the pointer.
 for(let i=0;i<5;i++){const p=deflect({x:width*(.56+(i%3)*.12)+Math.sin(time*.08+i)*22,y:height*((i*.19+.16)%1)+Math.cos(time*.06+i)*16,light:0});letters(['5′ ATGC · GTAC 3′','GCTA · CGAT','A—T   G—C','3′ TACG · CATG 5′','CGAT · ATGC'][i],p.x,p.y,.52+p.light*.45,15);}
 // Stylized expression tracks: exons joined by a transcript line and traveling signal.
 for(let k=0;k<2;k++){const x=width*(.58+k*.13),y=height*(.32+k*.43),len=Math.min(width*.19,220);ctx.strokeStyle='rgba(151,214,232,.3)';ctx.beginPath();ctx.moveTo(x,y);ctx.lineTo(x+len,y);ctx.stroke();for(let j=0;j<4;j++){ctx.fillStyle=['#7fffc3','#83dfff','#ceacff','#ffc482'][j];ctx.globalAlpha=.48;ctx.fillRect(x+j*len/4,y-3,len*.13,6);}ctx.globalAlpha=1;const phase=(time*.09+k*.4)%1;glow(x+phase*len,y,17,0,.85);ctx.font='11px ui-monospace, monospace';ctx.fillStyle='rgba(184,220,233,.58)';ctx.fillText(k?'TRANSCRIPT  /  RNA':'EXPRESSION  /  DNA → RNA',x,y-14);}
 lowerSystems();
 if(!paused&&pointer.x>0){glow(pointer.x,pointer.y,48,0,.15);for(let n=0;n<6;n++){const a=time*.5+n*Math.PI/3;glow(pointer.x+Math.cos(a)*25,pointer.y+Math.sin(a)*25,4,n%4,.55);}}

}
function sync(){button.innerHTML=(paused?'Resume motion':'Pause motion')+' <span aria-hidden="true">'+(paused?'▷':'Ⅱ')+'</span>';button.setAttribute('aria-pressed',String(paused));window.dispatchEvent(new CustomEvent('site-motion-change',{detail:{paused}}));}
function resize(){width=innerWidth;height=innerHeight;const ratio=Math.min(devicePixelRatio||1,2);canvas.width=width*ratio;canvas.height=height*ratio;ctx.setTransform(ratio,0,0,ratio,0,0);draw();}
button.onclick=()=>{paused=!paused;sync();draw();};
reduced.addEventListener('change',e=>{paused=e.matches;sync();draw();});
addEventListener('pointermove',e=>{pointer.x=e.clientX;pointer.y=e.clientY;},{passive:true});
document.documentElement.addEventListener('pointerleave',()=>{pointer.x=pointer.y=-2000;});
addEventListener('resize',resize);
addEventListener('scroll',()=>{if(paused)draw();},{passive:true});
function frame(now){if(!paused&&!document.hidden&&now-last>32){time+=Math.min((now-last)/1000,.05);last=now;draw();}else if(paused||document.hidden){last=now;}requestAnimationFrame(frame);}
sync();resize();requestAnimationFrame(frame);
