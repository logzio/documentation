### About array fields

Arrays are not natively supported by the OpenSearch Dashboards interface.
When an array is included in a log, the full array is displayed as a single field marked with the <i class="far fa-question-circle"></i> icon next to the field name. 

In the example below, the array **["a","b"] = [{"a":"1"}, {"b":"2"}]** becomes a single field.
![Arrays](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-mapping/array-field_2022.png)

Depending on the array, you may be able to seach for the string elements inside an array, as in the filter syntax example below. 
![Filter syntax](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-mapping/array-syntax-search_2022.png) 

In general, the more organized and consitent your log structure is (especially if the structure includes unique keys), the more accurate the result of transforming the data in the array will be.