import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'User Guide',
    link: "/docs/user-guide/logzio/home-db",
    Svg: require('@site/static/img/aws.svg').default,
    description: (
      <>
        Explore the comprehensive Logz.io User Guide and learn how to maximize your observability and security data.
      </>
    ),
  },
  {
    title: 'Integrations',
    link: "/docs/shipping/sample",
    Svg: require('@site/static/img/azure.svg').default,
    description: (
      <>
        Send logs, metrics and traces from your Azure cloud services to Logz.io.
      </>
    ),
  },
];

function Feature({Svg, title, description, link}) {
  return (
    <Link to={link} className={clsx('col col--4', styles.featureCard)}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </Link>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className={clsx('container', styles.featuresContainer)}>
        <div className={clsx('row', styles.centeredRow)}>
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}

