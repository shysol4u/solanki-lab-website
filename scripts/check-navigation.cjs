const fs=require('fs'),vm=require('vm'),assert=require('assert');
const source=fs.readFileSync(require('path').join(__dirname, '../dist/site.js'),'utf8');
function el(){const classes=new Set();return {events:{},attrs:{},children:new Set(),focused:false,classList:{toggle(c){if(classes.has(c)){classes.delete(c);return false}classes.add(c);return true},remove(c){classes.delete(c)},contains(c){return classes.has(c)}},setAttribute(k,v){this.attrs[k]=v},addEventListener(k,v){this.events[k]=v},contains(x){return this===x||this.children.has(x)},focus(){this.focused=true}}}
const nav=el(),toggle=el(),dropdowns=Array.from({length:5},()=>{const e=el();e.open=false;e.summary=el();e.querySelector=()=>e.summary;e.children.add(e.summary);return e});
const document={...el(),activeElement:null,getElementById(){return nav},querySelector(s){return s==='.nav-toggle'?toggle:null},querySelectorAll(){return dropdowns}};
vm.runInNewContext(source,{document});
toggle.events.click();assert(nav.classList.contains('is-open'));assert.equal(toggle.attrs['aria-expanded'],'true');
dropdowns[0].open=true;dropdowns[0].events.toggle();dropdowns[1].open=true;dropdowns[1].events.toggle();assert(!dropdowns[0].open&&dropdowns[1].open,'one dropdown open');
document.events.click({target:el()});assert(dropdowns.every(d=>!d.open),'outside click closes menus');
dropdowns[2].open=true;document.activeElement=dropdowns[2].summary;document.events.keydown({key:'Escape'});assert(!dropdowns[2].open&&dropdowns[2].summary.focused,'Escape returns focus to summary');
document.activeElement=null;document.events.keydown({key:'Escape'});assert(!nav.classList.contains('is-open')&&toggle.focused,'mobile Escape closes navigation');
toggle.events.click();dropdowns[1].open=true;nav.events.click({target:{closest(selector){assert.equal(selector,'a');return {href:'recruitment.html'}}}});
assert(!nav.classList.contains('is-open')&&dropdowns.every(d=>!d.open)&&toggle.attrs['aria-expanded']==='false','new Recruitment link closes mobile navigation normally');
console.log(JSON.stringify({result:'passed',checks:['mobile menu toggle','one open dropdown','outside click','Escape focus return','mobile Escape close','Recruitment link navigation close']},null,2));
