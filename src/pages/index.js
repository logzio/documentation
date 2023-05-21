import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/search">
            Start Searching ⏱️
          </Link>
        </div>
      </div>
    </header>
  );
}

// Sidebar component
const Sidebar = () => {
  const sidebarItems = [
    // Replace this data with your actual sidebar data
    { label: 'Home', link: '/docs/intro' },
    { label: 'Doc 2', link: '/docs/tutorial-basics/create-a-blog-post' },
    // ...
  ];

  return (
    <div>
      <h3>Navigation</h3>
      <ul>
        {sidebarItems.map((item, idx) => (
          <li key={idx}><Link to={item.link}>{item.label}</Link></li>
        ))}
      </ul>
    </div>
  );
};

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <main>
        <div className="container">
          <div className="row">
            <div className="col col--3">
              <Sidebar />
            </div>
            <div className="col col--9">
              <HomepageFeatures />
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
}
