// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Logz.io Docs',
  favicon: 'https://logz.io/wp-content/themes/Avada-Child-Theme-logz/theme_favicon/apple-touch-icon.png',

  // Set the production url of your site here
  url: 'https://your-docusaurus-test-site.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'facebook', // Usually your GitHub org/user name.
  projectName: 'docusaurus', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  plugins: [
    [
    '@cmfcmf/docusaurus-search-local',
    {
    // Add your options here, if any
    },
    ],
    [
      'docusaurus-plugin-includes',
      {
        sharedFolders: [
          { source: '../../_shared', target: '../docs/shared'},
          { source: '../../static/includes', target: '../docs/includes'}, // Added your shared folder here
        ],
        postBuildDeletedFolders: ['shared'],
        replacements: [
          { key: '{ProductName}', value: 'Logz.io' },
          { key: '{ShortName}', value: 'Logz' },
        ],
        embeds: [
          {
            key: 'myAwesomePlugin',
            embedFunction: function(code) { 
              return `...`; // Adjust according to your needs
            }
          }
        ],
        injectedHtmlTags: {
          preBodyTags: [`<link rel="stylesheet" href="https://cdn.example.com/style.css" type="text/css">`]
        }
      },
    ],
    ],

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/logzio/documentation/tree/master',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      docs: {
      sidebar: {
        hideable: true,
        autoCollapseCategories: true,
       },
      },
      // Replace with your project's social card
      image: 'https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg',
      navbar: {
        title: 'Logz.io Docs',
        logo: {
          alt: 'Logz.io Docs',
          src: 'https://docs.logz.io/images/logo/logz-symbol.svg',
        },
        items: [
          {
            type: 'search',
            position: 'right',
          },
          {to: '/docs/category/send-your-data/', label: 'Ship data', position: 'left'},
          {to: 'https://docs.logz.io/api/', label: 'API', position: 'left'},
          {to: 'https://status.logz.io/', label: 'System status', position: 'left'},
          {to: 'https://logz.io/blog/', label: 'Blog', position: 'left'},
          {
            href: 'https://app.logz.io/',
            label: 'Login',
            position: 'right',
          },
        ],
      },
      tableOfContents: {
        minHeadingLevel: 2,
        maxHeadingLevel: 5,
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Additional Links',
            items: [
              {
                label: 'Blog',
                href: 'https://logz.io/blog/',
              },
              {
                label: 'Videos',
                href: 'https://logz.io/learn/video/',
              },
              {
                label: 'Notices for 3rd Party Software included with the Logz.io Platform',
                to: 'https://dytvr9ot2sszz.cloudfront.net/logz-docs/legal/3rd-party-software-included-with-the-logz.io-platform-sep-2022.pdf',
              },
              {
                label: 'Report a security issue',
                to: 'https://docs.logz.io/report-a-security-issue/',
              },
            ],
          },
          {
            title: 'Legal',
            items: [
              {
                label: 'Privacy Policy',
                href: 'https://logz.io/about-us/privacy-policy/',
              },
              {
                label: 'Terms of Use',
                href: 'https://logz.io/about-us/terms-of-use/',
              },
              {
                label: 'Trademark Legal Notice',
                href: 'https://logz.io/about-us/trademarks-legal-notice/',
              },
              {
                label: 'Contributers',
                to: 'https://docs.logz.io/credits.html',
              },
            ],
          },
          {
            title: 'Social',
            items: [
              {
                label: 'Facebook',
                href: 'https://www.facebook.com/logz.io',
              },
              {
                label: 'Twitter',
                href: 'https://twitter.com/logzio',
              },
              {
                label: 'YouTube',
                href: 'https://www.youtube.com/channel/UC9Rc1hpWHUju8O2rYHAUVXA',
              },
              {
                label: 'LinkedIn',
                href: 'https://www.linkedin.com/company/4831888',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/logzio',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Logshero Ltd.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
