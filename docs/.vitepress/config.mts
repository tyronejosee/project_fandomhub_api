import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "FandomHub",
  description: "An API for managing and accessing anime and manga-related information, inspired by MyAnimeList. Built with Django and Django Rest Framework, PostgreSQL, SQLite, Redis, and Docker.",
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/assets/logo.svg' }]
  ],
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    siteTitle: 'FandomHub',
    logo: '/assets/logo.svg',
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Examples', link: '/markdown-examples' }
    ],
    footer: {
      message: 'Released under the <a href="https://github.com/tyronejosee/project_fandomhub_api/blob/main/LICENSE">MIT License</a>.',
      copyright: 'Copyright © 2023-present <a href="https://github.com/tyronejosee">Tyrone José</a>'
    },
    sidebar: [
      {
        text: 'Introduction',
        items: [
          { text: 'What is FandomHub', link: '/introduction/what_is_fandomhub' },
          { text: 'Installation', link: '/introduction/installation' },
          { text: 'Structure', link: '/introduction/structure' },
          { text: 'Structure', link: '/introduction/structure' },
          { text: 'Structure', link: '/introduction/structure' },
        ]
      },
      {
        text: 'Models',
        items: [
          { text: 'Anime', link: '/models/anime' },
          { text: 'Classic Fries', link: '/sides/classic-fries' },
        ]
      },
      {
        text: 'Sides',
        items: [
          { text: '8 Pc Cheesy Tots', link: '/sides/8-pc-cheesy-tots' },
          { text: 'Classic Fries', link: '/sides/classic-fries' },
        ]
      },
      {
        text: 'Sides',
        items: [
          { text: '8 Pc Cheesy Tots', link: '/sides/8-pc-cheesy-tots' },
          { text: 'Classic Fries', link: '/sides/classic-fries' },
        ]
      },
      {
        text: 'Sides',
        items: [
          { text: '8 Pc Cheesy Tots', link: '/sides/8-pc-cheesy-tots' },
          { text: 'Classic Fries', link: '/sides/classic-fries' },
        ]
      },
      {
        text: 'Examples',
        items: [
          { text: 'Markdown Examples', link: '/markdown-examples' },
          { text: 'Runtime API Examples', link: '/api-examples' },
          { text: 'Business', link: '/business_model' },
        ]
      },
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/tyronejosee/project_fandomhub_api' }
    ],
  },
  locales: {
    root: {
      label: 'English',
      lang: 'en'
    },
    fr: {
      label: 'Español',
      lang: 'es',
      link: '/es/index'
    }
  }
})
