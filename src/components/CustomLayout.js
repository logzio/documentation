import React from 'react';
import Tags from '@site/src/components/Tags';
import styles from './CustomLayout.module.css';

const CustomLayout = ({ logo, tags, overviewTitle, children, containerTitle, header, items }) => {
  return (
    <div className={styles.customLayout}>
      <div className={styles.logoTags}>
        <img src={logo} alt="Logo" className={styles.logo} />
        <Tags tags={tags} />
      </div>
      <div className={styles.overview}>
        <h1>{overviewTitle}</h1>
        <p className={styles.overviewText}>{children}</p>
      </div>
      <div className={styles.container}>
        <h2>{containerTitle}</h2>
        <h3>{header}</h3>
        {items.map((item, index) => (
          <p key={index}>{item}</p>
        ))}
      </div>
    </div>
  );
};

export default CustomLayout;
