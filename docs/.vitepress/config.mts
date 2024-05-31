import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "FandomHub",
  description: "An API for managing and accessing anime and manga-related information, inspired by MyAnimeList. Built with Django and Django Rest Framework, PostgreSQL, SQLite, Redis, and Docker.",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Examples', link: '/markdown-examples' }
    ],

    sidebar: [
      {
        text: 'Examples',
        items: [
          { text: 'Markdown Examples', link: '/markdown-examples' },
          { text: 'Runtime API Examples', link: '/api-examples' },
          { text: 'Business', link: '/business_model' },
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/tyronejosee/project_fandomhub_api' }
    ]
  }
})
