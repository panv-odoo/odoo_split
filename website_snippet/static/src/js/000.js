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
    let tbody = this.el.querySelector("tbody");
    let showConfirm = this.target.dataset.showConfirm;
    let id = 1;

    // Fetching data
    let data = await this.rpc("/getSalesOrders/", {
      show_all: showConfirm,
    });
    debugger;
    let filteredData;
    if (showConfirm) {
      filteredData = data.filter((order) => order.state === "sale");
    } else {
      filteredData = data;
    }

    // Map filtered data to orders array
    const orders = filteredData.map((order) => ({
      id: id++,
      name: order.name,
      partnerName: order.partner_id[1],
      status: order.state,
    }));

    const renderDetailsEl = renderToElement("s_sales_order_snippet", {
      orders: orders,
    });
    document.querySelector("#table_body_id").replaceChildren(renderDetailsEl);

    // Generate HTML for orders
    // let htmlEl = "";
    // let id = 1;
    // orders.forEach((data) => {
    //   htmlEl += `<tr>
    //     <td>${id++}</td>
    //     <td>${data.name}</td>
    //     <td>${data.partnerName}</td>
    //     <td>${data.status}</td>
    //   </tr>`;
    // });

    // Update table body with HTML
    // tbody.innerHTML = htmlEl;
  },
});

publicWidget.registry.SalesOrderSnippet = SalesOrderSnippet;
export default SalesOrderSnippet;
