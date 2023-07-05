const {createApp} = Vue;

createApp({
    data(){
        return{
            productos: [],
            url: 'http://127.0.0.1:5000/heladera' ,
            cargando: true,
            error: false,
        }
},
    methods: {
        fetchApi(url){
            fetch(url)
            .then(res => res.json())
            .then(data =>{
                this.productos = data;
                this.cargando =false;
            })
            .catch (err=>{
                console.error(err)
                this.error =true;
            })
        },

        eliminar(id) {
            Swal.fire({
              title: '¿Estás seguro de eliminar este elemento?',
              text: 'Esta acción no se puede deshacer',
              icon: 'warning',
              showCancelButton: true,
              confirmButtonText: 'Sí, eliminar',
              cancelButtonText: 'Cancelar'
            }).then((result) => {
              if (result.isConfirmed) {
                const url = this.url + "/" + id;
                let options = {
                  method: 'DELETE'
                };
          
                fetch(url, options)
                  .then((res) => res.json())
                  .then((data) => {
                    location.reload();
                  })
                  .catch((err) => console.error(err));
              }
            });
          }
          


    },

    created(){
        this.fetchApi(this.url)



    },
}).mount('#app')