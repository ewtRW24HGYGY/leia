(function(){
  var b=document.querySelector('.burger'),m=document.querySelector('.menu');
  if(b&&m){b.addEventListener('click',function(){var o=m.classList.toggle('open');b.setAttribute('aria-expanded',o)});
    m.addEventListener('click',function(e){if(e.target.tagName==='A'){m.classList.remove('open');b.setAttribute('aria-expanded',false)}})}
  // reveal on scroll
  var els=document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});els.forEach(function(el){io.observe(el)})}
  else els.forEach(function(el){el.classList.add('in')});
  // cookie notice
  var c=document.querySelector('.cookie');
  try{if(c&&!localStorage.getItem('trigo-cookie'))c.classList.add('show')}catch(e){if(c)c.classList.add('show')}
  var ok=document.getElementById('cookie-ok');
  if(ok)ok.addEventListener('click',function(){c.classList.remove('show');try{localStorage.setItem('trigo-cookie','1')}catch(e){}});
  // contact form -> opens WhatsApp / e-mail with message pre-filled
  var f=document.getElementById('contact-form');
  if(f){
    var msg=document.getElementById('form-msg');
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var d=new FormData(f);
      if(!d.get('lgpd')){msg.className='form-msg err';msg.textContent='Para enviar, confirme a ciência da Política de Privacidade.';return}
      var text='Olá, Trigo Advogados! Meu nome é '+d.get('nome')+'.\nÁrea: '+d.get('area')+'\nE-mail: '+d.get('email')+'\nTelefone: '+d.get('telefone')+'\n\n'+d.get('mensagem');
      var via=d.get('canal'),cfg=window.TRIGO||{};
      if(via==='whatsapp'){window.open('https://wa.me/'+cfg.whatsapp+'?text='+encodeURIComponent(text),'_blank','noopener')}
      else{location.href='mailto:'+cfg.email+'?subject='+encodeURIComponent('Contato pelo site – '+d.get('area'))+'&body='+encodeURIComponent(text)}
      msg.className='form-msg ok';msg.textContent='Obrigado! Sua mensagem foi preparada no canal escolhido. Retornaremos em breve.';
    });
    var tel=f.querySelector('[name=telefone]');
    if(tel)tel.addEventListener('input',function(){var v=tel.value.replace(/\D/g,'').slice(0,11);
      tel.value=v.length>10?v.replace(/(\d{2})(\d{5})(\d{0,4})/,'($1) $2-$3'):v.length>6?v.replace(/(\d{2})(\d{4})(\d{0,4})/,'($1) $2-$3'):v.length>2?v.replace(/(\d{2})(\d*)/,'($1) $2'):v});
  }
})();
