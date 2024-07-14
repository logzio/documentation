import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import styles from './styles.module.css';
import SearchHeader from '../../components/SearchHeader';  // Already imported

const InfrastructureEnvironmentFeatures = [
  {
    link: "/docs/user-guide/quick-start",
    Svg: require('@site/static/img/quick-start.svg').default,
  },
  {
    link: "/docs/user-guide/observability/assistantiq",
    Svg: require('@site/static/img/obsiq.svg').default,
  },
  {
    link: "/docs/user-guide/new-explore/",
    Svg: require('@site/static/img/explore.svg').default,
  },
  {
    link: "/docs/user-guide/k8s-360/overview",
    Svg: require('@site/static/img/k8s.svg').default,
  },
  {
    link: "/docs/category/send-your-data",
    Svg: require('@site/static/img/integrations.svg').default,
  },
  {
    link: "https://api-docs.logz.io/docs/category/logz-api",
    Svg: require('@site/static/img/api.svg').default,
  },
];

const ApplicationMonitoringFeatures = [
  {
    link: "/docs/user-guide/telemetry-collector/",
    Svg: require('@site/static/img/telemetry-collector.svg').default,
  },
  {
    link: "/docs/user-guide/log-management/troubleshooting/log-shipping-troubleshooting",
    Svg: require('@site/static/img/troubleshooting.svg').default,
  },
  {
    link: "/docs/user-guide/admin/logzio-accounts/accounts",
    Svg: require('@site/static/img/accounts.svg').default,
  },
  {
    link: "https://logz.io/freetrial/",
  },
  {
    link: "https://logz.io/learn/webinar/",
  },
  {
    link: "https://logz.io/learn/product/",
  },
];

const PopularIntegrationsFeatures = [
  {
    link: "/docs/user-guide/quick-start",
    Svg: require('@site/static/img/quick-start.svg').default,
  },
  {
    link: "/docs/user-guide/observability/assistantiq",
    Svg: require('@site/static/img/obsiq.svg').default,
  },
  {
    link: "/docs/user-guide/new-explore/",
    Svg: require('@site/static/img/explore.svg').default,
  },
  {
    link: "/docs/user-guide/k8s-360/overview",
    Svg: require('@site/static/img/k8s.svg').default,
  },
  {
    link: "/docs/category/send-your-data",
    Svg: require('@site/static/img/integrations.svg').default,
  },
  {
    link: "https://api-docs.logz.io/docs/category/logz-api",
    Svg: require('@site/static/img/api.svg').default,
  },
];

const ObservabilitySuiteFeatures = [
  {
    title: 'Logz.io quick start guide',
    link: "/docs/user-guide/quick-start",
    Svg: require('@site/static/img/quick-start.svg').default,
    description: <>Learn how to make the most out of the Logz.io platform.</>,
  },
  {
    title: 'Observability IQ',
    link: "/docs/user-guide/observability/assistantiq",
    Svg: require('@site/static/img/obsiq.svg').default,
    description: <>Engage in a dynamic conversation with your data.</>,
  },
  {
    title: 'Explore Dashboard',
    link: "/docs/user-guide/new-explore/",
    Svg: require('@site/static/img/explore.svg').default,
    description: <>A unified dashboard to monitor and quickly troubleshoot your data.</>,
  },
  {
    title: 'Kubernetes 360',
    link: "/docs/user-guide/k8s-360/overview",
    Svg: require('@site/static/img/k8s.svg').default,
    description: <>Monitor and troubleshoot applications deployed in Kubernetes environments.</>,
  },
  {
    title: 'Logz.io integrations',
    link: "/docs/category/send-your-data",
    Svg: require('@site/static/img/integrations.svg').default,
    description: <>All the different ways to send your data to Logz.io.</>,
  },
  {
    title: 'API',
    link: "https://api-docs.logz.io/docs/category/logz-api",
    Svg: require('@site/static/img/api.svg').default,
    description: <>Grow your own integration.</>,
  },
];

