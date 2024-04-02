import React from 'react';
import Translate, {translate} from '@docusaurus/Translate';
import {PageMetadata} from '@docusaurus/theme-common';
import Layout from '@theme/Layout';
export default function NotFound() {
  return (
    <>
      <PageMetadata
        title={translate({
          id: 'theme.NotFound.title',
          message: 'Page Not Found',
        })}
      />
      <Layout>
        <main className="container margin-vert--xl">
          <div className="row">
            <div className="col col--6 col--offset-3">
              <h1 className="hero__title">
                <Translate
                  id="theme.NotFound.title"
                  description="The title of the 404 page">
                  Page Not Found
                </Translate>
              </h1>
              <p>
                <Translate
                  id="theme.NotFound.p1"
                  description="The first paragraph of the 404 page">
                  The page you're searching for is playing hide-and-seek and winning.
                </Translate>
              </p>
              <p>
                <Translate
                id="theme.NotFound.p2"
                description='The second paragraph of the 404 page'>
                  While we're looking for it, here are some useful alternatives you can browse:
                </Translate>
              </p>
              <p>
              <ul>
                    <li><a href="/docs/user-guide/quick-start">Getting Started with Logz.io</a></li>
                    <li><a href="/docs/category/send-your-data/">Send Your Data</a></li>
                    <li><a href="https://api-docs.logz.io/docs/logz/logz-io-api/">Logz.io API</a></li>
                    <li><a href="/">Docs Homepage</a></li>
                  </ul>
              </p>
            </div>
          </div>
        </main>
      </Layout>
    </>
  );
}
