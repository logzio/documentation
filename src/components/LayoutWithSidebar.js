import React from 'react';
import Layout from '@docusaurus/Layout';
import Sidebar from './Sidebar'; // Ensure this path points to your Sidebar component

const LayoutWithSidebar = ({children, ...props}) => {
  return (
    <Layout {...props}>
      <div className="container">
        <div className="row">
          <div className="col col--3">
            <Sidebar />
           
          <div className="col col--9">
            {children}
           
         
       
    </Layout>
  );
};

export default LayoutWithSidebar;
