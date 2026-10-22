import os

def create_svgs():
    os.makedirs('assets/images', exist_ok=True)
    
    # Power BI Mockup
    svg_pbi = '''<svg viewBox="0 0 800 450" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="pbiBg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0e1525"/>
      <stop offset="100%" stop-color="#182338"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" rx="16" fill="url(#pbiBg)" stroke="#1e293b" stroke-width="2"/>
  <rect x="0" y="0" width="800" height="48" rx="16" fill="#111c30"/>
  <rect x="0" y="32" width="800" height="16" fill="#111c30"/>
  <circle cx="28" cy="24" r="6" fill="#ef4444"/>
  <circle cx="48" cy="24" r="6" fill="#f59e0b"/>
  <circle cx="68" cy="24" r="6" fill="#10b981"/>
  <rect x="96" y="12" width="24" height="24" rx="4" fill="#f59e0b"/>
  <path d="M104 28 L104 22 M108 28 L108 18 M112 28 L112 15" stroke="#111" stroke-width="2" stroke-linecap="round"/>
  <text x="130" y="28" fill="#f1f5f9" font-family="sans-serif" font-size="14" font-weight="bold">Retail Executive Dashboard — Power BI Enterprise</text>
  <rect x="660" y="14" width="120" height="20" rx="10" fill="#1e293b"/>
  <text x="675" y="28" fill="#38bdf8" font-family="sans-serif" font-size="11">10 Analytical Pages</text>

  <!-- Left Side Page Nav -->
  <rect x="16" y="60" width="170" height="374" rx="10" fill="#0b1120" stroke="#1e293b"/>
  <text x="28" y="84" fill="#94a3b8" font-family="sans-serif" font-size="11" font-weight="bold" letter-spacing="1">PAGES NAVIGATOR</text>
  <rect x="22" y="96" width="158" height="26" rx="6" fill="#0284c7" fill-opacity="0.2" stroke="#0284c7" stroke-width="1"/>
  <circle cx="34" cy="109" r="3" fill="#38bdf8"/>
  <text x="44" y="113" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="600">Executive Overview</text>
  <text x="44" y="137" fill="#cbd5e1" font-family="sans-serif" font-size="11">Penjualan &amp; Tren</text>
  <text x="44" y="161" fill="#cbd5e1" font-family="sans-serif" font-size="11">Toko &amp; Wilayah</text>
  <text x="44" y="185" fill="#cbd5e1" font-family="sans-serif" font-size="11">Produk &amp; Kategori</text>
  <text x="44" y="209" fill="#cbd5e1" font-family="sans-serif" font-size="11">Promosi &amp; ROI</text>
  <text x="44" y="233" fill="#cbd5e1" font-family="sans-serif" font-size="11">Inventori &amp; Supplier</text>
  <text x="44" y="257" fill="#cbd5e1" font-family="sans-serif" font-size="11">Pelanggan &amp; Loyalty</text>
  <text x="44" y="281" fill="#cbd5e1" font-family="sans-serif" font-size="11">Omnichannel Layanan</text>
  <text x="44" y="305" fill="#cbd5e1" font-family="sans-serif" font-size="11">Operasional Profit</text>
  <text x="44" y="329" fill="#cbd5e1" font-family="sans-serif" font-size="11">Simulasi What-If</text>

  <!-- KPI Cards Row -->
  <rect x="198" y="60" width="138" height="72" rx="8" fill="#131e33" stroke="#1e293b"/>
  <text x="210" y="78" fill="#94a3b8" font-family="sans-serif" font-size="10">NET SALES</text>
  <text x="210" y="102" fill="#f8fafc" font-family="sans-serif" font-size="17" font-weight="bold">Rp 14.82 M</text>
  <text x="210" y="120" fill="#10b981" font-family="sans-serif" font-size="10">▲ +18.4% YoY</text>

  <rect x="346" y="60" width="138" height="72" rx="8" fill="#131e33" stroke="#1e293b"/>
  <text x="358" y="78" fill="#94a3b8" font-family="sans-serif" font-size="10">GROSS MARGIN %</text>
  <text x="358" y="102" fill="#38bdf8" font-family="sans-serif" font-size="17" font-weight="bold">34.8 %</text>
  <text x="358" y="120" fill="#10b981" font-family="sans-serif" font-size="10">▲ +2.1 pts vs LY</text>

  <rect x="494" y="60" width="138" height="72" rx="8" fill="#131e33" stroke="#1e293b"/>
  <text x="506" y="78" fill="#94a3b8" font-family="sans-serif" font-size="10">TOTAL TRANSACTIONS</text>
  <text x="506" y="102" fill="#f8fafc" font-family="sans-serif" font-size="17" font-weight="bold">184,290</text>
  <text x="506" y="120" fill="#10b981" font-family="sans-serif" font-size="10">Avg Basket Rp 80.4k</text>

  <rect x="642" y="60" width="142" height="72" rx="8" fill="#131e33" stroke="#1e293b"/>
  <text x="654" y="78" fill="#94a3b8" font-family="sans-serif" font-size="10">EBITDA MARGIN</text>
  <text x="654" y="102" fill="#f59e0b" font-family="sans-serif" font-size="17" font-weight="bold">16.2 %</text>
  <text x="654" y="120" fill="#94a3b8" font-family="sans-serif" font-size="10">Optimal OpEx Ratio</text>

  <!-- Chart 1: Monthly Trend Combo Chart -->
  <rect x="198" y="142" width="340" height="140" rx="8" fill="#131e33" stroke="#1e293b"/>
  <text x="210" y="162" fill="#f1f5f9" font-family="sans-serif" font-size="11" font-weight="600">Tren Bulanan: Net Sales &amp; Target</text>
  <rect x="218" y="220" width="14" height="45" rx="2" fill="#0284c7" opacity="0.8"/>
  <rect x="242" y="210" width="14" height="55" rx="2" fill="#0284c7" opacity="0.8"/>
  <rect x="266" y="195" width="14" height="70" rx="2" fill="#0284c7" opacity="0.8"/>
  <rect x="290" y="205" width="14" height="60" rx="2" fill="#0284c7" opacity="0.8"/>
  <rect x="314" y="185" width="14" height="80" rx="2" fill="#0284c7" opacity="0.8"/>
  <rect x="338" y="175" width="14" height="90" rx="2" fill="#0284c7" opacity="0.8"/>
  <rect x="362" y="190" width="14" height="75" rx="2" fill="#0284c7" opacity="0.8"/>
  <rect x="386" y="170" width="14" height="95" rx="2" fill="#0284c7" opacity="0.8"/>
  <rect x="410" y="165" width="14" height="100" rx="2" fill="#06b6d4"/>
  <rect x="434" y="155" width="14" height="110" rx="2" fill="#06b6d4"/>
  <rect x="458" y="160" width="14" height="105" rx="2" fill="#06b6d4"/>
  <rect x="482" y="150" width="14" height="115" rx="2" fill="#06b6d4"/>
  <path d="M225 215 Q 275 190, 325 180 T 425 155 T 489 145" fill="none" stroke="#f59e0b" stroke-width="2.5"/>
  <circle cx="489" cy="145" r="4" fill="#f59e0b"/>

  <!-- Chart 2: Regional Contribution Clustered Bar -->
  <rect x="548" y="142" width="236" height="140" rx="8" fill="#131e33" stroke="#1e293b"/>
  <text x="560" y="162" fill="#f1f5f9" font-family="sans-serif" font-size="11" font-weight="600">Net Sales per Region</text>
  <text x="560" y="185" fill="#94a3b8" font-family="sans-serif" font-size="10">Jabodetabek</text>
  <rect x="630" y="175" width="130" height="12" rx="3" fill="#0ea5e9"/>
  <text x="560" y="210" fill="#94a3b8" font-family="sans-serif" font-size="10">Jawa Barat</text>
  <rect x="630" y="200" width="95" height="12" rx="3" fill="#0ea5e9" opacity="0.85"/>
  <text x="560" y="235" fill="#94a3b8" font-family="sans-serif" font-size="10">Jawa Timur</text>
  <rect x="630" y="225" width="80" height="12" rx="3" fill="#0ea5e9" opacity="0.7"/>
  <text x="560" y="260" fill="#94a3b8" font-family="sans-serif" font-size="10">Sumatera</text>
  <rect x="630" y="250" width="55" height="12" rx="3" fill="#0ea5e9" opacity="0.55"/>

  <!-- Bottom Visuals: ABC Pareto & Store Efficiency -->
  <rect x="198" y="292" width="286" height="142" rx="8" fill="#131e33" stroke="#1e293b"/>
  <text x="210" y="312" fill="#f1f5f9" font-family="sans-serif" font-size="11" font-weight="600">Analisis Pareto ABC (80/20 Rule)</text>
  <rect x="218" y="335" width="65" height="80" rx="4" fill="#10b981" fill-opacity="0.2" stroke="#10b981"/>
  <text x="235" y="360" fill="#10b981" font-family="sans-serif" font-size="14" font-weight="bold">Kelas A</text>
  <text x="225" y="380" fill="#cbd5e1" font-family="sans-serif" font-size="9">70% Revenue</text>
  <text x="225" y="395" fill="#94a3b8" font-family="sans-serif" font-size="9">20% SKU</text>

  <rect x="293" y="345" width="65" height="70" rx="4" fill="#3b82f6" fill-opacity="0.2" stroke="#3b82f6"/>
  <text x="310" y="370" fill="#38bdf8" font-family="sans-serif" font-size="14" font-weight="bold">Kelas B</text>
  <text x="300" y="390" fill="#cbd5e1" font-family="sans-serif" font-size="9">20% Revenue</text>

  <rect x="368" y="360" width="65" height="55" rx="4" fill="#8b5cf6" fill-opacity="0.2" stroke="#8b5cf6"/>
  <text x="385" y="385" fill="#c084fc" font-family="sans-serif" font-size="14" font-weight="bold">Kelas C</text>
  <text x="375" y="403" fill="#cbd5e1" font-family="sans-serif" font-size="9">10% Long-tail</text>

  <rect x="494" y="292" width="290" height="142" rx="8" fill="#131e33" stroke="#1e293b"/>
  <text x="506" y="312" fill="#f1f5f9" font-family="sans-serif" font-size="11" font-weight="600">Efisiensi Toko: Sales / m² vs Margin</text>
  <circle cx="540" cy="370" r="8" fill="#38bdf8" opacity="0.8"/>
  <circle cx="590" cy="345" r="14" fill="#10b981" opacity="0.8"/>
  <circle cx="640" cy="385" r="10" fill="#f59e0b" opacity="0.8"/>
  <circle cx="710" cy="335" r="16" fill="#06b6d4" opacity="0.85"/>
  <circle cx="745" cy="390" r="7" fill="#ec4899" opacity="0.8"/>
  <line x1="520" y1="410" x2="760" y2="410" stroke="#334155" stroke-width="1"/>
  <line x1="520" y1="330" x2="520" y2="410" stroke="#334155" stroke-width="1"/>
  <text x="710" y="422" fill="#64748b" font-family="sans-serif" font-size="9">Sales/m² →</text>
  <text x="500" y="325" fill="#64748b" font-family="sans-serif" font-size="9">Margin %</text>
</svg>'''

    # Tax K-Means Mockup
    svg_km = '''<svg viewBox="0 0 800 450" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="kmBg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0b1220"/>
      <stop offset="100%" stop-color="#131c31"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" rx="16" fill="url(#kmBg)" stroke="#1e293b" stroke-width="2"/>
  <rect x="0" y="0" width="800" height="48" rx="16" fill="#0f172a"/>
  <rect x="0" y="32" width="800" height="16" fill="#0f172a"/>
  <circle cx="28" cy="24" r="6" fill="#ef4444"/>
  <circle cx="48" cy="24" r="6" fill="#f59e0b"/>
  <circle cx="68" cy="24" r="6" fill="#10b981"/>
  <text x="96" y="29" fill="#f8fafc" font-family="sans-serif" font-size="14" font-weight="bold">PajakData K-Means Clustering &amp; Evaluasi Kepatuhan</text>
  <rect x="650" y="14" width="130" height="20" rx="10" fill="#1e293b"/>
  <text x="662" y="28" fill="#10b981" font-family="sans-serif" font-size="11">Python + Flask + MySQL</text>

  <rect x="24" y="64" width="460" height="360" rx="12" fill="#0a0f1d" stroke="#1e293b"/>
  <text x="40" y="92" fill="#f1f5f9" font-family="sans-serif" font-size="13" font-weight="600">Distribusi Clustering Wajib Pajak (K=3)</text>
  <text x="40" y="110" fill="#64748b" font-family="sans-serif" font-size="10">Feature: Selisih Hari Jatuh Tempo (avg_diff) vs Nominal Pembayaran</text>

  <line x1="70" y1="140" x2="450" y2="140" stroke="#1e293b" stroke-dasharray="4"/>
  <line x1="70" y1="220" x2="450" y2="220" stroke="#1e293b" stroke-dasharray="4"/>
  <line x1="70" y1="300" x2="450" y2="300" stroke="#1e293b" stroke-dasharray="4"/>
  <line x1="70" y1="380" x2="450" y2="380" stroke="#334155" stroke-width="1.5"/>
  <line x1="70" y1="130" x2="70" y2="380" stroke="#334155" stroke-width="1.5"/>

  <line x1="210" y1="130" x2="210" y2="380" stroke="#38bdf8" stroke-dasharray="5" stroke-width="1.5"/>
  <text x="215" y="145" fill="#38bdf8" font-family="sans-serif" font-size="9">Jatuh Tempo (H-0)</text>

  <g fill="#10b981" opacity="0.8">
    <circle cx="110" cy="230" r="5"/><circle cx="125" cy="270" r="5"/><circle cx="140" cy="190" r="6"/>
    <circle cx="155" cy="310" r="5"/><circle cx="170" cy="250" r="5"/><circle cx="185" cy="220" r="6"/>
    <circle cx="130" cy="340" r="5"/><circle cx="160" cy="170" r="6"/><circle cx="195" cy="290" r="5"/>
  </g>
  <polygon points="155,235 159,247 172,247 161,255 165,267 155,259 145,267 149,255 138,247 151,247" fill="#34d399" stroke="#fff" stroke-width="1.5"/>

  <g fill="#f59e0b" opacity="0.8">
    <circle cx="245" cy="260" r="5"/><circle cx="270" cy="220" r="6"/><circle cx="290" cy="320" r="5"/>
    <circle cx="310" cy="280" r="5"/><circle cx="260" cy="340" r="5"/><circle cx="325" cy="240" r="6"/>
  </g>
  <polygon points="290,250 294,262 307,262 296,270 300,282 290,274 280,282 284,270 273,262 286,262" fill="#fbbf24" stroke="#fff" stroke-width="1.5"/>

  <g fill="#ef4444" opacity="0.8">
    <circle cx="370" cy="330" r="5"/><circle cx="395" cy="280" r="6"/><circle cx="420" cy="350" r="5"/>
    <circle cx="405" cy="310" r="5"/><circle cx="380" cy="360" r="5"/><circle cx="430" cy="270" r="6"/>
  </g>
  <polygon points="400,290 404,302 417,302 406,310 410,322 400,314 390,322 394,310 383,302 396,302" fill="#f87171" stroke="#fff" stroke-width="1.5"/>

  <rect x="500" y="64" width="276" height="165" rx="10" fill="#111a2e" stroke="#1e293b"/>
  <text x="516" y="88" fill="#f1f5f9" font-family="sans-serif" font-size="12" font-weight="600">Evaluasi K-Means Model</text>
  
  <rect x="516" y="104" width="118" height="52" rx="6" fill="#0b1220"/>
  <text x="526" y="120" fill="#94a3b8" font-family="sans-serif" font-size="9">SILHOUETTE SCORE</text>
  <text x="526" y="143" fill="#38bdf8" font-family="sans-serif" font-size="16" font-weight="bold">0.684</text>
  <text x="575" y="143" fill="#10b981" font-family="sans-serif" font-size="9">Optimal</text>

  <rect x="644" y="104" width="118" height="52" rx="6" fill="#0b1220"/>
  <text x="654" y="120" fill="#94a3b8" font-family="sans-serif" font-size="9">ELBOW METHOD</text>
  <text x="654" y="143" fill="#f59e0b" font-family="sans-serif" font-size="16" font-weight="bold">K = 3</text>
  <text x="690" y="143" fill="#94a3b8" font-family="sans-serif" font-size="9">Inertia Drop</text>

  <path d="M526 205 Q 550 185, 580 178 T 640 173 T 730 170" fill="none" stroke="#a855f7" stroke-width="2"/>
  <circle cx="580" cy="178" r="4" fill="#f59e0b" stroke="#fff" stroke-width="1"/>
  <text x="590" y="194" fill="#f59e0b" font-family="sans-serif" font-size="9">Optimal Elbow (K=3)</text>

  <rect x="500" y="240" width="276" height="184" rx="10" fill="#111a2e" stroke="#1e293b"/>
  <text x="516" y="264" fill="#f1f5f9" font-family="sans-serif" font-size="12" font-weight="600">Distribusi Kepatuhan Wajib Pajak</text>

  <rect x="516" y="280" width="244" height="36" rx="6" fill="#0b1220" stroke="#10b981" stroke-opacity="0.3"/>
  <circle cx="532" cy="298" r="5" fill="#10b981"/>
  <text x="546" y="294" fill="#f1f5f9" font-family="sans-serif" font-size="11" font-weight="600">Cluster 0: Sangat Patuh</text>
  <text x="546" y="308" fill="#94a3b8" font-family="sans-serif" font-size="9">Bayar Tepat Waktu (diff ≤ 0 hari)</text>
  <text x="720" y="302" fill="#10b981" font-family="sans-serif" font-size="11" font-weight="bold">58%</text>

  <rect x="516" y="324" width="244" height="36" rx="6" fill="#0b1220" stroke="#f59e0b" stroke-opacity="0.3"/>
  <circle cx="532" cy="342" r="5" fill="#f59e0b"/>
  <text x="546" y="338" fill="#f1f5f9" font-family="sans-serif" font-size="11" font-weight="600">Cluster 1: Cukup Patuh</text>
  <text x="546" y="352" fill="#94a3b8" font-family="sans-serif" font-size="9">Terlambat 1 - 20 hari</text>
  <text x="720" y="346" fill="#f59e0b" font-family="sans-serif" font-size="11" font-weight="bold">27%</text>

  <rect x="516" y="368" width="244" height="36" rx="6" fill="#0b1220" stroke="#ef4444" stroke-opacity="0.3"/>
  <circle cx="532" cy="386" r="5" fill="#ef4444"/>
  <text x="546" y="382" fill="#f1f5f9" font-family="sans-serif" font-size="11" font-weight="600">Cluster 2: Tidak Patuh</text>
  <text x="546" y="396" fill="#94a3b8" font-family="sans-serif" font-size="9">Keterlambatan tinggi / Tunggakan</text>
  <text x="720" y="390" fill="#ef4444" font-family="sans-serif" font-size="11" font-weight="bold">15%</text>
</svg>'''

    # Workflow Automation Mockup
    svg_wf = '''<svg viewBox="0 0 800 450" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="n8nBg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0e111d"/>
      <stop offset="100%" stop-color="#161c2d"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" rx="16" fill="url(#n8nBg)" stroke="#1e293b" stroke-width="2"/>
  <rect x="0" y="0" width="800" height="48" rx="16" fill="#111827"/>
  <rect x="0" y="32" width="800" height="16" fill="#111827"/>
  <circle cx="28" cy="24" r="6" fill="#ef4444"/>
  <circle cx="48" cy="24" r="6" fill="#f59e0b"/>
  <circle cx="68" cy="24" r="6" fill="#10b981"/>
  <text x="96" y="29" fill="#f8fafc" font-family="sans-serif" font-size="14" font-weight="bold">Workflow Automation Architecture — n8n &amp; Data Pipeline</text>
  <rect x="635" y="14" width="145" height="20" rx="10" fill="#ea580c" fill-opacity="0.2" stroke="#ea580c" stroke-width="1"/>
  <text x="647" y="28" fill="#fb923c" font-family="sans-serif" font-size="11">⚡ Pipeline Architecture</text>

  <path d="M155 180 C 190 180, 200 180, 245 180" stroke="#ea580c" stroke-width="3" stroke-dasharray="6" fill="none"/>
  <path d="M375 180 C 410 180, 420 180, 465 180" stroke="#f59e0b" stroke-width="3" stroke-dasharray="6" fill="none"/>
  <path d="M595 180 C 625 180, 625 125, 655 125" stroke="#10b981" stroke-width="3" stroke-dasharray="6" fill="none"/>
  <path d="M595 180 C 625 180, 625 245, 655 245" stroke="#06b6d4" stroke-width="3" stroke-dasharray="6" fill="none"/>

  <g transform="translate(35, 125)">
    <rect width="120" height="110" rx="12" fill="#1f2937" stroke="#ea580c" stroke-width="2"/>
    <rect x="10" y="10" width="32" height="32" rx="8" fill="#ea580c"/>
    <text x="18" y="32" fill="#fff" font-family="sans-serif" font-size="16" font-weight="bold">⚡</text>
    <text x="50" y="28" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="bold">Webhook</text>
    <text x="50" y="42" fill="#9ca3af" font-family="sans-serif" font-size="9">Trigger Ingestion</text>
    <line x1="10" y1="52" x2="110" y2="52" stroke="#374151"/>
    <text x="12" y="72" fill="#d1d5db" font-family="sans-serif" font-size="9">• POST /api/data</text>
    <text x="12" y="88" fill="#d1d5db" font-family="sans-serif" font-size="9">• Webhook trigger</text>
    <circle cx="120" cy="55" r="5" fill="#ea580c"/>
  </g>

  <g transform="translate(245, 125)">
    <rect width="130" height="110" rx="12" fill="#1f2937" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="0" cy="55" r="5" fill="#f59e0b"/>
    <rect x="10" y="10" width="32" height="32" rx="8" fill="#f59e0b"/>
    <text x="16" y="32" fill="#111" font-family="sans-serif" font-size="14" font-weight="bold">&lt;/&gt;</text>
    <text x="50" y="28" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="bold">Data Clean</text>
    <text x="50" y="42" fill="#9ca3af" font-family="sans-serif" font-size="9">ETL &amp; Validation</text>
    <line x1="10" y1="52" x2="120" y2="52" stroke="#374151"/>
    <text x="12" y="72" fill="#d1d5db" font-family="sans-serif" font-size="9">• Schema normalize</text>
    <text x="12" y="88" fill="#d1d5db" font-family="sans-serif" font-size="9">• Deduplication</text>
    <circle cx="130" cy="55" r="5" fill="#f59e0b"/>
  </g>

  <g transform="translate(465, 125)">
    <rect width="130" height="110" rx="12" fill="#1f2937" stroke="#3b82f6" stroke-width="2"/>
    <circle cx="0" cy="55" r="5" fill="#3b82f6"/>
    <rect x="10" y="10" width="32" height="32" rx="8" fill="#3b82f6"/>
    <text x="19" y="32" fill="#fff" font-family="sans-serif" font-size="14" font-weight="bold">🗄️</text>
    <text x="50" y="28" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="bold">DB Pipeline</text>
    <text x="50" y="42" fill="#9ca3af" font-family="sans-serif" font-size="9">MySQL / Supabase</text>
    <line x1="10" y1="52" x2="120" y2="52" stroke="#374151"/>
    <text x="12" y="72" fill="#d1d5db" font-family="sans-serif" font-size="9">• Upsert records</text>
    <text x="12" y="88" fill="#d1d5db" font-family="sans-serif" font-size="9">• Trigger ML calc</text>
    <circle cx="130" cy="55" r="5" fill="#3b82f6"/>
  </g>

  <g transform="translate(655, 70)">
    <rect width="115" height="90" rx="10" fill="#1f2937" stroke="#10b981" stroke-width="2"/>
    <circle cx="0" cy="45" r="5" fill="#10b981"/>
    <rect x="10" y="10" width="28" height="28" rx="6" fill="#10b981"/>
    <text x="16" y="30" fill="#fff" font-family="sans-serif" font-size="13">🔔</text>
    <text x="44" y="26" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="bold">Alert Bot</text>
    <text x="44" y="38" fill="#9ca3af" font-family="sans-serif" font-size="8">Telegram/WA</text>
    <text x="12" y="60" fill="#d1d5db" font-family="sans-serif" font-size="9">• Summary send</text>
    <text x="12" y="74" fill="#d1d5db" font-family="sans-serif" font-size="9">• Anomaly alert</text>
  </g>

  <g transform="translate(655, 195)">
    <rect width="115" height="90" rx="10" fill="#1f2937" stroke="#06b6d4" stroke-width="2"/>
    <circle cx="0" cy="45" r="5" fill="#06b6d4"/>
    <rect x="10" y="10" width="28" height="28" rx="6" fill="#06b6d4"/>
    <text x="16" y="30" fill="#fff" font-family="sans-serif" font-size="13">📊</text>
    <text x="44" y="26" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="bold">BI Refresh</text>
    <text x="44" y="38" fill="#9ca3af" font-family="sans-serif" font-size="8">Daily Cron</text>
    <text x="12" y="60" fill="#d1d5db" font-family="sans-serif" font-size="9">• Auto dataset sync</text>
    <text x="12" y="74" fill="#d1d5db" font-family="sans-serif" font-size="9">• Power BI refresh</text>
  </g>

  <rect x="35" y="300" width="735" height="125" rx="12" fill="#111827" stroke="#1e293b"/>
  <text x="55" y="330" fill="#f8fafc" font-family="sans-serif" font-size="13" font-weight="bold">Workflow Automation Architecture &amp; Execution Pipeline</text>
  <text x="55" y="352" fill="#94a3b8" font-family="sans-serif" font-size="11">Mengotomatisasi pemrosesan data berulang tanpa intervensi manual: validasi webhook, pembersihan data terpusat,</text>
  <text x="55" y="370" fill="#94a3b8" font-family="sans-serif" font-size="11">pengiriman sinyal notifikasi anomali, hingga orkestrasi pembaruan dataset BI secara berkala.</text>
  
  <rect x="55" y="385" width="135" height="24" rx="6" fill="#1e293b"/>
  <text x="68" y="401" fill="#38bdf8" font-family="sans-serif" font-size="10" font-weight="bold">✓ Zero Human Error</text>

  <rect x="200" y="385" width="145" height="24" rx="6" fill="#1e293b"/>
  <text x="212" y="401" fill="#34d399" font-family="sans-serif" font-size="10" font-weight="bold">✓ Real-time Sync (API)</text>

  <rect x="355" y="385" width="140" height="24" rx="6" fill="#1e293b"/>
  <text x="367" y="401" fill="#fbbf24" font-family="sans-serif" font-size="10" font-weight="bold">✓ Event-Driven Cron</text>
</svg>'''

    # YMB Mockup
    svg_ymb = '''<svg viewBox="0 0 800 450" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="ymbBg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#081711"/>
      <stop offset="100%" stop-color="#0f2e21"/>
    </linearGradient>
  </defs>
  <rect width="800" height="450" rx="16" fill="url(#ymbBg)" stroke="#164e35" stroke-width="2"/>
  <rect x="0" y="0" width="800" height="48" rx="16" fill="#061a12"/>
  <rect x="0" y="32" width="800" height="16" fill="#061a12"/>
  <circle cx="28" cy="24" r="6" fill="#ef4444"/>
  <circle cx="48" cy="24" r="6" fill="#f59e0b"/>
  <circle cx="68" cy="24" r="6" fill="#10b981"/>
  <text x="96" y="29" fill="#ecfdf5" font-family="sans-serif" font-size="14" font-weight="bold">Yuk Main Bola (YMB) — Minisoccer Community Platform</text>
  <rect x="630" y="14" width="150" height="20" rx="10" fill="#059669" fill-opacity="0.2" stroke="#10b981" stroke-width="1"/>
  <text x="642" y="28" fill="#34d399" font-family="sans-serif" font-size="11">Next.js 16 + Supabase</text>

  <rect x="24" y="64" width="460" height="360" rx="12" fill="#092319" stroke="#164e35"/>
  <text x="40" y="92" fill="#f0fdf4" font-family="sans-serif" font-size="14" font-weight="bold">Jadwal &amp; Live Slot Minisoccer</text>
  <text x="40" y="110" fill="#86efac" font-family="sans-serif" font-size="10">Automated Booking • Midtrans Payment Gateway • QR Check-in</text>

  <rect x="40" y="128" width="428" height="80" rx="8" fill="#0d3324" stroke="#1e5b41"/>
  <text x="56" y="152" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="bold">Fun Match Minggu Pagi — Pitch Arena BSD</text>
  <text x="56" y="170" fill="#94a3b8" font-family="sans-serif" font-size="10">Minggu, 07:00 - 09:00 WIB • Rumput Sintetis FIFA Pro</text>
  <rect x="56" y="182" width="75" height="18" rx="9" fill="#ef4444" fill-opacity="0.2" stroke="#ef4444" stroke-width="1"/>
  <text x="66" y="195" fill="#fca5a5" font-family="sans-serif" font-size="9" font-weight="bold">FULL BOOKED</text>
  <text x="365" y="156" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold">Rp 65.000</text>
  <text x="380" y="170" fill="#94a3b8" font-family="sans-serif" font-size="9">/ player</text>

  <rect x="40" y="220" width="428" height="80" rx="8" fill="#0d3324" stroke="#10b981" stroke-width="1.5"/>
  <text x="56" y="244" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="bold">Minisoccer Wednesday Night — Bintaro Stadium</text>
  <text x="56" y="262" fill="#94a3b8" font-family="sans-serif" font-size="10">Rabu, 19:00 - 21:00 WIB • Wasit &amp; Rompi Lengkap</text>
  <rect x="56" y="274" width="95" height="18" rx="9" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="1"/>
  <text x="66" y="287" fill="#86efac" font-family="sans-serif" font-size="9" font-weight="bold">4 SLOT TERSISA</text>
  <text x="365" y="248" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold">Rp 70.000</text>
  <rect x="365" y="268" width="85" height="24" rx="6" fill="#10b981"/>
  <text x="382" y="284" fill="#061a12" font-family="sans-serif" font-size="10" font-weight="bold">Book Now</text>

  <rect x="40" y="312" width="428" height="80" rx="8" fill="#0d3324" stroke="#1e5b41"/>
  <text x="56" y="336" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="bold">Super League Internal Community Match</text>
  <text x="56" y="354" fill="#94a3b8" font-family="sans-serif" font-size="10">Sabtu, 16:00 - 18:00 WIB • Live Stream &amp; Fotografer</text>
  <rect x="56" y="366" width="95" height="18" rx="9" fill="#38bdf8" fill-opacity="0.2" stroke="#38bdf8" stroke-width="1"/>
  <text x="66" y="379" fill="#7dd3fc" font-family="sans-serif" font-size="9" font-weight="bold">OPEN REGIST</text>
  <text x="365" y="340" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold">Rp 75.000</text>

  <rect x="500" y="64" width="276" height="170" rx="10" fill="#0a2217" stroke="#164e35"/>
  <text x="516" y="88" fill="#ecfdf5" font-family="sans-serif" font-size="12" font-weight="bold">Key Production Features</text>
  <text x="516" y="110" fill="#34d399" font-family="sans-serif" font-size="10">✓ Realtime Booking &amp; Slot Lock</text>
  <text x="516" y="128" fill="#34d399" font-family="sans-serif" font-size="10">✓ Midtrans Payment Webhook</text>
  <text x="516" y="146" fill="#34d399" font-family="sans-serif" font-size="10">✓ Auto-Expire Unpaid Orders (Cron)</text>
  <text x="516" y="164" fill="#34d399" font-family="sans-serif" font-size="10">✓ Member Loyalty Point Engine</text>
  <text x="516" y="182" fill="#34d399" font-family="sans-serif" font-size="10">✓ Admin Dashboard with Recharts</text>
  <text x="516" y="200" fill="#34d399" font-family="sans-serif" font-size="10">✓ Role-Based Access Control</text>

  <rect x="500" y="246" width="276" height="178" rx="10" fill="#0a2217" stroke="#164e35"/>
  <text x="516" y="270" fill="#ecfdf5" font-family="sans-serif" font-size="12" font-weight="bold">Tech Stack Overview</text>
  <rect x="516" y="285" width="115" height="26" rx="6" fill="#061a12" stroke="#1e5b41"/>
  <text x="526" y="302" fill="#86efac" font-family="sans-serif" font-size="10">Next.js 16 (App)</text>

  <rect x="643" y="285" width="118" height="26" rx="6" fill="#061a12" stroke="#1e5b41"/>
  <text x="653" y="302" fill="#86efac" font-family="sans-serif" font-size="10">React 19 &amp; TS</text>

  <rect x="516" y="320" width="115" height="26" rx="6" fill="#061a12" stroke="#1e5b41"/>
  <text x="526" y="337" fill="#86efac" font-family="sans-serif" font-size="10">Supabase Postgres</text>

  <rect x="643" y="320" width="118" height="26" rx="6" fill="#061a12" stroke="#1e5b41"/>
  <text x="653" y="337" fill="#86efac" font-family="sans-serif" font-size="10">Tailwind CSS v4</text>

  <rect x="516" y="355" width="245" height="52" rx="6" fill="#061a12" stroke="#1e5b41"/>
  <text x="526" y="374" fill="#f8fafc" font-family="sans-serif" font-size="10" font-weight="bold">Midtrans Payment Gateway</text>
  <text x="526" y="392" fill="#94a3b8" font-family="sans-serif" font-size="9">Virtual Account, QRIS &amp; E-Wallet</text>
</svg>'''

    with open('assets/images/powerbi-mockup.svg', 'w', encoding='utf-8') as f:
        f.write(svg_pbi)
    with open('assets/images/kmeans-mockup.svg', 'w', encoding='utf-8') as f:
        f.write(svg_km)
    with open('assets/images/n8n-workflow.svg', 'w', encoding='utf-8') as f:
        f.write(svg_wf)
    with open('assets/images/ymb-mockup.svg', 'w', encoding='utf-8') as f:
        f.write(svg_ymb)

    print('Successfully generated all mockups!')

if __name__ == '__main__':
    create_svgs()
