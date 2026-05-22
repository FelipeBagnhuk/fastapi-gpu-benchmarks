const resultArea = document.getElementById('result-area');
const searchName = document.getElementById('search-name');
const searchButton = document.getElementById('search-button');
const brandSelect = document.getElementById('brand-select');
const brandButton = document.getElementById('brand-button');
const costName = document.getElementById('cost-name');
const priceInput = document.getElementById('price-input');
const costButton = document.getElementById('cost-button');

const apiBase = '/gpus';
const backendStatus = document.querySelector('.status-card strong');

function formatFps(val) {
  if (val === null || val === undefined || val === '') return '-';
  return `${val} FPS`;
}

function scrollToResults() {
  if (!resultArea) return;
  try {
    resultArea.scrollIntoView({ behavior: 'smooth', block: 'start' });
  } catch (e) {
    window.scrollTo({ top: resultArea.offsetTop, behavior: 'smooth' });
  }
}

function formatCurrency(val) {
  if (val === null || val === undefined || val === '') return '-';
  const n = Number(val);
  if (Number.isNaN(n)) return '-';
  return n.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL', minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

function showMessage(text, danger = false) {
  resultArea.innerHTML = `<div class="message">${text}</div>`;
}

async function checkBackend() {
  backendStatus.textContent = 'Verificando...';
  backendStatus.style.color = 'var(--muted)';
  try {
    const response = await fetch('/health');
    if (!response.ok) throw new Error();
    backendStatus.textContent = 'Ativo';
    backendStatus.style.color = 'var(--accent)';
  } catch {
    backendStatus.textContent = 'Offline';
    backendStatus.style.color = '#ff6f6f';
  }
}

window.addEventListener('load', checkBackend);

function createTable(headers, rows) {
  const table = document.createElement('table');
  const thead = document.createElement('thead');
  const headRow = document.createElement('tr');

  headers.forEach(header => {
    const th = document.createElement('th');
    th.textContent = header;
    headRow.appendChild(th);
  });

  thead.appendChild(headRow);
  table.appendChild(thead);

  const tbody = document.createElement('tbody');
  rows.forEach(row => {
    const tr = document.createElement('tr');
    row.forEach(cell => {
      const td = document.createElement('td');
      td.textContent = cell;
      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  });

  table.appendChild(tbody);
  return table;
}

function renderGpuSummary(gpu) {
  const content = document.createElement('div');
  content.className = 'table-shell';

  const headers = ['Campo', 'Valor'];
  const rows = [
    ['Nome', gpu.name],
    ['Marca', gpu.brand],
    ['1080p Medium', formatFps(gpu.fps_1080p_medium)],
    ['1080p Ultra', formatFps(gpu.fps_1080p_ultra)],
    ['1440p', formatFps(gpu.fps_1440p)],
    ['4K', formatFps(gpu.fps_4k)],
  ];

  content.appendChild(createTable(headers, rows));
  resultArea.innerHTML = '';
  resultArea.appendChild(content);
  scrollToResults();
}

function renderBrandList(gpus, brand) {
  const content = document.createElement('div');
  content.className = 'table-shell';

  const headers = ['Nome', '1080p Medium', '1080p Ultra', '1440p', '4K'];
  const rows = gpus.map(gpu => [
    gpu.name,
    formatFps(gpu.fps_1080p_medium),
    formatFps(gpu.fps_1080p_ultra),
    formatFps(gpu.fps_1440p),
    formatFps(gpu.fps_4k),
  ]);

  content.appendChild(createTable(headers, rows));
  resultArea.innerHTML = `<div class="card-line"><strong>Marca:</strong> ${brand}</div>`;
  resultArea.appendChild(content);
  scrollToResults();
}

function renderCostResult(data) {
  const content = document.createElement('div');
  content.innerHTML = `
    <div class="card-line"><strong>GPU:</strong> ${data.gpu} — ${data.brand}</div>
    <div class="table-shell"></div>
  `;

  const rows = [
    ['1080p Medium', formatCurrency(data.cost_per_frame['1080p_medium'])],
    ['1080p Ultra', formatCurrency(data.cost_per_frame['1080p_ultra'])],
    ['1440p', formatCurrency(data.cost_per_frame['1440p'])],
    ['4K', formatCurrency(data.cost_per_frame['4k'])],
  ];

  const tableContainer = content.querySelector('.table-shell');
  const table = createTable(['Resolução', 'Custo por frame (R$)'], rows);
  tableContainer.appendChild(table);

  resultArea.innerHTML = '';
  resultArea.appendChild(content);
  scrollToResults();
}

async function requestJson(url) {
  const response = await fetch(url);
  if (!response.ok) {
    const error = await response.json().catch(() => null);
    throw new Error(error?.detail || 'Erro na requisição');
  }
  return response.json();
}

searchButton.addEventListener('click', async () => {
  const query = searchName.value.trim();
  if (!query) {
    showMessage('Digite o nome da GPU para buscar.');
    return;
  }
  try {
    resultArea.innerHTML = '<p class="hint">Buscando...</p>';
    const gpu = await requestJson(`${apiBase}/search?q=${encodeURIComponent(query)}`);
    renderGpuSummary(gpu);
  } catch (error) {
    showMessage(error.message, true);
  }
});

brandButton.addEventListener('click', async () => {
  const brand = brandSelect.value;
  try {
    resultArea.innerHTML = '<p class="hint">Buscando GPUs da marca...</p>';
    const gpus = await requestJson(`${apiBase}/brand?brand=${encodeURIComponent(brand)}`);
    renderBrandList(gpus, brand);
  } catch (error) {
    showMessage(error.message, true);
  }
});

costButton.addEventListener('click', async () => {
  const query = costName.value.trim();
  const price = Number(priceInput.value);
  if (!query || !price || price <= 0) {
    showMessage('Informe o nome da GPU e um preço válido.');
    return;
  }
  try {
    resultArea.innerHTML = '<p class="hint">Calculando custo por frame...</p>';
    const data = await requestJson(`${apiBase}/cost?q=${encodeURIComponent(query)}&price=${encodeURIComponent(price)}`);
    renderCostResult(data);
  } catch (error) {
    showMessage(error.message, true);
  }
});
