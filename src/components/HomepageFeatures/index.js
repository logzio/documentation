import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: (
      <a href="/docs/intro">
        AWS cloud services
      </a>
    ),
    Svg: require('@site/static/img/aws.svg').default,
    description: (
      <>
        Send logs, metrics and traces from your AWS cloud services to Logz.io.
      </>
    ),
  },
  {
    title: 'Azure cloud services',
    Svg: require('@site/static/img/azure.svg').default,
    description: (
      <>
        Send logs, metrics and traces from your Azure cloud services to Logz.io.
      </>
    ),
  },
  {
    title: 'Google cloud services',
    Svg: require('@site/static/img/gcp.svg').default,
    description: (
      <>
        Send logs, metrics and traces from your Google cloud services to Logz.io.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
