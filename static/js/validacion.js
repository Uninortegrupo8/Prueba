function validarFormulario(){
    let Usuario = document.getElementById("inputUsuario").value;
    let Email = document.getElementById("inputEmail").value;
    let Password = document.getElementById("inputPassword").value;

    if ((Usuario.length == 0) || (Usuario.length < 8)){
        alert("Ingrese un Usuario valido");
        
    }

    let er = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;

    if(!Email.match(er)){
        alert("Formato de email no valido");
    }

    if ((Password.length == 0) || (Password.length < 8)){
        alert("El Password debe contener al menos 8 caracteres.");
    }
}
