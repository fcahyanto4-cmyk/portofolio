/* ===================================================================
   FAJAR SIDIQ CAHYANTO — PORTFOLIO JAVASCRIPT
   Interactive Simulations, Project Filtering & Navigation
=================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initProjectFilters();
  initPowerBiExplorer();
  initKmeansSimulator();
  initAutomationInspector();
  initCvModal();
  initCopyButtons();
});

/* ===================================================================
   1. NAVBAR & SCROLL BEHAVIOR
=================================================================== */
function initNavbar() {
  const navbar = document.querySelector('.navbar');
  const navLinks = document.querySelectorAll('.nav-link');
  const sections = document.querySelectorAll('section[id]');
  const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
  const navLinksContainer = document.querySelector('.nav-links');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }

    // Scroll spy
    let current = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop - 120;
      const sectionHeight = section.offsetHeight;
      if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  });

  if (mobileMenuBtn && navLinksContainer) {
    mobileMenuBtn.addEventListener('click', () => {
      const isVisible = navLinksContainer.style.display === 'flex';
      navLinksContainer.style.display = isVisible ? 'none' : 'flex';
      if (!isVisible) {
        navLinksContainer.style.flexDirection = 'column';
        navLinksContainer.style.position = 'absolute';
        navLinksContainer.style.top = '74px';
        navLinksContainer.style.left = '0';
        navLinksContainer.style.right = '0';
        navLinksContainer.style.background = 'rgba(9, 13, 22, 0.98)';
        navLinksContainer.style.padding = '20px';
        navLinksContainer.style.borderBottom = '1px solid rgba(255, 255, 255, 0.1)';
      }
    });
  }
}

