import fs from 'fs';
import path from 'path';

export interface SiteConfig {
  site: {
    name: string;
    url: string;
    description: string;
    author: string;
  };
  pages: Array<{
    slug: string;
    title: string;
    template: string;
    content: string;
  }>;
  blog: {
    enabled: boolean;
    title: string;
    description: string;
    postsPerPage: number;
  };
  theme: {
    name: string;
    colors: {
      primary: string;
      secondary: string;
    };
  };
  navigation: Array<{
    label: string;
    url: string;
  }>;
}

export function loadConfig(): SiteConfig {
  const configPath = path.join(process.cwd(), 'config.json');
  
  if (!fs.existsSync(configPath)) {
    throw new Error('config.json not found. Copy config.example.json to config.json');
  }
  
  const configData = fs.readFileSync(configPath, 'utf-8');
  return JSON.parse(configData) as SiteConfig;
}

export function generatePages(config: SiteConfig) {
  // Generate page files from config
  config.pages.forEach(page => {
    const pageContent = `---
title: "${page.title}"
description: "${page.content}"
template: "${page.template}"
---

# ${page.title}

${page.content}
`;
    
    const pagePath = path.join(process.cwd(), 'src/content/pages', `${page.slug}.md`);
    fs.writeFileSync(pagePath, pageContent);
  });
}
