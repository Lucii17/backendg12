function guardar() {
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
  

  let url = 'http://127.0.0.1:5000/';
  if (tablaSeleccionada === 'aire') {
    url += 'aires';
  } else if (tablaSeleccionada === 'lavarropa') {
    url += 'lavarropas';
  }
    else if (tablaSeleccionada === 'television') {
  url += 'television';
    }
    else if (tablaSeleccionada === 'heladera') {
    url += 'heladera';
}

  let options = {
    body: JSON.stringify(producto),
    method: 'POST',
    headers: {'Content-Type': 'application/json'}
  };

  fetch(url, options)
    .then(function() {
      alert('Producto agregado exitosamente');
      if (tablaSeleccionada === 'aire') {
        window.location.href = './aire.html';
      } else if (tablaSeleccionada === 'lavarropa') {
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






