/** @odoo-module **/

import { Component, onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class ExpenseLeftComponentView extends Component {
    static template = "splitwise.ExpenseLeftComponentView";
    setup() {
        this.rpc = useService('rpc');
        onWillStart(this.getExpenses);
    }
    async getExpenses() {
        console.log("data");
    }
}
