const fs=require('fs'),vm=require('vm'),assert=require('assert');
const source=fs.readFileSync(require('path').join(__dirname, '../dist/site.js'),'utf8');
function harness(width,height=340,reduced=false){
  const el=()=>({style:{},events:{},classList:{toggle(){},remove(){},contains(){return false}},setAttribute(){},addEventListener(n,f){this.events[n]=f;},contains(){return false}});
  const cards=Array.from({length:5},()=>({...el(),offsetWidth:264,offsetHeight:height}));
  const ring=el(),stage={...el(),clientWidth:Math.min(1260,width*.88),querySelectorAll(){return cards},querySelector(){return ring}};
  const nav=el(),toggle=el(),win=el(),body=el(),doc={...el(),body,hidden:false,querySelector(s){return s==='.orbit-stage'?stage:toggle},querySelectorAll(){return []},getElementById(){return nav}};
  let pending,now=0;
  const context={document:doc,window:win,matchMedia:q=>({matches:q.includes('reduce')?reduced:width>=1101,addEventListener(){}}),requestAnimationFrame:f=>{pending=f},Math};
  vm.runInNewContext(source,context);
  const step=(count=1)=>{for(let i=0;i<count;i++){now+=33;pending(now);}};
  const position=card=>{
    const m=card.style.transform?.match(/translate3d\(([^p]+)px,([^p]+)px,0\) scale\(([^)]+)\)/);
    return m?m.slice(1).map(Number):null;
  };
  const bounds=()=>{for(const c of cards){const [x,y,s]=position(c);assert(Number.isFinite(x+y+s));assert(Math.abs(x)+264*s/2<=stage.clientWidth/2-8,`horizontal clipping ${width} ${x} ${s}`);assert(Math.abs(y)+height*s/2<=parseFloat(stage.style.height)/2-8,`vertical clipping ${width} ${height}`);}};
  return {cards,stage,win,doc,step,position,bounds};
}
let frames=0;
for(const width of [1101,1200,1440,1920])for(const height of [260,340,420]){
  const h=harness(width,height);
  for(let i=0;i<5400;i++){
    if(i%900===0)h.cards[(i/900)%5].events.pointerenter({pointerType:'mouse'});
    if(i%900===180)h.cards.forEach(c=>c.events.pointerleave());
    h.step();h.bounds();frames++;
  }
}
for(const width of [390,768,1100]){
  const h=harness(width);h.cards[0].events.focus();h.step(60);
  assert(h.cards.every(c=>!c.style.transform),'mobile focus must leave cards in the grid');
}
{
  const h=harness(1440,340,true);h.cards[0].events.focus();h.step(60);
  assert(h.cards.every(c=>!c.style.transform),'reduced motion uses static readable grid');
}
{
  const h=harness(1440);h.step(100);
  const snapshot=()=>h.cards.map(c=>c.style.transform);
  h.win.events['site-motion-change']({detail:{paused:true}});let before=snapshot();h.step(100);assert.deepStrictEqual(snapshot(),before,'global pause stops orbit');
  h.win.events['site-motion-change']({detail:{paused:false}});h.step(50);assert.notDeepStrictEqual(snapshot(),before,'global resume works');
  h.doc.hidden=true;before=snapshot();h.step(100);assert.deepStrictEqual(snapshot(),before,'hidden tab stops work');h.doc.hidden=false;
  h.cards[0].events.pointerenter({pointerType:'mouse'});h.step(200);
  const beforeHover=h.position(h.cards[0]);h.step(30);const afterHover=h.position(h.cards[0]);
  assert(Math.hypot(afterHover[0]-beforeHover[0],afterHover[1]-beforeHover[1])<.01,'hovered card eases to rest');
  assert(afterHover[2]>=.999,'hovered distant card is readable');
  h.cards[0].events.pointerleave();h.cards[2].events.focus();h.step(60);const coords=h.cards.map(c=>h.position(c).slice(0,2));h.step(60);
  assert.deepStrictEqual(h.cards.map(c=>h.position(c).slice(0,2)),coords,'keyboard focus freezes the orbit');
  assert.strictEqual(h.cards[2].style.zIndex,'1000','focused card above other cards');
  h.cards[2].events.blur();h.step(60);assert.notDeepStrictEqual(h.cards.map(c=>h.position(c).slice(0,2)),coords,'blur resumes motion');
}
console.log(JSON.stringify({result:'passed',geometry_frames:frames,desktop_widths:[1101,1200,1440,1920],card_heights:[260,340,420],behaviors:['mobile focus','reduced motion','global pause/resume','hidden tab','hover slowdown/readability','keyboard focus/resume']},null,2));
