import React from 'react';

const iconsData = [
    { "escape-sequence": "\\f154", "class": "li-bar-graph" },
    { "escape-sequence": "\\f192", "class": "li-eye" },
    { "escape-sequence": "\\f10d", "class": "li-left-arrow" },
    { "escape-sequence": "\\f10f", "class": "li-right-arrow" },
    { "escape-sequence": "\\f15e", "class": "li-logz" },
    { 
      "escape-sequence": "\\f164", 
      "class": "li-ellipsis-v", 
      "additional-css": "padding-left: .2rem; padding-right: .2rem;" 
    },
    { "escape-sequence": "\\f18b", "class": "li-data" },
    { "escape-sequence": "\\f135", "class": "li-pencil" },
    { "escape-sequence": "\\f1b1", "class": "li-trash" },
    { "escape-sequence": "\\f17b", "class": "li-plus" },
    { "escape-sequence": "\\f106", "class": "li-wrench" },
    { "escape-sequence": "\\f121", "class": "li-x" },
    { "escape-sequence": "\\f11e", "class": "li-clear" },
    { "escape-sequence": "\\f15b", "class": "li-plane" },
    { "escape-sequence": "\\f10a", "class": "li-bell" },
    { "escape-sequence": "\\f122", "class": "li-code" },
    { "escape-sequence": "\\f159", "class": "li-signal" },
    { "escape-sequence": "\\f18c", "class": "li-gear" },
    { "escape-sequence": "\\f167", "class": "li-minus" },
    { 
      "escape-sequence": "\\f189", 
      "class": "li-scroll", 
      "additional-css": "font-size: 1.1rem;" 
    },
    { "escape-sequence": "\\f177", "class": "li-play" },
    { "escape-sequence": "\\f19c", "class": "li-stop" },
    { "escape-sequence": "\\f175", "class": "li-pie_chart" },
    { "escape-sequence": "\\f12e", "class": "li-donut_small" },
    { "escape-sequence": "\\f12f", "class": "li-donut_large" },
    { "escape-sequence": "\\f153", "class": "li-kibana" },
    { "escape-sequence": "\\f1Bd", "class": "li-stars" },
    { "escape-sequence": "\\f129", "class": "li-dashboard" },
    { "escape-sequence": "\\f1ba", "class": "li-visualization" },
    { "escape-sequence": "\\f141", "class": "li-blob" },
    { "escape-sequence": "\\f155", "class": "li-points" },
    { "escape-sequence": "\\f180", "class": "li-repository" },
    { "escape-sequence": "\\f137", "class": "li-infinity" }
  ];
  
const Icon = ({ iconName }) => {
  const icon = iconsData.find(icon => icon.class === iconName);

  if (!icon) {
    console.warn(`Icon ${iconName} not found`);
    return null;
  }

  return (
    <i className={icon.class} style={{ content: `"${icon['escape-sequence']}"`, ...parseCss(icon['additional-css']) }} />
  );
};

// Function to parse additional CSS from a string into a JS object
function parseCss(cssString = '') {
  return cssString.split(';')
    .filter(style => style.split(':')[0] && style.split(':')[1])
    .map(style => [
      style.split(':')[0].trim().replace(/-./g, c => c.substr(1).toUpperCase()),
      style.split(':')[1].trim()
    ])
    .reduce((styleObj, style) => ({
      ...styleObj,
      [style[0]]: style[1],
    }), {});
}

export default Icon;
