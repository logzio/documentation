import React from 'react';
import Link from '@docusaurus/Link';

const sidebarItems = [
  // This is just an example. You could fetch this data from an API, a database, 
  // or generate it based on the file structure of your docs.
  { label: 'Home', link: '/docs/intro' },
  { label: 'Doc 2', link: '/docs/tutorial-basics/create-a-blog-post' },
  // ...
];

const Sidebar = () => (
  <div>
    <h3>Navigation</h3>
    <ul>
      {sidebarItems.map((item, idx) => (
        <li key={idx}><Link to={item.link}>{item.label}</Link></li>
      ))}
    </ul>
   
);

export default Sidebar;
