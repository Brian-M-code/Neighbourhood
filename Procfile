web: gunicorn hood.wsgi --log-file -





{%extends 'base.html'%}
{% block content %}
  {{block.super}}
  <div style="text-align:center; padding-top: 130px; padding-bottom: 130px; " class="container-fluid" id="moda">
    <div class="content text-center">
      <h1 style="color:white" data-hover="Thee Hood">
        Karibu NeighbourHood</h1>
        <p style="color: white;">Neighbourhood is still Home.</p>
    </div>
  </div>
  <div class="container">
    <hr>
    <a href="{% url 'new-hood'%}">
      <button class="btn btn-outline-dark btn-sm" style="color:white">Create a neighbourhood</button>
    </a>
    <hr>