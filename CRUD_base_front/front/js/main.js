document.getElementById('header').innerHTML = `
<nav class="navbar navbar-expand-sm navbar-light bg-light">
  <div class="container d-flex align-items-center">
    <a class="navbar-brand" href="index.html">
      <img src="./CRUD_base_front/front/img/G.png" alt="Logo" width="150" height="150">
    </a>
    <button class="navbar-toggler d-lg-none" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavId" aria-controls="collapsibleNavId"
      aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="collapsibleNavId">
      <ul class="navbar-nav me-auto mt-2 mt-lg-0">
        <li class="nav-item">
          <a class="nav-link active" href="index.html" aria-current="page" style="font-size: 25px;" >Home <span class="visually-hidden">(current)</span></a>
        </li>  
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="dropdownId" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="font-size: 25px;" >Productos</a>
          <div class="dropdown-menu" aria-labelledby="dropdownId">
            <a class="dropdown-item" href="aire.html">Aire acondicionados</a>
            <a class="dropdown-item" href="heladera.html">Heladeras</a>
            <a class="dropdown-item" href="television.html">TV y Smart</a>
            <a class="dropdown-item" href="lavarropas.html">Lavarropas</a>
          </div>
        </li>
      </ul>
      <form class="d-flex my-2 my-lg-0">
        <input class="form-control me-sm-2" type="text" style="font-size: 20px;" placeholder="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit"style="font-size: 20px;">Search</button>
      </form>
    </div>
  </div>
</nav>
`;
