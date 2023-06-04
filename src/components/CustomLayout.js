import React from 'react';
import Tags from './Tags';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './CustomLayout.module.css';

export default function CustomLayout({ logo, tags, overviewTitle, children }) {
  const logoUrl = useBaseUrl(logo);
  
  return (
    <div className={styles.customLayout}>
      <div className={styles.logoTags}>
        <img src={logoUrl} alt="logo" className={styles.logo} />
        <Tags tags={tags} />
      </div>

      <div>
        <h2 className={styles.overview}>{overviewTitle}</h2>
        <p className={styles.overviewText}>{children}</p>
      </div>
    </div>
  );
}
