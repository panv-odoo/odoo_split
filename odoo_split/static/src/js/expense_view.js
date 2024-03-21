/** @odoo-module **/

import { Component } from "@odoo/owl";
import { ExpenseHeader } from "./header/header";
import { Contact } from "./contact/contact";
import { Transaction } from "./transaction/transaction";
import { Balance } from "./balance/balance";

export class ExpenseView extends Component {
  static template = "odoo_split.ExpenseView";
  static components = {
    ExpenseHeader,
    Contact,
    Transaction,
    Balance
    
  };
}
