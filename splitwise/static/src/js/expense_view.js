/** @odoo-module **/

import { Component } from "@odoo/owl";
import { ExpenseHeaderView } from "./header/expense_header";
import { ExpenseLeftComponentView } from "./left_component/expense_left_component";
import { ExpenseMiddleComponentView } from "./middle_component/expense_middle_component";
import { ExpenseRightComponentView } from "./right_component/expense_right_component";

export class ExpenseView extends Component {
  static template = "splitwise.ExpenseView";
  static components = { ExpenseHeaderView, ExpenseLeftComponentView, ExpenseMiddleComponentView, ExpenseRightComponentView };
}
