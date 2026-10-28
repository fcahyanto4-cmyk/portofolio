import { defineConfig } from 'vite';
import { resolve } from 'path';
import fs from 'fs';

const rootDir = import.meta.dirname;

// Dynamically discover all HTML files in root
const htmlFiles = fs.readdirSync(rootDir).filter(file => file.endsWith('.html'));
const input = {};
for (const file of htmlFiles) {
  const name = file.replace(/\.html$/, '');
  input[name] = resolve(rootDir, file);
}

// Custom plugin to ensure all static assets and subfolders are preserved in dist
function copyStaticAssetsPlugin() {
  return {
    name: 'copy-static-assets',
    closeBundle() {
      // 1. Copy entire assets directory to dist/assets
      if (fs.existsSync('assets')) {
        fs.cpSync('assets', 'dist/assets', { recursive: true });
        console.log('✓ Copied assets/ directory to dist/assets/');
      }

      // 2. Copy stitch_design if it exists
      if (fs.existsSync('stitch_design')) {
        fs.cpSync('stitch_design', 'dist/stitch_design', { recursive: true });
        console.log('✓ Copied stitch_design/ directory to dist/stitch_design/');
      }

      // 3. Copy root standalone files (PDFs, JSON, preview images)
      const rootFiles = [
        'CV Fajar sidiq cahyanto.pdf',
        'CV_Fajar_Sidiq_Cahyanto.pdf',
        'tax_ml_data.json',
        'cv_page_1.png',
        'cv_page_2.png'
      ];

      for (const file of rootFiles) {
        if (fs.existsSync(file)) {
          fs.copyFileSync(file, resolve(rootDir, 'dist', file));
          console.log(`✓ Copied ${file} to dist/`);
        }
      }
    }
  };
}

export default defineConfig({
  base: './',
  build: {
    outDir: 'dist',
    rollupOptions: {
      input
    }
  },
  plugins: [
    copyStaticAssetsPlugin()
  ]
});
