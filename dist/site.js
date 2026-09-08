(() => {
  const nav = document.getElementById('site-nav');
  const toggle = document.querySelector('.nav-toggle');
  const dropdowns = [...document.querySelectorAll('.nav-dropdown')];
  function closeNav(){nav.classList.remove('is-open');toggle.setAttribute('aria-expanded','false');}
  toggle.addEventListener('click',()=>{const open=nav.classList.toggle('is-open');toggle.setAttribute('aria-expanded',String(open));});
  dropdowns.forEach(item=>item.addEventListener('toggle',()=>{if(item.open)dropdowns.forEach(other=>{if(other!==item)other.open=false;});}));
  document.addEventListener('click',event=>{dropdowns.forEach(item=>{if(!item.contains(event.target))item.open=false;});});
  nav.addEventListener('click',event=>{if(event.target.closest('a')){dropdowns.forEach(item=>{item.open=false;});closeNav();}});
  document.addEventListener('keydown',event=>{if(event.key!=='Escape')return;const focused=dropdowns.find(item=>item.open&&item.contains(document.activeElement));dropdowns.forEach(item=>{item.open=false;});if(focused)focused.querySelector('summary').focus();else if(nav.classList.contains('is-open')){closeNav();toggle.focus();}});

  const stage=document.querySelector('.orbit-stage');
  if(!stage)return;
  const cards=[...stage.querySelectorAll('.orbit-card')];
  const reduced=matchMedia('(prefers-reduced-motion: reduce)');
  const desktop=matchMedia('(min-width: 1101px)');
  let hovered=null,focused=null,manualPause=false,inView=true,last=0,rotation=0,focal=1;
  const active=()=>focused===null?hovered:focused;
  const orbital=()=>desktop.matches&&!reduced.matches;
  // Reference motion: individual speeds, a gently rotating 3D orbit, vertical
  // drift, and eased hover slowdown. Keep the existing HTML cards and links.
  const bodies=cards.map((_,index)=>({phase:index/cards.length*Math.PI*2,speed:.25+.05*index,velocity:.25+.05*index,zoom:0}));
  function place(){
    if(!orbital())return;
    const turnCos=Math.cos(rotation),turnSin=Math.sin(rotation);
    cards.forEach((card,index)=>{
      const body=bodies[index];
      const localX=Math.cos(body.phase)*1.8*1.2,localZ=Math.sin(body.phase)*1.8;
      const x=localX*turnCos+localZ*turnSin,z=-localX*turnSin+localZ*turnCos;
      const y=.15*Math.sin(.5*body.phase+index),distance=Math.hypot(x,y-.5,4-z);
      const px=x/(4-z)*focal,py=(.5-y)/(4-z)*focal-focal*.125;
      const depthScale=2.5/distance;
      // Expand a selected card to a readable size without changing its path.
      const scale=depthScale+(Math.max(1,depthScale*1.05)-depthScale)*body.zoom;
      card.style.transform=`translate(-50%,-50%) translate3d(${px}px,${py}px,0) scale(${scale})`;
      card.style.zIndex=String(active()===index?1000:Math.round(100+z*20));
    });
  }
  function layout(){
    document.body.classList.toggle('orbit-ready',orbital());
    if(!orbital()){stage.style.height='';cards.forEach(card=>{card.style.transform='';card.style.zIndex='';});return;}
    const cardWidth=Math.max(...cards.map(card=>card.offsetWidth));
    const cardHeight=Math.max(...cards.map(card=>card.offsetHeight));
    focal=Math.max(100,(stage.clientWidth-cardWidth*1.5-48)/1.4);
    stage.style.height=`${Math.ceil(Math.max(660,cardHeight*1.6+focal*.35+50))}px`;
    const ring=stage.querySelector('.orbit-ring');
    ring.style.width=`${focal*.98}px`;ring.style.height=`${focal*.137}px`;
    ring.style.marginTop=`${focal*.03}px`;
    place();
  }
  cards.forEach((card,index)=>{
    card.addEventListener('pointerenter',event=>{if(event.pointerType!=='touch')hovered=index;});
    card.addEventListener('pointerleave',()=>{if(hovered===index)hovered=null;});
    card.addEventListener('focus',()=>{focused=index;place();});
    card.addEventListener('blur',()=>{focused=null;});
  });
  window.addEventListener('site-motion-change',event=>{manualPause=event.detail.paused;});
  reduced.addEventListener('change',layout);
  desktop.addEventListener('change',layout);
  window.addEventListener('resize',layout);
  if('IntersectionObserver' in window)new IntersectionObserver(entries=>{inView=entries[0].isIntersecting;},{rootMargin:'100px'}).observe(stage);
  function frame(now){
    if(now-last>=32){
      const delta=Math.min((now-last)/1000,.06);last=now;
      if(orbital()&&inView&&!document.hidden){
        const selected=active();
        bodies.forEach((body,index)=>{
          body.zoom+=((selected===index?1:0)-body.zoom)*Math.min(1,delta*5);
          if(manualPause||focused!==null)return;
          const target=selected===null?body.speed:selected===index?0:body.speed*.1;
          body.velocity+=(target-body.velocity)*Math.min(1,delta*3);
          body.phase+=body.velocity*delta;
        });
        if(!manualPause&&selected===null)rotation+=delta*.03;
        place();
      }
    }
    requestAnimationFrame(frame);
  }
  layout();if(document.fonts)document.fonts.ready.then(layout);requestAnimationFrame(frame);
})();
