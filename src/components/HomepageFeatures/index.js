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

const WhatsNewFeatures = [
  {
    title: 'New Feature 1',
    link: "/docs/new-feature-1",
    Svg: require('@site/static/img/quick-start.svg').default, // Use existing image as placeholder
    description: <>Check out the latest feature 1.</>,
  },
  {
    title: 'New Feature 2',
    link: "/docs/new-feature-2",
    Svg: require('@site/static/img/obsiq.svg').default, // Use existing image as placeholder
    description: <>Discover what's new in feature 2.</>,
  },
  {
    title: 'New Feature 3',
    link: "/docs/new-feature-3",
    Svg: require('@site/static/img/explore.svg').default, // Use existing image as placeholder
    description: <>Learn about the new feature 3.</>,
  },
  {
    title: 'New Feature 4',
    link: "/docs/new-feature-4",
    Svg: require('@site/static/img/k8s.svg').default, // Use existing image as placeholder
    description: <>Learn about the new feature 4.</>,
  },
  {
    title: 'New Feature 5',
    link: "/docs/new-feature-5",
    Svg: require('@site/static/img/integrations.svg').default, // Use existing image as placeholder
    description: <>Learn about the new feature 5.</>,
  },
  {
    title: 'New Feature 6',
    link: "/docs/new-feature-6",
    Svg: require('@site/static/img/api.svg').default, // Use existing image as placeholder
    description: <>Learn about the new feature 6.</>,
  },
];

const BestPracticesAndTools = [
  {
    Svg: require('@site/static/img/quick-start.svg').default,
    title: 'Best Practice 1',
    links: [
      { text: 'Link 1', url: '/docs/link1' },
      { text: 'Link 2', url: '/docs/link2' },
      { text: 'Link 3', url: '/docs/link3' },
      { text: 'Link 4', url: '/docs/link4' },
    ],
  },
  {
    Svg: require('@site/static/img/quick-start.svg').default,
    title: 'Best Practice 2',
    links: [
      { text: 'Link 1', url: '/docs/link1' },
      { text: 'Link 2', url: '/docs/link2' },
      { text: 'Link 3', url: '/docs/link3' },
      { text: 'Link 4', url: '/docs/link4' },
    ],
  },
  {
    Svg: require('@site/static/img/quick-start.svg').default,
    title: 'Best Practice 3',
    links: [
      { text: 'Link 1', url: '/docs/link1' },
      { text: 'Link 2', url: '/docs/link2' },
      { text: 'Link 3', url: '/docs/link3' },
      { text: 'Link 4', url: '/docs/link4' },
    ],
  },
  {
    Svg: require('@site/static/img/quick-start.svg').default,
    title: 'Best Practice 4',
    links: [
      { text: 'Link 1', url: '/docs/link1' },
      { text: 'Link 2', url: '/docs/link2' },
      { text: 'Link 3', url: '/docs/link3' },
      { text: 'Link 4', url: '/docs/link4' },
    ],
  },
];

function Feature({Svg, link}) {
  return (
    <Link to={link} className={styles.featureCard}>
      <div className="text--center">
        {Svg && <Svg className={styles.featureSvg} role="img" />}
      </div>
    </Link>
  );
}

function FeatureWithDetails({Svg, link, title, description}) {
  return (
    <Link to={link} className={styles.featureCardWithDetails}>
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
  const firstRowFeatures = features.slice(0, 3);
  const secondRowFeatures = features.slice(3, 6);
  return (
    <div className="col col--4">
      <h3 className="text--center">{header}</h3>
      <div className="row">
        {firstRowFeatures.map((props, idx) => (
          <div className="col col--4" key={idx}>
            {isDetailed ? 
            <FeatureWithDetails {...props} /> :
            <Feature {...props} />}
          </div>
        ))}
      </div>
      <div className="row">
        {secondRowFeatures.map((props, idx) => (
          <div className="col col--4" key={idx}>
            {isDetailed ? 
            <FeatureWithDetails {...props} /> :
            <Feature {...props} />}
          </div>
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

function WhatsNewHorizontalScroll() {
  return (
    <div className={styles.whatsNewHorizontalScroll}>
      <h2 className="text--center">What's New</h2>
      <div className={styles.scrollContainer}>
        {WhatsNewFeatures.map((props, idx) => (
          <div key={idx} className={styles.scrollCard}>
            <Link to={props.link} className={styles.carouselCard}>
              <div className="text--center">
                {props.Svg && <props.Svg className={styles.featureSvg} role="img" />}
              </div>
              <div className="text--center padding-horiz--md">
                <h3>{props.title}</h3>
                <p>{props.description}</p>
              </div>
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
}

function BestPracticesAndToolsSection() {
  return (
    <div className={styles.bestPracticesAndTools}>
      <h2 className="text--center">Best Practices and Tools</h2>
      <div className="row">
        {BestPracticesAndTools.map((column, idx) => (
          <div className="col col--3" key={idx}>
            <div className={styles.bestPracticesColumn}>
              <img src={column.Svg} alt={column.title} className={styles.bestPracticesImage} />
              <h3 className="text--center">{column.title}</h3>
              <ul>
                {column.links.map((link, linkIdx) => (
                  <li key={linkIdx}>
                    <Link to={link.url}>{link.text}</Link>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function ContactSupportSection() {
  return (
    <div className={styles.contactSupportSection}>
      <h2 className="text--center">Not finding the help you need?</h2>
      <div className="text--center">
        <Link to="/contact-support" className={styles.contactSupportButton}>Contact Support</Link>
      </div>
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
                <div className="col col--4" key={idx}>
                  <FeatureWithDetails {...props} />
                </div>
              ))}
            </div>
          </div>
        </div>
        <div className="row" style={{ marginTop: '40px' }}>
          <WhatsNewHorizontalScroll />
        </div>
        <div className="row" style={{ marginTop: '40px' }}>
          <BestPracticesAndToolsSection />
        </div>
        <div className="row" style={{ marginTop: '40px' }}>
          <ContactSupportSection />
        </div>
      </div>
    </section>
  );
}
