document.addEventListener('DOMContentLoaded', async () => {
  const container = document.getElementById('planes-container');

  try {
    const response = await fetch('/planes/api/planes');
    const planes = await response.json();

    if (planes.length === 0) {
      container.innerHTML = '<p>No hay planes disponibles.</p>';
      return;
    }

    planes.forEach(plan => {
      const card = document.createElement('div');
      card.className = 'plan-card';
      card.innerHTML = `
        <h2>${plan.nombre}</h2>
        <p>${plan.descripcion}</p>
        <p><strong>Precio:</strong> $${plan.precio}</p>
        <p><strong>Duración:</strong> ${plan.duracion} horas</p>
      `;
      container.appendChild(card);
    });
  } catch (error) {
    console.error('Error cargando los planes:', error);
    container.innerHTML = '<p>Error al cargar los planes.</p>';
  }
});
