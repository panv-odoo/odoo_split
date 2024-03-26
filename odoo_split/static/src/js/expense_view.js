/** @odoo-module **/

import { Component } from "@odoo/owl";
import { ExpenseHeader } from "./header/header";
import { Contact } from "./contact/contact";
import { Transaction } from "./transaction/transaction";
import { Balance } from "./balance/balance";
import { registry } from "@web/core/registry";

export class ExpenseView extends Component {
  static template = "odoo_split.ExpenseView";
  static components = {
    ExpenseHeader,
    Contact,
    Transaction,
    Balance,
  };

  setup() {
    debugger;
    if ("serviceWorker" in navigator) {
      navigator.serviceWorker
        .register("/split/service-worker.js")
        .catch(function (error) {
            console.error("Service worker registration failed, error:", error);
        });
    }
  }
}

registry.category("public_components").add("odoo_split.mysplits", ExpenseView);
