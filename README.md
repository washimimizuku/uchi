# Uchi - Website Generator

A modern, config-driven website generator that creates complete websites with both frontend and backend from a simple configuration file.

## Objective

Uchi generates custom websites including:
- **Homepage** - Landing page with customizable sections
- **Static Pages** - About, Contact, Services, etc.
- **Blog System** - Full blog with posts, categories, and pagination
- **Admin Interface** - Content management system

All generated from a single configuration file that defines your site structure, content types, and styling preferences.

## Philosophy

- **Config-driven**: Define your entire site structure in one file
- **Zero-code**: Generate complete websites without writing code
- **Modern stack**: Built with Astro for performance and developer experience
- **Flexible**: Support for various content types and layouts
- **Fast**: Static generation for optimal performance

## Features

- 🚀 **Static Site Generation** - Fast, secure, and SEO-friendly
- 📝 **Content Management** - Built-in admin for easy content editing
- 🎨 **Customizable Themes** - Multiple design options
- 📱 **Responsive Design** - Mobile-first approach
- 🔍 **SEO Optimized** - Meta tags, sitemaps, and structured data
- 📊 **Analytics Ready** - Easy integration with tracking tools

## Quick Start

```bash
# Install dependencies
npm install

# Configure your site
cp config.example.json config.json
# Edit config.json with your site details

# Generate your website
npm run generate

# Start development server
npm run dev
```

## Configuration

Your entire website is defined in `config.json`:

```json
{
  "site": {
    "name": "My Website",
    "url": "https://mysite.com",
    "description": "A beautiful website"
  },
  "pages": [
    { "slug": "about", "title": "About Us", "template": "page" },
    { "slug": "contact", "title": "Contact", "template": "contact" }
  ],
  "blog": {
    "enabled": true,
    "postsPerPage": 10
  },
  "theme": "modern"
}
```

## Status

🚧 **Work in Progress** - This is a proof of concept resurrection of the original Uchi project, updated for modern web development practices.

## Legacy

This project is the spiritual successor to:
- [Apoidea](https://github.com/washimimizuku/apoidea) - Admin-only generator
- [Original Uchi](https://github.com/washimimizuku/uchi) - Django-based website generator

Built with modern tools while maintaining the simplicity and power of the original vision.
