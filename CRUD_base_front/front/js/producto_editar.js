

let argsUrl = location.search.substring(1).split('&');
console.log(argsUrl)

let data = [];
for (let i = 0; i < argsUrl.length; i++) {
    data[i] = argsUrl[i].split('=');
  
}
console.log(data);

document.getElementById('id').value = decodeURIComponent(data[0][1])
document.getElementById('nombre').value = decodeURIComponent(data[1][1])
document.getElementById('imagen').value = decodeURIComponent(data[2][1])
document.getElementById('precio').value = decodeURIComponent(data[3][1])
document.getElementById('stock').value = decodeURIComponent(data[4][1])
document.getElementById('marca').value = decodeURIComponent(data[5][1])


function modificar(){
    let id =document.getElementById('id').value;
    let n = document.getElementById('nombre').value;
    let i = document.getElementById('imagen').value;
    let p = document.getElementById('precio').value;
    let s = document.getElementById('stock').value;
    let m = document.getElementById('marca').value;
   
    let producto = {
        nombre: n,
        imagen: i,
        precio: p,
        stock: s,
        marca: m,




    };

    let tablaSeleccionada = document.getElementById('tabla').value;
  

    let url = 'https://lucii17.pythonanywhere.com/';
    if (tablaSeleccionada === 'aire') {
        url += 'aires/'+id;
    }   else if (tablaSeleccionada === 'lavarropa') {
        url += 'lavarropas/'+id;
    }
        else if (tablaSeleccionada === 'television') {
        url += 'television/'+id;
    }
        else if (tablaSeleccionada === 'heladera') {
      url += 'heladera/'+id;
  }
  
    let options = {
      body: JSON.stringify(producto),
      method: 'PUT',
      headers: {'Content-Type': 'application/json'}
    };
  
    fetch(url, options)
      .then(function() {
        alert('Producto agregado exitosamente');
        if (tablaSeleccionada === 'aire') {
          window.location.href = './aire.html';
        }   else if (tablaSeleccionada === 'lavarropa') {
          window.location.href = './lavarropas.html';
        }
            else if (tablaSeleccionada === 'television') {
            window.location.href = './television.html';
        }
            else if (tablaSeleccionada === 'heladera') {
          window.location.href = './heladera.html';
      }
      })
      .catch(error => {
        alert('Ha ocurrido un error al agregar el producto');
        console.error(error);
      });
  }

    /*let url = 'http://127.0.0.1:5000/aires/'+id; 
    let options = {
        body: JSON.stringify(producto),
        method: 'PUT',
        headers: {'Content-Type' : 'application/json'}
    }
    fetch(url, options)
    .then(function(){
        alert("Producto agregado exitosamente");
        window.location.href = './aire.html'


    })
    

    .catch(error => {
        alert('Ha ocurrido un error al agregar el producto');
        console.error(error);
        
    })

}
*/