// src/components/CustomFooter.js

import React from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './CustomFooter.module.css';

function FooterLink({ to, href, label }) {
  return (
    <Link className={styles.footerLinkItem} to={to} href={href}>
      {label}
    </Link>
  );
}

function CustomFooter() {
  const { siteConfig } = useDocusaurusContext();
  const { themeConfig } = siteConfig;
  const { footer } = themeConfig;

  return (
    <footer className={styles.footer}>
      <div className="container container--fluid">
        <div className={styles.footerLinks}>
          <div className={styles.footerLinkSection}>
            <div className={styles.footerLogoText}>
              <img src={footer.logo.src} alt={footer.logo.alt} className={styles.footerLogo} />
              <p>This is text</p>
            </div>
          </div>
          {footer.links.map((linkGroup, i) => (
            <div key={i} className={styles.footerLinkSection}>
              <h4 className={styles.footerTitle}>{linkGroup.title}</h4>
              <ul className={styles.footerItems}>
                {linkGroup.items.map((item, key) => (
                  <li key={key} className={styles.footerItem}>
                    {item.html ? (
                      <div dangerouslySetInnerHTML={{ __html: item.html }} />
                    ) : (
                      <FooterLink {...item} />
                    )}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
        <div className={styles.footerBottom}>
          <p className={styles.footerCopyright}>
            {footer.copyright}
          </p>
        </div>
      </div>
    </footer>
  );
}

export default CustomFooter;
