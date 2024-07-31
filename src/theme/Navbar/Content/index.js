import React from 'react';
import NavbarItem from '@theme/NavbarItem';
import { useThemeConfig } from '@docusaurus/theme-common';
import Logo from '@theme/Logo';


function NavbarContent() {
  const {
    navbar: { items, title, logo },
  } = useThemeConfig();

  // Separate items into left-aligned and right-aligned
  const leftItems = items.filter(item => item.position !== 'right');
  const rightItems = items.filter(item => item.position === 'right');

  return (
    <div className="navbar__inner">
      <div className="navbar__items navbar__items--left">
        <Logo />
        {leftItems.map((item, i) => (
          <NavbarItem {...item} key={i} />
        ))}
      </div>
      <div className="navbar__items navbar__items--right">
        {rightItems.map((item, i) => (
          <NavbarItem {...item} key={i} />
        ))}
      </div>
    </div>
  );
}

export default NavbarContent;
