import React from 'react';
import Layout from '@theme/Layout';
import DocSidebar from '@theme/DocSidebar';
import '.../css/custom.css';

function LayoutWithSidebar({ children, sidebar }) {
  return (
    <Layout>
      <div className="container-fluid">
        <div className="row">
          <div className="col col--2">
            <DocSidebar sidebar={sidebar} />
          </div>
          <div className="col col--10">
            {children}
          </div>
        </div>
      </div>
    </Layout>
  );
}

export default LayoutWithSidebar;
