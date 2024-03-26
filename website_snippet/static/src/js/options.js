/** @odoo-module **/

import options from "@web_editor/js/editor/snippets.options";

const SalesOrderSnippetOptions = options.Class.extend({
  start() {
    console.log('options called')
  },
    
});

options.registry.SalesOrderSnippetOptions = SalesOrderSnippetOptions;
export default SalesOrderSnippetOptions;