/* ===================================================================
   2. PROJECT FILTER TABS
=================================================================== */
function initProjectFilters() {
  const filterTabs = document.querySelectorAll('.filter-tab');
  const projectCards = document.querySelectorAll('.project-card');

  filterTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      filterTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      const filterValue = tab.getAttribute('data-filter');

      projectCards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (filterValue === 'all' || category.includes(filterValue)) {
          card.style.display = 'grid';
          card.style.animation = 'fadeIn 0.4s ease';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* ===================================================================
   3. POWER BI 10-PAGE EXPLORER (MODAL / INTERACTION)
=================================================================== */
const powerBiPages = [
  {
    id: 'overview',
    title: '1. Executive Overview',
    kpi: 'Net Sales: Rp 14.82 M | Gross Margin: 34.8% | Transaksi: 184.2k',
    desc: 'Halaman ringkasan eksekutif tingkat tinggi menampilkan tren penjualan bulanan, pencapaian target tahunan, kontribusi Net Sales per wilayah, dan sebaran toko geografis.',
    dax: `// Measure: Total Net Sales
Net Sales = SUMX(FactSales, FactSales[Qty] * FactSales[UnitPrice] * (1 - FactSales[DiscountPct]))`
  },
  {
    id: 'sales-trends',
    title: '2. Penjualan & Tren',
    kpi: 'YoY Growth: +18.4% | MoM Growth: +4.2% | Peak Day: Weekend',
    desc: 'Analisis mendalam pergerakan tren bulanan & kuartalan, Ribbon Chart peringkat kategori produk, serta visual matriks heatmap Net Sales (Bulan × Hari).',
    dax: `// Measure: Sales Growth YoY %
Sales YoY % = 
VAR PrevYear = CALCULATE([Net Sales], SAMEPERIODLASTYEAR(DimDate[Date]))
RETURN DIVIDE([Net Sales] - PrevYear, PrevYear, 0)`
  },
  {
    id: 'stores-region',
    title: '3. Toko & Wilayah',
    kpi: 'Toko Terbaik: Grand Indonesia | Sales/m² Rata-rata: Rp 4.2 Juta',
    desc: 'Evaluasi efisiensi ruang toko fisik menggunakan Scatter Chart (Sales per meter persegi vs Gross Margin %) serta tabel pencapaian target bulanan per gerai.',
    dax: `// Measure: Sales Efficiency per Square Meter
Sales per SqM = DIVIDE([Net Sales], SELECTEDVALUE(DimStore[FloorArea_SqM]), 0)`
  },
  {
    id: 'products-abc',
    title: '4. Produk & Kategori (Pareto ABC)',
    kpi: 'Kelas A: 70% Revenue (20% SKU) | Kelas B: 20% | Kelas C: 10%',
    desc: 'Klasifikasi inventori menggunakan prinsip Pareto 80/20. Memetakan produk kontributor pendapatan utama dan Decomposition Tree penelusuran akar penjualan.',
    dax: `// Measure: Cumulative Sales % for Pareto ABC
Cumulative Sales % = 
VAR CurrentSales = [Net Sales]
VAR TotalSales = CALCULATE([Net Sales], ALLSELECTED(DimProduct))
RETURN DIVIDE(CurrentSales, TotalSales, 0)`
  },
  {
    id: 'promotion',
    title: '5. Promosi & Efektivitas Diskon',
    kpi: 'Rasio Profit/Diskon: 3.2x | Promo Terbaik: Bundling Weekend',
    desc: 'Mengukur ROI promosi ritel. Scatter chart biaya diskon vs Net Sales dan perbandingan Gross Margin antara produk berdiskon vs harga reguler.',
    dax: `// Measure: Profit per Rp Discount
Profit per Discount = DIVIDE([Gross Profit], [Total Discount Cost], 0)`
  },
  {
    id: 'inventory',
    title: '6. Inventori & Kinerja Supplier',
    kpi: 'DIO: 42 Hari | Fill Rate Supplier: 94.8% | Stockout: 3.1 Hari',
    desc: 'Monitoring kesehatan rantai pasok ritel: Days Inventory Outstanding (DIO), kartu skor pemenuhan PO supplier, serta tingkat waste & shrinkage.',
    dax: `// Measure: Days Inventory Outstanding (DIO)
DIO = DIVIDE([Average Inventory Value], [COGS], 0) * 365`
  },
  {
    id: 'customers-rfm',
    title: '7. Pelanggan & Loyalty (RFM Matrix)',
    kpi: 'Active Members: 42.1k | Champions: 18% | At-Risk: 12%',
    desc: 'Segmentasi pelanggan menggunakan model RFM (Recency, Frequency, Monetary Value) untuk membedakan loyalitas tier (Gold, Silver, Bronze) dan laju retensi.',
    dax: `// DAX Calculated Column: RFM Score
RFM_Segment = 
SWITCH(TRUE(),
    [R_Score] >= 4 && [F_Score] >= 4, "Champion",
    [R_Score] >= 3 && [F_Score] >= 3, "Loyal Customer",
    [R_Score] <= 2, "At Risk",
    "Standard")`
  },
  {
    id: 'omnichannel',
    title: '8. Omnichannel & Layanan Pengiriman',
    kpi: 'Avg Delivery: 2.1 Hari | Return Rate: 1.8% | Top Pay: QRIS (46%)',
    desc: 'Analisis performa penjualan multi-kanal (Offline Store vs Mobile App vs Web) serta kecepatan fulfillment regional dan preferensi sistem pembayaran.',
    dax: `// Measure: Cancellation Rate %
Cancel Rate % = DIVIDE([Cancelled Orders], [Total Orders Placed], 0)`
  },
  {
    id: 'profitability',
    title: '9. Operasional & Profitabilitas (EBITDA)',
    kpi: 'EBITDA Margin: 16.2% | Payroll % Sales: 8.4% | Store Conversion: 24%',
    desc: 'Analisis kesehatan keuangan gerai: Footfall toko vs rasio konversi pembeli, Gross Profit vs OpEx vs EBITDA per wilayah operasi.',
    dax: `// Measure: EBITDA Margin %
EBITDA Margin % = DIVIDE([Gross Profit] - [Total Operating Expenses], [Net Sales], 0)`
  },
  {
    id: 'what-if',
    title: '10. Simulasi Skenario What-if',
    kpi: 'Simulasi Dinamis: Sensitivitas Diskon & Target Inflasi',
    desc: 'Menggunakan parameter DAX interaktif untuk memproyeksikan laba bersih saat terjadi kenaikan harga jual, penambahan diskon promo, atau kenaikan biaya sewa gerai.',
    dax: `// What-If Parameter Measure
Simulated Revenue = [Net Sales] * (1 + 'Price Parameter'[Price Value])`
  }
];

function initPowerBiExplorer() {
  const pbiModalBtn = document.getElementById('btn-open-pbi-modal');
  const pbiModal = document.getElementById('pbi-detail-modal');

  if (pbiModalBtn && pbiModal) {
    pbiModalBtn.addEventListener('click', () => {
      openModal(pbiModal);
      renderPbiPageDetails(0);
    });
  }

  // Interactive page buttons inside modal
  const pbiNavList = document.getElementById('pbi-nav-list');
  if (pbiNavList) {
    pbiNavList.innerHTML = powerBiPages.map((page, index) => `
      <button class="pbi-nav-btn ${index === 0 ? 'active' : ''}" data-idx="${index}">
        <span>${page.title}</span>
      </button>
    `).join('');

    const pbiButtons = pbiNavList.querySelectorAll('.pbi-nav-btn');
    pbiButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        pbiButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const idx = parseInt(btn.getAttribute('data-idx'));
        renderPbiPageDetails(idx);
      });
    });
  }
}

