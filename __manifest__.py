# -*- coding: utf-8 -*-
{
    "name": "Account Dashboard Bank Buttons",
    "version": "18.0.1.0.0",
    "summary": "Add Bank Statement and CAMT import buttons on bank journals dashboard",
    "category": "Accounting",
    "author": "Custom",
    "license": "LGPL-3",
    "depends": [
        "account",
        "account_statement_import_file",
    ],
    "data": [
        "views/account_journal_dashboard.xml",
        "views/account_bank_statement_buttons.xml",
        "views/account_reconcile_buttons.xml",
    ],
    "installable": True,
    "application": False,
}