function Feature({Svg, link}) {
  return (
    <Link to={link} className={clsx('col col--4', styles.featureCard)}>
      <div className="text--center">
        {Svg && <Svg className={styles.featureSvg} role="img" />}
      </div>
    </Link>
  );
}

function FeatureWithDetails({Svg, link, title, description}) {
  return (
    <Link to={link} className={clsx('col col--4', styles.featureCardWithDetails)}>
      <div className="text--center">
        {Svg && <Svg className={styles.featureSvg} role="img" />}
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </Link>
  );
}

function StaticCard({ title, description }) {
  return (
    <div className={clsx('col col--12', styles.staticCard)}>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

function FeatureSection({header, features, showLink, isDetailed}) {
  return (
    <div className="col col--4">
      <h3 className="text--center">{header}</h3>
      <div className="row">
        {features.map((props, idx) => (
          isDetailed ? 
          <FeatureWithDetails key={idx} {...props} /> :
          <Feature key={idx} {...props} />
        ))}
      </div>
      {showLink && (
        <div className="text--center" style={{ marginTop: '20px' }}>
          <Link to="/docs/user-guide/quick-start" className={styles.seeAllLink}>
            See All Integrations
          </Link>
        </div>
      )}
    </div>
  );
}

function PopularLinks() {
  return (
    <div className={styles.popularLinks}>
      Popular: 
      <Link to="/docs/user-guide/quick-start">Agent quick setup</Link>
      <span className={styles.separator}>|</span>
      <Link to="/docs/user-guide/k8s-360/overview">K8S</Link>
      <span className={styles.separator}>|</span>
      <Link to="/docs/user-guide/new-explore/">Metrics</Link>
      <span className={styles.separator}>|</span>
      <Link to="/docs/category/send-your-data">Integration setup</Link>
      <span className={styles.separator}>|</span>
      <Link to="https://api-docs.logz.io/docs/category/logz-api">API</Link>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className={clsx('container', styles.featuresContainer)}>
        <div className="row">
          <div className="col col--12 text--center" style={{ marginBottom: '20px' }}>
            <h1 className={styles.mainTitle}>Logz.io Documentation</h1>
          </div>
          <div className="col col--12 text--center" style={{ marginBottom: '20px' }}>
            <div className={clsx(styles.searchContainer)}>
              <SearchHeader /> {/* Centered and wider SearchHeader component here */}
            </div>
          </div>
          <div className="col col--12 text--center" style={{ marginBottom: '20px' }}>
            <PopularLinks /> {/* Popular links under the search bar */}
          </div>
          <div className="col col--12 text--center" style={{ marginBottom: '20px' }}>
            <h1 className={styles.stepTitle}>Getting Started with Logz.io</h1> {/* Centered heading here */}
          </div>
          <div className="col col--12 text--center" style={{ marginBottom: '20px' }}>
            <h2 className={styles.stepSubtitle}>Step 1: Ship your data</h2> {/* Centered heading here */}
          </div>
        </div>
        <div className="row">
          <FeatureSection header="Infrastructure Environment" features={InfrastructureEnvironmentFeatures} showLink={false} isDetailed={false} />
          <FeatureSection header="Application Monitoring" features={ApplicationMonitoringFeatures} showLink={true} isDetailed={false} />
          <FeatureSection header="Popular Integrations" features={PopularIntegrationsFeatures} showLink={false} isDetailed={false} />
        </div>
        <div className="row" style={{ marginTop: '40px' }}>
          <div className="col col--12 text--center" style={{ marginBottom: '20px' }}>
            <h2 className={styles.stepSubtitle}>Step 2: Get the 360 Observability Suite</h2> {/* Centered heading for Step 2 */}
          </div>
          <div className="col col--12">
            <div className="row">
              {ObservabilitySuiteFeatures.map((props, idx) => (
                <FeatureWithDetails key={idx} {...props} />
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
