// In your DocCardWrapper.jsx
import React from 'react';
import DocCard from '@theme-original/DocCard';

export default function DocCardWrapper(props) {
  // Extract item and restProps from props
  const { item, ...restProps } = props;

  // Check if customProps and description exist and log it
  if (item.customProps?.description) {
    console.log('Custom description exists:', item.customProps.description);
  } else {
    console.log('Using default description:', item.description);
  }

  // Override the description if customProps.description exists
  const newItem = {
    ...item,
    description: item.customProps?.description || item.description,
  };

  return <DocCard {...restProps} item={newItem} />;
}