function renderPbiPageDetails(index) {
  const page = powerBiPages[index];
  const titleEl = document.getElementById('pbi-page-title');
  const kpiEl = document.getElementById('pbi-page-kpi');
  const descEl = document.getElementById('pbi-page-desc');
  const daxEl = document.getElementById('pbi-page-dax');

  if (titleEl) titleEl.textContent = page.title;
  if (kpiEl) kpiEl.textContent = page.kpi;
  if (descEl) descEl.textContent = page.desc;
  if (daxEl) daxEl.textContent = page.dax;
}

/* ===================================================================
   4. K-MEANS TAX COMPLIANCE SIMULATOR
=================================================================== */
function initKmeansSimulator() {
  const delaySlider = document.getElementById('sim-delay-slider');
  const delayDisplay = document.getElementById('sim-delay-val');
  const taxTypeSelect = document.getElementById('sim-tax-type');
  const clusterResultBadge = document.getElementById('sim-cluster-badge');
  const clusterResultDesc = document.getElementById('sim-cluster-desc');
  const clusterCentroidDist = document.getElementById('sim-centroid-dist');

  function calculateCluster() {
    if (!delaySlider) return;
    const delayDays = parseInt(delaySlider.value);
    const taxType = taxTypeSelect ? taxTypeSelect.value : 'ppn';

    if (delayDisplay) {
      delayDisplay.textContent = delayDays > 0 ? `+${delayDays} Hari (Terlambat)` : `${delayDays} Hari (Tepat Waktu / Lebih Awal)`;
    }

    let status = '';
    let badgeClass = '';
    let description = '';
    let centroid = '';

    // Algoritma evaluasi kepatuhan sesuai skema KKP DJP Fajar
    if (delayDays <= 0) {
      status = 'Cluster 0: Sangat Patuh (Tepat Waktu)';
      badgeClass = 'tepat';
      description = `Wajib Pajak menyetorkan pajak sebelum atau tepat pada tanggal jatuh tempo (${taxType === 'ppn' ? 'tgl 15' : 'tgl 10'}). Masuk ke segmen Wajib Pajak Berisiko Rendah (Low Risk).`;
      centroid = 'Jarak ke Centroid 0: 0.12 (Sangat Dekat)';
    } else if (delayDays <= 20) {
      status = 'Cluster 1: Cukup Patuh (Keterlambatan Minor)';
      badgeClass = 'terlambat';
      description = `Wajib Pajak mengalami keterlambatan pembayaran antara 1 s/d 20 hari dari batas akhir. Terindikasi kendala likuiditas temporer atau administratif. Masuk ke segmen Moderate Risk.`;
      centroid = 'Jarak ke Centroid 1: 0.28 (Moderate)';
    } else {
      status = 'Cluster 2: Tidak Patuh (Keterlambatan Kronis / Belum Bayar)';
      badgeClass = 'belum';
      description = `Keterlambatan melebihi 20 hari atau pembayaran belum terdata. Membutuhkan tindakan surat teguran aktif atau penagihan seketika. Masuk ke segmen High Risk.`;
      centroid = 'Jarak ke Centroid 2: 0.85 (High Risk Centroid)';
    }

    if (clusterResultBadge) {
      clusterResultBadge.textContent = status;
      clusterResultBadge.className = `sim-status-badge ${badgeClass}`;
    }
    if (clusterResultDesc) clusterResultDesc.textContent = description;
    if (clusterCentroidDist) clusterCentroidDist.textContent = centroid;
  }

  if (delaySlider) {
    delaySlider.addEventListener('input', calculateCluster);
  }
  if (taxTypeSelect) {
    taxTypeSelect.addEventListener('change', calculateCluster);
  }
}

