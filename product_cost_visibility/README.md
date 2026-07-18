# Product Cost Visibility

Odoo 19 custom module that controls **who can see the product Cost field**
(`standard_price`) on the product screen.

## How it works

1. Adds a security group **"Show Product Cost"**.
2. **Field-level security**: `standard_price` is restricted to that group at
   the model level, so for a user who is **not** in the group the Cost is
   removed from **every view, export and read-based report** across the
   database — list, kanban, pivot, form, etc.
3. On the product form the Cost **label** is also hidden so no empty row is
   left behind.
4. Under **Settings → General Settings → Product Cost Visibility**, an
   administrator selects the users who are allowed to see the cost. Saving the
   setting syncs the selected users into the security group.

The administrator (`base.user_admin`) is added to the group by default so the
cost stays visible right after installation.

## Installation

Copy the `product_cost_visibility` folder into your Odoo addons path, update
the apps list, and install **Product Cost Visibility**.

## Notes

* Cost is hidden at the **data level** (`groups=` on the model field), so it is
  enforced across all views, exports and the read/RPC layer — not only on the
  product screen.
* QWeb reports that print the cost through direct attribute access
  (`t-esc="o.standard_price"`) are a special case: attribute access does not go
  through the field ACL. Odoo's standard reports do not print product cost, so
  nothing extra is needed out of the box. If you have a **custom** report that
  prints cost, wrap that part in a group check, e.g.
  `t-if="env.user.has_group('product_cost_visibility.group_product_cost_visibility')"`.
