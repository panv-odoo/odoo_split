/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { renderToElement } from "@web/core/utils/render";

const SalesOrderSnippet = publicWidget.Widget.extend({
  selector: ".s_sales_order_snippet",
  init: function () {
    this._super.apply(this, arguments);
    this.rpc = this.bindService("rpc");
  },

  start: async function () {
    let showConfirm = this.target.dataset.showConfirm;

    // Fetching data
    let orders = await this.rpc("/getSalesOrders/", {
      show_all: showConfirm,
    });

    if (Object.keys(orders).length) {
      // Rendering data into the table template
      const renderDetailsEl = renderToElement("s_sales_order_snippet", {
        orders: orders,
      });

      document.querySelector("#table_body_id").replaceChildren(renderDetailsEl);
    } else {
      document.querySelector("#table_td").replaceChildren(
        'No record present !!'
      );
    }
  },
});

publicWidget.registry.SalesOrderSnippet = SalesOrderSnippet;
export default SalesOrderSnippet;
