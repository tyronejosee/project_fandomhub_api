import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "FandomHub",
  description: "An API for managing and accessing anime and manga-related information, inspired by MyAnimeList. Built with Django and Django Rest Framework, PostgreSQL, SQLite, Redis, and Docker.",
  lang: 'en-US',
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/assets/logo.svg' }]
  ],

  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    siteTitle: 'FandomHub',
    logo: '/assets/logo.svg',

    nav: [
      { text: 'Documentation', link: '/en/introduction/what_is_fandomhub' },
      { text: 'Examples', link: '/markdown-examples' }
    ],
    search: {
      provider: 'local'
    },
    footer: {
      message: 'Released under the <a href="https://github.com/tyronejosee/project_fandomhub_api/blob/main/LICENSE">MIT License</a>.',
      copyright: 'Copyright © 2023-present <a href="https://github.com/tyronejosee">Tyrone José</a>'
    },

    sidebar: [
      {
        text: 'Introduction',
        // collapsed: true,
        items: [
          { text: 'What is FandomHub', link: '/en/introduction/what_is_fandomhub' },
          { text: 'Installation', link: '/en/introduction/installation' },
          { text: 'Structure folder', link: '/en/introduction/structure' },
        ]
      },
      {
        text: 'Models',
        items: [
          { text: 'Anime model', link: '/en/models/anime' },
          { text: 'Manga model', link: '/en/models/manga' },
          { text: 'Character model', link: '/en/models/character' },
          { text: 'Review model', link: '/en/models/review' },
          { text: 'User model', link: '/en/models/user' },
        ]
      },
      {
        text: 'FAQs',
        items: [
          { text: 'Business model', link: '/en/faqs/business_model' },
          { text: 'License', link: '/en/faqs/license' },
          { text: 'Contribution', link: '/en/faqs/code-style' },
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
      lang: 'en',
    },
    es: {
      label: 'Español',
      lang: 'es',
      link: '/es/index'
    }
  },
  ignoreDeadLinks: true
})
