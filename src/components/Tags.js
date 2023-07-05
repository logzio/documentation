import React from 'react';

const Tags = ({ tags }) => (
    <div className="tags">
      {tags && tags.map((tag, index) => (
        <span key={index} style={{ backgroundColor: 'grey', padding: '5px', margin: '5px' }}>{tag}</span>
      ))}
     
  );
  
  export default Tags;
