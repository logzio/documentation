import '@docsearch/css'; // Import default styles for DocSearch
import React from 'react';
import { DocSearch } from '@docsearch/react';
import { useAlgoliaContextualFacetFilters } from '@docusaurus/theme-search-algolia/client';


function SearchHeader() {
  const facetFilters = useAlgoliaContextualFacetFilters();
  return (
    <DocSearch
      apiKey="7f9d22d433c66f1a108b092d02c8d034"
      appId="GAVMESY4FI"
      indexName="shiny-alfajores-ede8d8"
      searchParameters={{
        facetFilters
      }}
    />
  );
}

export default SearchHeader;