/* ===================================================================
   5. WORKFLOW AUTOMATION (n8n) NODE INSPECTOR
=================================================================== */
const automationNodesData = {
  1: {
    title: 'Node 1: Webhook Trigger (Incoming Ingestion)',
    type: 'n8n-nodes-base.webhook',
    desc: 'Menerima payload JSON secara asinkron dari sistem eksternal (misal callback pembayaran Midtrans, input formulir web, atau push API data pajak).',
    json: `{
  "event": "payment.success",
  "order_id": "YMB-20261008-041",
  "gross_amount": 75000,
  "transaction_status": "settlement",
  "timestamp": "2026-10-08T00:33:00+07:00"
}`
  },
  2: {
    title: 'Node 2: Data Cleaning & Normalization (Code / Function)',
    type: 'n8n-nodes-base.code',
    desc: 'Menormalisasi format teks, validasi regex string NPWP (menghilangkan tanda titik dan strip), memverifikasi keabsahan tanggal jatuh tempo, dan mendeteksi duplikasi record.',
    json: `// Clean NPWP & Calculate Difference
const items = $input.all();
return items.map(item => {
  const rawNpwp = item.json.npwp || "";
  const cleanNpwp = rawNpwp.replace(/[^0-9]/g, "");
  return {
    json: {
      ...item.json,
      clean_npwp: cleanNpwp,
      is_valid: cleanNpwp.length === 15 || cleanNpwp.length === 16
    }
  };
});`
  },
  3: {
    title: 'Node 3: Database Upsert & ML Queue (MySQL / Supabase)',
    type: 'n8n-nodes-base.mySql',
    desc: 'Menyimpan record yang sudah tervalidasi ke dalam tabel relasional database dan memicu pipeline kalkulasi K-Means atau penambahan poin loyalty member.',
    json: `INSERT INTO pajak_data (
  nama_wajib_pajak, npwp, masa_pajak, bulan_pajak, jenis_pajak, tanggal_bayar, jumlah_bayar
) VALUES (
  'PT Cipta Kreasi', '012345678901000', '2026', 'September', 'PPN', '2026-10-12', 45000000
) ON DUPLICATE KEY UPDATE tanggal_bayar = VALUES(tanggal_bayar);`
  },
  4: {
    title: 'Node 4: Automated Alerts & BI Sync (Telegram / WhatsApp / Cron)',
    type: 'n8n-nodes-base.telegram',
    desc: 'Mengirimkan notifikasi ringkasan instan kepada admin via Telegram Bot / WhatsApp API, serta memicu endpoint refresh dataset Power BI secara terjadwal.',
    json: `{
  "chat_id": "@tax_data_monitoring",
  "text": "✅ [DATA PIPELINE SUCCESS]\\nNPWP: 012345678901000\\nStatus: Tepat Waktu (H-3 Jatuh Tempo)\\nPower BI Dataset: Synchronized",
  "parse_mode": "Markdown"
}`
  }
};

function initAutomationInspector() {
  const nodes = document.querySelectorAll('.pipeline-node');
  const inspectorTitle = document.getElementById('inspector-title');
  const inspectorDesc = document.getElementById('inspector-desc');
  const inspectorCode = document.getElementById('inspector-code');

  nodes.forEach(node => {
    node.addEventListener('click', () => {
      nodes.forEach(n => n.classList.remove('active'));
      node.classList.add('active');

      const step = node.getAttribute('data-step');
      const data = automationNodesData[step];

      if (data) {
        if (inspectorTitle) inspectorTitle.textContent = data.title;
        if (inspectorDesc) inspectorDesc.textContent = data.desc;
        if (inspectorCode) inspectorCode.textContent = data.json;
      }
    });
  });
}

/* ===================================================================
   6. CV MODAL HANDLER
=================================================================== */
function initCvModal() {
  const openCvBtns = document.querySelectorAll('.btn-open-cv');
  const cvModal = document.getElementById('cv-modal');

  openCvBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      if (cvModal) openModal(cvModal);
    });
  });

  // Generic modal close
  document.querySelectorAll('.modal-close-btn, .modal-backdrop').forEach(el => {
    el.addEventListener('click', (e) => {
      if (e.target.classList.contains('modal-backdrop') || e.target.classList.contains('modal-close-btn') || e.target.closest('.modal-close-btn')) {
        closeAllModals();
      }
    });
  });

  // ESC key to close modal
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeAllModals();
  });
}

function openModal(modalEl) {
  modalEl.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeAllModals() {
  document.querySelectorAll('.modal-backdrop').forEach(m => m.classList.remove('open'));
  document.body.style.overflow = 'auto';
}

/* ===================================================================
   7. COPY TO CLIPBOARD BUTTONS & TOAST
=================================================================== */
function initCopyButtons() {
  const copyButtons = document.querySelectorAll('.copy-trigger');
  const toast = document.getElementById('toast');

  copyButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const textToCopy = btn.getAttribute('data-copy');
      if (textToCopy) {
        navigator.clipboard.writeText(textToCopy).then(() => {
          showToast(`Tersalin ke clipboard: ${textToCopy}`);
        }).catch(() => {
          showToast(`Berhasil disalin!`);
        });
      }
    });
  });
}

function showToast(message) {
  const toast = document.getElementById('toast');
  if (!toast) return;
  toast.textContent = message;
  toast.classList.add('show');
  setTimeout(() => {
    toast.classList.remove('show');
  }, 2800);
}
