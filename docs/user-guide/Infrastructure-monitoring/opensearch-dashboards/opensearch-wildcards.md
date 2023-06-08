---
sidebar_position: 5
---


# Wildcard searches


Wildcards can be useful when you need to run a search on an indefinite term or a partial string.

When using the Lucene query syntax in OpenSearch Dashboards:

* Use a question mark **<i class="fas fa-question"></i>** to replace a single character. It's like a Joker in a card game.
* Use an asterisk **<i class="fas fa-asterisk"></i>** to replace an indefinite number of characters (even 0).

## Leading wildcards are disabled

Wildcard searches can be very resource heavy and slow to run.

**Leading wildcards are disabled** to prevent potential issues. In other words, your searches cannot begin with a wildcard.

For example, you can run a free text search for `string` but not for `*string`. Similarly, you can run a search for a `field:value` pair, such as `key:string` but not `key:*string`.

### Workarounds and alternatives



##### Change the field mapping to an **analyzed field**

If you want to search by partial field content, you have the option to change the field mapping to **analyzed text**.

Analyzed fields support filtering for a value that contains a certain string and can replace the need for leading wildcards.

For example, say you are looking for a particular host, instead of searching with a leading wildcard for `host:*prod*`, you can use the filters to filter under the field `host` for a value that contains `prod`.

###### Analyzed text fields tokenize strings

Analyzed text fields tokenize longer strings to support full-text search on individual terms.

Tokenization can mean indexing the words in a sentence, or breaking up a complex naming structure into stand-alone naming components to support more robust filtering options.

The tokenizing processor can use different predefined characters as delimiters to cut up the string into shorter terms. These can be spaces, periods, slashes, underscores, etc.

To change a field mapping,
select [Data Hub > Field mappings](https://app.logz.io/#/dashboard/tools/field-mapping)
from the navigation menu. Search for the field name, hover over it, and select the **analyzed** mapping option. The field will be explicitly mapped.

![Explicit field mapping in Logz.io](https://dytvr9ot2sszz.cloudfront.net/logz-docs/kibana-mapping/kibana-field-mapping_aug2021.png)

##### Contact support to request a custom configuration

If the above solutions do not satisfy your needs, please [contact support](mailto:help@logz.io?subject=Requesting%20alternatives%20to%20wildcard%20searches&body=Hi!%20Please%20be%20in%20touch%20regarding%20search%20methods%20that%20don't%20require%20leading%20wildcards.%20Thanks!) to request a customized solution.

