import { loadConfig, generatePages } from '../src/lib/config.ts';

console.log('🚀 Generating Uchi website...');

try {
  const config = loadConfig();
  console.log(`📝 Loaded config for: ${config.site.name}`);
  
  // Generate pages from config
  generatePages(config);
  console.log(`✅ Generated ${config.pages.length} pages`);
  
  console.log('🎉 Website generation complete!');
} catch (error) {
  console.error('❌ Generation failed:', error.message);
  process.exit(1);
}
