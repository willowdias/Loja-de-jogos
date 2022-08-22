function jogonovo(){
    
  document.getElementById('container-addjogo').style.display='block';
  }
  function closeaddjogo(){
  
  document.getElementById('container-addjogo').style.display='none';
  }

 
  function closealerta(){
      document.getElementById('messages').style.display='none';
  }
  //essa function atribuir focus no input
  window.onload = function() {
      document.getElementById("Buscar").focus();
    }

 //validar campos em branco

 function valida_form ()
 
 
  
 {
  

  if(document.getElementById("nome").value == ""){
  alert('Por favor, preencha o campo nome');
  document.getElementById("nome").focus();
  return false
  }
  if(document.getElementById("categoria").value == ""){
      alert('Por favor, preencha o campo Categoria');
      document.getElementById("categoria").focus();
      return false
      }
  if(document.getElementById("Console").value == ""){
      alert('Por favor, preencha o campo Console');
        document.getElementById("Console").focus();
        return false
        }
    if(document.getElementById("foto").value == ""){
          alert('Por favor, preencha o campo Foto Vazio');
            document.getElementById("foto").focus();
            return false
            }
 
  }

  //verfica tamanho do noe dados input

