// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Logz.io Docs',
  favicon: 'https://logz.io/wp-content/themes/Avada-Child-Theme-logz/theme_favicon/apple-touch-icon.png',

  // Set the production url of your site here
  url: 'https://docs.logz.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'logzio', // Usually your GitHub org/user name.
  projectName: 'documentation', // Usually your repo name.

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
      '@docusaurus/plugin-google-gtag',
      {
        trackingID: 'GTM-NH9MTDW',
        anonymizeIP: true,
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
          editUrl: 'https://github.com/logzio/documentation/tree/master',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl: 'https://github.com/logzio/documentation/tree/master',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],
  scripts: [
    {
      src: '/js/intercomSettings.js'
    },
    {
      src: '/js/intercomWidget.js'
    }
  ],
  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      hotjar: {
        applicationId: "3812613",
      },
      docs: {
        sidebar: {
          hideable: true,
          autoCollapseCategories: true,
        },
      },
      // Replace with your project's social card
      image: 'https://dytvr9ot2sszz.cloudfront.net/logz-docs/social-assets/docs-social.jpg',
      navbar: {
        logo: {
          alt: 'Logz.io Docs',
          src: 'img/logz-logo.svg',
        },
        items: [
          { to: '/docs/category/user-guide/', label: 'Docs', position: 'left' },
          { to: 'https://logz.io/blog/', label: 'Blog', position: 'left' },
          { to: '/docs/category/send-your-data/', label: 'Ship data', position: 'left' },
          { to: 'https://status.logz.io/', label: 'System status', position: 'left' },
          { to: 'https://api-docs.logz.io/docs/logz/logz-io-api', label: 'API', position: 'left' },
          {
            href: 'https://app.logz.io/',
            label: 'Login',
            position: 'right',
          },
          {
            href: 'https://logz.io/freetrial/?utm_medium=referral&utm_source=docs-portal&utm_campaign=docs_trial&utm_content=lp&utm_term=free+trial',
            label: 'Free Trial',
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
            title: 'Resources',
            items: [
              {
                label: 'Link 1',
                to: '/docs/link1',
              },
              {
                label: 'Link 2',
                to: '/docs/link2',
              },
              {
                label: 'Link 3',
                to: '/docs/link3',
              },
            ],
          },
          {
            title: 'Company',
            items: [
              {
                label: 'Link 4',
                to: '/docs/link4',
              },
              {
                label: 'Link 5',
                to: '/docs/link5',
              },
              {
                label: 'Link 6',
                to: '/docs/link6',
              },
            ],
          },
          {
            title: 'Contact',
            items: [
              {
                label: 'Link 7',
                to: '/docs/link7',
              },
              {
                label: 'Link 8',
                to: '/docs/link8',
              },
              {
                label: 'Link 9',
                to: '/docs/link9',
              },
            ],
          },
          {
            title: 'Follow Us',
            items: [
              {
                label: 'Twitter',
                href: 'https://twitter.com/logzio',
              },
              {
                label: 'LinkedIn',
                href: 'https://www.linkedin.com/company/logzio',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/logzio',
              },
            ],
          },
        ],
        copyright: `
          <div class="footer__separator"></div>
          <div class="footer__bottom">
            <span class="footer__copyright">© ${new Date().getFullYear()} Logz.io. All rights reserved.</span>
            <div class="footer__links-right">
              <a href="/privacy">Privacy Policy</a>
              <a href="/terms">Terms of Service</a>
              <a href="/contact">Contact Us</a>
            </div>
          </div>
        `,
      },
    }),
};

module.exports = config;
